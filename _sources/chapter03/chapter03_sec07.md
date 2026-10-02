# Übungen zum Selbststudium

```{admonition} Übung 3.1
:class: miniexercise
Gegeben sind die Vektoren

$$\vec{a}=\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix},\quad \vec{b}=\begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix},\quad \vec{c}=\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$$

Berechnen Sie:

a) $\vec{a}+\vec{b}$

b) $\vec{a}+\frac{1}{2}\vec{b}+2\vec{c}$

c) $\vec{b}-2\vec{a}$

d) $\left|\vec{a}\right|$

e) $\left|\vec{b}\right|$

f) $\left|\vec{a}-\vec{b}\right|$

g) Einheitsvektor in Richtung $\vec{a}$

h) Einheitsvektor in Richtung $\vec{b}$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $\begin{pmatrix} 3 \\ 3 \\ 1 \end{pmatrix}$

b) $\begin{pmatrix} 2 \\ 4 \\ 5/2 \end{pmatrix}$

c) $\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$

d) $\sqrt{2}$

e) $3$

f) $\sqrt{3}$

g) $\begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \\ 0 \end{pmatrix}$

h) $\begin{pmatrix} \frac{2}{3} \\ \frac{2}{3} \\ \frac{1}{3} \end{pmatrix}$

```{dropdown} Lösungsweg
a)

$$\vec{a}+\vec{b}=\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}+\begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix}=\begin{pmatrix} 3 \\ 3 \\ 1 \end{pmatrix}$$

b)

$$\vec{a}+\frac{1}{2}\vec{b}+2\vec{c}=\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}+\frac{1}{2}\begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix}+\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}=\begin{pmatrix} 2 \\ 4 \\ 5/2 \end{pmatrix}$$

c)

$$\vec{b}-2\vec{a}=\begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix}-2\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}=\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$

d)

$$\left|\vec{a}\right|=\sqrt{{1}^{2}+{1}^{2}}=\sqrt{2}$$

e)

$$\left|\vec{b}\right|=\sqrt{{2}^{2}+{2}^{2}+{1}^{2}}=\sqrt{9}=3$$

f)

$$\left|\vec{a}-\vec{b}\right|=\left|\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}-\begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix}\right|=\left|\begin{pmatrix} -1 \\ -1 \\ -1 \end{pmatrix}\right|=\sqrt{{(-1)}^{2}+{(-1)}^{2}+{(-1)}^{2}}=\sqrt{3}$$

g)

$$\vec{e}_{a}=\frac{1}{|\vec{a}|}\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}=\begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \\ 0 \end{pmatrix}$$

h)

$$\vec{e}_{b}=\frac{1}{|\vec{b}|}\begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix}=\begin{pmatrix} \frac{2}{3} \\ \frac{2}{3} \\ \frac{1}{3} \end{pmatrix}$$
```
````

```{admonition} Übung 3.2
:class: miniexercise
Auf ein Teilchen wirken folgende Kräfte in Newton:

$$\vec{F}_{1}=\begin{pmatrix} 3 \\ -2 \\ 5 \end{pmatrix},\quad \vec{F}_{2}=\begin{pmatrix} -1 \\ 7 \\ -3 \end{pmatrix},\quad \vec{F}_{3}=\begin{pmatrix} 5 \\ -1 \\ 4 \end{pmatrix},\quad \vec{F}_{4}=\begin{pmatrix} 0 \\ -2 \\ 3 \end{pmatrix}$$

Bestimmen Sie die Größe und die Richtung der resultierenden Kraft.
```

````{admonition} Lösung
:class: miniexercise, toggle

$${F}_{\mathrm{res}}=\sqrt{134}\,\mathrm{N}$$

$$\vec{e}_{{F}_{\mathrm{res}}}=\frac{1}{\sqrt{134}}\begin{pmatrix} 7 \\ 2 \\ 9 \end{pmatrix}$$

```{dropdown} Lösungsweg
$$\vec{F}_{\mathrm{res}}=\vec{F}_{1}+\vec{F}_{2}+\vec{F}_{3}+\vec{F}_{4}=\begin{pmatrix} 3 \\ -2 \\ 5 \end{pmatrix}+\begin{pmatrix} -1 \\ 7 \\ -3 \end{pmatrix}+\begin{pmatrix} 5 \\ -1 \\ 4 \end{pmatrix}+\begin{pmatrix} 0 \\ -2 \\ 3 \end{pmatrix}=\begin{pmatrix} 7 \\ 2 \\ 9 \end{pmatrix}$$

Damit:

$${F}_{\mathrm{res}}=|\vec{F}_{r}|=\sqrt{{7}^{2}+{2}^{2}+{9}^{2}}=\sqrt{49+4+81}=\sqrt{134}\,\mathrm{N}$$

$$\vec{e}_{{F}_{\mathrm{res}}}=\frac{1}{|\vec{F}_{r}|}\vec{F}_{\mathrm{res}}=\frac{1}{\sqrt{134}}\begin{pmatrix} 7 \\ 2 \\ 9 \end{pmatrix}$$
```
````

```{admonition} Übung 3.3
:class: miniexercise
Gegeben sind:

$$\vec{a}=\begin{pmatrix} 3 \\ -2 \\ 1 \end{pmatrix},\quad \vec{b}=\begin{pmatrix} -2 \\ 5 \\ 4 \end{pmatrix},\quad \vec{c}=\begin{pmatrix} -4 \\ 1 \\ -2 \end{pmatrix},\quad \vec{d}=\begin{pmatrix} 2 \\ -1 \\ 4 \end{pmatrix}$$

Bestimmen Sie $\alpha$, $\beta$ und $\gamma$ so, dass

$$\vec{d}=\alpha\cdot\vec{a}+\beta\cdot\vec{b}+\gamma\cdot\vec{c}$$
```

````{admonition} Lösung
:class: miniexercise, toggle

$$\alpha=4\qquad \beta=1\qquad \gamma=2$$

```{dropdown} Lösungsweg
Es soll gelten:

$$
\begin{aligned}
\begin{pmatrix} 2 \\ -1 \\ 4 \end{pmatrix}&=\alpha\begin{pmatrix} 3 \\ -2 \\ 1 \end{pmatrix} \\
&\quad +\beta\begin{pmatrix} -2 \\ 5 \\ 4 \end{pmatrix} \\
&\quad +\gamma\begin{pmatrix} -4 \\ 1 \\ -2 \end{pmatrix}
\end{aligned}
$$

Dadurch entsteht folgendes Lineares Gleichungssystem:

$$\begin{array}{rcll} 2 & = & 3\alpha-2\beta-4\gamma & \text{(I)} \\ -1 & = & -2\alpha+5\beta+1\gamma & \text{(II) } \\ 4 & = & 1\alpha+4\beta-2\gamma & \text{(III)} \end{array}$$

Gamma eliminieren:

$$\begin{array}{lrcll} \text{(I) + 4}\cdot \text{(II):} & -2 & = & -5\alpha+18\beta & \text{(Ia)} \\ \text{(III) + 2}\cdot \text{(II):} & 2 & = & -3\alpha+14\beta & \text{(IIIa)} \end{array}$$

Alpha eliminieren:

$$\begin{array}{lrcll} \text{3}\cdot \text{(Ia)-5}\cdot \text{(IIIa):} & -16 & = & (54-70)\beta & \text{(Ib) } \\ \Rightarrow & \beta & = & 1 & \end{array}$$

$$\begin{array}{lrcl} \beta\text{ in (Ia):} & -2 & = & -5\alpha+18\cdot1 \\ \Rightarrow & \alpha & = & 4 \end{array}$$

$$\begin{array}{lrcl} \alpha\text{ und }\beta\text{ in (I):} & 2 & = & 3\cdot4-2\cdot1-4\gamma \\ \Rightarrow & \gamma & = & 2 \end{array}$$

$$\alpha=4\qquad \beta=1\qquad \gamma=2$$
```
````

```{admonition} Übung 3.4
:class: miniexercise
Gegeben seien die Punkte $P=(1,-3,4)$, $Q=(2,2,1)$ und $R=(3,7,-2)$. Bestimmen Sie $\overrightarrow{PQ}$ und $\overrightarrow{QR}$. Zeigen Sie, dass die Punkte $P$, $Q$ und $R$ auf einer Linie liegen und bestimmen Sie das Verhältnis $\left|\overrightarrow{PQ}\right|:\left|\overrightarrow{QR}\right|$.
```

````{admonition} Lösung
:class: miniexercise, toggle

$$\overrightarrow{PQ}=\overrightarrow{QR}=\begin{pmatrix} 1 \\ 5 \\ -3 \end{pmatrix}$$

Also gleiche Richtung durch gemeinsamen Punkt Q, also eine Linie. Längen

$$\left|PQ\right|:\left|QR\right|=1:1$$

```{dropdown} Lösungsweg
$$
\begin{aligned}
\overrightarrow{PQ}&=Q-P=\begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix}-\begin{pmatrix} 1 \\ -3 \\ 4 \end{pmatrix}=\begin{pmatrix} 1 \\ 5 \\ -3 \end{pmatrix} \\
\overrightarrow{QR}&=R-Q=\begin{pmatrix} 3 \\ 7 \\ -2 \end{pmatrix}-\begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix}=\begin{pmatrix} 1 \\ 5 \\ -3 \end{pmatrix}
\end{aligned}
$$

somit:

$$\overrightarrow{PQ}=\overrightarrow{QR}=\begin{pmatrix} 1 \\ 5 \\ -3 \end{pmatrix}$$

Also gleiche Richtung durch gemeinsamen Punkt Q, also eine Linie. Längen

$$\left|PQ\right|:\left|QR\right|=1:1$$
```
````

```{admonition} Übung 3.5
:class: miniexercise
Berechnen Sie den Abstand folgender Punkte und den Mittelpunkt der Strecke $\overline{AB}$.

a) $A=(7,11),\ B=(5,15)$

b) $A=(-8,-3),\ B=(4,1)$

c) $A=(1,2,3),\ B=(3,4,5)$

d) $A=(-1,-2,3),\ B=(3,-4,-5)$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $d(A,\ B)=\sqrt{20},\quad M=\begin{pmatrix} 6 \\ 13 \end{pmatrix}$

b) $d(A,\ B)=\sqrt{160},\quad M=\begin{pmatrix} -2 \\ -1 \end{pmatrix}$

c) $d(A,\ B)=\sqrt{12},\quad M=\begin{pmatrix} 2 \\ 3 \\ 4 \end{pmatrix}$

d) $d(A,\ B)=\sqrt{84},\quad M=\begin{pmatrix} 1 \\ -3 \\ -1 \end{pmatrix}$

```{dropdown} Lösungsweg
Mittelpunkt der Strecke $\overline{AB}$:

$$d(A,\ B)=\left|\overrightarrow{AB}\right|,\quad M=A+\frac{1}{2}\overrightarrow{AB}$$

Damit:

a)

$$\overrightarrow{AB}=\begin{pmatrix} -2 \\ 4 \end{pmatrix},\quad d(A,\ B)=\sqrt{{(-2)}^{2}+{4}^{2}}=\sqrt{20},\quad M=\begin{pmatrix} 7 \\ 11 \end{pmatrix}+\begin{pmatrix} -1 \\ 2 \end{pmatrix}=\begin{pmatrix} 6 \\ 13 \end{pmatrix}$$

b)

$$\overrightarrow{AB}=\begin{pmatrix} 12 \\ 4 \end{pmatrix},\quad d(A,\ B)=\sqrt{{12}^{2}+{4}^{2}}=\sqrt{160},\quad M=\begin{pmatrix} -8 \\ -3 \end{pmatrix}+\begin{pmatrix} 6 \\ 2 \end{pmatrix}=\begin{pmatrix} -2 \\ -1 \end{pmatrix}$$

c)

$$\overrightarrow{AB}=\begin{pmatrix} 2 \\ 2 \\ 2 \end{pmatrix},\quad d(A,\ B)=\sqrt{{2}^{2}+{2}^{2}+{2}^{2}}=\sqrt{12},\quad M=\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}+\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}=\begin{pmatrix} 2 \\ 3 \\ 4 \end{pmatrix}$$

d)

$$\overrightarrow{AB}=\begin{pmatrix} 4 \\ -2 \\ -8 \end{pmatrix},\quad d(A,\ B)=\sqrt{{4}^{2}+{(-2)}^{2}+{(-8)}^{2}}=\sqrt{84},\quad M=\begin{pmatrix} -1 \\ -2 \\ 3 \end{pmatrix}+\begin{pmatrix} 2 \\ -1 \\ -4 \end{pmatrix}=\begin{pmatrix} 1 \\ -3 \\ -1 \end{pmatrix}$$
```
````
