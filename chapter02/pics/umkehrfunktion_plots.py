"""Erzeugt die Grafiken für Abschnitt 2.6 Umkehrfunktion.

Aufruf (im Ordner chapter02/pics):  python3 umkehrfunktion_plots.py
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.size": 12,
    "mathtext.fontset": "cm",
    "svg.fonttype": "path",
})

BLAU = "#005A94"
ROT = "#C00000"
GRAU = "#888888"


def achsen(ax, xmin, xmax, ymin, ymax):
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_aspect("equal")
    ax.grid(True, color="#dddddd", linewidth=0.8)
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    for s in ["left", "bottom"]:
        ax.spines[s].set_position("zero")
        ax.spines[s].set_linewidth(1.2)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.text(xmax, 0.25, "$x$", ha="right", va="bottom", fontsize=14)
    ax.text(0.15, ymax, "$y$", ha="left", va="top", fontsize=14)
    ax.set_xticks(range(int(np.ceil(xmin)), int(xmax) + 1))
    ax.set_yticks(range(int(np.ceil(ymin)), int(ymax) + 1))
    ax.set_xticklabels([str(t) if t != 0 else "" for t in ax.get_xticks()])
    ax.set_yticklabels([str(t) if t != 0 else "" for t in ax.get_yticks()])


# 1) x^3 umkehrbar, x^2 nicht umkehrbar
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.6))
x = np.linspace(-2, 2, 400)

achsen(a1, -2.5, 2.5, -3, 3)
a1.plot(x, x**3, color=BLAU, linewidth=2.5)
x0 = 1.3
y0 = x0**3
a1.plot([0, x0], [y0, y0], "--", color=ROT, linewidth=1.5)
a1.plot([x0, x0], [y0, 0], "--", color=ROT, linewidth=1.5)
a1.plot([x0], [0], "o", color=ROT)
a1.text(-0.15, y0, "$y_0$", color=ROT, ha="right", va="center")
a1.text(x0, -0.25, "$x_0$", color=ROT, ha="center", va="top")
a1.text(-2.3, 2.4, "$f(x)=x^3$", color=BLAU, fontsize=14)
a1.set_title("umkehrbar: zu $y_0$ genau ein $x_0$", pad=18)

achsen(a2, -2.5, 2.5, -1, 5)
a2.plot(x, x**2, color=BLAU, linewidth=2.5)
x0 = 1.5
y0 = x0**2
a2.plot([-x0, x0], [y0, y0], "--", color=ROT, linewidth=1.5)
for xx in [-x0, x0]:
    a2.plot([xx, xx], [y0, 0], "--", color=ROT, linewidth=1.5)
    a2.plot([xx], [0], "o", color=ROT)
a2.text(0.1, y0 + 0.1, "$y_0$", color=ROT, ha="left", va="bottom")
a2.text(x0, -0.2, "$x_0$", color=ROT, ha="center", va="top")
a2.text(-x0, -0.2, "$-x_0$", color=ROT, ha="center", va="top")
a2.text(0.2, 4.0, "$f(x)=x^2$", color=BLAU, fontsize=14)
a2.set_title("nicht umkehrbar: zu $y_0$ zwei $x$-Werte", pad=18)

fig.tight_layout()
fig.savefig("umkehrfunktion_eindeutig.svg")
plt.close(fig)

# 2) f(x) = 1/4 x^3 - 2 und f^-1(x) = cbrt(4x + 8)
fig, ax = plt.subplots(figsize=(6, 6))
achsen(ax, -5, 5, -5, 5)
x = np.linspace(-5, 5, 600)
ax.plot(x, x, color=GRAU, linewidth=1.2, linestyle="--")
ax.plot(x, 0.25 * x**3 - 2, color=BLAU, linewidth=2.5)
ax.plot(x, np.cbrt(4 * x + 8), color=ROT, linewidth=2.5)
ax.text(2.4, -1.2, r"$f(x)=\frac{1}{4}x^3-2$", color=BLAU, fontsize=14)
ax.text(-0.8, 3.6, r"$f^{-1}(x)=\sqrt[3]{4x+8}$", color=ROT, fontsize=14, ha="right")
ax.text(-4.6, -3.6, "$y=x$", color=GRAU, fontsize=14)
ax.plot([0, -2], [-2, 0], "o", color="k", markersize=4)
ax.annotate("", xy=(-1.85, -0.15), xytext=(-0.15, -1.85),
            arrowprops=dict(arrowstyle="<->", color=GRAU, linewidth=1))
fig.tight_layout()
fig.savefig("umkehrfunktion_kubisch.svg")
plt.close(fig)

# 3) f(x) = x^2 für x >= 0 und f^-1(x) = sqrt(x)
fig, ax = plt.subplots(figsize=(6, 6))
achsen(ax, -1, 5, -1, 5)
x = np.linspace(0, 5, 400)
ax.plot([-1, 5], [-1, 5], color=GRAU, linewidth=1.2, linestyle="--")
xn = np.linspace(-1, 0, 100)
ax.plot(xn, xn**2, color=BLAU, linewidth=1.5, linestyle=":")
ax.plot(x, x**2, color=BLAU, linewidth=2.5)
ax.plot(x, np.sqrt(x), color=ROT, linewidth=2.5)
ax.text(2.4, 4.6, r"$f(x)=x^2,\ x\geq 0$", color=BLAU, fontsize=14)
ax.text(3.2, 1.35, r"$f^{-1}(x)=\sqrt{x}$", color=ROT, fontsize=14)
ax.text(4.1, 3.6, "$y=x$", color=GRAU, fontsize=14)
fig.tight_layout()
fig.savefig("umkehrfunktion_wurzel.svg")
plt.close(fig)
