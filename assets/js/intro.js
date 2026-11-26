/* Shows the logo intro once per browser session. Loaded in <head> so the
   overlay is in place before the page paints. */
(function () {
  try {
    // Hold the first headline until main.js lifts it line by line (failsafe: show after 3s)
    if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      var root = document.documentElement;
      root.classList.add("split-hold");
      setTimeout(function () { root.classList.remove("split-hold"); }, 3000);
    }
  } catch (e) { /* ignore */ }
  try {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    if (sessionStorage.getItem("ts_intro")) return;
    sessionStorage.setItem("ts_intro", "1");
    document.documentElement.classList.add("show-intro");
  } catch (e) { /* storage blocked: skip the intro */ }
})();
