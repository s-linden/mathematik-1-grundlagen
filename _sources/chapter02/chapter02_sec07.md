# Übungen zum Selbststudium

```{admonition} Übung 2.1
:class: miniexercise
Bestimmen Sie die Umkehrfunktionen folgender Funktionen. Geben Sie auch die Definitionsbereiche der Umkehrfunktionen an!

a) $\displaystyle f(x)={x}^{2}-1\qquad x\geq0,\ x\in\mathbb{R}$

b) $\displaystyle f(x)={(x+1)}^{2}\qquad x\geq-1,\ x\in\mathbb{R}$

c) $\displaystyle f(x)={x}^{3}+1\qquad x\in\mathbb{R}$

d) $\displaystyle f(x)={e}^{-x}\qquad x\in\mathbb{R}$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $\displaystyle {f}^{-1}(x)=\sqrt{x+1},\quad x\geq-1,\ x\in\mathbb{R}$

b) $\displaystyle {f}^{-1}(x)=\sqrt{x}-1,\quad x\geq0,\ x\in\mathbb{R}$

c) $\displaystyle {f}^{-1}(x)=\sqrt[3]{x-1},\quad x\in\mathbb{R}$

d) $\displaystyle {f}^{-1}(x)=-\ln (x),\quad x>0,\ x\in\mathbb{R}$

```{dropdown} Lösungsweg
a)

$$\begin{array}{lrcll} & f(x) & = & {x}^{2}-1 & \\ \Leftrightarrow & y & = & {x}^{2}-1 & \\ \Leftrightarrow & y+1 & = & {x}^{2} & \\ \Leftrightarrow & \sqrt{y+1} & = & x & |x={f}^{-1}(y) \\ \Rightarrow & {f}^{-1}(y) & = & \sqrt{y+1} & \text{| y gegen x tauschen} \\ \Rightarrow & {f}^{-1}(x) & = & \sqrt{x+1} & x\geq-1,\ x\in\mathbb{R} \end{array}$$

b)

$$\begin{array}{lrcll} & f(x) & = & {(x+1)}^{2} & \\ \Leftarrow & y & = & {(x+1)}^{2} & \\ \Leftarrow & \sqrt{y} & = & x+1 & \\ \Leftarrow & \sqrt{y}-1 & = & x & \text{| }x={f}^{-1}(y) \\ \Rightarrow & {f}^{-1}(y) & = & \sqrt{y}-1 & \text{| y gegen x tauschen} \\ \Rightarrow & {f}^{-1}(x) & = & \sqrt{x}-1 & x\geq0,\ x\in\mathbb{R} \end{array}$$

c)

$$\begin{array}{lrcll} & f(x) & = & {x}^{3}+1 & \\ \Leftrightarrow & y & = & {x}^{3}+1 & \\ \Leftrightarrow & y-1 & = & {x}^{3} & \\ \Leftrightarrow & \sqrt[3]{y-1} & = & x & \text{| }x={f}^{-1}(y) \\ \Rightarrow & {f}^{-1}(y) & = & \sqrt[3]{y-1} & \text{| y gegen x tauschen} \\ \Rightarrow & {f}^{-1}(x) & = & \sqrt[3]{x-1} & ,\quad x\in\mathbb{R} \end{array}$$

d)

$$\begin{array}{lrcll} & f(x) & = & {e}^{-x} & \\ \Leftrightarrow & y & = & {e}^{-x} & \\ \Leftrightarrow & \ln (y) & = & \ln ({e}^{-x}) & \\ \Leftrightarrow & \ln (y) & = & -x & \\ \Leftrightarrow & -\ln (y) & = & x & \text{| }x={f}^{-1}(y) \\ \Rightarrow & {f}^{-1}(y) & = & -\ln (y) & \text{| y gegen x tauschen} \\ \Rightarrow & {f}^{-1}(x) & = & -\ln (x) & x>0,\ x\in\mathbb{R} \end{array}$$
```
````

```{admonition} Übung 2.2
:class: miniexercise
Zeigen Sie:

a) $\displaystyle {\sin }^{2}x=\frac{1}{2}(1-\cos (2x))$

b) $\displaystyle {\cos }^{2}x=\frac{1}{2}(1+\cos (2x))$

c) $\displaystyle {\sin }^{4}x=\frac{1}{8}(3-4\cos (2x)+\cos (4x))$

Hinweis zu c): Dazu kann man a) quadrieren.
```

````{admonition} Lösung
:class: miniexercise, toggle

Umrechnung durch Verwendung der Additionstheoreme.

```{dropdown} Lösungsweg
a)

$$\text{z.z.: }\,{\sin }^{2}x\,=\,\frac{1}{2}(1-\cos (2x))$$

cos-Additionstheorem: $\cos (a+b)\,=\,\cos (a)\cos (b)-\sin (a)\sin (b)$

Mit $a=b=x\qquad \Rightarrow\,\cos (2x)\,=\,{\cos }^{2}x-{\sin }^{2}x$

Es gilt: ${\sin }^{2}x+{\cos }^{2}x\,=\,1\,\Rightarrow\,{\cos }^{2}x\,=\,1-{\sin }^{2}x$

Damit $\Rightarrow\,\cos (2x)\,=\,(1-{\sin }^{2}x)-{\sin }^{2}x\,=\,1-2{\sin }^{2}x$

$$\Rightarrow\qquad {\sin }^{2}x\,=\,\frac{1}{2}(1-\cos (2x))$$

b)

$$\text{z.z.: }\,{\cos }^{2}x=\frac{1}{2}(1+\cos (2x))$$

cos-Additionstheorem: $\cos (a+b)\,=\,\cos (a)\cos (b)-\sin (a)\sin (b)$

Mit $a=b=x\qquad \Rightarrow\,\cos (2x)\,=\,{\cos }^{2}x-{\sin }^{2}x$

Es gilt: ${\sin }^{2}x+{\cos }^{2}x\,=\,1\,\Rightarrow\,{\sin }^{2}x\,=\,1-{\cos }^{2}x$

Damit $\Rightarrow\,\cos (2x)\,=\,{\cos }^{2}x-(1-{\cos }^{2}x)\,=\,2{\cos }^{2}x-1$

$$\Rightarrow\,{\cos }^{2}x\,=\,\frac{1}{2}(1+\cos (2x))$$

c)

$$
\begin{aligned}
{\sin }^{4}x\,&=\,{({\sin }^{2}x)}^{2}\,\overset{\text{Teilaufgabe }a}{=}\,{\left( \frac{1}{2}(1-\cos (2x)) \right)}^{2}\,=\,\frac{1}{4}{(1-\cos (2x))}^{2} \\
&=\,\frac{1}{4}(1-2\cos (2x)+{\color{green} {\cos }^{2}(2x)})\qquad \text{| Teilaufgabe b mit 2x statt x} \\
&=\,\frac{1}{4}\left( 1-2\cos (2x)+{\color{green} \frac{1}{2}(1+\cos (4x))} \right)\qquad \text{| }\frac{1}{2}\text{ ausklammern} \\
&=\,\frac{1}{8}\left( 3-4\cos (2x)+\cos (4x) \right)
\end{aligned}
$$
```
````

```{admonition} Übung 2.3
:class: miniexercise
Vereinfachen Sie die folgenden Terme.

a) $\displaystyle 2{\sin }^{2}(x)\cos (\frac{x}{2})+\cos (2x)\sin (\frac{x}{2}+\frac{\pi}{2})$

b) $\displaystyle \sin (2x)\cos (x)-{\cos }^{2}(x)\sin (x)+{\sin }^{3}(x)$

c) $\displaystyle {\cos }^{3}(x)-3{\sin }^{2}(x)\cos (x)$

d) $\displaystyle 2\sin (2x)\left( 1-2{\sin }^{2}(x) \right)$

Hinweis: Die Terme lassen sich auf einen einzelnen Sinus- oder Cosinus-Term reduzieren.
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $\displaystyle \cos (x/2)$

b) $\displaystyle \sin (x)$

c) $\displaystyle \cos (3x)$

d) $\displaystyle \sin (4x)$

```{dropdown} Lösungsweg
a)

$$
\begin{aligned}
&2{\sin }^{2}(x)\cos (\frac{x}{2})+{\color{green} \cos (2x)}{\color{blue} \sin (\frac{x}{2}+\frac{\pi}{2})} \\
&=2{\sin }^{2}(x)\cos (x/2)+{\color{green} \left( {\cos }^{2}(x)-{\sin }^{2}(x) \right)}{\color{blue} \cos (x/2)} \\
&=\cos (x/2)\left( {\sin }^{2}(x)+{\cos }^{2}(x) \right)\qquad =\cos (x/2)
\end{aligned}
$$

b)

$$
\begin{aligned}
&\sin (2x)\cos (x)-{\cos }^{2}(x)\sin (x)+{\sin }^{3}(x) \\
&=\cos (x)\left( {\color{blue} \sin (2x)}-\cos (x)\sin (x) \right)+{\sin }^{3}(x) \\
&=\cos (x)\left( {\color{blue} 2\cos (x)\sin (x)}-\cos (x)\sin (x) \right)+{\sin }^{3}(x) \\
&={\cos }^{2}(x)\sin (x)+{\sin }^{3}(x)=\sin (x)\left( {\cos }^{2}(x)+{\sin }^{2}(x) \right)\qquad =\sin (x)
\end{aligned}
$$

c)

$$
\begin{aligned}
&{\cos }^{3}(x)-3{\sin }^{2}(x)\cos (x) \\
&=\cos (x)\left( {\color{blue} {\cos }^{2}(x)-{\sin }^{2}(x)}-2{\sin }^{2}(x) \right) \\
&=\cos (x)\left( {\color{blue} \cos (2x)}-2{\sin }^{2}(x) \right) \\
&=\cos (x)\cos (2x)-\sin (x)\left( {\color{green} 2\sin (x)\cos (x)} \right) \\
&=\cos (x)\cos (2x)-\sin (x){\color{green} \sin (2x)}\qquad =\cos (3x)
\end{aligned}
$$

d)

$$
\begin{aligned}
&2\sin (2x)\left( 1-2{\sin }^{2}(x) \right) \\
&=2\sin (2x)\left( {\color{green} 1-{\sin }^{2}(x)}-{\sin }^{2}(x) \right) \\
&=2\sin (2x)\left( {\color{green} {\cos }^{2}(x)}-{\sin }^{2}(x) \right) \\
&=2\sin (2x)\cos (2x)\qquad =\sin (4x)
\end{aligned}
$$

Letzter Schritt:

sin-Additionstheorem: $\sin (a+b)\,=\,\sin a\cos b+\cos a\sin b$

Nun a=b=y : $\sin (2y)\,=\,2\sin y\cos y$

Nun y = 2x : $\sin (4x)\,=\,2\sin 2x\cos 2x$
```
````
