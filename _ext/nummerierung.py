"""Kapitelweise Nummern für Abbildungen und freigestellte Formeln.

* Abbildungen: "Abb. 2.1", "Abb. 2.2", ... statt fortlaufend durchs ganze Buch.
* Formeln: jede freigestellte Formel ($$ ... $$) bekommt eine Nummer "(7.3)",
  rechtsbündig in der Zeile der Formel.

Sphinx nummeriert ohne nummeriertes Inhaltsverzeichnis fortlaufend durch das
ganze Buch. Diese Erweiterung ersetzt die Nummern nachträglich durch
(Kapitel, laufende Nummer im Kapitel). Die Kapitelnummer kommt aus dem
Dateinamen (chapterNN/...). Querverweise mit {numref}/{eq} passen sich an.
"""
import re

from docutils import nodes

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
    app.connect("doctree-read", formeln_markieren, priority=400)
    # nach der Nummernvergabe durch Sphinx (env-get-updated), vor dem Schreiben
    app.connect("env-get-updated", kapitelweise_nummerieren, priority=900)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
