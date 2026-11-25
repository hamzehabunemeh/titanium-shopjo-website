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
      }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
      reveals.forEach(function (el) { io.observe(el); });
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
