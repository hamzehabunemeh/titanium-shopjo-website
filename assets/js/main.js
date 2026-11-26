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

    var isAr = doc.lang === "ar";

    // Live Amman time
    var clocks = document.querySelectorAll("[data-amman-clock]");
    if (clocks.length && window.Intl) {
      var tick = function () {
        var now = new Date(), time;
        try {
          if (isAr) {
            var hm = new Intl.DateTimeFormat("en-GB", { timeZone: "Asia/Amman", hour: "numeric", minute: "2-digit", hour12: false }).format(now).split(":");
            var h24 = parseInt(hm[0], 10) % 24, h12 = h24 % 12 || 12;
            var part = h24 < 5 ? "فجراً" : h24 < 12 ? "صباحاً" : h24 < 17 ? "ظهراً" : "مساءً";
            time = h12 + ":" + hm[1] + " " + part;
          } else {
            time = new Intl.DateTimeFormat("en-US", { timeZone: "Asia/Amman", hour: "numeric", minute: "2-digit" }).format(now);
          }
        } catch (e) { return; }
        var text = isAr ? "الساعة الآن " + time + " في عمّان، وفريقنا متاح." : "It's " + time + " in Amman, and our team is available.";
        clocks.forEach(function (c) { c.textContent = text; c.hidden = false; });
      };
      tick();
      setInterval(tick, 30000);
    }

    // Home planner: live count of chosen services
    var planner = document.querySelector("[data-planner]");
    if (planner) {
      var count = planner.querySelector("[data-planner-count]");
      var upd = function () {
        var n = planner.querySelectorAll("input:checked").length;
        count.textContent = !n ? "" : n === 1 ? (isAr ? "خدمة واحدة مختارة" : "1 service selected") : (isAr ? n + " خدمات مختارة" : n + " services selected");
      };
      planner.addEventListener("change", upd);
      upd();
    }

    // Car details dialog
    var dlg = document.querySelector("[data-car-dialog]");
    if (dlg && typeof dlg.showModal === "function") {
      var dImg = dlg.querySelector("[data-car-img]"), dTitle = dlg.querySelector("[data-car-title]");
      var dCat = dlg.querySelector("[data-car-cat-out]"), dReq = dlg.querySelector("[data-car-request]");
      var dWa = dlg.querySelector("[data-car-wa]"), lastBtn = null;
      var waBase = dWa.href.split("?")[0];
      document.querySelectorAll("[data-car]").forEach(function (btn) {
        btn.addEventListener("click", function () {
          var name = btn.getAttribute("data-car"), im = btn.querySelector("img");
          lastBtn = btn;
          dImg.src = im.currentSrc || im.src; dImg.srcset = im.srcset; dImg.sizes = "(min-width: 900px) 60vw, 100vw"; dImg.alt = name;
          dTitle.textContent = name; dCat.textContent = btn.getAttribute("data-car-cat");
          dReq.href = "contact.html?services=cars&car=" + encodeURIComponent(name) + "#request";
          dWa.href = waBase + "?text=" + encodeURIComponent(isAr ? "مرحباً Titanium Shop، أنا مهتم بسيارة " + name + "." : "Hello Titanium Shop, I'm interested in the " + name + ".");
          dlg.showModal();
          document.body.style.overflow = "hidden";
        });
      });
      var closeDlg = function () { dlg.close(); };
      dlg.querySelector("[data-car-close]").addEventListener("click", closeDlg);
      dlg.addEventListener("click", function (e) { if (e.target === dlg) closeDlg(); });
      dlg.addEventListener("close", function () { document.body.style.overflow = ""; if (lastBtn) lastBtn.focus(); });
    }

    // Request form: several services, their fields, subject line, WhatsApp follow-up
    var form = document.querySelector("[data-request-form]");
    if (form) {
      var boxes = form.querySelectorAll("[data-service-picker] input[type=checkbox]");
      var groups = form.querySelectorAll("[data-service-fields]");
      var err = form.querySelector("[data-service-error]");
      var chosen = function () { return Array.prototype.filter.call(boxes, function (b) { return b.checked; }); };
      var showFields = function () {
        var on = chosen().map(function (b) { return b.value; });
        groups.forEach(function (g) {
          var vis = on.indexOf(g.getAttribute("data-service-fields")) > -1;
          g.hidden = !vis;
          g.querySelectorAll("input, select, textarea").forEach(function (el) { el.disabled = !vis; });
        });
        if (on.length) err.hidden = true;
      };
      var params = new URLSearchParams(window.location.search);
      var preset = [];
      params.getAll("services").concat(params.getAll("service")).forEach(function (v) { preset = preset.concat(v.split(",")); });
      boxes.forEach(function (b) { if (preset.indexOf(b.value) > -1) b.checked = true; });
      var car = params.get("car"), carSel = form.querySelector('[name="car"]');
      if (car && carSel) Array.prototype.forEach.call(carSel.options, function (o) { if (o.text === car) carSel.value = o.value || o.text; });
      showFields();
      boxes.forEach(function (b) { b.addEventListener("change", showFields); });

      form.addEventListener("submit", function (e) {
        var picked = chosen();
        if (!picked.length) {
          e.preventDefault(); err.hidden = false;
          boxes[0].focus(); return;
        }
        if (!form.checkValidity()) { e.preventDefault(); form.reportValidity(); return; }
        var label = picked.map(function (b) { return b.getAttribute("data-label"); }).join(" + ");
        form.querySelector('[name="service"]').value = label;
        form.querySelector('[name="_subject"]').value = form.getAttribute("data-subject-prefix") + ": " + label;
        form.querySelector('[name="_next"]').value = new URL("thanks.html", window.location.href).href;

        var lines = [form.getAttribute("data-wa-intro"), "• " + label];
        ["name", "car", "date", "details"].forEach(function (n) {
          var el = form.querySelector('[name="' + n + '"]');
          if (el && !el.disabled && el.value.trim()) lines.push("• " + el.value.trim().slice(0, 300));
        });
        storage("set", "ts_wa_message", lines.join("\n"));
        storage("set", "ts_wa_number", form.getAttribute("data-wa-number"));
      });
    }

    // Ornament light wave: once when it scrolls into view, then on hover (desktop) or tap (phone)
    var orns = document.querySelectorAll(".ornament");
    if (orns.length && !reduce) {
      var wave = function (el) {
        if (el.classList.contains("is-waving")) return;
        el.classList.add("is-waving");
        setTimeout(function () { el.classList.remove("is-waving"); }, 1000);
      };
      var canHover = window.matchMedia("(hover: hover)").matches;
      Array.prototype.forEach.call(orns, function (el) {
        el.insertAdjacentHTML("beforeend", '<span class="orn-hit"></span><span class="orn-wave"></span><span class="orn-shine"></span>');
        if (canHover) el.addEventListener("mouseenter", function () { wave(el); });
        else el.addEventListener("pointerdown", function () { wave(el); });
      });
      if ("IntersectionObserver" in window) {
        var oo = new IntersectionObserver(function (entries) {
          entries.forEach(function (e) {
            if (!e.isIntersecting) return;
            oo.unobserve(e.target);
            setTimeout(function () { wave(e.target); }, 250);
          });
        }, { threshold: 1, rootMargin: "0px 0px -12% 0px" });
        Array.prototype.forEach.call(orns, function (el) { oo.observe(el); });
      }
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
