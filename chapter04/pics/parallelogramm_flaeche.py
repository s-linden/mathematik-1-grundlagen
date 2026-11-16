"""Skizze zur Begründung von (4.95): Parallelogramm mit Höhe h (Abschnitt 4.5).

Aufruf (im Ordner chapter04/pics):  python3 parallelogramm_flaeche.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Polygon

plt.rcParams.update({"font.size": 12, "mathtext.fontset": "cm", "svg.fonttype": "path"})

BLAU = "#005A94"
ROT = "#C00000"
GRAU = "#888888"

a = np.array([4.0, 0.0])
b = np.array([1.6, 2.2])
phi = np.arctan2(b[1], b[0])

fig, ax = plt.subplots(figsize=(6.2, 2.9))
ax.add_patch(Polygon([(0, 0), a, a + b, b], closed=True, facecolor="#e8f0f7", edgecolor="none"))
ax.plot([b[0], a[0] + b[0]], [b[1], b[1]], color=GRAU, lw=1.2)
ax.plot([a[0], a[0] + b[0]], [0, b[1]], color=GRAU, lw=1.2)
pfeil = dict(arrowstyle="-|>", lw=2.2, mutation_scale=18)
ax.annotate("", xy=a, xytext=(0, 0), arrowprops=dict(color=BLAU, **pfeil))
ax.annotate("", xy=b, xytext=(0, 0), arrowprops=dict(color=BLAU, **pfeil))
ax.text(a[0] / 2, -0.3, r"$\vec{a}$", color=BLAU, ha="center", va="top", fontsize=16)
ax.text(b[0] / 2 - 0.25, b[1] / 2 + 0.1, r"$\vec{b}$", color=BLAU, ha="right", fontsize=16)
# Höhe
ax.plot([b[0], b[0]], [0, b[1]], "--", color=ROT, lw=1.5)
ax.text(b[0] + 0.1, b[1] / 2, "$h$", color=ROT, ha="left", va="center", fontsize=16)
s = 0.22
ax.plot([b[0] - s, b[0] - s, b[0]], [0, s, s], color=ROT, lw=1)
# Flächeninhalt
ax.text((a[0] + b[0]) / 2 + 0.2, b[1] / 2, "$A$", ha="center", va="center", fontsize=18)
# Winkel
ax.add_patch(Arc((0, 0), 1.3, 1.3, theta1=0, theta2=np.degrees(phi), color="k", lw=1.2))
ax.text(0.85 * np.cos(phi / 2), 0.85 * np.sin(phi / 2), r"$\varphi$", ha="left", va="center", fontsize=16)
ax.set_xlim(-0.3, 6.0)
ax.set_ylim(-0.7, 2.5)
ax.set_aspect("equal")
ax.axis("off")
fig.savefig("parallelogramm_flaeche.svg", bbox_inches="tight", transparent=True)
