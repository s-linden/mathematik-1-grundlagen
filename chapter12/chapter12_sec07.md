# Übungen zum Selbststudium

```{admonition} Übung 12.1
:class: miniexercise
Bestimmen Sie die folgenden bestimmten Integrale.

a) $\displaystyle \int_{-2}^{3}(x+2)(x-3)\,dx$

b) $\displaystyle \int_{a}^{b}\left(a_0+a_1x+a_2x^2\right)dx$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $\displaystyle -\frac{125}{6}$

b) $\displaystyle a_0(b-a)+\frac{1}{2}a_1(b^2-a^2)+\frac{1}{3}a_2(b^3-a^3)$

```{dropdown} Lösungsweg
a)

$$
\begin{aligned}
\int_{-2}^{3}(x+2)(x-3)\,dx&=\int_{-2}^{3}\left(x^2-x-6\right)dx=\left[\frac{x^3}{3}-\frac{x^2}{2}-6x\right]_{-2}^{3}=-\frac{125}{6}
\end{aligned}
$$

b)

$$
\begin{aligned}
\int_{a}^{b}\left(a_0+a_1x+a_2x^2\right)dx&=a_0(b-a)+\frac{1}{2}a_1(b^2-a^2)+\frac{1}{3}a_2(b^3-a^3)
\end{aligned}
$$
```
````

```{admonition} Übung 12.2
:class: miniexercise
Integrieren Sie.

a) $\displaystyle \int\left(x^4+x\right)dx$

b) $\displaystyle \int\left(2x^3-3x^2+6\right)dx$

c) $\displaystyle \int\frac{2}{3}\left(3x-5x^3+2x^6\right)dx$

d) $\displaystyle \int\cos x\,dx$

e) $\displaystyle \int\left(3\cos x+\sin x\right)dx$

f) $\displaystyle \int\frac{1}{\cos^2x}\,dx$

g) $\displaystyle \int x\left(3x^2+4x\right)dx$

h) $\displaystyle \int(x-1)(x^2-4)\,dx$

i) $\displaystyle \int e^x\,dx$

j) $\displaystyle \int e^{-2x}\,dx$

k) $\displaystyle \int a^x\,dx$ mit $a\in\mathbb{R}^{+}\setminus\{1\}$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $\displaystyle \int\left(x^4+x\right)dx=\frac{x^5}{5}+\frac{x^2}{2}+C$

b) $\displaystyle \int\left(2x^3-3x^2+6\right)dx=\frac{x^4}{2}-x^3+6x+C$

c) $\displaystyle \int\frac{2}{3}\left(3x-5x^3+2x^6\right)dx=x^2-\frac{5}{6}x^4+\frac{4}{21}x^7+C$

d) $\displaystyle \int\cos x\,dx=\sin x+C$

e) $\displaystyle \int\left(3\cos x+\sin x\right)dx=3\sin x-\cos x+C$

f) $\displaystyle \int\frac{1}{\cos^2x}\,dx=\tan x+C$

g) $\displaystyle \int x\left(3x^2+4x\right)dx=\frac{3}{4}x^4+\frac{4}{3}x^3+C$

h) $\displaystyle \int(x-1)(x^2-4)\,dx=\frac{x^4}{4}-\frac{x^3}{3}-2x^2+4x+C$

i) $\displaystyle \int e^x\,dx=e^x+C$

j) $\displaystyle \int e^{-2x}\,dx=-\frac{1}{2}e^{-2x}+C$

k) $\displaystyle \int a^x\,dx=\frac{1}{\ln a}\,a^x+C$

```{dropdown} Lösungsweg
k)

$$
\begin{aligned}
\int a^x\,dx&=\int e^{x\ln a}\,dx=\frac{1}{\ln a}\,e^{x\ln a}+C=\frac{1}{\ln a}\,a^x+C
\end{aligned}
$$
```
````

```{admonition} Übung 12.3
:class: miniexercise
Integrieren Sie mit der Substitutionsregel.

a) $\displaystyle \int(ax+b)\,dx$ (setze $z=ax+b$)

b) $\displaystyle \int 2\cos(2x)\,dx$

c) $\displaystyle \int\sin(4x+2)\,dx$

d) $\displaystyle \int\sin\!\left(\frac{ax+b}{c}\right)dx$

e) $\displaystyle \int\frac{3}{(x+7)^2}\,dx$

f) $\displaystyle \int\frac{1}{2(5-3x)^2}\,dx$

g) $\displaystyle \int\sqrt{1+x}\,dx$

h) $\displaystyle \int\frac{x}{\sqrt{x^2+1}}\,dx$

i) $\displaystyle \int e^x\sqrt{1+e^x}\,dx$

j) $\displaystyle \int a^x\sqrt{1+a^x}\,dx$ mit $a\in\mathbb{R}^{+}\setminus\{1\}$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $\displaystyle \int(ax+b)\,dx=\frac{a}{2}x^2+bx+C$

b) $\displaystyle \int 2\cos(2x)\,dx=\sin(2x)+C$

c) $\displaystyle \int\sin(4x+2)\,dx=-\frac{1}{4}\cos(4x+2)+C$

d) $\displaystyle \int\sin\!\left(\frac{ax+b}{c}\right)dx=-\frac{c}{a}\cos\!\left(\frac{ax+b}{c}\right)+C$

e) $\displaystyle \int\frac{3}{(x+7)^2}\,dx=-\frac{3}{x+7}+C$

f) $\displaystyle \int\frac{1}{2(5-3x)^2}\,dx=\frac{1}{6}\cdot\frac{1}{5-3x}+C$

g) $\displaystyle \int\sqrt{1+x}\,dx=\frac{2}{3}(1+x)^{3/2}+C$

h) $\displaystyle \int\frac{x}{\sqrt{x^2+1}}\,dx=\sqrt{x^2+1}+C$

i) $\displaystyle \int e^x\sqrt{1+e^x}\,dx=\frac{2}{3}(1+e^x)^{3/2}+C$

j) $\displaystyle \int a^x\sqrt{1+a^x}\,dx=\frac{1}{\ln a}\cdot\frac{2}{3}\left(1+a^x\right)^{3/2}+C$

```{dropdown} Lösungsweg
a)

$$
\begin{aligned}
\int(ax+b)\,dx\quad&\text{mit}\quad z=ax+b,\ dz=a\,dx \\
&=\frac{1}{a}\int(ax+b)\,a\,dx=\frac{1}{a}\int z\,dz \\
&=\frac{1}{a}\left(\frac{1}{2}z^2+B\right)=\frac{1}{a}\left(\frac{1}{2}(ax+b)^2+B\right) \\
&=\frac{a}{2}x^2+bx+C\quad\text{mit}\quad C=\frac{b^2}{2a}+\frac{B}{a}
\end{aligned}
$$

b)

$$
\begin{aligned}
\int 2\cos(2x)\,dx\quad&\text{mit}\quad z=2x,\ dz=2\,dx \\
&=\int\cos(z)\,dz=\sin(z)+C=\sin(2x)+C
\end{aligned}
$$

c)

$$
\begin{aligned}
\int\sin(4x+2)\,dx\quad&\text{mit}\quad z=4x+2,\ dz=4\,dx \\
&=\int\sin(z)\,\frac{dz}{4}=\frac{1}{4}\bigl(-\cos(z)\bigr)+C=-\frac{1}{4}\cos(4x+2)+C
\end{aligned}
$$

d)

$$
\begin{aligned}
\int\sin\!\left(\frac{ax+b}{c}\right)dx\quad&\text{mit}\quad \bar a=\frac{a}{c},\ \bar b=\frac{b}{c},\ z=\bar a x+\bar b,\ dz=\bar a\,dx \\
&=\int\sin(\bar a x+\bar b)\,dx \\
&=\frac{1}{\bar a}\int\sin(z)\,dz \\
&=\frac{1}{\bar a}\bigl(-\cos(z)\bigr)+C \\
&=\frac{1}{\bar a}\bigl(-\cos(\bar a x+\bar b)\bigr)+C \\
&=-\frac{c}{a}\cos\!\left(\frac{ax+b}{c}\right)+C
\end{aligned}
$$

e)

$$
\begin{aligned}
\int\frac{3}{(x+7)^2}\,dx\quad&\text{mit}\quad z=x+7,\ dz=dx \\
&=3\int\frac{dz}{z^2}=-3\cdot\frac{1}{z}=-3\cdot\frac{1}{x+7}+C
\end{aligned}
$$

f)

$$
\begin{aligned}
\int\frac{1}{2(5-3x)^2}\,dx\quad&\text{mit}\quad z=5-3x,\ dz=-3\,dx \\
&=-\frac{1}{3}\int\frac{1}{2z^2}\,dz=-\frac{1}{6}\int\frac{1}{z^2}\,dz \\
&=-\frac{1}{6}\left(-\frac{1}{z}\right)+C=\frac{1}{6}\cdot\frac{1}{5-3x}+C
\end{aligned}
$$

g)

$$
\begin{aligned}
\int\sqrt{1+x}\,dx\quad&\text{mit}\quad z=1+x,\ dz=dx \\
&=\int\sqrt{z}\,dz=\int z^{1/2}\,dz=\frac{2}{3}z^{3/2}+C=\frac{2}{3}(1+x)^{3/2}+C
\end{aligned}
$$

h)

$$
\begin{aligned}
\int\frac{x}{\sqrt{x^2+1}}\,dx\quad&\text{mit}\quad z=x^2+1,\ dz=2x\,dx \\
&=\frac{1}{2}\int\frac{1}{\sqrt{z}}\,dz=\sqrt{z}+C=\sqrt{x^2+1}+C
\end{aligned}
$$

i)

$$
\begin{aligned}
\int e^x\sqrt{1+e^x}\,dx\quad&\text{mit}\quad z=1+e^x,\ dz=e^x\,dx \\
&=\int\sqrt{z}\,dz=\frac{2}{3}z^{3/2}+C=\frac{2}{3}(1+e^x)^{3/2}+C
\end{aligned}
$$

j)

$$
\begin{aligned}
\int a^x\sqrt{1+a^x}\,dx\quad&\text{mit}\quad z=1+a^x,\ dz=(\ln a)\,a^x\,dx \\
&=\frac{1}{\ln a}\int\sqrt{z}\,dz=\frac{1}{\ln a}\cdot\frac{2}{3}z^{3/2}+C \\
&=\frac{1}{\ln a}\cdot\frac{2}{3}\left(1+a^x\right)^{3/2}+C
\end{aligned}
$$
```
````

```{admonition} Übung 12.4
:class: miniexercise
Integrieren Sie mittels partieller Integration.

a) $\displaystyle \int x\sin x\,dx$

b) $\displaystyle \int x\cos 3x\,dx$

c) $\displaystyle \int x^2\sin x\,dx$

d) $\displaystyle \int\cos^2x\,dx$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $\displaystyle \int x\sin x\,dx=-x\cos x+\sin x+C$

b) $\displaystyle \int x\cos 3x\,dx=\frac{x}{3}\sin(3x)+\frac{1}{9}\cos(3x)+C$

c) $\displaystyle \int x^2\sin x\,dx=-x^2\cos x+2x\sin x+2\cos x+C$

d) $\displaystyle \int\cos^2x\,dx=\frac{1}{2}\left(\cos x\sin x+x\right)+C$

```{dropdown} Lösungsweg
a)

$$
\begin{aligned}
\int\underbrace{x}_{u}\,\underbrace{\sin x}_{v'}\,dx&=\underbrace{x}_{u}\,\underbrace{(-\cos x)}_{v}-\int\underbrace{1}_{u'}\,\underbrace{(-\cos x)}_{v}\,dx \\
&=-x\cos x+\sin x+C
\end{aligned}
$$

b)

$$
\begin{aligned}
\int\underbrace{x}_{u}\,\underbrace{\cos 3x}_{v'}\,dx&=\underbrace{x}_{u}\,\underbrace{\tfrac{1}{3}\sin(3x)}_{v}-\int\underbrace{1}_{u'}\,\underbrace{\tfrac{1}{3}\sin(3x)}_{v}\,dx \\
&=\frac{x}{3}\sin(3x)+\frac{1}{9}\cos(3x)+C
\end{aligned}
$$

c)

$$
\begin{aligned}
\int\underbrace{x^2}_{u}\,\underbrace{\sin x}_{v'}\,dx&=x^2(-\cos x)-\int(-2x)\cos x\,dx=-x^2\cos x+2\int x\cos x\,dx \\
&=-x^2\cos x+2x\sin x-2\int\sin x\,dx \\
&=-x^2\cos x+2x\sin x+2\cos x+C
\end{aligned}
$$

d)

$$
\begin{aligned}
\int\cos^2x\,dx\quad&\text{mit}\quad u=\cos x,\ u'=-\sin x,\ v'=\cos x,\ v=\sin x \\
&=\cos x\sin x-\int(-\sin x)\sin x\,dx\quad\text{mit}\quad\sin^2x=1-\cos^2x \\
\Rightarrow\quad\int\cos^2x\,dx&=\frac{1}{2}\left(\cos x\sin x+x\right)+C
\end{aligned}
$$
```
````

```{admonition} Übung 12.5
:class: miniexercise
Sei die Funktion $f(x)$ auf dem Intervall $[-a,a]$ integrierbar. Zeigen Sie:

$$\int_{-a}^{a}f(x)\,dx=\begin{cases}0 & \text{falls } f \text{ ungerade ist,}\\ 2\displaystyle\int_{0}^{a}f(x)\,dx & \text{falls } f \text{ gerade ist.}\end{cases}$$
```

````{admonition} Lösung
:class: miniexercise, toggle

Aufteilen des Integrationsintervalls in $[-a,0]$ und $[0,a]$ und Substitution $x=-z$ im ersten Integral.

```{dropdown} Lösungsweg
Teile das Integrationsintervall:

$$\int_{-a}^{a}f(x)\,dx=\int_{-a}^{0}f(x)\,dx+\int_{0}^{a}f(x)\,dx$$

Im ersten Integral substituiere $x=-z$, $dx=-dz$. D.h. für die Integralgrenzen: $x=-a$ wird zu $z=a$, $x=0$ wird zu $z=0$.

$$\int_{-a}^{a}f(x)\,dx=\int_{-a}^{0}f(x)\,dx+\int_{0}^{a}f(x)\,dx=-\int_{a}^{0}f(-z)\,dz+\int_{0}^{a}f(x)\,dx$$

$f$ gerade: $f(-z)=f(z)$

$$
\begin{aligned}
\int_{-a}^{a}f(x)\,dx&=-\int_{a}^{0}f(-z)\,dz+\int_{0}^{a}f(x)\,dx=-\int_{a}^{0}f(z)\,dz+\int_{0}^{a}f(x)\,dx \\
&=\int_{0}^{a}f(z)\,dz+\int_{0}^{a}f(x)\,dx=2\int_{0}^{a}f(x)\,dx
\end{aligned}
$$

$f$ ungerade: $f(-z)=-f(z)$

$$
\begin{aligned}
\int_{-a}^{a}f(x)\,dx&=-\int_{a}^{0}f(-z)\,dz+\int_{0}^{a}f(x)\,dx=-\int_{a}^{0}\bigl(-f(z)\bigr)dz+\int_{0}^{a}f(x)\,dx \\
&=-\int_{0}^{a}f(z)\,dz+\int_{0}^{a}f(x)\,dx=0
\end{aligned}
$$
```
````
