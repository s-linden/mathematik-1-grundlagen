# Übungen zum Selbststudium

```{admonition} Übung 9.1
:class: miniexercise
Berechnen oder begründen Sie das Ergebnis. Es ist $n\in\mathbb{N}$.

a) $\displaystyle \lim_{n\to\infty}\frac{1}{n}$

b) $\displaystyle \lim_{n\to\infty}\frac{n-2}{n}$

c) $\displaystyle \lim_{n\to\infty}\frac{n+1}{{n}^{2}}$

d) $\displaystyle \lim_{n\to\infty}\frac{{n}^{2}+2n+1}{{n}^{2}-1},\quad n>1$

e) $\displaystyle \lim_{n\to\infty}\frac{2n+1}{3n-1}$

f) $\displaystyle \lim_{n\to\infty}\frac{2-4n}{3n+9}$

g) $\displaystyle \lim_{n\to\infty}\frac{4{n}^{2}-6n+10}{2{n}^{2}+100}$

h) $\displaystyle \lim_{n\to\infty}\frac{{n}^{4}+3{n}^{2}}{{n}^{2}+10n}$

i) $\displaystyle \lim_{n\to\infty}\frac{1+\sqrt{n}}{3+\sqrt{n}}$

j) $\displaystyle \lim_{n\to\infty}\frac{3n-\sqrt{n}}{2\sqrt{n}+5n}$

k) $\displaystyle \lim_{n\to\infty}\frac{2{n}^{2}(n-3+4{n}^{2})}{5{(n-1)}^{3}(3n+4)}$

l) $\displaystyle \lim_{n\to\infty}\frac{\sqrt{32n}+7}{13-\sqrt{2n}}$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $0$

b) $1$

c) $0$

d) $1$

e) $\frac{2}{3}$

f) $-\frac{4}{3}$

g) $2$

h) $\infty$

i) $1$

j) $\frac{3}{5}$

k) $\frac{8}{15}$

l) $-4$

```{dropdown} Lösungsweg
a)

$0$ (monoton fallend und nach unten durch $0$ beschränkt).

b)

$$\lim_{n\to\infty}\frac{n-2}{n}=\lim_{n\to\infty}\left(\frac{n}{n}-\frac{2}{n}\right)=1-0=1$$

c)

$0$ (monoton fallend und nach unten durch $0$ beschränkt).

alternativ:

$$\lim_{n\to\infty}\frac{n+1}{{n}^{2}}=\lim_{n\to\infty}\left(\frac{n}{{n}^{2}}+\frac{1}{{n}^{2}}\right)=\lim_{n\to\infty}\left(\frac{1}{n}+\frac{1}{{n}^{2}}\right)=0+0=0$$

d)

Es ist $n>1$

$$\lim_{n\to\infty}\frac{{n}^{2}+2n+1}{{n}^{2}-1}=\lim_{n\to\infty}\frac{{n}^{2}(1+\frac{{\color{red} 2}}{n}+\frac{1}{{n}^{2}})}{{n}^{2}(1-\frac{1}{{n}^{2}})}=\lim_{n\to\infty}\frac{(1+\frac{{\color{red} 2}}{n}+\frac{1}{{n}^{2}})}{(1-\frac{1}{{n}^{2}})}=\frac{1+0+0}{1-0}=1$$

e)

$$\lim_{n\to\infty}\frac{2n+1}{3n-1}=\lim_{n\to\infty}\frac{n(2+\frac{1}{n})}{n(3-\frac{1}{n})}=\frac{2}{3}$$

f)

$$\lim_{n\to\infty}\frac{2-4n}{3n+9}=\lim_{n\to\infty}\frac{n(\frac{2}{n}-4)}{n(3+\frac{9}{n})}=\frac{-4}{3}$$

g)

$$\lim_{n\to\infty}\frac{4{n}^{2}-6n+10}{2{n}^{2}+100}=\lim_{n\to\infty}\frac{{n}^{2}(4-\frac{6}{n}+\frac{10}{{n}^{2}})}{{n}^{2}(2+\frac{100}{{n}^{2}})}=2$$

h)

$$\lim_{n\to\infty}\frac{{n}^{4}+3{n}^{2}}{{n}^{2}+10n}=\lim_{n\to\infty}\frac{{n}^{4}\left( 1+\frac{3}{{n}^{2}} \right)}{{n}^{2}\left( 1+\frac{10}{n} \right)}=\lim_{n\to\infty}\frac{{n}^{2}\left( 1+\frac{3}{{n}^{2}} \right)}{\left( 1+\frac{10}{n} \right)}=\frac{\infty}{1}=\infty$$

i)

$$\lim_{n\to\infty}\frac{1+\sqrt{n}}{3+\sqrt{n}}=\lim_{n\to\infty}\frac{\sqrt{n}\left( \frac{1}{\sqrt{n}}+1 \right)}{\sqrt{n}\left( \frac{3}{\sqrt{n}}+1 \right)}=1$$

j)

$$\lim_{n\to\infty}\frac{3n-\sqrt{n}}{2\sqrt{n}+5n}=\lim_{n\to\infty}\frac{n(3-\frac{1}{\sqrt{n}})}{n(5+\frac{2}{\sqrt{n}})}=\frac{3}{5}$$

k)

$$
\begin{aligned}
\lim_{n\to\infty}\frac{2{n}^{2}(n-3+4{n}^{2})}{5{(n-1)}^{3}(3n+4)}&=\lim_{n\to\infty}\frac{2{n}^{2}(n-3+4{n}^{2})}{5\left( ({n}^{3}-3{n}^{2}+3n-1)(3n+4) \right)} \\
&=\lim_{n\to\infty}\frac{2{n}^{2}(n-3+4{n}^{2})}{5\left( 3{n}^{4}+4{n}^{3}-9{n}^{3}-12{n}^{2}+9{n}^{2}+12n-3n-4 \right)}=\lim_{n\to\infty}\frac{2{n}^{2}(n-3+4{n}^{2})}{5\left( 3{n}^{4}-5{n}^{3}-3{n}^{2}+9n-4 \right)} \\
&=\lim_{n\to\infty}\frac{2{n}^{4}\left( \frac{1}{n}-\frac{3}{{n}^{2}}+4 \right)}{5{n}^{4}\left( 3-\frac{5}{n}-\frac{3}{{n}^{2}}+\frac{9}{{n}^{3}}-\frac{4}{{n}^{4}} \right)}=\frac{2}{5}\cdot\frac{4}{3}=\frac{8}{15}
\end{aligned}
$$

l)

$$\lim_{n\to\infty}\frac{\sqrt{32n}+7}{13-\sqrt{2n}}=\lim_{n\to\infty}\frac{{n}^{1/2}(\sqrt{32}+\frac{7}{{n}^{1/2}})}{{n}^{1/2}(\frac{13}{{n}^{1/2}}-\sqrt{2})}=\frac{\sqrt{32}}{-\sqrt{2}}=-\sqrt{\frac{32}{2}}=-\sqrt{16}=-4$$
```
````

```{admonition} Übung 9.2
:class: miniexercise
Berechnen oder begründen Sie das Ergebnis. Es ist $x\in\mathbb{R}$.

a) $\displaystyle \lim_{x\to\infty}\left(x-\frac{{x}^{2}}{x-3}\right)$

b) $\displaystyle \lim_{x\to\pm\infty}-\frac{x}{\left| x \right|}$ (Einmal Limes gegen $+\infty$ und einmal gegen $-\infty$)

c) $\displaystyle \lim_{x\to\infty}\frac{x+1}{{x}^{2}-1}$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $-3$

b) $\displaystyle \lim_{x\to+\infty}-\frac{x}{\left|x\right|}=-1$ und $\displaystyle \lim_{x\to-\infty}-\frac{x}{\left|x\right|}=1$

c) $0$

```{dropdown} Lösungsweg
a)

$$\lim_{x\to\infty}\left(x-\frac{{x}^{2}}{x-3}\right)=\lim_{x\to\infty}\frac{x(x-3)-{x}^{2}}{x-3}=\lim_{x\to\infty}\frac{-3x}{x-3}=-3$$

b)

$$x>0:\,\lim_{x\to+\infty}-\frac{x}{\left|x\right|}=\lim_{x\to+\infty}-\frac{x}{x}=-1$$

$$x<0:\,\lim_{x\to-\infty}-\frac{x}{\left|x\right|}=\lim_{x\to-\infty}-\frac{x}{-x}=1$$

c)

$$\lim_{x\to\infty}\frac{x+1}{{x}^{2}-1}=\lim_{x\to\infty}\frac{x+1}{(x-1)(x+1)}=\lim_{x\to\infty}\frac{1}{x-1}=0$$
```
````

```{admonition} Übung 9.3
:class: miniexercise
Berechnen Sie. Es ist $x\in\mathbb{R}$.

a) $\displaystyle \lim_{x\to{x}_{0}}\frac{{x}^{2}-1}{x+1}$ bei ${x}_{0}=-1$.

b) $\displaystyle \lim_{x\to{x}_{0}}\frac{{x}^{2}-x-6}{x+2}$ bei ${x}_{0}=-2$ und ${x}_{0}=3$.

c) $\displaystyle \lim_{x\to{x}_{0}}x\left|x-1\right|$ bei ${x}_{0}=1$.
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $-2$

b) $-5$ bei $x_0=-2$ und $0$ bei $x_0=3$

c) $0$

```{dropdown} Lösungsweg
a)

$$\lim_{x\to-1}\frac{{x}^{2}-1}{x+1}=\lim_{x\to-1}\frac{(x-1)(x+1)}{x+1}=\lim_{x\to-1}(x-1)=-2$$

b)

$$\lim_{x\to-2}\frac{{x}^{2}-x-6}{x+2}=\lim_{x\to-2}\frac{(x+2)(x-3)}{x+2}=\lim_{x\to-2}(x-3)=-5$$

$$\lim_{x\to3}\frac{{x}^{2}-x-6}{x+2}=\lim_{x\to3}\frac{(x+2)(x-3)}{x+2}=\lim_{x\to3}(x-3)=0$$

c)

$\lim_{x\to1}x\left|x-1\right|$: Aufteilen in einseitige Grenzwerte!

$$\lim_{x\downarrow 1}x\left|x-1\right|=\lim_{x\downarrow 1}x(x-1)=0$$

$$\lim_{x\uparrow 1}x\left|x-1\right|=\lim_{x\uparrow 1}x(-(x-1))=0$$

Also

$$0=\lim_{x\downarrow 1}x\left|x-1\right|=\lim_{x\uparrow 1}x\left|x-1\right|=\lim_{x\to1}x\left|x-1\right|$$
```
````
