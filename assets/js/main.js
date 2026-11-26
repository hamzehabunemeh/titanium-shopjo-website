/* Titanium Shop — small, dependency-free enhancements. */
(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.add("js");

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  function storage(action, key, value) {
    try {
      if (action === "set") window.sessionStorage.setItem(key, value);
      else return window.sessionStorage.getItem(key);
    } catch (e) { return null; }
    return null;
  }

  ready(function () {
    // Current year in the footer
    var year = String(new Date().getFullYear());
    document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = year; });

    // Header: solid background after scrolling
    var header = document.querySelector("[data-header]");
    var floatWa = document.querySelector(".float-wa");
    function onScroll() {
      if (header) header.classList.toggle("is-solid", window.scrollY > 40);
      if (floatWa) floatWa.classList.toggle("is-visible", window.scrollY > 520);
    }
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });

    // Mobile menu
    var toggle = document.querySelector("[data-menu-toggle]");
    var menu = document.querySelector("[data-mobile-menu]");
    if (toggle && menu) {
      var setMenu = function (open) {
        menu.hidden = !open;
        toggle.setAttribute("aria-expanded", String(open));
        header.classList.toggle("menu-open", open);
        document.body.style.overflow = open ? "hidden" : "";
      };
      toggle.addEventListener("click", function () { setMenu(menu.hidden); });
      menu.addEventListener("click", function (e) { if (e.target.closest("a")) setMenu(false); });
      document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !menu.hidden) { setMenu(false); toggle.focus(); } });
    }

    // Reveal on scroll
    var reveals = document.querySelectorAll(".reveal");
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (!("IntersectionObserver" in window) || reduce) {
      reveals.forEach(function (el) { el.classList.add("in"); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) { entry.target.classList.add("in"); io.unobserve(entry.target); }
        });
      }, { rootMargin: "0px 0px 15% 0px", threshold: 0 });
      reveals.forEach(function (el) { io.observe(el); });
    }

    // Press effect on photos for touch screens
    document.querySelectorAll(".frame").forEach(function (frame) {
      var timer;
      frame.addEventListener("touchstart", function () {
        clearTimeout(timer); frame.classList.add("is-pressed");
      }, { passive: true });
      ["touchend", "touchcancel"].forEach(function (ev) {
        frame.addEventListener(ev, function () {
          timer = setTimeout(function () { frame.classList.remove("is-pressed"); }, 450);
        }, { passive: true });
      });
    });

    // Founder portrait: colour when it is well in view (phones) or tapped
    var founders = document.querySelectorAll("[data-founder]");
    if (founders.length && "IntersectionObserver" in window && !window.matchMedia("(hover: hover)").matches) {
      var fo = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) { e.target.classList.toggle("is-active", e.intersectionRatio > 0.6); });
      }, { threshold: [0, 0.6, 1] });
      founders.forEach(function (f) { fo.observe(f); });
    }
    founders.forEach(function (f) {
      f.addEventListener("click", function () { f.classList.toggle("is-active"); });
    });

    // Count-up for numbers when they first appear ("5 min", "2018", "24/7" stays as is)
    if (!reduce && "IntersectionObserver" in window) {
      var counters = document.querySelectorAll(".stat-num");
      var co = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          co.unobserve(e.target);
          var el = e.target, text = el.textContent, m = text.match(/^(\D*)(\d+)(\D*)$/);
          if (!m || text.indexOf("/") > -1) return;
          var end = parseInt(m[2], 10), start = end > 1000 ? end - 30 : 0, t0 = null;
          var step = function (ts) {
            if (!t0) t0 = ts;
            var k = Math.min((ts - t0) / 1400, 1), eased = 1 - Math.pow(1 - k, 3);
            el.textContent = m[1] + Math.round(start + (end - start) * eased) + m[3];
            if (k < 1) requestAnimationFrame(step); else el.textContent = text;
          };
          requestAnimationFrame(step);
        });
      }, { threshold: 0.6 });
      counters.forEach(function (c) { co.observe(c); });
    }

    // Logo intro: finish early on any interaction, always clean up
    if (doc.classList.contains("show-intro")) {
      var endIntro = function () {
        doc.classList.add("intro-done"); doc.classList.remove("show-intro");
        ["wheel", "touchstart", "keydown", "mousedown"].forEach(function (ev) { window.removeEventListener(ev, endIntro); });
      };
      setTimeout(endIntro, 1800);
      ["wheel", "touchstart", "keydown", "mousedown"].forEach(function (ev) { window.addEventListener(ev, endIntro, { passive: true }); });
    }

    var fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

    // Showroom spotlight
    if (fine) {
      document.querySelectorAll("[data-spotlight]").forEach(function (sec) {
        sec.addEventListener("pointermove", function (e) {
          var r = sec.getBoundingClientRect();
          sec.style.setProperty("--mx", (e.clientX - r.left) + "px");
          sec.style.setProperty("--my", (e.clientY - r.top) + "px");
          sec.classList.add("is-lit");
        });
        sec.addEventListener("pointerleave", function () { sec.classList.remove("is-lit"); });
      });
    }

    // Parallax on wide photos (desktop only)
    var plx = document.querySelectorAll("[data-parallax] img");
    if (plx.length && fine && !reduce && window.innerWidth >= 900) {
      var ticking = false;
      var update = function () {
        var vh = window.innerHeight;
        plx.forEach(function (im) {
          var r = im.parentElement.getBoundingClientRect();
          if (r.bottom < 0 || r.top > vh) return;
          var k = (r.top + r.height / 2 - vh / 2) / (vh / 2 + r.height / 2); // -1..1
          im.style.translate = "0 " + (-k * 40).toFixed(1) + "px";
        });
        ticking = false;
      };
      window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
      update();
    }

    // Fleet filter
    var fleet = document.querySelector("[data-fleet]");
    if (fleet) {
      var chips = document.querySelectorAll("[data-filter]");
      chips.forEach(function (chip) {
        chip.addEventListener("click", function () {
          var f = chip.getAttribute("data-filter");
          chips.forEach(function (c) { c.setAttribute("aria-pressed", String(c === chip)); });
          fleet.querySelectorAll("[data-cat]").forEach(function (card) {
            card.hidden = f !== "all" && card.getAttribute("data-cat") !== f;
          });
        });
      });
    }

    // Request form: service-specific fields, subject line, WhatsApp follow-up
    var form = document.querySelector("[data-request-form]");
    if (form) {
      var select = form.querySelector("[data-service-select]");
      var groups = form.querySelectorAll("[data-service-fields]");
      var showFields = function () {
        groups.forEach(function (g) {
          var on = g.getAttribute("data-service-fields") === select.value;
          g.hidden = !on;
          g.querySelectorAll("input, select, textarea").forEach(function (el) { el.disabled = !on; });
        });
      };
      var preset = new URLSearchParams(window.location.search).get("service");
      if (preset && select.querySelector('option[value="' + preset.replace(/[^a-z-]/g, "") + '"]')) {
        select.value = preset;
      }
      showFields();
      select.addEventListener("change", showFields);

      form.addEventListener("submit", function (e) {
        if (!form.checkValidity()) return; // let the browser show its messages
        var label = select.options[select.selectedIndex].text;
        form.querySelector('[name="service"]').value = label;
        form.querySelector('[name="_subject"]').value = form.getAttribute("data-subject-prefix") + ": " + label;
        form.querySelector('[name="_next"]').value = new URL("thanks.html", window.location.href).href;

        var lines = [form.getAttribute("data-wa-intro"), "• " + label];
        ["name", "date", "details"].forEach(function (n) {
          var el = form.querySelector('[name="' + n + '"]');
          if (el && el.value.trim()) lines.push("• " + el.value.trim().slice(0, 300));
        });
        storage("set", "ts_wa_message", lines.join("\n"));
        storage("set", "ts_wa_number", form.getAttribute("data-wa-number"));
      });
    }

    // Thank-you page: WhatsApp button carries the request summary
    var cont = document.querySelector("[data-wa-continue]");
    if (cont) {
      var msg = storage("get", "ts_wa_message");
      var num = storage("get", "ts_wa_number");
      if (msg && num && /^[0-9]{8,15}$/.test(num)) {
        cont.href = "https://wa.me/" + num + "?text=" + encodeURIComponent(msg);
      }
    }
  });
})();
