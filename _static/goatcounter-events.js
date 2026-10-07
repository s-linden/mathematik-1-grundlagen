/* Zählt, wie oft in einer Übung "Lösung" bzw. "Lösungsweg" aufgeklappt wird.
   Pro Seitenaufruf und Feld wird nur das erste Aufklappen gezählt.
   Ereignis-Pfad in GoatCounter: loesung/<Seite>/<Übung X.Y>/<Lösung|Lösungsweg>
   Debug: in der Browser-Konsole  localStorage.gcdebug = 1  setzen, dann Seite neu laden. */
(function () {
  var counted = {};
  var debug = false;
  try { debug = !!localStorage.gcdebug; } catch (e) {}

  function pageName() {
    // Basispfad des Repos (/mathematik-1-grundlagen/) nicht mitzählen
    var p = location.pathname.replace(/^\/+/, '').replace(/\.html$/, '').replace(/\/+$/, '');
    var parts = p.split('/');
    if (parts.length > 1 && !/^chapter/i.test(parts[0])) parts.shift();
    return parts.join('/') || 'start';
  }

  function textOf(el) {
    return (el && el.textContent || '').replace(/\s+/g, ' ').trim();
  }

  function titleOf(box) {
    for (var i = 0; i < box.children.length; i++) {
      var c = box.children[i];
      if (c.tagName === 'SUMMARY' || (c.classList && c.classList.contains('admonition-title'))) return c;
    }
    return null;
  }

  function exerciseOf(el) {
    var box = el.closest('.admonition') || el;
    var outer = box.parentElement && box.parentElement.closest('.admonition');
    if (outer) box = outer;
    var prev = box.previousElementSibling;
    while (prev) {
      var t = textOf(titleOf(prev) || prev.querySelector('.admonition-title') || prev);
      var m = t.match(/Übung\s*[\d.]+/);
      if (m) return m[0];
      prev = prev.previousElementSibling;
    }
    return 'Übung ?';
  }

  function kindOf(el) {
    var t = textOf(titleOf(el));
    if (/Lösungsweg/i.test(t)) return 'Lösungsweg';
    if (/Lösung/i.test(t)) return 'Lösung';
    return null;
  }

  function send(path, title, tries) {
    if (window.goatcounter && window.goatcounter.count) {
      window.goatcounter.count({ path: path, title: title, event: true });
      if (debug) console.log('[gc] gesendet:', path);
    } else if (tries < 20) {
      // count.js lädt asynchron und ist evtl. noch nicht da
      setTimeout(function () { send(path, title, tries + 1); }, 500);
    } else if (debug) {
      console.warn('[gc] goatcounter nicht geladen (Adblocker?):', path);
    }
  }

  function report(el) {
    var kind = kindOf(el);
    if (!kind) return;
    var ex = exerciseOf(el);
    var path = 'loesung/' + pageName() + '/' + ex + '/' + kind;
    if (counted[path]) return;
    counted[path] = true;
    send(path, ex + ' – ' + kind, 0);
  }

  // 1) <details> (sphinx-design Dropdown "Lösungsweg")
  document.addEventListener('toggle', function (e) {
    var el = e.target;
    if (el && el.tagName === 'DETAILS' && el.open) report(el);
  }, true);

  // 2) Admonition mit Klasse "toggle" (sphinx-togglebutton, "Lösung"):
  //    Klick auf Titelzeile oder Pfeil, danach Zustand prüfen
  document.addEventListener('click', function (e) {
    var t = e.target;
    if (!t || !t.closest) return;
    var box = t.closest('.admonition.toggle');
    if (!box || t.closest('details')) return;
    var head = titleOf(box);
    if (!head || !(head === t || head.contains(t))) return;
    setTimeout(function () {
      var hidden = box.classList.contains('toggle-hidden') ||
                   (box.querySelector(':scope > .admonition-title ~ *') &&
                    getComputedStyle(box.querySelector(':scope > .admonition-title ~ *')).display === 'none');
      if (!hidden) report(box);
    }, 50);
  }, true);

  if (debug) console.log('[gc] events-script aktiv, Seite:', pageName());
})();
