/* Zählt, wie oft in einer Übung "Lösung" bzw. "Lösungsweg" aufgeklappt wird.
   Pro Seitenaufruf und Feld wird nur das erste Aufklappen gezählt.
   Ereignis-Pfad in GoatCounter: loesung/<Seite>/<Übung X.Y>/<Lösung|Lösungsweg> */
(function () {
  var counted = {};

  function pageName() {
    return location.pathname.replace(/^\/+/, '').replace(/\.html$/, '').replace(/\/+$/, '') || 'start';
  }

  function textOf(el) {
    return (el && el.textContent || '').replace(/\s+/g, ' ').trim();
  }

  // Übungsnummer: zuständiges Aufgaben-Feld ("Übung 5.3") finden
  function exerciseOf(el) {
    var box = el.closest('.admonition') || el;
    // Falls "Lösungsweg" in "Lösung" steckt: das äußere Lösungs-Feld nehmen
    var outer = box.parentElement && box.parentElement.closest('.admonition');
    if (outer) box = outer;
    var prev = box.previousElementSibling;
    while (prev) {
      var title = prev.querySelector && (prev.querySelector('.admonition-title') || prev.querySelector('summary'));
      var t = textOf(title || prev);
      var m = t.match(/Übung\s*[\d.]+/);
      if (m) return m[0];
      prev = prev.previousElementSibling;
    }
    return 'Übung ?';
  }

  function kindOf(el) {
    // Titel des Feldes ("Lösung" oder "Lösungsweg")
    var head = el.querySelector(':scope > summary') || el.querySelector(':scope > .admonition-title') || el.querySelector('summary');
    var t = textOf(head);
    if (/Lösungsweg/i.test(t)) return 'Lösungsweg';
    if (/Lösung/i.test(t)) return 'Lösung';
    return null;
  }

  function report(el) {
    var kind = kindOf(el);
    if (!kind) return;
    var ex = exerciseOf(el);
    var path = 'loesung/' + pageName() + '/' + ex + '/' + kind;
    if (counted[path]) return;
    counted[path] = true;
    if (window.goatcounter && window.goatcounter.count) {
      window.goatcounter.count({ path: path, title: ex + ' – ' + kind, event: true });
    }
  }

  // Moderne Variante: <details>-Elemente (Dropdown und aufklappbare Admonitions)
  document.addEventListener('toggle', function (e) {
    var el = e.target;
    if (el && el.tagName === 'DETAILS' && el.open) report(el);
  }, true);

  // Ältere Variante von sphinx-togglebutton: Klick auf den Pfeil-Button
  document.addEventListener('click', function (e) {
    var btn = e.target.closest && e.target.closest('button.toggle-button');
    if (!btn) return;
    var box = btn.closest('.admonition');
    if (box && !box.closest('details')) {
      window.setTimeout(function () {
        if (!box.classList.contains('toggle-hidden')) report(box);
      }, 0);
    }
  }, true);
})();
