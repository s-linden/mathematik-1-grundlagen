"""Kapitelweise Abbildungsnummern: "Abb. 2.1", "Abb. 2.2", ... statt fortlaufend.

Sphinx nummeriert Abbildungen ohne nummeriertes Inhaltsverzeichnis fortlaufend
durch das ganze Buch. Diese Erweiterung ersetzt die Nummern nachträglich durch
(Kapitel, laufende Nummer im Kapitel). Die Kapitelnummer kommt aus dem
Dateinamen (chapterNN/...). Querverweise mit {numref} passen sich automatisch an.
"""
import re

KAPITEL = re.compile(r"chapter(\d+)/")


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
    # nach der Nummernvergabe durch Sphinx (env-get-updated), vor dem Schreiben
    app.connect("env-get-updated", kapitelweise_nummerieren, priority=900)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
