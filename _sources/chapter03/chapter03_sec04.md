# 3.4 Vektoren und Punkte

Im letzten Abschnitt haben wir Punkte durch ihre Koordinaten beschrieben und
Vektoren als Verschiebungen kennengelernt. Jetzt bringen wir beides zusammen:
Wir verschieben einen Punkt mit einem Vektor und erhalten wieder einen Punkt.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können zwischen **Punkten** (Orten) und **Vektoren** (Verschiebungen)
  unterscheiden.
* Sie können einen Punkt mit einem Vektor verschieben (**Punkt + Vektor =
  Punkt**) und den **Verbindungsvektor** zweier Punkte berechnen (**Punkt −
  Punkt = Vektor**).
* Sie wissen, welche Rechnungen mit Punkten und Vektoren sinnvoll sind und
  welche nicht.
```

## Punkte und Vektoren

Ein **Punkt** beschreibt einen Ort, zum Beispiel $P(3,2)$. Ein **Vektor**
beschreibt eine Verschiebung, also eine Bewegung um eine bestimmte Strecke in
eine bestimmte Richtung, zum Beispiel

$$\vec{v} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}.$$

Ein Vektor hat keinen festen Ort. Jeder Pfeil, der zwei Einheiten nach rechts
und eine Einheit nach oben zeigt, stellt denselben Vektor $\vec{v}$ dar, egal
wo er gezeichnet wird.

## Punkt plus Vektor ergibt Punkt

Wenden wir die Verschiebung $\vec{v}$ auf den Punkt $P$ an, landen wir bei
einem neuen Punkt $Q$. Wir schreiben dafür

$$P + \vec{v} = Q.$$

Gerechnet wird komponentenweise. Dazu schreiben wir auch die Koordinaten des
Punktes als Spalte:

$$\begin{pmatrix} 3 \\ 2 \end{pmatrix} + \begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 5 \\ 3 \end{pmatrix},$$

also $Q(5,3)$.

Die Schreibweise sieht aus wie eine Vektoraddition, es werden aber zwei
verschiedene Objekte verknüpft: ein Ort und eine Bewegung. Das Ergebnis ist
wieder ein Ort.

Führen wir zwei Verschiebungen nacheinander aus, ist es egal, ob wir den Punkt
zweimal verschieben oder die beiden Verschiebungen erst zu einer
zusammenfassen:

$$(P + \vec{v}) + \vec{w} = P + (\vec{v} + \vec{w}).$$

```{figure} pics/affiner_punktraum_2D.png
---
width: 75%
name: affiner_punktraum_2D
---
Verschieben von $P(3,2)$ erst um $\vec{v}$ und dann um $\vec{w}$ führt zum
selben Punkt $R(1,6)$ wie das Verschieben um $\vec{v}+\vec{w}$
(Quelle: eigene Darstellung; Lizenz: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0))
```

Mit $\vec{w} = \begin{pmatrix} -4 \\ 3 \end{pmatrix}$ ergibt sich auf beiden
Wegen

$$\begin{pmatrix} 3 \\ 2 \end{pmatrix} + \begin{pmatrix} 2 \\ 1 \end{pmatrix} + \begin{pmatrix} -4 \\ 3 \end{pmatrix} = \begin{pmatrix} 1 \\ 6 \end{pmatrix}.$$

## Punkt minus Punkt ergibt Vektor

Zu zwei Punkten $P$ und $Q$ gibt es genau eine Verschiebung, die $P$ nach $Q$
bringt. Sie heißt **Verbindungsvektor** und wird mit $\overrightarrow{PQ}$
bezeichnet. Aus $P + \overrightarrow{PQ} = Q$ folgt

$$\overrightarrow{PQ} = Q - P.$$

Man rechnet also »Spitze minus Fuß«. Im Beispiel:

$$\overrightarrow{PQ} = \begin{pmatrix} 5 \\ 3 \end{pmatrix} - \begin{pmatrix} 3 \\ 2 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}.$$

Wählt man für $P$ den Koordinatenursprung $O$, erhält man den **Ortsvektor**
$\overrightarrow{OQ}$. Er hat dieselben Komponenten wie die Koordinaten von
$Q$. Deshalb dürfen wir mit den Koordinaten von Punkten so rechnen wie mit
Vektoren.

## Was darf man rechnen?

```{admonition} Rechenregeln für Punkte und Vektoren
:class: note
* Punkt $+$ Vektor $=$ Punkt
* Punkt $-$ Punkt $=$ Vektor
* Vektor $+$ Vektor $=$ Vektor
* Punkt $+$ Punkt ist nicht definiert.
```

Dass Punkt plus Punkt keinen Sinn ergibt, sieht man an einem Vergleich: Hamburg
plus Berlin ist kein Ort. Hamburg plus »rund 250 km nach Osten« dagegen schon,
nämlich ungefähr Berlin. Rechnerisch zeigt sich das daran, dass die Summe der
Koordinaten zweier Punkte davon abhängt, wo man den Ursprung des
Koordinatensystems hinlegt.

Eine Ausnahme scheint der **Mittelpunkt** $M$ der Strecke $PQ$ zu sein, den man
oft als $M = \frac{1}{2}(P + Q)$ schreibt. Sauber gelesen ist das aber Punkt
plus Vektor, denn man geht von $P$ aus die halbe Strecke in Richtung $Q$:

$$M = P + \tfrac{1}{2}\,\overrightarrow{PQ}.$$

Mit $\overrightarrow{PQ} = Q - P$ und komponentenweiser Rechnung in
Koordinaten erhalten wir daraus wieder die bekannte Formel:

$$M = P + \tfrac{1}{2}(Q - P) = P + \tfrac{1}{2}Q - \tfrac{1}{2}P = \tfrac{1}{2}P + \tfrac{1}{2}Q = \tfrac{1}{2}(P + Q).$$

Im Beispiel ist

$$M = \begin{pmatrix} 3 \\ 2 \end{pmatrix} + \frac{1}{2}\begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 4 \\ 2{,}5 \end{pmatrix}.$$

Alles hier gilt genauso im $\mathbb{R}^3$ und allgemein im $\mathbb{R}^n$:
Gerechnet wird immer komponentenweise.

## Vertiefung: Der affine Punktraum

````{dropdown} Mathematische Definition
Die Regeln oben lassen sich exakt fassen. Gegeben sind eine nichtleere Menge
$A$, deren Elemente wir Punkte nennen, ein reeller Vektorraum $V$ und eine
Verknüpfung $+: A\times V \to A$. Man spricht von einem **affinen Punktraum**,
wenn gilt:

1. Für alle Punkte $P \in A$ gilt $P + \vec{0} = P$.
2. Für alle Punkte $P, Q \in A$ gibt es genau einen Vektor $\vec{v} \in V$ mit
   $P + \vec{v} = Q$.
3. Für alle Punkte $P \in A$ und Vektoren $\vec{v}, \vec{w} \in V$ gilt
   $P + (\vec{v} + \vec{w}) = (P + \vec{v}) + \vec{w}$.

Eigenschaft 2 liefert den Verbindungsvektor $\overrightarrow{PQ}$, Eigenschaft 3
das Hintereinanderausführen von Verschiebungen.

Für $A = \mathbb{R}^n$ mit der komponentenweisen Addition

$$\begin{pmatrix} P_1 \\ \vdots \\ P_n \end{pmatrix} + \begin{pmatrix} v_1 \\ \vdots \\ v_n \end{pmatrix} = \begin{pmatrix} P_1 + v_1 \\ \vdots \\ P_n + v_n \end{pmatrix}$$

sind alle drei Eigenschaften erfüllt. Eigenschaft 1 gilt, weil $P_i + 0 = P_i$
ist. Für Eigenschaft 2 ist $v_i = Q_i - P_i$ die einzige Wahl. Eigenschaft 3
folgt aus $P_i + (v_i + w_i) = (P_i + v_i) + w_i$, also aus dem
Assoziativgesetz der reellen Zahlen.
````

## Zusammenfassung und Ausblick

Punkte beschreiben Orte, Vektoren beschreiben Verschiebungen. Mit Punkt + Vektor
= Punkt und Punkt − Punkt = Vektor können wir geometrische Probleme algebraisch
beschreiben. In den nächsten Kapiteln nutzen wir das, um Geraden und Ebenen
darzustellen.
