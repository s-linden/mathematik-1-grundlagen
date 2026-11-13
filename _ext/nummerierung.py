"""Kapitelweise Nummern für Abbildungen und freigestellte Formeln.

* Abbildungen: "Abb. 2.1", "Abb. 2.2", ... statt fortlaufend durchs ganze Buch.
* Interaktive Abbildungen (iframe) bekommen mit {interaktive-abbildung} ebenfalls
  eine Abbildungsnummer und eine Bildunterschrift.
* In Bildunterschriften wird "(Quelle: ...; Lizenz: ...)" ausgegraut (CSS-Klasse quelle).
* Tabellen: jede Tabelle bekommt eine Unterschrift "Tab. 6.1" (ohne Beschreibung).
* Formeln: jede freigestellte Formel ($$ ... $$) bekommt eine Nummer "(7.3)",
  rechtsbündig in der Zeile der Formel.

Sphinx nummeriert ohne nummeriertes Inhaltsverzeichnis fortlaufend durch das
ganze Buch. Diese Erweiterung ersetzt die Nummern nachträglich durch
(Kapitel, laufende Nummer im Kapitel). Die Kapitelnummer kommt aus dem
Dateinamen (chapterNN/...). Querverweise mit {numref}/{eq} passen sich an.
"""
import re

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

KAPITEL = re.compile(r"chapter(\d+)/")


def formeln_markieren(app, doctree):
    """Gibt jeder freigestellten Formel ohne Label ein Label, damit Sphinx sie nummeriert."""
    env = app.env
    domain = env.get_domain("math")
    docname = env.docname
    for i, node in enumerate(doctree.findall(nodes.math_block)):
        if node.get("label") or node["ids"]:
            continue
        label = "auto-" + re.sub(r"[^a-z0-9]+", "-", docname.lower()) + f"-{i + 1}"
        domain.note_equation(docname, label, location=node)
        node["label"] = label
        node["number"] = domain.get_equation_number_for(label)
        node["docname"] = docname
        node["ids"].append(nodes.make_id("equation-" + label))


class InteraktiveAbbildung(SphinxDirective):
    """Nummerierte Abbildung mit eingebetteter HTML-Seite (GeoGebra, Kugelbahn, ...).

    ```{interaktive-abbildung} ../_static/geogebra/richtungswinkel.html
    ---
    height: 640
    name: richtungswinkel
    title: Interaktive Darstellung der Richtungswinkel
    ---
    Bildunterschrift (Quelle: eigene Darstellung; Lizenz: ...)
    ```
    """

    required_arguments = 1
    has_content = True
    option_spec = {
        "height": directives.unchanged,
        "name": directives.unchanged,
        "title": directives.unchanged,
        "class": directives.unchanged,
    }

    def run(self):
        src = self.arguments[0]
        height = self.options.get("height", "500")
        title = self.options.get("title", "Interaktive Darstellung")
        wrapper = self.options.get("class", "interaktiv")
        html = (
            f'<div class="{wrapper}"><iframe src="{src}" width="100%" '
            f'height="{height}" frameborder="0" scrolling="no" title="{title}">'
            "</iframe></div>"
        )
        figure = nodes.figure(classes=["interaktive-abbildung"])
        figure += nodes.raw("", html, format="html")
        inhalt = nodes.Element()
        self.state.nested_parse(self.content, self.content_offset, inhalt)
        if inhalt.children and isinstance(inhalt[0], nodes.paragraph):
            absatz = inhalt[0]
            caption = nodes.caption(absatz.rawsource, "", *absatz.children)
            caption.source, caption.line = absatz.source, absatz.line
            figure += caption
        if "name" in self.options:
            self.add_name(figure)
        self.set_source_info(figure)
        return [figure]


def tabellen_markieren(app, doctree):
    """Gibt jeder Tabelle ohne Überschrift eine leere, damit Sphinx sie nummeriert."""
    docname = app.env.docname
    for i, tabelle in enumerate(doctree.findall(nodes.table)):
        if not any(isinstance(k, nodes.title) for k in tabelle.children):
            # unsichtbarer Inhalt, weil Sphinx Tabellen ohne Titeltext nicht nummeriert
            tabelle.insert(0, nodes.title("", "\u200b"))
        if not tabelle["ids"]:
            name = "tabelle-" + re.sub(r"[^a-z0-9]+", "-", docname.lower()) + f"-{i + 1}"
            tabelle["ids"].append(nodes.make_id(name))


def quelle_ausgrauen(app, doctree):
    """Packt "(Quelle: ...)" in Bildunterschriften in <span class="quelle">."""
    for caption in doctree.findall(nodes.caption):
        if not isinstance(caption.parent, nodes.figure):
            continue
        for i, kind in enumerate(caption.children):
            if isinstance(kind, nodes.Text) and "(Quelle:" in kind.astext():
                text = kind.astext()
                k = text.index("(Quelle:")
                rest = caption.children[i + 1:]
                for r in rest:
                    caption.remove(r)
                caption.remove(kind)
                if text[:k]:
                    caption.insert(i, nodes.Text(text[:k]))
                    i += 1
                span = nodes.inline(classes=["quelle"])
                span += nodes.Text(text[k:])
                for r in rest:
                    span += r
                caption.insert(i, span)
                break


def kapitelweise_nummerieren(app, env):
    alle = []  # (globale Nummer, Dokument, Typ, ID)
    for docname, typen in env.toc_fignumbers.items():
        for typ, nummern in typen.items():
            for fig_id, nummer in nummern.items():
                alle.append((nummer, docname, typ, fig_id))

    zaehler = {}
    for nummer, docname, typ, fig_id in sorted(alle):
        m = KAPITEL.match(docname)
        if not m:
            continue
        kapitel = int(m.group(1))
        zaehler[(typ, kapitel)] = zaehler.get((typ, kapitel), 0) + 1
        env.toc_fignumbers[docname][typ][fig_id] = (kapitel, zaehler[(typ, kapitel)])
    return []


def setup(app):
    # vor dem Einsammeln der Nummern durch Sphinx (doctree-read, Priorität 500)
    app.add_directive("interaktive-abbildung", InteraktiveAbbildung)
    app.connect("doctree-read", formeln_markieren, priority=400)
    app.connect("doctree-read", quelle_ausgrauen)
    app.connect("doctree-read", tabellen_markieren, priority=400)
    # nach der Nummernvergabe durch Sphinx (env-get-updated), vor dem Schreiben
    app.connect("env-get-updated", kapitelweise_nummerieren, priority=900)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
