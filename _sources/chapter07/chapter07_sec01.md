# 7.1 Determinanten

In den vorangegangenen Kapiteln haben wir Matrizen kennengelernt, die eine
besondere Struktur haben. In diesem Kapitel geht es um eine Eigenschaft von
quadratischen Matrizen, die durch eine Zahl gemessen wird und nützliche
Anwendungen hat, die sogenannte Determinante.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können die **Determinante** einer $(2\times 2)$-Matrix berechnen.
* Sie können die Determinante einer $(3\times 3)$-Matrix mit der **Regel von Sarrus** berechnen.
* Sie können die Determinante einer $(n\times n)$-Matrix mit $n>2$ berechnen,
  indem Sie den **Laplaceschen Entwicklungssatz** anwenden.
```

## Determinante von $(2\times 2)$-Matrizen

Die Determinante gibt es nur für quadratische Matrizen. Für eine $2\times
2$-Matrix

$$\mathbf{A} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

wird die Determinante durch den Ausdruck $a\cdot d - c\cdot b$ berechnet.Die
Determinante ordnet jeder quadratischen Matrix eine reelle Zahl zu. Diese
Eigenschaft ist also eine Funktion und wird in der Regel mit $\det$ abgekürzt.
Es gilt also

$$\det(\mathbf{A}) = a\cdot d - c\cdot b.$$

Manchmal werden auch zwei senkrechte Striche genommen, die die Matrixklammern
ersetzen, um die Determinante einer Matrix zu kennzeichnen:

$$\left|\begin{matrix} a & b \\ c & d \end{matrix}\right|
= a\cdot d - c\cdot b.$$

Wir betrachten ein Beispiel:

$$\det\begin{pmatrix} 2 & 3 \\ 1 & 5 \end{pmatrix} =
\left|\begin{matrix} 2 & 3 \\ 1 & 5 \end{matrix}\right| =
2\cdot 5 - 1\cdot 3 = 7.$$

## Determinante von $(3\times 3)$-Matrizen

Für $(3\times 3)$-Matrizen gibt es ein einfaches Rechenschema, die **Regel von Sarrus**. Für die Matrix

$$\mathbf{A} = \begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix}$$

schreibt man die ersten beiden Spalten noch einmal rechts neben die Matrix:

$$\begin{array}{ccc|cc} a & b & c & a & b \\ d & e & f & d & e \\ g & h & i & g & h \end{array}$$

Dann bildet man sechs Produkte aus je drei Faktoren entlang der Diagonalen:

* Die drei Produkte entlang der Diagonalen von links oben nach rechts unten werden **addiert**: $a\cdot e\cdot i$, $b\cdot f\cdot g$ und $c\cdot d\cdot h$.
* Die drei Produkte entlang der Diagonalen von rechts oben nach links unten werden **subtrahiert**: $c\cdot e\cdot g$, $a\cdot f\cdot h$ und $b\cdot d\cdot i$.

Insgesamt gilt also

$$\det(\mathbf{A}) = a\cdot e\cdot i + b\cdot f\cdot g + c\cdot d\cdot h - c\cdot e\cdot g - a\cdot f\cdot h - b\cdot d\cdot i.$$

Wir betrachten ein Beispiel. Für die Matrix

$$\mathbf{A} = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 4 \end{pmatrix}$$

schreiben wir die ersten beiden Spalten rechts daneben:

$$\begin{array}{ccc|cc} 1 & 2 & 0 & 1 & 2 \\ 2 & 1 & 0 & 2 & 1 \\ 0 & 0 & 4 & 0 & 0 \end{array}$$

Die Produkte entlang der Diagonalen von links oben nach rechts unten sind

$$1\cdot 1\cdot 4 + 2\cdot 0\cdot 0 + 0\cdot 2\cdot 0 = 4,$$

die Produkte entlang der Diagonalen von rechts oben nach links unten sind

$$0\cdot 1\cdot 0 + 1\cdot 0\cdot 0 + 2\cdot 2\cdot 4 = 16.$$

Damit ist

$$\det(\mathbf{A}) = 4 - 16 = -12.$$

```{admonition} Achtung
:class: warning
Die Regel von Sarrus gilt **nur** für $(3\times 3)$-Matrizen. Für größere Matrizen verwendet man den Laplaceschen Entwicklungssatz aus dem nächsten Abschnitt.
```

## Determinante von $(n\times n)$-Matrizen

Hat die Matrix eine höhere Dimension, wird die Determinante rekursiv aus den
Determinanten von kleineren Teilmatrizen berechnet. Dazu verwenden wir den
sogenannten **Laplaceschen Entwicklungssatz**.

Bei der Determinantenberechnung mit dem Laplaceschen Entwicklungssatz entwickeln
wir die Determinante nach einer Zeile oder einer Spalte. Wenn wir die
Determinante der Matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ nach der i-ten
Zeile entwickeln, gilt

$$\det(\mathbf{A}) = \sum_{j=1}^{n} a_{ij}\cdot
(-1)^{i+j}\cdot\det(\mathbf{A}_{ij}),$$

wobei $\mathbf{A_{ij}}$ diejenige Matrix ist, die entsteht, wenn die i-te Zeile
und j-te Spalte gestrichen werden.

Wird hingegen nach der j-ten Spalte entwickelt, lautet die Formel folgendermaßen:

$$\det(\mathbf{A}) = \sum_{i=1}^{n} a_{ij}\cdot
(-1)^{i+j}\cdot \det(\mathbf{A}_{ij}).$$

Auch hier bezeichnet $\mathbf{A}_{ij}$ die Untermatrix, die durch Streichen der
i-ten Zeile und j-ten Spalte entsteht.

Die Formeln sind trocken und schwer zu merken. Am einfachsten ist es, vorab die
Matrixelelemente mit einem Schachbrettmuster von Plus und Minus zu versehen, wie
in dem folgenden Video demonstriert wird.

```{dropdown} Video "Determinante - Laplace Entwicklungssatz" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/3cG0HWdmHLI?si=UT5KjVo88k9dNPoj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

```{admonition} Übung "Berechnung von (3×3)-Matrizen"
:class: miniexercise
Berechnen Sie auf der Internetseite
[https://matex.mint-kolleg.kit.edu/MATeX/](https://matex.mint-kolleg.kit.edu/MATeX/download.php?0ef5d0cbc6d9fc21b7ad04cc96f84ca4) solange Determinanten von $(3\times 3)$-Matrizen, bis Sie dreimal hintereinander eine Aufgabe korrekt gelöst haben.

Hinweis: Die Frage nach der Invertierbarkeit können Sie (voererst) ignorieren.
```

```{admonition} Übung "Berechnung von (4×4)-Matrizen"
:class: miniexercise
Berechnen Sie auf der Internetseite
[https://matex.mint-kolleg.kit.edu/MATeX/](https://matex.mint-kolleg.kit.edu/MATeX/download.php?6e6981333ada6c29ae902aae68873c0f) solange Determinanten von $(4\times 4)$-Matrizen, bis Sie dreimal hintereinander eine Aufgabe korrekt gelöst haben.

Hinweis: Die Frage nach der Invertierbarkeit können Sie (voererst) ignorieren.
```

## Eigenschaften von Determinanten

Die Determinante ist eine Eigenschaft von quadratischen Matrizen, aber sie
selbst hat auch wiederum Eigenschaften und Besonderheiten, die wir hier
notieren.

1. Die Determinante der Einheitmatrix ist Eins.
2. Die Determinante der transponierten Marix ist gleich der Determinanten der
   ursprünglichen Matrix.
3. Für quadratische Matrizen gleicher Dimension gilt:

   $$\det(\mathbf{A}\cdot\mathbf{B}) = \det(\mathbf{A})\cdot\det(\mathbf{B}).$$
4. Multipliziert man eine Zeile der Matrix mit einem Skalar, so wird auch die
   Determinante mit diesen Skalar multipliziert.
5. Ist $s$ ein Skalar und $\mathbf{A}$ eine quadratische Matrix der Dimension
   $(n\times n)$, dann gilt:

   $$\det(s\cdot\mathbf{A}) = s^{n}\cdot\det(\mathbf{A}).$$

6. Hat die Matrix eine Zeile oder eine Spalte, die komplett aus Nullen besteht,
   dann ist die Determinante Null.
7. Sind zwei Zeilen gleich, ist die Determinante Null.
8. Sind zwei Spalten gleich, ist die Determinante Null.
9. Vertauscht man zwei Zeilen, dann wechselt das Vorzeichen der Determinante.
10. Vertauscht man zwei Spalten, dann wechselt das Vorzeichen der Determinante.
11. Addiert man das Vielfache einer anderen Zeile(Spalte) zu einer anderen Zeile, dann
    ändert sich die Determinante nicht. Das kann man ausnutzen, um die
    Determinante einer Matrix beispielsweise mit dem Gauß-Algorithmus zu
    berechnen oder viele Nullen in der Matrix zu erzeugen.

Diese und weitere Rechenregeln werden auch in dem folgenden Video erläutert.

```{dropdown} Video "Rechenregeln für Determinanten" von MathePeter
<iframe width="560" height="315" src="https://www.youtube.com/embed/jDerrYHsLcY?si=NQI8V8OeTT034bKN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

Zunächst ist die Determinante nur eine Kennzahl einer quadratischen Matrix. Wir
haben uns in diesem Kapitel mit der Definition und den Rechenregeln beschäftigt.
In den nächsten Kapiteln werden wir die Determinante anwenden um beispielsweise
zu entscheiden, ob eine Matrix invertierbar ist oder um die Eigenwerte und
Eigenvektoren von Matrizen zu berechnen.
