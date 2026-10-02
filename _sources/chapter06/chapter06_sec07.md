# Übungen zum Selbststudium

```{admonition} Übung 6.1
:class: miniexercise
Gegeben seien die Matrizen

$$\mathbf{A}=\begin{pmatrix} 1 & 0 & 1 \\ 2 & 1 & 2 \end{pmatrix}\qquad \mathbf{B}=\begin{pmatrix} 0 & 1 \\ 1 & 0 \\ 0 & 1 \end{pmatrix}\qquad \mathbf{C}=\begin{pmatrix} 2 & 1 \\ -1 & 2 \end{pmatrix}$$

Berechnen Sie die folgenden Matrizen, wenn möglich:

$$\mathbf{A}\cdot\mathbf{B},\quad \mathbf{B}\cdot\mathbf{A},\quad \mathbf{B}\cdot\mathbf{C},\quad \mathbf{C}\cdot\mathbf{B},\quad \mathbf{C}\cdot\mathbf{A},\quad \mathbf{A}\cdot\mathbf{C}.$$
```

````{admonition} Lösung
:class: miniexercise, toggle

$$
\begin{aligned}
\mathbf{A}\cdot\mathbf{B}&=\begin{pmatrix} 0 & 2 \\ 1 & 4 \end{pmatrix} \\
\mathbf{B}\cdot\mathbf{A}&=\begin{pmatrix} 2 & 1 & 2 \\ 1 & 0 & 1 \\ 2 & 1 & 2 \end{pmatrix} \\
\mathbf{B}\cdot\mathbf{C}&=\begin{pmatrix} -1 & 2 \\ 2 & 1 \\ -1 & 2 \end{pmatrix} \\
\mathbf{C}\cdot\mathbf{B}&\quad\text{nicht möglich} \\
\mathbf{C}\cdot\mathbf{A}&=\begin{pmatrix} 4 & 1 & 4 \\ 3 & 2 & 3 \end{pmatrix} \\
\mathbf{A}\cdot\mathbf{C}&\quad\text{nicht möglich}
\end{aligned}
$$

```{dropdown} Lösungsweg
$$
\begin{aligned}
\mathbf{A}\cdot\mathbf{B}&=\begin{pmatrix} 1\cdot0+0\cdot1+1\cdot0 & 1\cdot1+0\cdot0+1\cdot1 \\ 2\cdot0+1\cdot1+2\cdot0 & 2\cdot1+1\cdot0+2\cdot1 \end{pmatrix}=\begin{pmatrix} 0 & 2 \\ 1 & 4 \end{pmatrix} \\
\mathbf{B}\cdot\mathbf{A}&=\begin{pmatrix} 2 & 1 & 2 \\ 1 & 0 & 1 \\ 2 & 1 & 2 \end{pmatrix} \\
\mathbf{B}\cdot\mathbf{C}&=\begin{pmatrix} -1 & 2 \\ 2 & 1 \\ -1 & 2 \end{pmatrix} \\
\mathbf{C}\cdot\mathbf{B}&\quad\text{nicht möglich} \\
\mathbf{C}\cdot\mathbf{A}&=\begin{pmatrix} 4 & 1 & 4 \\ 3 & 2 & 3 \end{pmatrix} \\
\mathbf{A}\cdot\mathbf{C}&\quad\text{nicht möglich}
\end{aligned}
$$
```
````

```{admonition} Übung 6.2
:class: miniexercise
Gegeben seien die Matrizen

$$\mathbf{A}=\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\qquad \mathbf{B}=\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

a) Berechnen Sie $(\mathbf{A}+\mathbf{B})^{2}$ und $\mathbf{A}^{2}+2\mathbf{A}\cdot\mathbf{B}+\mathbf{B}^{2}$.

b) Berechnen Sie $(\mathbf{A}+\mathbf{B})\cdot(\mathbf{A}-\mathbf{B})$ und $\mathbf{A}^{2}-\mathbf{B}^{2}$.

Hinweis: Es ist $\mathbf{A}^{2}=\mathbf{A}\cdot\mathbf{A}$ usw.
```

````{admonition} Lösung
:class: miniexercise, toggle

a)

$$
\begin{aligned}
(\mathbf{A}+\mathbf{B})^{2}&=\begin{pmatrix} 3 & 4 \\ 2 & 3 \end{pmatrix} \\
\mathbf{A}^{2}+2\mathbf{A}\cdot\mathbf{B}+\mathbf{B}^{2}&=\begin{pmatrix} 4 & 4 \\ 2 & 2 \end{pmatrix}
\end{aligned}
$$

b)

$$
\begin{aligned}
(\mathbf{A}+\mathbf{B})\cdot(\mathbf{A}-\mathbf{B})&=\begin{pmatrix} -1 & 2 \\ 0 & 1 \end{pmatrix} \\
\mathbf{A}^{2}-\mathbf{B}^{2}&=\begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}
\end{aligned}
$$

```{dropdown} Lösungsweg
a)

$$
\begin{aligned}
(\mathbf{A}+\mathbf{B})^{2}&={\begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}}^{2}=\begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}\cdot\begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}=\begin{pmatrix} 3 & 4 \\ 2 & 3 \end{pmatrix} \\
\mathbf{A}^{2}+2\mathbf{A}\cdot\mathbf{B}+\mathbf{B}^{2}&=\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\cdot\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}+2\cdot\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\cdot\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}+\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\cdot\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \\
&=\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}+\begin{pmatrix} 2 & 2 \\ 0 & 2 \end{pmatrix}\cdot\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}+\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}=\begin{pmatrix} 2 & 2 \\ 0 & 2 \end{pmatrix}+\begin{pmatrix} 2 & 2 \\ 2 & 0 \end{pmatrix}=\begin{pmatrix} 4 & 4 \\ 2 & 2 \end{pmatrix}
\end{aligned}
$$

b)

$$
\begin{aligned}
(\mathbf{A}+\mathbf{B})\cdot(\mathbf{A}-\mathbf{B})&=\begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}\cdot\begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}=\begin{pmatrix} -1 & 2 \\ 0 & 1 \end{pmatrix} \\
\mathbf{A}^{2}-\mathbf{B}^{2}&=\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\cdot\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}-\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\cdot\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}=\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}-\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}=\begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}
\end{aligned}
$$
```
````

```{admonition} Übung 6.3
:class: miniexercise
Wiederholen Sie Aufgabe 6.2 nun mit diesen Matrizen:

$$\mathbf{A}=\begin{pmatrix} 1 & 2 \\ 5 & 2 \end{pmatrix}\qquad \mathbf{B}=\begin{pmatrix} 2 & -2 \\ -5 & 1 \end{pmatrix}$$

Können Sie die Unterschiede erklären?
```

````{admonition} Lösung
:class: miniexercise, toggle

a)

$$(\mathbf{A}+\mathbf{B})^{2}=\begin{pmatrix} 9 & 0 \\ 0 & 9 \end{pmatrix}=\mathbf{A}^{2}+2\mathbf{A}\cdot\mathbf{B}+\mathbf{B}^{2}$$

b)

$$(\mathbf{A}+\mathbf{B})\cdot(\mathbf{A}-\mathbf{B})=\begin{pmatrix} -3 & 12 \\ 30 & 3 \end{pmatrix}=\mathbf{A}^{2}-\mathbf{B}^{2}$$

Die Matrizen aus 6.3 kommutieren, die aus 6.2 nicht.

```{dropdown} Lösungsweg
a)

$$(\mathbf{A}+\mathbf{B})^{2}=\begin{pmatrix} 9 & 0 \\ 0 & 9 \end{pmatrix}=\mathbf{A}^{2}+2\mathbf{A}\cdot\mathbf{B}+\mathbf{B}^{2}$$

b)

$$(\mathbf{A}+\mathbf{B})\cdot(\mathbf{A}-\mathbf{B})=\begin{pmatrix} -3 & 12 \\ 30 & 3 \end{pmatrix}=\mathbf{A}^{2}-\mathbf{B}^{2}$$

Die Matrizen aus 6.3 kommutieren, die aus 6.2 nicht.

D.h. für die Matrizen aus 6.2 gilt $\mathbf{A}\cdot\mathbf{B}\neq\mathbf{B}\cdot\mathbf{A}$, aber für die Matrizen aus 6.3 gilt in der Tat $\mathbf{A}\cdot\mathbf{B}=\mathbf{B}\cdot\mathbf{A}$.
```
````

```{admonition} Übung 6.4
:class: miniexercise
Sei $\mathbf{A}$ eine quadratische Matrix.

a) Ist $\mathbf{A}\cdot{\mathbf{A}}^{T}$ eine symmetrische Matrix? Wenn ja, warum?

b) Ist ${\mathbf{A}}^{T}\cdot\mathbf{A}$ eine symmetrische Matrix?

c) Gilt $\mathbf{A}\cdot{\mathbf{A}}^{T}={\mathbf{A}}^{T}\cdot\mathbf{A}$?

d) Testen Sie Ihre Antworten mit $\mathbf{A}=\begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}$.
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $\mathbf{A}\cdot{\mathbf{A}}^{T}$ ist symmetrisch.

b) ${\mathbf{A}}^{T}\cdot\mathbf{A}$ ist symmetrisch.

c) Im Allgemeinen ist $\mathbf{A}\cdot{\mathbf{A}}^{T}\neq{\mathbf{A}}^{T}\cdot\mathbf{A}$.

d) Test mit $\mathbf{A}=\begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}$:

$$
\begin{aligned}
\begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}{\begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}}^{T}&=\begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 2 & 0 \end{pmatrix}=\begin{pmatrix} 5 & 1 \\ 1 & 1 \end{pmatrix} \\
{\begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}}^{T}\begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}&=\begin{pmatrix} 1 & 1 \\ 2 & 0 \end{pmatrix}\begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}=2\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}
\end{aligned}
$$

Beide Matrizen sind symmetrisch, aber nicht gleich.

```{dropdown} Lösungsweg
Zu zeigen ist, dass das Produkt gleich seiner Transponierten ist.

a)

Es ist

$${(\mathbf{A}\cdot{\mathbf{A}}^{T})}^{T}={({\mathbf{A}}^{T})}^{T}\cdot{\mathbf{A}}^{T}=\mathbf{A}\cdot{\mathbf{A}}^{T}.$$

Also ist $\mathbf{A}\cdot{\mathbf{A}}^{T}$ gleich seiner Transponierten, also ist $\mathbf{A}\cdot{\mathbf{A}}^{T}$ symmetrisch.

b)

$${({\mathbf{A}}^{T}\cdot\mathbf{A})}^{T}={\mathbf{A}}^{T}\cdot{({\mathbf{A}}^{T})}^{T}={\mathbf{A}}^{T}\cdot\mathbf{A}$$

analog.

c)

Im Allgemeinen ist $\mathbf{A}\cdot{\mathbf{A}}^{T}\neq{\mathbf{A}}^{T}\cdot\mathbf{A}$.

d) Test mit $\mathbf{A}=\begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}$:

$$
\begin{aligned}
\begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}{\begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}}^{T}&=\begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 2 & 0 \end{pmatrix}=\begin{pmatrix} 5 & 1 \\ 1 & 1 \end{pmatrix} \\
{\begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}}^{T}\begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}&=\begin{pmatrix} 1 & 1 \\ 2 & 0 \end{pmatrix}\begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}=2\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}
\end{aligned}
$$

Beide Matrizen sind symmetrisch, aber nicht gleich.
```
````

```{admonition} Übung 6.5
:class: miniexercise
Zerlegen Sie die Matrix

$$\mathbf{A}=\begin{pmatrix} 1 & 3 & 2 \\ 2 & -1 & 0 \\ 1 & 4 & 1 \end{pmatrix}$$

in ihren symmetrischen und antisymmetrischen Anteil.
```

````{admonition} Lösung
:class: miniexercise, toggle

$$\mathbf{A}=\frac{1}{2}\begin{pmatrix} 2 & 5 & 3 \\ 5 & -2 & 4 \\ 3 & 4 & 2 \end{pmatrix}+\frac{1}{2}\begin{pmatrix} 0 & 1 & 1 \\ -1 & 0 & -4 \\ -1 & 4 & 0 \end{pmatrix}$$

```{dropdown} Lösungsweg
$$\mathbf{A}=\frac{1}{2}(\mathbf{A}+{\mathbf{A}}^{T})+\frac{1}{2}(\mathbf{A}-{\mathbf{A}}^{T})=\frac{1}{2}\begin{pmatrix} 2 & 5 & 3 \\ 5 & -2 & 4 \\ 3 & 4 & 2 \end{pmatrix}+\frac{1}{2}\begin{pmatrix} 0 & 1 & 1 \\ -1 & 0 & -4 \\ -1 & 4 & 0 \end{pmatrix}$$
```
````

```{admonition} Übung 6.6
:class: miniexercise
Gegeben seien Matrizen mit folgender Struktur:

$$\mathbf{A}=h\begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}\qquad \mathbf{B}=\begin{pmatrix} k & -l & -l \\ -l & m & m \\ -l & m & m \end{pmatrix}$$

Bestimmen Sie die Werte der Parameter $h$, $k$, $l$ und $m$ so, dass gilt

$$\mathbf{A}\neq\mathbf{0},\quad \mathbf{B}\neq\mathbf{0},\quad \mathbf{A}^{2}=\mathbf{A},\quad \mathbf{B}^{2}=\mathbf{B},\quad \mathbf{A}\cdot\mathbf{B}=\mathbf{0}.$$

Hinweis: Die Aufgabe ist aufwendig, aber eine gute Übung zum Lösen von Gleichungssystemen.
```

````{admonition} Lösung
:class: miniexercise, toggle

$$h=\frac{1}{3},\quad k=\frac{2}{3},\quad l=\frac{1}{3},\quad m=\frac{1}{6}$$

```{dropdown} Lösungsweg
$$\mathbf{A}^{2}=\mathbf{A}:\qquad \begin{pmatrix} h & h & h \\ h & h & h \\ h & h & h \end{pmatrix}\cdot\begin{pmatrix} h & h & h \\ h & h & h \\ h & h & h \end{pmatrix}=\begin{pmatrix} h & h & h \\ h & h & h \\ h & h & h \end{pmatrix}$$

$$\begin{array}{lrcl} \Rightarrow & h^{2}+h^{2}+h^{2} & = & h \\ \Rightarrow & 3h^{2} & = & h \\ \Rightarrow & 3h & = & 1 \\ \Rightarrow & h & = & \frac{1}{3} \end{array}$$

$$\mathbf{B}^{2}=\mathbf{B}:\qquad \begin{pmatrix} k & -l & -l \\ -l & m & m \\ -l & m & m \end{pmatrix}\cdot\begin{pmatrix} k & -l & -l \\ -l & m & m \\ -l & m & m \end{pmatrix}=\begin{pmatrix} k & -l & -l \\ -l & m & m \\ -l & m & m \end{pmatrix}$$

$$\begin{aligned}\Rightarrow\quad k^{2}+l^{2}+l^{2}&=k\quad\Rightarrow\quad k^{2}+2l^{2}=k && \text{(I)} \\ \Rightarrow\quad l^{2}+m^{2}+m^{2}&=m\quad\Rightarrow\quad l^{2}+2m^{2}=m && \text{(II)} \end{aligned}$$

$$\mathbf{A}\cdot\mathbf{B}=\mathbf{0}:\qquad \begin{pmatrix} \\tfrac{1}{3} & \\tfrac{1}{3} & \\tfrac{1}{3} \\ \\tfrac{1}{3} & \\tfrac{1}{3} & \\tfrac{1}{3} \\ \\tfrac{1}{3} & \\tfrac{1}{3} & \\tfrac{1}{3} \end{pmatrix}\cdot\begin{pmatrix} k & -l & -l \\ -l & m & m \\ -l & m & m \end{pmatrix}=\mathbf{0}$$

$$\begin{array}{lrcll} \Rightarrow & \frac{1}{3}k-\frac{1}{3}l-\frac{1}{3}l & = & 0 & \\ \Rightarrow & k-2l & = & 0 & \\ \Rightarrow & k & = & 2l & \text{(III)} \end{array}$$

$$\begin{array}{lrcll} \Rightarrow & -\frac{1}{3}l+\frac{1}{3}m+\frac{1}{3}m & = & 0 & \\ \Rightarrow & -l+2m & = & 0 & \\ \Rightarrow & l & = & 2m & \text{(IV)} \end{array}$$

(III) in (I) einsetzen:

$$\begin{array}{lrcl} \Rightarrow & {(2l)}^{2}+2l^{2} & = & 2l \\ \Rightarrow & 6l^{2} & = & 2l \\ \Rightarrow & 3l & = & 1 \\ \Rightarrow & l & = & \frac{1}{3} \end{array}$$

$$\text{(III) }\Rightarrow\quad k=2\cdot\frac{1}{3}=\frac{2}{3}$$

(IV) in (II) einsetzen:

$$\begin{array}{lrcl} \Rightarrow & {(2m)}^{2}+2m^{2} & = & m \\ \Rightarrow & 6m^{2} & = & m \\ \Rightarrow & 6m & = & 1 \\ \Rightarrow & m & = & \frac{1}{6} \end{array}$$

Damit:

$$h=\frac{1}{3},\quad k=\frac{2}{3},\quad l=\frac{1}{3},\quad m=\frac{1}{6}$$
```
````
