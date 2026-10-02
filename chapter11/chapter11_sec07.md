# Übungen zum Selbststudium

```{admonition} Übung 11.1
:class: miniexercise
Bestimmen Sie die lokalen Extrema. M.a.W., an welchen Stellen haben die Funktionen lokale Extrema, und handelt es sich um ein Minimum oder Maximum?

a) $\displaystyle f(x)=x^2-5x$

b) $\displaystyle f(x)=(1-x)^2$

c) $\displaystyle f(x)=1-x^2$

d) $\displaystyle f(x)=(x-1)^2$

e) $\displaystyle f(x)=x^3-75x$

f) $\displaystyle f(x)=\frac{1}{1+x^2}$

g) $\displaystyle f(x)=\frac{x}{1+x^2}$

h) $\displaystyle f(x)=\frac{x^2}{1+x^2}$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) Minimum bei $x=\frac{5}{2}$

b) Minimum bei $x=1$

c) Maximum bei $x=0$

d) Minimum bei $x=1$ (siehe b))

e) Minimum bei $x=5$, Maximum bei $x=-5$

f) Maximum bei $x=0$

g) Minimum bei $x=-1$, Maximum bei $x=1$

h) Minimum bei $x=0$

```{dropdown} Lösungsweg
a)

$$
\begin{aligned}
f(x)&=x^2-5x \\
f'(x)&=2x-5=0\ \Rightarrow\ x=\frac{5}{2} \\
f''(x)&=2>0:\ \text{Minimum}
\end{aligned}
$$

b)

$$
\begin{aligned}
f(x)&=(1-x)^2 \\
f'(x)&=-2(1-x)=2x-2=0\ \Rightarrow\ x=1 \\
f''(x)&=2>0:\ \text{Minimum}
\end{aligned}
$$

c)

$$
\begin{aligned}
f(x)&=1-x^2 \\
f'(x)&=-2x=0\ \Rightarrow\ x=0 \\
f''(x)&=-2<0:\ \text{Maximum}
\end{aligned}
$$

d)

$f(x)=(x-1)^2=(-1)^2(1-x)^2=(1-x)^2$, siehe b).

e)

$$
\begin{aligned}
f(x)&=x^3-75x \\
f'(x)&=3x^2-75=0\ \Rightarrow\ x=\pm5 \\
f''(x)&=6x \\
f''(5)&=30>0:\ \text{Minimum} \\
f''(-5)&=-30<0:\ \text{Maximum}
\end{aligned}
$$

f)

$$
\begin{aligned}
f(x)&=\frac{1}{1+x^2} \\
f'(x)&=-\frac{2x}{(1+x^2)^2}=0\ \Rightarrow\ x=0 \\
f''(x)&=\frac{-2(1+x^2)+8x^2}{(1+x^2)^3} \\
f''(0)&=-2<0:\ \text{Maximum}
\end{aligned}
$$

g)

$$
\begin{aligned}
f(x)&=\frac{x}{1+x^2} \\
f'(x)&=\frac{1-x^2}{(1+x^2)^2}=0\ \Rightarrow\ x=1\ \text{oder}\ x=-1 \\
f''(x)&=\frac{-2x(1+x^2)-(1-x^2)\cdot4x}{(1+x^2)^3} \\
f''(-1)&>0:\ \text{Minimum} \\
f''(1)&<0:\ \text{Maximum}
\end{aligned}
$$

h)

$$
\begin{aligned}
f(x)&=\frac{x^2}{1+x^2} \\
f'(x)&=\frac{2x}{(1+x^2)^2}=0\ \Rightarrow\ x=0 \\
f''(x)&=\frac{2(1+x^2)-8x^2}{(1+x^2)^3} \\
f''(0)&>0:\ \text{Minimum}
\end{aligned}
$$
```
````

```{admonition} Übung 11.2
:class: miniexercise
Welche Bedingung müssen die Koeffizienten $a$, $b$, $c$ und $d$ erfüllen, damit $f(x)=ax^3+bx^2+cx+d$ zwei lokale Extrema hat?
```

````{admonition} Lösung
:class: miniexercise, toggle

$b^2-3ac>0$

```{dropdown} Lösungsweg
$$
\begin{aligned}
f'(x)&=3ax^2+2bx+c \\
f'(x)=0\ \Rightarrow\ x^2+\frac{2b}{3a}\,x+\frac{c}{3a}&=0\quad\text{mit}\quad p=\frac{2b}{3a},\ q=\frac{c}{3a} \\
\Rightarrow\ x&=-\frac{p}{2}\pm\sqrt{\left(\frac{p}{2}\right)^2-q}
\end{aligned}
$$

Zwei Extrema gibt es genau dann, wenn $\left(\dfrac{p}{2}\right)^2-q>0$, d.h. $b^2-3ac>0$.
```
````

```{admonition} Übung 11.3
:class: miniexercise
Zerlegen Sie die Zahl 60 so in zwei Summanden, dass das Produkt dieser Zahlen ein Maximum annimmt.
```

````{admonition} Lösung
:class: miniexercise, toggle

Die beiden Summanden sind $30$ und $30$ (das Produkt ist dann $900$).

```{dropdown} Lösungsweg
$$
\begin{aligned}
60&=a+b\ \Rightarrow\ b=60-a \\
f(a)&=a(60-a)=60a-a^2 \\
f'(a)&=60-2a=0\ \Rightarrow\ a=30 \\
f''(a)&=-2<0:\ \text{Maximum}
\end{aligned}
$$
```
````

```{admonition} Übung 11.4
:class: miniexercise
Zerlegen Sie die Zahl 24 so in zwei Summanden, dass die Summe der Quadrate dieser Zahlen möglichst klein wird.
```

````{admonition} Lösung
:class: miniexercise, toggle

Die beiden Summanden sind $12$ und $12$.

```{dropdown} Lösungsweg
$$
\begin{aligned}
24&=a+b\ \Rightarrow\ b=24-a \\
f(a)&=a^2+(24-a)^2 \\
f'(a)&=2a+2(24-a)(-1)=4a-48=0\ \Rightarrow\ a=12 \\
f''(a)&=4>0:\ \text{Minimum}
\end{aligned}
$$
```
````

```{admonition} Übung 11.5
:class: miniexercise
Berechnen Sie die folgenden Grenzwerte.

Hinweis: Verwenden Sie die Regel von l'Hospital.

a) $\displaystyle \lim_{x\to0}\frac{\sin x}{e^x-1}$

b) $\displaystyle \lim_{x\to1}\frac{\ln x}{x^2-1}$

c) $\displaystyle \lim_{x\to0}\frac{1-\cos x}{x^2}$

d) $\displaystyle \lim_{x\to0}x^b\ln x$ für $x>0$, $b>0$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $1$

b) $\dfrac{1}{2}$

c) $\dfrac{1}{2}$

d) $0$

```{dropdown} Lösungsweg
a)

$$
\begin{aligned}
\lim_{x\to0}\frac{\sin x}{e^x-1}&=\lim_{x\to0}\frac{\cos x}{e^x}=\frac{1}{1}=1
\end{aligned}
$$

b)

$$
\begin{aligned}
\lim_{x\to1}\frac{\ln x}{x^2-1}&=\lim_{x\to1}\frac{\frac{1}{x}}{2x}=\lim_{x\to1}\frac{1}{2x^2}=\frac{1}{2}
\end{aligned}
$$

c)

$$
\begin{aligned}
\lim_{x\to0}\frac{1-\cos x}{x^2}&=\lim_{x\to0}\frac{\sin x}{2x}=\lim_{x\to0}\frac{\cos x}{2}=\frac{1}{2}
\end{aligned}
$$

d)

Wegen des Logarithmus ist der Grenzwert ohnehin nur für $x\downarrow0$ definiert.

Es ist $\displaystyle x^b\ln x=\frac{\ln x}{x^{-b}}$ für $x>0$, $b>0$. Wegen $\displaystyle\lim_{x\downarrow0}\ln x=-\infty$ und $\displaystyle\lim_{x\downarrow0}x^{-b}=\infty$ lässt sich die Regel von l'Hospital anwenden. Also:

$$
\begin{aligned}
\lim_{x\downarrow0}x^b\ln x&=\lim_{x\downarrow0}\frac{\ln x}{x^{-b}}=\lim_{x\downarrow0}\frac{\frac{1}{x}}{-b\,x^{-b-1}} \\
&=\lim_{x\downarrow0}\left(-\frac{1}{b}\right)x^{-1}\,x^{b+1}=\lim_{x\downarrow0}\left(-\frac{1}{b}\right)x^{b}=0
\end{aligned}
$$
```
````

```{admonition} Übung 11.6
:class: miniexercise
Ermitteln Sie die Gleichung der Tangente.

a) $\displaystyle f(x)=\frac{x^2}{2}$ bei $x_0=1$

b) $\displaystyle f(x)=\frac{x^2}{4}\sqrt{8-x}$ bei $x_0=-1$

c) $\displaystyle f(x)=\frac{1}{x+4}$ bei $x_0=3$

d) $\displaystyle f(x)=\frac{x^2-4}{x+4}$ bei $x_0=3$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $g(x)=x-\dfrac{1}{2}$

b) $g(x)=-\dfrac{19}{24}-\dfrac{37}{24}\,x$

c) $g(x)=\dfrac{10}{49}-\dfrac{x}{49}$

d) $g(x)=\dfrac{5}{7}+\dfrac{37}{49}(x-3)=\dfrac{37x-76}{49}$

```{dropdown} Lösungsweg
a)

$$
\begin{aligned}
f(1)&=\frac{1}{2},\qquad f'(x)=x,\qquad f'(1)=1 \\
g(x)&=\frac{1}{2}+1\cdot(x-1)=x-\frac{1}{2}
\end{aligned}
$$

b)

$$
\begin{aligned}
f(-1)&=\frac{3}{4},\qquad f'(x)=\frac{32x-5x^2}{8\sqrt{8-x}},\qquad f'(-1)=-\frac{37}{24} \\
g(x)&=\frac{3}{4}-\frac{37}{24}(x+1)=-\frac{19}{24}-\frac{37}{24}\,x
\end{aligned}
$$

c)

$$
\begin{aligned}
f(3)&=\frac{1}{7},\qquad f'(x)=-\frac{1}{(x+4)^2},\qquad f'(3)=-\frac{1}{49} \\
g(x)&=\frac{1}{7}-\frac{1}{49}(x-3)=\frac{10}{49}-\frac{x}{49}
\end{aligned}
$$

d)

$$
\begin{aligned}
f(3)&=\frac{5}{7},\qquad f'(x)=\frac{x^2+8x+4}{(x+4)^2},\qquad f'(3)=\frac{37}{49} \\
g(x)&=\frac{5}{7}+\frac{37}{49}(x-3)
\end{aligned}
$$
```
````

```{admonition} Übung 11.7
:class: miniexercise
Bei einem Pendel der Länge $L$ berechnet sich die Schwingungsdauer $T$ einer Schwingung nach der Formel $T=2\pi\sqrt{\dfrac{L}{g}}$, wobei $g$ die Erdbeschleunigung ist ($g\approx10\ \mathrm{m/s^2}$).

a) Auf wie viel Prozent genau kann man die Schwingungsdauer $T$ angeben, wenn man die Pendellänge auf 1 % genau bestimmt?

b) Nach wie viel Sekunden geht ein „Sekundenpendel“ ($T=2\,\mathrm{s}$) um 1 Sekunde vor, wenn man die Pendellänge um 0,1 % zu kurz macht?
```

````{admonition} Lösung
:class: miniexercise, toggle

a) Die Schwingungsdauer ist auf $0{,}5\,\%$ genau.

b) Nach ca. $2000\,\mathrm{s}$, also ca. einer halben Stunde.

```{dropdown} Lösungsweg
a)

$$
\begin{aligned}
T(L)&=\frac{2\pi}{\sqrt{g}}\sqrt{L} \\
T'(L)&=\frac{2\pi}{\sqrt{g}}\cdot\frac{1}{2}\cdot\frac{1}{\sqrt{L}} \\
\Delta L&=L\cdot\Delta_{\mathrm{rel}}L=0{,}01\,L \\
\Delta T&=T'(L)\,\Delta L=\frac{\pi}{\sqrt{g}\sqrt{L}}\,L\cdot\Delta_{\mathrm{rel}}L=\frac{\pi}{\sqrt{g}}\sqrt{L}\cdot\Delta_{\mathrm{rel}}L=\frac{1}{2}\,T\cdot\Delta_{\mathrm{rel}}L \\
\Delta_{\mathrm{rel}}T&=\frac{\Delta T}{T}=\frac{1}{2}\cdot\Delta_{\mathrm{rel}}L=\frac{1}{2\cdot100}
\end{aligned}
$$

Beachten Sie die Formel für $\Delta T$.

Genauigkeit für die Periode: $0{,}5\,\%$.

b)

„Geht vor“ bedeutet: Die Zeit, die bei gleicher Anzahl Schwingungen verstrichen ist, ist eine Sekunde kürzer. Die Periode des „Sekundenpendels“ sei $T_{2\mathrm{s}}$, die Periode des kürzeren Pendels sei $T$. Die Anzahl der verstrichenen Schwingungen sei $n$. Dann gilt

$$nT=nT_{2\mathrm{s}}-1\,\mathrm{s}$$

Es verstreichen also

$$n=\frac{1\,\mathrm{s}}{T_{2\mathrm{s}}-T}$$

Schwingungen, bis die Zeitdifferenz $1\,\mathrm{s}$ beträgt.

Die Periode $T$ des kürzeren Pendels lässt sich näherungsweise aus der Fehlerfortpflanzung berechnen: $T\approx T_{2\mathrm{s}}+\Delta T$. Es ist

$$\Delta T=T_{2\mathrm{s}}\cdot\frac{1}{2}\,\Delta_{\mathrm{rel}}L=2\,\mathrm{s}\cdot\frac{1}{2}\cdot\frac{1}{1000}=\frac{1}{1000}\,\mathrm{s}.$$

D.h., $n=1000$. Die Zeit, die verstreicht, sind also ca. $2000\,\mathrm{s}$, also ca. eine halbe Stunde.
```
````

```{admonition} Übung 11.8
:class: miniexercise
Bestimmen Sie die ersten 3 nichtverschwindenden Terme der Taylor-Reihen.

a) $\displaystyle f(x)=\ln x$ bei $x_0=1$

b) $\displaystyle f(x)=\frac{1}{\sqrt{x}}$ bei $x_0=1$

c) $\displaystyle f(x)=(x+1)^2(x-1)^2$ bei $x_0=-1$
```

````{admonition} Lösung
:class: miniexercise, toggle

Taylor-Polynome sind hier mit $T(x)$ bezeichnet.

a) $\displaystyle T(x)=(x-1)-\frac{1}{2}(x-1)^2+\frac{1}{3}(x-1)^3$

b) $\displaystyle T(x)=1-\frac{1}{2}(x-1)+\frac{3}{8}(x-1)^2$

c) $\displaystyle T(x)=4(x+1)^2-4(x+1)^3+(x+1)^4$
````
