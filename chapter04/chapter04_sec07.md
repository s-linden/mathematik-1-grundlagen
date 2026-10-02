# Übungen zum Selbststudium

Hinweis: $\vec{e}_{a}$ bezeichnet den Einheitsvektor in Richtung des Vektors $\vec{a}$.

```{admonition} Übung 4.1
:class: miniexercise
Gegeben seien die Vektoren

$$\vec{u}=\begin{pmatrix} 4 \\ 0 \\ -2 \end{pmatrix},\quad \vec{v}=\begin{pmatrix} 3 \\ 1 \\ -1 \end{pmatrix},\quad \vec{w}=\begin{pmatrix} 2 \\ 1 \\ 6 \end{pmatrix},\quad \vec{s}=\begin{pmatrix} 1 \\ 4 \\ 1 \end{pmatrix}$$

Berechnen Sie die folgenden Ausdrücke. Ist das Ergebnis eine Zahl oder ein Vektor?

a) $\vec{u}\cdot\vec{v}$

b) $\vec{v}\cdot\vec{s}$

c) $\vec{e}_{w}$

d) $(\vec{v}\cdot\vec{s})\cdot\vec{e}_{u}$

e) $(\vec{u}\cdot\vec{w})\cdot(\vec{v}\cdot\vec{s})$

f) $(\vec{u}\cdot\vec{e}_{1})\cdot\vec{v}+(\vec{w}\cdot\vec{s})\cdot\vec{e}_{3}$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $\vec{u}\cdot\vec{v}=14$

b) $\vec{v}\cdot\vec{s}=6$

c) $\vec{e}_{w}=\frac{1}{\sqrt{41}}\begin{pmatrix} 2 \\ 1 \\ 6 \end{pmatrix}$

d) $(\vec{v}\cdot\vec{s})\vec{e}_{u}=\frac{1}{\sqrt{5}}\begin{pmatrix} 12 \\ 0 \\ -6 \end{pmatrix}$

e) $(\vec{u}\cdot\vec{w})(\vec{v}\cdot\vec{s})=-24$

f) $(\vec{u}\cdot\vec{e}_{1})\vec{v}+(\vec{w}\cdot\vec{s})\vec{e}_{3}=\begin{pmatrix} 12 \\ 4 \\ 8 \end{pmatrix}$

```{dropdown} Lösungsweg
a)

$$\vec{u}\cdot\vec{v}=\begin{pmatrix} 4 \\ 0 \\ -2 \end{pmatrix}\cdot\begin{pmatrix} 3 \\ 1 \\ -1 \end{pmatrix}=4\cdot3+0\cdot1+(-2)(-1)=14$$

b)

$$\vec{v}\cdot\vec{s}=\begin{pmatrix} 3 \\ 1 \\ -1 \end{pmatrix}\cdot\begin{pmatrix} 1 \\ 4 \\ 1 \end{pmatrix}=3\cdot1+1\cdot4+(-1)\cdot1=6$$

c)

$$\vec{e}_{w}=\frac{1}{|\vec{w}|}\vec{w}=\frac{1}{\sqrt{{2}^{2}+{1}^{2}+{6}^{2}}}\begin{pmatrix} 2 \\ 1 \\ 6 \end{pmatrix}=\frac{1}{\sqrt{41}}\begin{pmatrix} 2 \\ 1 \\ 6 \end{pmatrix}$$

d)

$$
\begin{aligned}
(\vec{v}\cdot\vec{s})\vec{e}_{u}&=6\cdot\frac{1}{\sqrt{{4}^{2}+{(-2)}^{2}}}\begin{pmatrix} 4 \\ 0 \\ -2 \end{pmatrix}=6\cdot\frac{1}{\sqrt{20}}\begin{pmatrix} 4 \\ 0 \\ -2 \end{pmatrix}=6\cdot\frac{1}{\sqrt{5\cdot4}}\begin{pmatrix} 4 \\ 0 \\ -2 \end{pmatrix} \\
&=6\cdot\frac{1}{2\sqrt{5}}\begin{pmatrix} 4 \\ 0 \\ -2 \end{pmatrix}=3\cdot\frac{1}{\sqrt{5}}\begin{pmatrix} 4 \\ 0 \\ -2 \end{pmatrix}=\frac{1}{\sqrt{5}}\begin{pmatrix} 12 \\ 0 \\ -6 \end{pmatrix}
\end{aligned}
$$

e)

$$(\vec{u}\cdot\vec{w})(\vec{v}\cdot\vec{s})=\begin{pmatrix} 4 \\ 0 \\ -2 \end{pmatrix}\cdot\begin{pmatrix} 2 \\ 1 \\ 6 \end{pmatrix}\cdot6=[4\cdot2+(-2)\cdot6]\cdot6=-24$$

f)

$$
\begin{aligned}
(\vec{u}\cdot\vec{e}_{1})\vec{v}+(\vec{w}\cdot\vec{s})\vec{e}_{3}&=\left[ \begin{pmatrix} 4 \\ 0 \\ -2 \end{pmatrix}\cdot\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \right]\cdot\begin{pmatrix} 3 \\ 1 \\ -1 \end{pmatrix}+\left[ \begin{pmatrix} 2 \\ 1 \\ 6 \end{pmatrix}\cdot\begin{pmatrix} 1 \\ 4 \\ 1 \end{pmatrix} \right]\cdot\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \\
&=(4\cdot1)\cdot\begin{pmatrix} 3 \\ 1 \\ -1 \end{pmatrix}+(2\cdot1+1\cdot4+6\cdot1)\cdot\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \\
&=\begin{pmatrix} 12 \\ 4 \\ -4 \end{pmatrix}+\begin{pmatrix} 0 \\ 0 \\ 12 \end{pmatrix} \\
&=\begin{pmatrix} 12 \\ 4 \\ 8 \end{pmatrix}
\end{aligned}
$$
```
````

```{admonition} Übung 4.2
:class: miniexercise
Gegeben seien $\vec{u}$, $\vec{v}$, $\vec{w}$ und $\vec{s}$ wie in Aufgabe 4.1. Berechnen Sie

a) den Winkel zwischen $\vec{u}$ und $\vec{w}$,

b) den Winkel zwischen $\vec{v}$ und $\vec{s}$,

c) den Wert $\lambda$, für den $\vec{u}+\lambda\vec{e}_{3}$ und $\vec{v}-\lambda\vec{e}_{1}$ senkrecht aufeinander stehen,

d) den Wert $\mu$, für den $\vec{w}+\mu\vec{e}_{1}$ und $\vec{s}-\mu\vec{e}_{1}$ senkrecht aufeinander stehen.
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $\varphi=98{,}03^\circ\quad \text{oder}\quad 1{,}7111\,\mathrm{rad}$

b) $\varphi=64{,}76^\circ\quad \text{oder}\quad 1{,}130\,\mathrm{rad}$

c) $\lambda=\frac{14}{5}$

d) ${\mu}_{1}=3,\quad {\mu}_{2}=-4$

```{dropdown} Lösungsweg
Der Winkel $\varphi$ zwischen zwei Vektoren $\vec{a}$ und $\vec{b}$ lässt sich mithilfe folgender Formel berechnen:

$$\cos (\varphi)=\frac{\mathbf{a}\cdot\mathbf{b}}{|\mathbf{a}|\cdot|\mathbf{b}|}$$

a)

$$
\begin{aligned}
\cos (\varphi)&=\frac{\vec{u}\cdot\vec{w}}{|\vec{u}|\cdot|\vec{w}|}=\frac{4\cdot2+(-2)\cdot6}{\sqrt{{4}^{2}+{(-2)}^{2}}\cdot\sqrt{{2}^{2}+{1}^{2}+{6}^{2}}}=\frac{{\color{red} -4}}{\sqrt{20}\cdot\sqrt{41}} \\
\varphi&=98{,}03^\circ\quad \text{oder}\quad 1{,}7111\,\mathrm{rad}
\end{aligned}
$$

b)

$$
\begin{aligned}
\cos (\varphi)&=\frac{\vec{v}\cdot\vec{s}}{|\vec{v}|\cdot|\vec{s}|}=\frac{6}{\sqrt{{3}^{2}+{1}^{2}+{(-1)}^{2}}\cdot\sqrt{{1}^{2}+{4}^{2}+{1}^{2}}}=\frac{6}{\sqrt{11}\cdot\sqrt{18}} \\
\varphi&=64{,}76^\circ\quad \text{oder}\quad 1{,}130\,\mathrm{rad}
\end{aligned}
$$

c)

$$
\begin{aligned}
\vec{u}+\lambda\vec{e}_{3}&=\begin{pmatrix} 4 \\ 0 \\ -2 \end{pmatrix}+\begin{pmatrix} 0 \\ 0 \\ \lambda \end{pmatrix}=\begin{pmatrix} 4 \\ 0 \\ -2+\lambda \end{pmatrix} \\
\vec{v}-\lambda\vec{e}_{1}&=\begin{pmatrix} 3 \\ 1 \\ -1 \end{pmatrix}-\begin{pmatrix} \lambda \\ 0 \\ 0 \end{pmatrix}=\begin{pmatrix} 3-\lambda \\ 1 \\ -1 \end{pmatrix}
\end{aligned}
$$

Die Vektoren stehen senkrecht aufeinander, wenn das Skalarprodukt zu null wird.

$$\begin{array}{lrcl} & (\vec{u}+\lambda\vec{e}_{3})\cdot(\vec{v}-\lambda\vec{e}_{1}) & = & 0 \\ \Rightarrow & \begin{pmatrix} 4 \\ 0 \\ -2+\lambda \end{pmatrix}\cdot\begin{pmatrix} 3-\lambda \\ 1 \\ -1 \end{pmatrix} & = & 0 \\ \Rightarrow & 4\cdot(3-\lambda)+(-2+\lambda)(-1) & = & 0 \\ \Rightarrow & 12-4\lambda+2-\lambda & = & 0 \\ \Rightarrow & 14 & = & 5\lambda \\ \Rightarrow & \lambda & = & \frac{14}{5} \end{array}$$

d)

Gesucht wird der Wert $\mu$, für den $\vec{w}+\mu\vec{e}_{1}$ und $\vec{s}-\mu\vec{e}_{1}$ senkrecht aufeinander stehen.

$$
\begin{aligned}
\vec{w}+\mu\vec{e}_{1}&=\begin{pmatrix} 2 \\ 1 \\ 6 \end{pmatrix}+\begin{pmatrix} \mu \\ 0 \\ 0 \end{pmatrix}=\begin{pmatrix} 2+\mu \\ 1 \\ 6 \end{pmatrix} \\
\vec{s}-\mu\vec{e}_{1}&=\begin{pmatrix} 1 \\ 4 \\ 1 \end{pmatrix}-\begin{pmatrix} \mu \\ 0 \\ 0 \end{pmatrix}=\begin{pmatrix} 1-\mu \\ 4 \\ 1 \end{pmatrix}
\end{aligned}
$$

$$\begin{array}{lrcl} & (\vec{w}+\mu\vec{e}_{1})\cdot(\vec{s}-\mu\vec{e}_{1}) & = & 0 \\ \Rightarrow & \begin{pmatrix} 2+\mu \\ 1 \\ 6 \end{pmatrix}\cdot\begin{pmatrix} 1-\mu \\ 4 \\ 1 \end{pmatrix} & = & 0 \\ \Rightarrow & (2+\mu)(1-\mu)+4+6 & = & 0 \\ \Rightarrow & 2-2\mu+\mu-{\mu}^{2}+10 & = & 0 \\ \Rightarrow & {\color{red} -}\mu-{\mu}^{2}+12 & = & 0 \\ \Rightarrow & -{\mu}^{2}{\color{red} -}\mu+12 & = & 0 \\ \Rightarrow & {\mu}^{2}{\color{red} +}\mu-12 & = & 0 \\ \Rightarrow & {\mu}_{1,2} & = & -\frac{1}{2}\pm\sqrt{{\left( \frac{1}{2} \right)}^{2}+12} \\ \Rightarrow & {\mu}_{1,2} & = & -\frac{1}{2}\pm\sqrt{\frac{1}{4}+\frac{48}{4}} \\ \Rightarrow & {\mu}_{1,2} & = & -\frac{1}{2}\pm\sqrt{\frac{49}{4}} \\ \Rightarrow & {\mu}_{1,2} & = & -\frac{1}{2}\pm\frac{7}{2} \end{array}$$

$$\Rightarrow\quad {\mu}_{1}=3,\quad {\mu}_{2}=-4$$
```
````

```{admonition} Übung 4.3
:class: miniexercise
Gegeben sei die Richtung $\vec{a}=(3,\,2,\,1)$.

a) Berechnen Sie $\vec{e}_{a}$.

b) Welche Komponenten hat der Vektor $\vec{b}$ in Richtung von $\vec{e}_{a}$, der die Länge 5 hat?

c) Berechnen Sie den Vektor, der durch die Projektion von $\vec{b}$ in Richtung von $\vec{c}=(2,\,-3,\,1)$ entsteht.
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $\vec{e}_{a}=\frac{1}{\sqrt{14}}\begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix}$

b) $\vec{b}=\frac{5}{\sqrt{14}}\begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix}$

c) $(\vec{e}_{c}\cdot\vec{b})\vec{e}_{c}=\frac{5}{14\sqrt{14}}\begin{pmatrix} 2 \\ -3 \\ 1 \end{pmatrix}$

```{dropdown} Lösungsweg
a)

$$\vec{e}_{a}=\frac{1}{|\vec{a}|}\vec{a}=\frac{1}{\sqrt{{3}^{2}+{2}^{2}+{1}^{2}}}\begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix}=\frac{1}{\sqrt{14}}\begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix}$$

b)

$$
\begin{aligned}
\vec{b}&=c\cdot\vec{e}_{a}=\frac{c}{\sqrt{14}}\cdot\begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix}\quad \text{mit}\quad c\in\mathbb{R} \\
5&=\left|\vec{b}\right|=\left|\frac{c}{\sqrt{14}}\cdot\begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix}\right|=\sqrt{{\left( \frac{c}{\sqrt{14}} \right)}^{2}\cdot({3}^{2}+{2}^{2}+{1}^{2})}=\sqrt{\frac{{c}^{2}}{14}\cdot14}=c
\end{aligned}
$$

Also

$$\vec{b}=5\vec{e}_{a}=\frac{5}{\sqrt{14}}\begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix}$$

$$\begin{array}{lrcl} \text{Alternative Lösung (deutlich einfacher):} & \left|\vec{e}_{a}\right| & = & 1 \\ \text{Also muss gelten:} & \vec{b} & = & 5\vec{e}_{a} \end{array}$$

c)

Dafür wird $\vec{e}_{c}$ benötigt:

$$\vec{e}_{c}=\frac{1}{|\vec{c}|}\vec{c}=\frac{1}{\sqrt{{2}^{2}+{3}^{2}+{1}^{2}}}\begin{pmatrix} 2 \\ -3 \\ 1 \end{pmatrix}=\frac{1}{\sqrt{14}}\begin{pmatrix} 2 \\ -3 \\ 1 \end{pmatrix}$$

Orthogonale Projektion eines Vektors auf einen zweiten Vektor:

$$(\vec{e}_{c}\cdot\vec{b})\vec{e}_{c}=\left[ \frac{1}{\sqrt{14}}\begin{pmatrix} 2 \\ -3 \\ 1 \end{pmatrix}\cdot\frac{5}{\sqrt{14}}\begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix} \right]\cdot\frac{1}{\sqrt{14}}\begin{pmatrix} 2 \\ -3 \\ 1 \end{pmatrix}=\left[ \frac{5}{14}(2\cdot 3-3\cdot 2+1\cdot1) \right]\cdot\frac{1}{\sqrt{14}}\begin{pmatrix} 2 \\ -3 \\ 1 \end{pmatrix}=\frac{5}{14\sqrt{14}}\begin{pmatrix} 2 \\ -3 \\ 1 \end{pmatrix}$$
```
````

```{admonition} Übung 4.4
:class: miniexercise
Bestimmen Sie den Wert von $t$, der den Winkel zwischen den Vektoren $\vec{a}=(3,\,1,\,0)$ und $\vec{b}=(t,\,0,\,1)$ zu $45^\circ$ macht.
```

````{admonition} Lösung
:class: miniexercise, toggle

$$t=\frac{1}{2}\sqrt{5}$$

```{dropdown} Lösungsweg
$$\cos (\varphi)=\frac{\vec{a}\cdot\vec{b}}{|\vec{a}|\cdot|\vec{b}|}$$

Es soll gelten $\varphi=45^\circ$:

$$\begin{array}{lrcl} & \cos (45^\circ ) & = & \frac{\begin{pmatrix} 3 \\ 1 \\ 0 \end{pmatrix}\cdot\begin{pmatrix} t \\ 0 \\ 1 \end{pmatrix}}{\sqrt{{3}^{2}+{1}^{2}}\cdot\sqrt{{1}^{2}+{t}^{2}}} \\ \Rightarrow & \frac{\sqrt{2}}{2} & = & \frac{3t}{\sqrt{10}\sqrt{1+{t}^{2}}} \\ \Rightarrow & \frac{\sqrt{2}}{2}\cdot\sqrt{10}\sqrt{1+{t}^{2}} & = & 3t \\ \Rightarrow & {\left( \frac{\sqrt{2}}{2}\cdot\sqrt{10}\sqrt{1+{t}^{2}} \right)}^{2} & = & {(3t)}^{2} \\ \Rightarrow & \frac{2}{4}\cdot10\cdot(1+{t}^{2}) & = & 9{t}^{2} \\ \Rightarrow & 5+5{t}^{2} & = & 9{t}^{2} \\ \Rightarrow & 5 & = & 4{t}^{2} \\ \Rightarrow & {t}_{1{,}2} & = & \pm\sqrt{\frac{5}{4}} \\ \Rightarrow & {t}_{1{,}2} & = & \pm\frac{1}{2}\sqrt{5} \end{array}$$

Probe liefert die Lösung für das positive Vorzeichen: $t=\frac{1}{2}\sqrt{5}$
```
````

```{admonition} Übung 4.5
:class: miniexercise
Zeigen Sie, dass die beiden Linien durch die Punkte $(2,3,4)$ und $(1,2,3)$ bzw. $(1,0,2)$ und $(2,3,-2)$ senkrecht zueinander stehen.
```

````{admonition} Lösung
:class: miniexercise, toggle

$$\vec{a}=\begin{pmatrix} 2 \\ 3 \\ 4 \end{pmatrix}-\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}=\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}\qquad\vec{b}=\begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix}-\begin{pmatrix} 2 \\ 3 \\ -2 \end{pmatrix}=\begin{pmatrix} -1 \\ -3 \\ 4 \end{pmatrix}$$

Es soll gelten:

$$0=\vec{a}\cdot\vec{b}=1\cdot(-1)+1\cdot(-3)+1\cdot4=-1-3+4=0$$

```{dropdown} Lösungsweg
$$\vec{a}=\begin{pmatrix} 2 \\ 3 \\ 4 \end{pmatrix}-\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}=\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}\qquad\vec{b}=\begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix}-\begin{pmatrix} 2 \\ 3 \\ -2 \end{pmatrix}=\begin{pmatrix} -1 \\ -3 \\ 4 \end{pmatrix}$$

Es soll gelten:

$$0=\vec{a}\cdot\vec{b}=1\cdot(-1)+1\cdot(-3)+1\cdot4=-1-3+4=0$$
```
````

```{admonition} Übung 4.6
:class: miniexercise
Gegeben seien $\vec{p}=(1,\,1,\,1)$, $\vec{q}=(0,\,-1,\,2)$ und $\vec{r}=(2,\,2,\,1)$. Berechnen Sie die folgenden Ausdrücke. Ist das Ergebnis eine Zahl oder ein Vektor?

a) $\vec{p}\times\vec{q}$

b) $\vec{p}\times\vec{r}$

c) $\vec{r}\times\vec{q}$

d) $(\vec{p}\times\vec{r})\cdot\vec{q}$

e) $\vec{q}\cdot(\vec{r}\times\vec{p})$

f) $(\vec{p}\times\vec{r})\times\vec{q}$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) Vektor: $\vec{p}\times\vec{q}=\begin{pmatrix} 3 \\ -2 \\ {\color{red} -1} \end{pmatrix}$

b) Vektor: $\vec{p}\times\vec{r}=\begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}$

c) Vektor: $\vec{r}\times\vec{q}=\begin{pmatrix} 5 \\ -4 \\ -2 \end{pmatrix}$

d) Skalar: $(\vec{p}\times\vec{r})\cdot\vec{q}=-1$

e) Skalar: $\vec{q}\cdot(\vec{r}\times\vec{p})=1$

f) Vektor: $(\vec{p}\times\vec{r})\times\vec{q}=\begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix}$

```{dropdown} Lösungsweg
a)

Das Vektorprodukt liefert einen Vektor:

$$\vec{p}\times\vec{q}=\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}\times\begin{pmatrix} 0 \\ -1 \\ 2 \end{pmatrix}=\begin{pmatrix} 3 \\ -2 \\ {\color{red} -1} \end{pmatrix}$$

b)

Ebenfalls ein Vektor:

$$\vec{p}\times\vec{r}=\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}\times\begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix}=\begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}$$

c)

Ebenfalls ein Vektor:

$$\vec{r}\times\vec{q}=\begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix}\times\begin{pmatrix} 0 \\ -1 \\ 2 \end{pmatrix}=\begin{pmatrix} 5 \\ -4 \\ -2 \end{pmatrix}$$

d)

Das Vektorprodukt multipliziert mit einem Vektor ergibt ein Skalar. Mit $\vec{p}\times\vec{r}$ aus b):

$$(\vec{p}\times\vec{r})\cdot\vec{q}=\begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}\cdot\begin{pmatrix} 0 \\ -1 \\ 2 \end{pmatrix}=-1$$

e)

Fast das gleiche wie bei d), allerdings in anderer Reihenfolge:

Beachte: $\vec{p}\times\vec{r}=-(\vec{r}\times\vec{p})$

Der Term lässt sich durch Umformen direkt zu Beginn vereinfachen:

$$\vec{q}\cdot(\vec{r}\times\vec{p})=\vec{q}\cdot(-1)(\vec{p}\times\vec{r})=-\vec{q}\cdot(\vec{p}\times\vec{r})=-(\vec{p}\times\vec{r})\cdot\vec{q}\overset{\text{Teilaufgabe d)}}{=}-(-1)=1$$

f)

Die zweifache Anwendung des Vektorprodukts ergibt wiederum einen Vektor:

$$(\vec{p}\times\vec{r})\times\vec{q}=\begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}\times\begin{pmatrix} 0 \\ -1 \\ 2 \end{pmatrix}=\begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix}$$
```
````

```{admonition} Übung 4.7
:class: miniexercise
Zeigen Sie, dass $(\vec{a}-\vec{b})\times(\vec{a}+\vec{b})=2(\vec{a}\times\vec{b})$.
```

````{admonition} Lösung
:class: miniexercise, toggle

$$
\begin{aligned}
(\vec{a}-\vec{b})\times(\vec{a}+\vec{b})&=\vec{a}\times\vec{a}+\vec{a}\times\vec{b}-\vec{b}\times\vec{a}-\vec{b}\times\vec{b} \\
&=\vec{a}\times\vec{b}-((-1)\vec{a}\times\vec{b}) \\
&=\vec{a}\times\vec{b}+\vec{a}\times\vec{b} \\
&=2(\vec{a}\times\vec{b})
\end{aligned}
$$

```{dropdown} Lösungsweg
Beachte: ${\color{green} \vec{a}\times\vec{a}}=0$ und ${\color{blue} \vec{b}\times\vec{b}}=0$ und $\vec{b}\times\vec{a}=(-1)\vec{a}\times\vec{b}$

Damit kann man losrechnen:

$$
\begin{aligned}
(\vec{a}-\vec{b})\times(\vec{a}+\vec{b})&={\color{green} \vec{a}\times\vec{a}}+\vec{a}\times\vec{b}-\vec{b}\times\vec{a}-{\color{blue} \vec{b}\times\vec{b}} \\
&=\vec{a}\times\vec{b}-((-1)\vec{a}\times\vec{b}) \\
&=\vec{a}\times\vec{b}+\vec{a}\times\vec{b} \\
&=2(\vec{a}\times\vec{b})
\end{aligned}
$$
```
````

```{admonition} Übung 4.8
:class: miniexercise
Seien $\vec{a}$, $\vec{b}$ und $\vec{c}$ drei Vektoren, für die gilt $\vec{a}+\vec{b}+\vec{c}=0$. Zeigen Sie, dass dann gilt $\vec{a}\times\vec{b}=\vec{b}\times\vec{c}=\vec{c}\times\vec{a}$. Interpretieren Sie das Ergebnis geometrisch.
```

````{admonition} Lösung
:class: miniexercise, toggle

Interpretation: $\vec{a}, \vec{b}, \vec{c}$ bilden ein Dreieck. Für die Fläche ist es unerheblich, mit welchem Paar von Kanten man sie berechnet. Und, mit welchem Paar von Kanten man den Normalenvektor berechnet.

```{dropdown} Lösungsweg
Interpretation: $\vec{a}, \vec{b}, \vec{c}$ bilden ein Dreieck. Für die Fläche ist es unerheblich, mit welchem Paar von Kanten man sie berechnet. Und, mit welchem Paar von Kanten man den Normalenvektor berechnet.
```
````
