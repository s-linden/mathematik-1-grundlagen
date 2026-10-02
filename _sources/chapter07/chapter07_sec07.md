# Übungen zum Selbststudium

```{admonition} Übung 7.1
:class: miniexercise
Berechnen Sie, wenn möglich, die inverse Matrix zu folgenden Matrizen:

a) $\mathbf{A}=\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$

b) $\mathbf{B}=\begin{pmatrix} 2 & 3 \\ -1 & -2 \end{pmatrix}$

c) $\mathbf{C}=\begin{pmatrix} 3 & 3 \\ -1 & -1 \end{pmatrix}$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $\displaystyle\mathbf{A}^{-1}=\begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}$

b) $\displaystyle\mathbf{B}^{-1}=\begin{pmatrix} 2 & 3 \\ -1 & -2 \end{pmatrix}$

c) $\mathbf{C}^{-1}$ existiert nicht, da $\det(\mathbf{C})=0$.

```{dropdown} Lösungsweg
a)

$$\mathbf{A}^{-1}=\frac{1}{\det(\mathbf{A})}\cdot\begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}=\frac{1}{1\cdot1-0\cdot2}\cdot\begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}=\begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}$$

b)

$$\mathbf{B}^{-1}=\frac{1}{\det(\mathbf{B})}\cdot\begin{pmatrix} -2 & -3 \\ 1 & 2 \end{pmatrix}=\frac{1}{2\cdot(-2)-(-1\cdot3)}\cdot\begin{pmatrix} -2 & -3 \\ 1 & 2 \end{pmatrix}=-1\cdot\begin{pmatrix} -2 & -3 \\ 1 & 2 \end{pmatrix}=\begin{pmatrix} 2 & 3 \\ -1 & -2 \end{pmatrix}$$

c)

$\det(\mathbf{C})=3\cdot(-1)-(-1\cdot3)={\color{red} 0}\ \Rightarrow\ \mathbf{C}^{-1}$ existiert nicht.
```
````

```{admonition} Übung 7.2
:class: miniexercise
Berechnen Sie die Determinante der Matrix

$$\mathbf{A}=\begin{pmatrix} 4 & 2 & 1 \\ -2 & 1 & 0 \\ 1 & 0 & 5 \end{pmatrix}$$
```

````{admonition} Lösung
:class: miniexercise, toggle

$$\det(\mathbf{A})=39$$

```{dropdown} Lösungsweg
Entwicklung nach 3. Zeile:

$$\det(\mathbf{A})=1\cdot(+1)\begin{vmatrix} 2 & 1 \\ 1 & 0 \end{vmatrix}+5\cdot(+1)\begin{vmatrix} 4 & 2 \\ -2 & 1 \end{vmatrix}=1\left( 2\cdot0-1\cdot1 \right)+5\left( 4\cdot1-(-2)\cdot2 \right)=-1+20+20=39$$
```
````

```{admonition} Übung 7.3
:class: miniexercise
Berechnen Sie die Determinanten der folgenden Matrizen:

a) $\displaystyle \begin{pmatrix} -1 & 3 & 1 \\ 1 & 1 & 1 \\ -2 & 18 & 8 \end{pmatrix}$

b) $\displaystyle \begin{pmatrix} 2 & 5 & 18 & -1 \\ 4 & -3 & 5 & 6 \\ -6 & 3 & -9 & 3 \\ 0 & 2 & 5 & 0 \end{pmatrix}$

c) $\displaystyle \begin{pmatrix} 0 & 1 & 0 & 0 & 0 \\ 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 1 \\ 0 & 0 & 0 & 1 & 0 \end{pmatrix}$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $0$

b) $0$

c) $0$

```{dropdown} Lösungsweg
a)

Zum Beispiel Entwicklung nach der 1. Spalte:

$$
\begin{aligned}
\begin{vmatrix} -1 & 3 & 1 \\ 1 & 1 & 1 \\ -2 & 18 & 8 \end{vmatrix}&=(-1)\cdot(+1)\cdot\begin{vmatrix} 1 & 1 \\ 18 & 8 \end{vmatrix}+(1)\cdot(-1)\begin{vmatrix} 3 & 1 \\ 18 & 8 \end{vmatrix}+(-2)\cdot(+1)\cdot\begin{vmatrix} 3 & 1 \\ 1 & 1 \end{vmatrix} \\
&=-(1\cdot8-18\cdot1)-(3\cdot8-18\cdot1)-2(3\cdot1-1\cdot1)=10-6-4=0
\end{aligned}
$$

b)

Entwicklung nach 4. Zeile

$$
\begin{aligned}
\begin{vmatrix} 2 & 5 & 18 & -1 \\ 4 & -3 & 5 & 6 \\ -6 & 3 & -9 & 3 \\ 0 & 2 & 5 & 0 \end{vmatrix}&=2\begin{vmatrix} 2 & 18 & -1 \\ 4 & 5 & 6 \\ -6 & -9 & 3 \end{vmatrix}-5\begin{vmatrix} 2 & 5 & -1 \\ 4 & -3 & 6 \\ -6 & 3 & 3 \end{vmatrix} \\
\begin{vmatrix} 2 & 18 & -1 \\ 4 & 5 & 6 \\ -6 & -9 & 3 \end{vmatrix}&=2\cdot5\cdot3+18\cdot6\cdot(-6)+(-1)\cdot4\cdot(-9)-[(-6)\cdot5\cdot(-1)+(-9)\cdot6\cdot2+3\cdot4\cdot18]=-720 \\
\begin{vmatrix} 2 & 5 & -1 \\ 4 & -3 & 6 \\ -6 & 3 & 3 \end{vmatrix}&=2\cdot(-3)\cdot3+5\cdot6\cdot(-6)+(-1)\cdot4\cdot3-[(-6)\cdot(-3)\cdot(-1)+3\cdot6\cdot2+3\cdot4\cdot5]=-288 \\
&\Rightarrow\,\begin{vmatrix} 2 & 5 & 18 & -1 \\ 4 & -3 & 5 & 6 \\ -6 & 3 & -9 & 3 \\ 0 & 2 & 5 & 0 \end{vmatrix}=2\cdot(-720)-5\cdot(-288)=0
\end{aligned}
$$

c)

$$\begin{vmatrix} {\color{red} 0} & 1 & 0 & 0 & 0 \\ {\color{red} 1} & {\color{red} 0} & {\color{red} 1} & {\color{red} 0} & {\color{red} 0} \\ {\color{red} 0} & 1 & 0 & 1 & 0 \\ {\color{red} 0} & 0 & 1 & 0 & 1 \\ {\color{red} 0} & 0 & 0 & 1 & 0 \end{vmatrix}=-1\begin{vmatrix} {\color{green} 1} & {\color{green} 0} & {\color{green} 0} & {\color{green} 0} \\ {\color{green} 1} & 0 & 1 & 0 \\ {\color{green} 0} & 1 & 0 & 1 \\ {\color{green} 0} & 0 & 1 & 0 \end{vmatrix}=-1\cdot1\begin{vmatrix} {\color{blue} 0} & {\color{blue} 1} & {\color{blue} 0} \\ 1 & {\color{blue} 0} & 1 \\ 0 & {\color{blue} 1} & 0 \end{vmatrix}=(-1)\cdot1\cdot(-1)\begin{vmatrix} 1 & 1 \\ 0 & 0 \end{vmatrix}=(-1)\cdot1\cdot(-1)\cdot0=0$$
```
````

```{admonition} Übung 7.4
:class: miniexercise
Berechnen Sie die inverse Matrix für die folgende $(3\times3)$-Matrix:

$$\mathbf{A}=\begin{pmatrix} -1 & 2 & 1 \\ 0 & 1 & -2 \\ 1 & 4 & -1 \end{pmatrix}$$
```

````{admonition} Lösung
:class: miniexercise, toggle

$$\mathbf{A}^{-1}=\frac{1}{12}\begin{pmatrix} -7 & -6 & 5 \\ 2 & 0 & 2 \\ 1 & -6 & 1 \end{pmatrix}$$

```{dropdown} Lösungsweg
$$\mathbf{A}^{-1}=\frac{1}{12}\begin{pmatrix} -7 & -6 & 5 \\ 2 & 0 & 2 \\ 1 & -6 & 1 \end{pmatrix}$$
```
````

```{admonition} Übung 7.5
:class: miniexercise
Bestimmen Sie die Eigenwerte und Eigenvektoren für folgende Matrizen:

a) $\mathbf{A}=\begin{pmatrix} 1 & 2 \\ 2 & -2 \end{pmatrix}$

b) $\mathbf{B}=\begin{pmatrix} -3 & -3 & -3 \\ -3 & 1 & -1 \\ -3 & -1 & 1 \end{pmatrix}$

Hinweis: Nutzen Sie zum Beispiel Wolframalpha oder ChatGPT mit der Wolframalpha-Schnittstelle, um die kubische Gleichung in 7.5 b) zu lösen.
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $\lambda_1=-3$, $\lambda_2=2$

Eigenvektor zu $\lambda_1$: $\vec{v}_1=s\cdot\begin{pmatrix} 1 \\ -2 \end{pmatrix}$.

Eigenvektor zu $\lambda_2$: $\vec{v}_2=t\cdot\begin{pmatrix} 2 \\ 1 \end{pmatrix}$.

b) $\lambda_1=-6$, $\lambda_2=2$, $\lambda_3=3$

Eigenvektor zu $\lambda_1$: $\vec{v}_1=r\cdot\begin{pmatrix} 2 \\ 1 \\ 1 \end{pmatrix}$.

Eigenvektor zu $\lambda_2$: $\vec{v}_2=s\cdot\begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}$.

Eigenvektor zu $\lambda_3$: $\vec{v}_3=t\cdot\begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}$.

```{dropdown} Lösungsweg
a)

$$\mathbf{A}=\begin{pmatrix} 1 & 2 \\ 2 & -2 \end{pmatrix}$$

charakteristische Gleichung:

$$
\begin{aligned}
0&=\left|\mathbf{A}-\lambda\cdot\mathbf{E}\right|=\begin{vmatrix} 1-\lambda & 2 \\ 2 & -2-\lambda \end{vmatrix}=(1-\lambda)(-2-\lambda)-4=-2-\lambda+2\lambda+{\lambda}^{2}-4=-6+\lambda+{\lambda}^{2} \\
&=(\lambda+3)(\lambda-2)
\end{aligned}
$$

Lösung: ${\lambda}_{1}=-3\,,\,{\lambda}_{2}=2$ sind die Eigenwerte.

Für Eigenvektoren zum EW ${\lambda}_{i}$ gilt:

$$(\mathbf{A}-{\lambda}_{i}\mathbf{E})\begin{pmatrix} {v}_{i1} \\ {v}_{i2} \end{pmatrix}=\vec{0}\Rightarrow\,\begin{array}{lrcl} (1-{\lambda}_{i}){v}_{i1} & +2{v}_{i2} & = & 0 \\ 2{v}_{i1} & +(-2-{\lambda}_{i}){v}_{i2} & = & 0 \end{array}$$

Für

$${\lambda}_{1}=-3:\quad\begin{array}{lrcl} 4{v}_{11} & +2{v}_{12} & = & 0 \\ 2{v}_{11} & +{v}_{12} & = & 0 \end{array}$$

Die erste Gleichung ist das doppelte der zweiten. Die zweite Gleichung reicht aus. Wir wählen ${v}_{11}=1$ und erhalten damit ${v}_{12}=-2{v}_{11}=-2$.

Ein EV zu ${\lambda}_{1}$ ist damit $\vec{v}_{1}=\begin{pmatrix} 1 \\ -2 \end{pmatrix}$.

Für

$${\lambda}_{2}=2:\quad\begin{array}{lrcl} -{v}_{21} & +2{v}_{22} & = & 0 \\ 2{v}_{21} & -4{v}_{22} & = & 0 \end{array}$$

Die zweite Gleichung folgt aus der ersten durch Multiplikation mit -2. Die erste reicht also aus. Um im Ergebnis ganze Zahlen zu erhalten, wählen wir ${v}_{21}=2$.

Damit erhalten wir ${v}_{22}={v}_{21}/2=1$. Ein EV zu ${\lambda}_{2}$ ist damit $\vec{v}_{2}=\begin{pmatrix} 2 \\ 1 \end{pmatrix}$.

b)

$$\mathbf{B}=\begin{pmatrix} -3 & -3 & -3 \\ -3 & 1 & -1 \\ -3 & -1 & 1 \end{pmatrix}$$

Charakteristische Gleichung:

$$
\begin{aligned}
0&=\left|\mathbf{B}-\lambda\mathbf{E}\right|=\begin{vmatrix} -3-\lambda & -3 & -3 \\ -3 & 1-\lambda & -1 \\ -3 & -1 & 1-\lambda \end{vmatrix} \\
&=(-3-\lambda)(1-\lambda)(1-\lambda)+(-3)(-1)(-3)+(-3)(-3)(-1) \\
&-\left[ (-3)(1-\lambda)(-3)+(-1)(-1)(-3-\lambda)+(1-\lambda)(-3)(-3) \right] \\
&=(-3-\lambda){(1-\lambda)}^{2}-9-9-9(1-\lambda)-(-3-\lambda)-9(1-\lambda) \\
&=(-3-\lambda){(1-\lambda)}^{2}-18-9+9\lambda+3+\lambda-9+9\lambda \\
&=(-3-\lambda)(1-2\lambda+{\lambda}^{2})-33+19\lambda \\
&={\color{red} -3}+{\color{green} 6\lambda}-{\color{blue} {3\lambda}^{2}}-{\color{green} \lambda}+{\color{blue} {2\lambda}^{2}}-{\lambda}^{3}-{\color{red} 33}+{\color{green} 19\lambda}=-{\lambda}^{3}-{\lambda}^{2}+24\lambda-36
\end{aligned}
$$

Gleichung mithilfe von zum Beispiel wolframalpha.com oder ChatGPT lösen:

$${\lambda}_{1}=-6,\quad{\lambda}_{2}=2,\quad{\lambda}_{3}=3$$

Für Eigenvektoren zum EW ${\lambda}_{i}$ gilt:

$$(\mathbf{B}-\lambda\mathbf{E})\begin{pmatrix} {v}_{i1} \\ {v}_{i2} \\ {v}_{i3} \end{pmatrix}=\vec{0}\Rightarrow\,\begin{array}{llrcl} (-3-{\lambda}_{i}){v}_{i1} & -3{v}_{i2} & -3{v}_{i3} & = & 0 \\ -3{v}_{i1} & +(1-{\lambda}_{i}){v}_{i2} & -{v}_{i3} & = & 0 \\ -3{v}_{i1} & -{v}_{i2} & +(1-{\lambda}_{i}){v}_{i3} & = & 0 \end{array}$$

Das Gleichungssystem wird keine eindeutige Lösung haben, weil seine Determinante Null ist. Sie erhalten für die Eigenwerte:

Für ${\lambda}_{1}=-6$:

$$\begin{array}{llrcl} 3{v}_{11} & -3{v}_{12} & -3{v}_{13} & = & 0 \\ -3{v}_{11} & +7{v}_{12} & -{v}_{13} & = & 0 \\ -3{v}_{11} & -{v}_{12} & +7{v}_{13} & = & 0 \end{array}\,\begin{array}{l} (\text{I}) \\ (\text{II}) \\ (\text{III}) \end{array}$$

Die erste Gleichung kann eliminiert werden mit 2(I)+(II)+(III).

Aus (II)-(III) folgt:

$$8{v}_{12}-8{v}_{13}=0\Rightarrow\,{v}_{12}={v}_{13}$$

Damit folgt aus (II):

$$-3{v}_{11}+6{v}_{12}=0\Rightarrow\,{v}_{11}=2{v}_{12}$$

Wir wählen ${v}_{13}=1$ und erhalten ${v}_{12}=1$ und ${v}_{11}=2$.

Ein EV zu ${\lambda}_{1}$ ist damit $\vec{v}_{1}=\begin{pmatrix} 2 \\ 1 \\ 1 \end{pmatrix}$.

Für ${\lambda}_{2}=2$:

$$\begin{array}{llrcl} -5{v}_{21} & -3{v}_{22} & -3{v}_{23} & = & 0 \\ -3{v}_{21} & -{v}_{22} & -{v}_{23} & = & 0 \\ -3{v}_{21} & -{v}_{22} & -{v}_{23} & = & 0 \end{array}\begin{array}{l} (\text{I}) \\ (\text{II}) \\ (\text{III}) \end{array}$$

Gleichungen (II) und (III) sind identisch. Wir verwenden also nur (I) und (II).

Aus (I)-3(II) folgt direkt: $4{v}_{21}=0\Rightarrow\,{v}_{21}=0$

Damit folgt aus (II):

$$-{v}_{22}-{v}_{23}=0\Rightarrow\,{v}_{22}=-{v}_{23}$$

Wir wählen ${v}_{22}=1$ und erhalten ${v}_{23}=-1$ und ${v}_{21}=0$.

Ein EV zu ${\lambda}_{2}$ ist damit $\vec{v}_{2}=\begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}$.

Für ${\lambda}_{3}=3$:

$$\begin{array}{llrcl} -6{v}_{31} & -3{v}_{32} & -3{v}_{33} & = & 0 \\ -3{v}_{31} & -2{v}_{32} & -{v}_{33} & = & 0 \\ -3{v}_{31} & -{v}_{32} & -2{v}_{33} & = & 0 \end{array}\,\begin{array}{l} (\text{I}) \\ (\text{II}) \\ (\text{III}) \end{array}$$

Die erste Gleichung kann eliminiert werden mit (I)-(II)-(III).

Wir verwenden also nur (II) und (III).

Aus (II)-(III) folgt direkt: $-{v}_{32}+{v}_{33}=0\Rightarrow\,{v}_{32}={v}_{33}$

Damit folgt aus (II):

$$-3{v}_{31}-3{v}_{32}=0\Rightarrow\,{v}_{31}=-{v}_{32}$$

Wir wählen ${v}_{33}=1$ und erhalten ${v}_{32}=1$ und ${v}_{31}=-1$.

Ein EV zu ${\lambda}_{3}$ ist damit $\vec{v}_{3}=\begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}$.
```
````
