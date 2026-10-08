(function () {
  var input = document.getElementById("q");
  var clear = document.getElementById("q-clear");
  var status = document.getElementById("q-status");
  var none = document.getElementById("no-results");
  var form = document.getElementById("search-form");
  var cards = Array.prototype.slice.call(document.querySelectorAll(".card[data-search]"));
  var hideable = Array.prototype.slice.call(document.querySelectorAll(".hide-on-search"));
  var groups = Array.prototype.slice.call(document.querySelectorAll(".group, .search-zone"));

  function run() {
    var q = input.value.trim().toLowerCase();
    var words = q.split(/\s+/).filter(Boolean);
    var searching = words.length > 0;
    var shown = 0;
    cards.forEach(function (c) {
      var hay = c.getAttribute("data-search");
      var ok = !searching || words.every(function (w) { return hay.indexOf(w) !== -1; });
      c.hidden = !ok;
      if (ok && searching) shown++;
    });
    hideable.forEach(function (el) { el.hidden = searching; });
    groups.forEach(function (g) {
      if (!searching) { g.hidden = false; return; }
      var any = g.querySelector(".card[data-search]:not([hidden])");
      g.hidden = !any;
    });
    clear.hidden = !searching;
    none.hidden = !(searching && shown === 0);
    status.textContent = searching ? (shown === 1 ? "1 match" : shown + " matches") : "";
  }

  input.addEventListener("input", run);
  form.addEventListener("submit", function (ev) { ev.preventDefault(); run(); });
  clear.addEventListener("click", function () { input.value = ""; run(); input.focus(); });
})();

(function () {
  var menu = document.getElementById("topnav-menu");
  var input = document.getElementById("q");
  document.querySelectorAll('.topnav a[href^="#"]').forEach(function (a) {
    a.addEventListener("click", function () {
      if (menu) menu.open = false;
      if (input && input.value) { input.value = ""; input.dispatchEvent(new Event("input")); }
    });
  });
  document.addEventListener("click", function (ev) {
    if (menu && menu.open && !menu.contains(ev.target)) menu.open = false;
  });
})();
