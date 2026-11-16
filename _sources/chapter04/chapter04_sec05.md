# 4.5 Vektorprodukt

Nachdem wir uns zwei Kapitel lang mit dem Skalarprodukt beschäftigt haben,
werden wir in diesem Kapitel das Vektorprodukt kennenlernen. Im Gegensatz zum
Skalarprodukt ist das Ergebnis dieser Verknüpfung ein Vektor.

## Lernziele

```{admonition} Lernziele
:class: goals
- Sie können das **Vektorprodukt** von Vektoren in Komponentenschreibweise **ausrechnen**.
- Sie können folgende **Rechenregeln** anwenden:
  - Antikommutativgesetz: $\vec{a}\times\vec{b} =
    \textcolor{red}{-}\vec{b}\times\vec{a}$
  - Distributivgesetz Skalarmultiplikation:
    $s\cdot\left(\vec{a}\times\vec{b}\right) =
    \left(s\cdot\vec{a}\right)\times\vec{b} =
    \vec{a}\times\left(s\cdot\vec{b}\right)$
  - Distributivgesetz Addition: $\vec{a}\times\left(\vec{b}+\vec{c}\right) =
    \vec{a}\times\vec{b} + \vec{a}\times\vec{c}$
  - *kein* Assoziativgesetz:
    $\left(\vec{a}\times\vec{b}\right)\times\vec{c}\textcolor{red}{\,\neq\,}
    \vec{a}\times \left(\vec{b} \times \vec{c}\right)$.
- Sie wissen, wie das **Vektorprodukt** zweier Vektoren **geometrisch
  interpretiert** wird: Das Vektorprodukt der beiden Vektoren $\vec{a}$ und
  $\vec{b}$ ist der Vektor $\vec{c}$ für den gilt:
  - Die Richtung von $\vec{c}$ ist senkrecht zu $\vec{a}$ und senkrecht zu
    $\vec{b}$.
  - Die Vektoren $\vec{a}$, $\vec{b}$ und $\vec{c}$ bilden ein Rechtssystem.
  - Die Länge von $\vec{c}$ ist die Fläche des Parallelogramms, das durch
    $\vec{a}$ und $\vec{b}$ gebildet wird. Wenn
    $\varphi=\angle(\vec{a},\vec{b})$ der eingeschlossene Winkel zwischen
    $\vec{a}$ und $\vec{b}$ ist, dann gilt:

    $$|\vec{a}\times\vec{b}| = |\vec{a}|\cdot|\vec{b}|\cdot\sin(\varphi).$$
```

## Vektorprodukt

Das Skalarprodukt ist eine Verknüpfung von zwei Vektoren, bei der das Ergebnis
ein Skalar ist. Jetzt wollen wir einen Verknüpfung von zwei Vektoren einführen,
bei der das Ergebnis ein Vektor ist. Diese Verknüpfung hat eine sehr wichtige
Besonderheit: es gibt sie nur im dreidimensionalen Standardvektorraum
$\mathbb{R}^3$.

Um das **Vektorprodukt** zu erklären, nehmen wir ein Beispiel aus dem Video
["Kreuzprodukt zweier Vektoren"](https://youtu.be/tg9oiUPdrFc?feature=shared)
von VisualX, nämlich die beiden 3D-Vektoren

$$\vec{a} = \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix} \; \text{ und } \;
\vec{b} = \begin{pmatrix} 3 \\ 0 \\ 2 \end{pmatrix}.$$

Das Vektorprodukt wird berechnet als

$$\vec{a} \times \vec{b} =
\begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix} \times \begin{pmatrix} 3 \\ 0 \\ 2 \end{pmatrix} =
\begin{pmatrix} 2\cdot 2 -(-1)\cdot 0 \\-1\cdot 3 -1\cdot 2 \\1\cdot 0 - 2\cdot 3\end{pmatrix}=
\begin{pmatrix} 4 \\-5 \\-6\end{pmatrix}.$$

Die genaue Formel zur Berechnung lautet

$$\vec{a} \times \vec{b} =
\begin{pmatrix}a_1\\a_2\\a_3\end{pmatrix} \times \begin{pmatrix}b_1\\b_2\\b_3\end{pmatrix}=
\begin{pmatrix}a_2 b_3 - a_3 b_2 \\ a_3 b_1 - a_1 b_3\\a_1 b_2 - a_2 b_1\end{pmatrix}.$$

```{admonition} Was ist ... das Vektorprodukt?
:class: note
In einem rechtshändischen kartesischen Koordinatensystem $\mathbb{R}^3$ wird das
Vektorprodukt zweier Vektoren $\vec{a}$ und $\vec{b}$ defininert als

$$\vec{a} \times \vec{b} =
\begin{pmatrix}a_1\\a_2\\a_3\end{pmatrix} \times \begin{pmatrix}b_1\\b_2\\b_3\end{pmatrix}=
\begin{pmatrix}a_2 b_3 - a_3 b_2 \\ a_3 b_1 - a_1 b_3\\a_1 b_2 - a_2 b_1\end{pmatrix}.$$

Das Vektorprodukt wird auch manchmal Kreuzprodukt genannt.
```

Die Formel zur Berechnung des Vektorproduktes ist leider nicht ganz einfach zu
merken. Daher werden im folgenden Video zwei Merkregeln vorgestellt. Wundern Sie
sich nicht, wenn im Video von Kreizprodukt gesprochen wird. Das ist eine
alternative Bezeichnung für das Vektorprodukt, die von dem Symbol $\times$
kommt.

```{dropdown} Video "Kreuzprodukt zweier Vektoren" von VisualX
<iframe width="560" height="315" src="https://www.youtube.com/embed/tg9oiUPdrFc"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Rechenregeln

Für das Vektorprodukt gelten einige Rechenregeln, die zuerst nicht intuitiv
sind.

Das Vektorprodukt ist nicht kommutativ, sondern **antikommutativ**. Wir greifen
das obige Beispiel erneut auf:

$$\vec{a} \times \vec{b} = \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix} \times
\begin{pmatrix} 3 \\ 0 \\ 2 \end{pmatrix} = \begin{pmatrix} 4 \\-5
\\-6\end{pmatrix}.$$

Wenn wir nun $\vec{b}\times\vec{a}$ ausrechnen, erhalten wir aber

$$\begin{pmatrix} 3 \\ 0 \\ 2 \end{pmatrix}\times\begin{pmatrix} 1 \\ 2 \\ -1
\end{pmatrix}= \begin{pmatrix} -4 \\5 \\6\end{pmatrix}.$$

Das ist der Gegenvektor zu $\vec{a}\times\vec{b}$. Das ist kein Zufall.
Tatsächlich können wir beweisen, dass immer das Antikommutativgesetz

$$\vec{a}\times\vec{b} = \textcolor{red}{-}\vec{b}\times\vec{a}$$

für alle Vektoren $\vec{a}\in\mathbb{R}^3$ und $\vec{b}\in\mathbb{R}^3$ gilt.

Die Regel für die Mischung von Skalarmultiplikation und Vektorprodukt sind
wieder natürlich. Es gilt

 $$s\cdot\left(\vec{a}\times\vec{b}\right) = \left(s\cdot\vec{a}\right)\times\vec{b} =
\vec{a}\times\left(s\cdot\vec{b}\right).$$

Es gilt also das **Distributivgesetz für die Skalarmultiplikation**. Ebenso gilt
das **Distributivgesetz für die Addition**, also

$$\vec{a}\times\left(\vec{b}+\vec{c}\right) = \vec{a}\times\vec{b} +
\vec{a}\times\vec{c}.$$

Umgekehrt halten wir noch fest, dass das Vektorprodukt **nicht assoziativ** ist.
Allgemein gilt also

$$\left(\vec{a}\times\vec{b}\right)\times\vec{c}
  \textcolor{red}{\, \neq \, } \vec{a}\times \left(\vec{b} \times
  \vec{c}\right).$$

## Geometrische Interpretation Vektorprodukt

Das Vektorprodukt wurde eingeführt, dass es zwei sehr spannende Anwendungen in
der Geometrie hat, die viele Rechnungen deutlich vereinfachen. Halten wir
zunächst einmal folgende Beobachtung fest. Der Vektor $\vec{n} =
\vec{a}\times\vec{b}$ steht senkrecht auf dem Vektor $\vec{a}$ und senkrecht auf
dem Vektor $\vec{b}$.

Probieren wir zunächst ein Beispiel. Wir greifen wieder auf das Beispiel von
oben zurück, d.h. wir nehmen die beiden Vektoren

$$\vec{a} = \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix} \; \text{ und } \;
\vec{b} = \begin{pmatrix} 3 \\ 0 \\ 2 \end{pmatrix}.$$

Das Kreuzprodukt ist dann

$$\vec{n} = \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix} \times
\begin{pmatrix} 3 \\ 0 \\ 2 \end{pmatrix} = \begin{pmatrix} 4 \\-5
\\-6\end{pmatrix}.$$

Als erstes testen wir, ob $\vec{n}$ senkrecht auf $\vec{a}$ steht und berechnen
dazu das Skalarprodukt:

$$\vec{n}\cdot\vec{a} = \begin{pmatrix} 4 \\-5 \\-6\end{pmatrix}\cdot
\begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix} =
4\cdot 1 + (-5)\cdot 2 + (-6)\cdot (-1) = 0.$$

Da das Skalarprodukt der beiden Vektoren Null ist, steht $\vec{n}$ senkrecht auf
$\vec{a}$. Als zweites testen wir $\vec{n}$ und $\vec{b}$.

$$\vec{n}\cdot\vec{b} = \begin{pmatrix} 3 \\ 0 \\ 2 \end{pmatrix}\cdot
\begin{pmatrix} 4 \\-5 \\-6\end{pmatrix} = 3\cdot 4 + 0\cdot (-5) + 2\cdot (-6)
= 0.$$

Nur weil bei unserem Beispiel das Vektorprodukt$\vec{a}\times\vec{b}$ senkrecht
auf $\vec{a}$ und $\vec{b}$ steht, muss das nicht immer so sein. Das könnte auch
Zufall gewesen sein. Schauen wir uns also allgemein an, was
$\vec{n}\cdot\vec{a}$ und $\vec{n}\cdot\vec{b}$ ergeben.

$$\begin{aligned}
\vec{n}\cdot\vec{a} &= (\vec{a}\times\vec{b})\cdot\vec{a} =
\begin{pmatrix}a_2 b_3 - a_3 b_2 \\ a_3 b_1 - a_1 b_3\\a_1 b_2 - a_2 b_1\end{pmatrix}
\cdot \begin{pmatrix}a_1\\a_2\\a_3\end{pmatrix} \\
&= (a_2 b_3 - a_3 b_2)\cdot a_1 + (a_3 b_1 - a_1 b_3)\cdot a_2 + (a_1 b_2 - a_2 b_1)\cdot a_3\\
&= a_1 a_2 b_3 - a_1 a_3 b_2 + a_2 a_3 b_1 - a_1 a_2 b_3 + a_1 a_2 b_3 - a_2 a_3 b_1 \\
&= 0
\end{aligned}$$

Die Rechnung $\vec{n}\cdot\vec{b}$ funktioniert genauso und ergibt ebenfalls $0$.

Etwas kniffliger ist der Nachweis, dass die Länge des Vektorproduktes gleich dem
Flächeninhalt des Parallelogramms ist, das die Vektoren $\vec{a}$ und $\vec{b}$
aufspannen. Den Beweis können Sie sich in dem folgenden Video ansehen.

```{dropdown} Video "Kreuzprodukt geometrisch" von VisualX
<iframe width="560" height="315" src="https://www.youtube.com/embed/vhfwxWjHqeI"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

Halten wir also die geometrische Interpretation des Vektorproduktes fest.

`````{admonition} Wie wird das Vektorprodukt geometrisch interpretiert?
:class: note
Das Vektorprodukt $\vec{n}=\vec{a}\times\vec{b}$ ist ein Vektor, der sowohl auf
dem Vektor $\vec{a}$ als auf dem Vektor $\vec{b}$ senkrecht steht. Die drei
Vektoren bilden zusammen ein Rechtssystem. Die Länge $|\vec{n}|$ des Vektors
$\vec{n}$ ist gleich dem Flächeninhalt $A$ des Parallelogramms, das die beiden
Vektoren $\vec{a}$ und $\vec{b}$ aufspannen. Es gilt

$$|\vec{n}| = A = |\vec{a}\times\vec{b}| =
|\vec{a}|\cdot|\vec{b}|\cdot\sin(\varphi),$$

wobei $\varphi=\angle(\vec{a},\vec{b})$ der eingeschlossene Winkel zwischen
$\vec{a}$ und $\vec{b}$ ist.

````{dropdown} Begründung
:class-container: ohne-formelnummern
**1. Schritt: Flächeninhalt des Parallelogramms.** Der Flächeninhalt eines
Parallelogramms ist Grundseite mal Höhe. Als Grundseite nehmen wir den Vektor
$\vec{a}$, sie hat also die Länge $|\vec{a}|$. Die Höhe $h$ ist der Abstand der
Spitze von $\vec{b}$ zur Grundseite.

```{image} pics/parallelogramm_flaeche.svg
:alt: Parallelogramm aus den Vektoren a und b mit eingeschlossenem Winkel phi und Höhe h
:width: 420px
:align: center
```

Im rechtwinkligen Dreieck mit der Hypotenuse $|\vec{b}|$ ist $h$ die
Gegenkathete des Winkels $\varphi$, also

$$\sin(\varphi) = \frac{h}{|\vec{b}|} \quad\Longrightarrow\quad h = |\vec{b}|\cdot\sin(\varphi).$$

(Ist $\varphi$ stumpf, liegt im rechtwinkligen Dreieck der Winkel
$\pi-\varphi$, und wegen $\sin(\pi-\varphi)=\sin(\varphi)$ ergibt sich dieselbe
Höhe.) Damit ist

$$A = |\vec{a}|\cdot h = |\vec{a}|\cdot|\vec{b}|\cdot\sin(\varphi).$$

**2. Schritt: Betrag des Vektorprodukts zum Quadrat.** Wir quadrieren den Betrag
des Vektorprodukts, damit keine Wurzel stört, und multiplizieren aus:

$$\begin{aligned}
|\vec{a}\times\vec{b}|^2 &= (a_2 b_3 - a_3 b_2)^2 + (a_3 b_1 - a_1 b_3)^2\\
&\quad {}+ (a_1 b_2 - a_2 b_1)^2\\
&= a_1^2 b_2^2 + a_1^2 b_3^2 + a_2^2 b_1^2 + a_2^2 b_3^2 + a_3^2 b_1^2 + a_3^2 b_2^2\\
&\quad {}- 2\,a_1 a_2 b_1 b_2 - 2\,a_1 a_3 b_1 b_3 - 2\,a_2 a_3 b_2 b_3.
\end{aligned}$$

Dasselbe kommt heraus, wenn wir $|\vec{a}|^2\cdot|\vec{b}|^2 - (\vec{a}\cdot\vec{b})^2$
ausrechnen. Es ist

$$\begin{aligned}
|\vec{a}|^2\cdot|\vec{b}|^2 &= (a_1^2 + a_2^2 + a_3^2)\cdot(b_1^2 + b_2^2 + b_3^2)\\
&= a_1^2 b_1^2 + a_2^2 b_2^2 + a_3^2 b_3^2\\
&\quad {}+ a_1^2 b_2^2 + a_1^2 b_3^2 + a_2^2 b_1^2 + a_2^2 b_3^2 + a_3^2 b_1^2 + a_3^2 b_2^2
\end{aligned}$$

und

$$\begin{aligned}
(\vec{a}\cdot\vec{b})^2 &= (a_1 b_1 + a_2 b_2 + a_3 b_3)^2\\
&= a_1^2 b_1^2 + a_2^2 b_2^2 + a_3^2 b_3^2\\
&\quad {}+ 2\,a_1 a_2 b_1 b_2 + 2\,a_1 a_3 b_1 b_3 + 2\,a_2 a_3 b_2 b_3.
\end{aligned}$$

Beim Abziehen fallen die Terme $a_1^2 b_1^2$, $a_2^2 b_2^2$ und $a_3^2 b_3^2$
weg, und es bleibt genau der Ausdruck für $|\vec{a}\times\vec{b}|^2$ von oben
übrig. Also gilt

$$|\vec{a}\times\vec{b}|^2 = |\vec{a}|^2\cdot|\vec{b}|^2 - (\vec{a}\cdot\vec{b})^2.$$

Jetzt setzen wir für das Skalarprodukt
$\vec{a}\cdot\vec{b} = |\vec{a}|\cdot|\vec{b}|\cdot\cos(\varphi)$ ein und
benutzen $\sin^2(\varphi) + \cos^2(\varphi) = 1$:

$$\begin{aligned}
|\vec{a}\times\vec{b}|^2 &= |\vec{a}|^2\cdot|\vec{b}|^2 - \left(|\vec{a}|\cdot|\vec{b}|\cdot\cos(\varphi)\right)^2\\
&= |\vec{a}|^2\cdot|\vec{b}|^2 - |\vec{a}|^2\cdot|\vec{b}|^2\cdot\cos^2(\varphi)\\
&= |\vec{a}|^2\cdot|\vec{b}|^2\cdot\left(1 - \cos^2(\varphi)\right)\\
&= |\vec{a}|^2\cdot|\vec{b}|^2\cdot\sin^2(\varphi).
\end{aligned}$$

**3. Schritt: Wurzel ziehen.** Beim Wurzelziehen müssen wir auf das Vorzeichen
achten, denn $\sqrt{x^2} = |x|$:

$$|\vec{a}\times\vec{b}| = |\vec{a}|\cdot|\vec{b}|\cdot|\sin(\varphi)|.$$

Der Winkel zwischen zwei Vektoren liegt immer im Bereich $0 \le \varphi \le \pi$,
und dort ist $\sin(\varphi) \ge 0$. Die Betragsstriche um $\sin(\varphi)$
können also entfallen, und mit dem 1. Schritt folgt

$$|\vec{a}\times\vec{b}| = |\vec{a}|\cdot|\vec{b}|\cdot\sin(\varphi) = A.$$
````
`````

## Zusammenfassung und Ausblick

Das Vektorprodukt gibt es nur im dreidimensionalen Vektorraum, da es geometrisch
motiviert ist. Mit dem Spatprodukt, das im nächsten Kapitel erläutert wird,
werden wir erneut ein Hilfsmittel erhalten, um geometrische Probleme zu lösen.
