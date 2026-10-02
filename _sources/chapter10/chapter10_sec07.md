# Übungen zum Selbststudium

```{admonition} Übung 10.1
:class: miniexercise
Hinweis: Wenn zu der Anwendung einer bestimmten Regel aufgefordert wird, schließt das nicht aus, dass Sie (zusätzlich) auch andere Regeln benutzen müssen, können und dürfen.

Berechnen Sie die Ableitung $f'(x)$ mit der Produktregel.

a) $\displaystyle f(x)={x}^{2}(1-3{x}^{2})$

b) $\displaystyle f(x)=({x}^{5}-{x}^{2})({x}^{2}-{x}^{4})$

c) $\displaystyle f(x)=({x}^{2}-1)\sqrt{x}$

d) $\displaystyle f(x)=({x}^{4}-3{x}^{3})\sqrt{x}$

e) $\displaystyle f(x)=\frac{1}{{x}^{2}}\left( =\frac{1}{x}\frac{1}{x} \right)$

f) $\displaystyle f(x)=\frac{1}{{x}^{3}}$

g) $\displaystyle f(x)=\sin x\cdot\cos x$

h) $\displaystyle f(x)={(\sin x)}^{2}$

i) $\displaystyle f(x)={(\cos x)}^{2}$

j) $\displaystyle f(x)={(\sin x)}^{3}$

k) $\displaystyle f(x)={(\cos x)}^{3}$

l) $\displaystyle f(x)=({x}^{5}-1)\sin x$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $\displaystyle f'(x)=2x-12{x}^{3}$

b) $\displaystyle f'(x)=-9{x}^{8}+7{x}^{6}+6{x}^{5}-4{x}^{3}$

c) $\displaystyle f'(x)=\frac{5}{2}{x}^{\frac{3}{2}}-\frac{1}{2\sqrt{x}}$

d) $\displaystyle f'(x)=\frac{9}{2}{x}^{\frac{7}{2}}-\frac{21}{2}{x}^{\frac{5}{2}}$

e) $\displaystyle f'(x)=-2\frac{1}{{x}^{3}}$

f) $\displaystyle f'(x)=-3\frac{1}{{x}^{4}}$

g) $\displaystyle f'(x)=\cos (2x)$

h) $\displaystyle f'(x)=\sin (2x)$

i) $\displaystyle f'(x)=-\sin (2x)$

j) $\displaystyle f'(x)=3{(\sin x)}^{2}\cos x$

k) $\displaystyle f'(x)=-3\sin x\cdot{(\cos x)}^{2}$

l) $\displaystyle f'(x)=5{x}^{4}\sin x+({x}^{5}-1)\cos x$

```{dropdown} Lösungsweg
a)

$$f'(x)=2x(1-3{x}^{2})+{x}^{2}(-6x)=2x-12{x}^{3}$$

b)

$$
\begin{aligned}
f'(x)&=(5{x}^{4}-2x)({x}^{2}-{x}^{4})+({x}^{5}-{x}^{2})(2x-4{x}^{3}) \\
&=-9{x}^{8}+7{x}^{6}+6{x}^{5}-4{x}^{3}
\end{aligned}
$$

c)

$$f'(x)=2x\sqrt{x}+({x}^{2}-1)\frac{1}{2\sqrt{x}}=\frac{5}{2}{x}^{\frac{3}{2}}-\frac{1}{2\sqrt{x}}$$

d)

$$f'(x)=(4{x}^{3}-9{x}^{2})\sqrt{x}+({x}^{4}-3{x}^{3})\frac{1}{2\sqrt{x}}=\frac{9}{2}{x}^{\frac{7}{2}}-\frac{21}{2}{x}^{\frac{5}{2}}$$

e)

$$f'(x)=-{x}^{-2}{x}^{-1}+{x}^{-1}(-{x}^{-2})=-2\frac{1}{{x}^{3}}$$

f)

$$f'(x)=-2{x}^{-3}{x}^{-1}+{x}^{-2}(-{x}^{-2})=-3\frac{1}{{x}^{4}}$$

g)

$$f'(x)=\cos x\cdot\cos x+\sin x(-\sin x)=\cos (2x)$$

h)

$$f'(x)=\sin x\cdot\cos x+\cos x\cdot\sin x=2\sin x\cos x=\sin (2x)$$

i)

$$f'(x)=\cos x\cdot(-\sin x)+(-\sin x)\cdot\cos x=-2\sin x\cos x=-\sin (2x)$$

j)

$$f'(x)=\sin (2x)\sin x+{(\sin x)}^{2}\cos x=3{(\sin x)}^{2}\cos x$$

k)

$$f'(x)=-\sin (2x)\cos x+{(\cos x)}^{2}(-\sin x)=-3\sin x\cdot{(\cos x)}^{2}$$

l)

$$f'(x)=5{x}^{4}\sin x+({x}^{5}-1)\cos x$$
```
````

```{admonition} Übung 10.2
:class: miniexercise
Geben Sie die Ableitung von $\displaystyle f(x)=u(x)\cdot v(x)\cdot w(x)$ an.

(Produktregel für drei Faktoren.)
```

````{admonition} Lösung
:class: miniexercise, toggle

$$f'=u'\cdot v\cdot w+u\cdot v'\cdot w+u\cdot v\cdot w'$$

```{dropdown} Lösungsweg
Definiere die Produktfunktion $\omega=v\cdot w$

$$\Rightarrow\,\omega'=v'\cdot w+v\cdot w'$$

Nun:

$$
\begin{aligned}
f&=u\cdot\omega \\
f'&=u'\cdot\omega+u\cdot\omega' \\
f'&=u'\cdot v\cdot w+u\cdot v'\cdot w+u\cdot v\cdot w'
\end{aligned}
$$
```
````

```{admonition} Übung 10.3
:class: miniexercise
Berechnen Sie die Ableitung $f'(x)$ mit der Quotientenregel.

a) $\displaystyle f(x)=\frac{x-1}{x+1}$

b) $\displaystyle f(x)=\frac{{x}^{2}}{x+1}$

c) $\displaystyle f(x)=\frac{3}{{x}^{2}+1}$

d) $\displaystyle f(x)=\frac{{x}^{2}-4}{1-x}$

e) $\displaystyle f(x)=\frac{1}{1+2{x}^{2}}$

f) $\displaystyle f(x)=\frac{{x}^{3}}{1+{x}^{2}}$

g) $\displaystyle f(x)=\frac{{x}^{2}-2x}{{x}^{2}-4}$

h) $\displaystyle f(x)=\frac{{x}^{2}-9}{{x}^{3}-64}$

i) $\displaystyle f(x)=\frac{{x}^{2}-x-6}{{x}^{2}+x-6}$

j) $\displaystyle f(x)=\frac{\sqrt{x}}{1-x}$

k) $\displaystyle f(x)=\frac{2\sqrt{x}}{1-\sqrt{x}}$

l) $\displaystyle f(x)=\frac{{x}^{2}}{\cos x}$

m) $\displaystyle f(x)=\frac{\cos x+1}{\cos x-1}$

n) $\displaystyle f(x)=\frac{\sin x-\cos x}{\sin x+\cos x}$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $\displaystyle f'(x)=\frac{2}{{(x+1)}^{2}}$

b) $\displaystyle f'(x)=\frac{{x}^{2}+2x}{{(x+1)}^{2}}$

c) $\displaystyle f'(x)=\frac{-6x}{{({x}^{2}+1)}^{2}}$

d) $\displaystyle f'(x)=\frac{2x-{x}^{2}-4}{{(1-x)}^{2}}$

e) $\displaystyle f'(x)=-\frac{4x}{{(1+2{x}^{2})}^{2}}$

f) $\displaystyle f'(x)=\frac{3{x}^{2}+{x}^{4}}{{(1+{x}^{2})}^{2}}$

g) $\displaystyle f'(x)=\frac{2}{{(x+2)}^{2}}$

h) $\displaystyle f'(x)=\frac{-{x}^{4}-128x+27{x}^{2}}{{({x}^{3}-64)}^{2}}$

i) $\displaystyle f'(x)=\frac{2{x}^{2}+12}{{({x}^{2}+x-6)}^{2}}$

j) $\displaystyle f'(x)=\frac{1}{2}\frac{{x}^{-\frac{1}{2}}+{x}^{\frac{1}{2}}}{{(1-x)}^{2}}$

k) $\displaystyle f'(x)=\frac{1}{\sqrt{x}{(1-\sqrt{x})}^{2}}$

l) $\displaystyle f'(x)=\frac{2x\cos x-{x}^{2}(-\sin x)}{{(\cos x)}^{2}}$

m) $\displaystyle f'(x)=\frac{2\sin x}{{(\cos x-1)}^{2}}$

n) $\displaystyle f'(x)=\frac{2}{1+2\sin x\cos x}$

```{dropdown} Lösungsweg
a)

$$f'(x)=\frac{1\cdot(x+1)-(x-1)\cdot1}{{(x+1)}^{2}}=\frac{2}{{(x+1)}^{2}}$$

b)

$$f'(x)=\frac{2x(x+1)-{x}^{2}}{{(x+1)}^{2}}=\frac{{x}^{2}+2x}{{(x+1)}^{2}}$$

c)

$$f'(x)=\frac{0\cdot({x}^{2}+1)-3\cdot2x}{{({x}^{2}+1)}^{2}}=\frac{-6x}{{({x}^{2}+1)}^{2}}$$

d)

$$f'(x)=\frac{2x(1-x)-({x}^{2}-4)\cdot(-1)}{{(1-x)}^{2}}=\frac{2x-{x}^{2}-4}{{(1-x)}^{2}}$$

e)

$$f'(x)=-\frac{4x}{{(1+2{x}^{2})}^{2}}$$

f)

$$f'(x)=\frac{3{x}^{2}(1+{x}^{2})-{x}^{3}\cdot2x}{{(1+{x}^{2})}^{2}}=\frac{3{x}^{2}+{x}^{4}}{{(1+{x}^{2})}^{2}}$$

g)

$$
\begin{aligned}
f'(x)&=\frac{(2x-2)({x}^{2}-4)-({x}^{2}-2x)2x}{{({x}^{2}-4)}^{2}} \\
&=\frac{2{x}^{2}-8x+8}{{({x}^{2}-4)}^{2}}=\frac{2({x}^{2}-4x+4)}{{(x+2)}^{2}{(x-2)}^{2}} \\
&=\frac{2}{{(x+2)}^{2}}
\end{aligned}
$$

Alternativ:

$$
\begin{aligned}
f(x)&=\frac{{x}^{2}-2x}{{x}^{2}-4}=\frac{x(x-2)}{(x+2)(x-2)}=\frac{x}{(x+2)} \\
f'(x)&=\frac{1\cdot(x+2)-x\cdot1}{{(x+2)}^{2}}=\frac{2}{{(x+2)}^{2}}
\end{aligned}
$$

h)

$$f'(x)=\frac{2x({x}^{3}-64)-({x}^{2}-9)3{x}^{2}}{{({x}^{3}-64)}^{2}}=\frac{-{x}^{4}-128x+27{x}^{2}}{{({x}^{3}-64)}^{2}}$$

i)

$$f'(x)=\frac{(2x-1)({x}^{2}+x-6)-({x}^{2}-x-6)(2x+1)}{{({x}^{2}+x-6)}^{2}}=\frac{2{x}^{2}+12}{{({x}^{2}+x-6)}^{2}}$$

j)

$$f'(x)=\frac{\frac{1}{2\sqrt{x}}(1-x)-\sqrt{x}\cdot(-1)}{{(1-x)}^{2}}=\frac{1}{2}\frac{{x}^{-\frac{1}{2}}+{x}^{\frac{1}{2}}}{{(1-x)}^{2}}$$

k)

$$f'(x)=\frac{\frac{1}{\sqrt{x}}(1-\sqrt{x})-2\sqrt{x}\left( -\frac{1}{2\sqrt{x}} \right)}{{(1-\sqrt{x})}^{2}}=\frac{1}{\sqrt{x}{(1-\sqrt{x})}^{2}}$$

l)

$$f'(x)=\frac{2x\cos x-{x}^{2}(-\sin x)}{{(\cos x)}^{2}}$$

m)

$$f'(x)=\frac{(-\sin x)(\cos x-1)-(\cos x+1)(-\sin x)}{{(\cos x-1)}^{2}}=\frac{2\sin x}{{(\cos x-1)}^{2}}$$

n)

$$
\begin{aligned}
f'(x)&=\frac{(\cos x+\sin x)(\sin x+\cos x)-(\sin x-\cos x)(\cos x-\sin x)}{{(\sin x+\cos x)}^{2}} \\
&=\frac{2}{1+2\sin x\cos x}
\end{aligned}
$$
```
````

```{admonition} Übung 10.4
:class: miniexercise
Berechnen Sie die Ableitung $f'(x)$ von $f$ mit der Kettenregel.

a) $\displaystyle f(x)={({x}^{2}-4x)}^{5}$

b) $\displaystyle f(x)={({x}^{3}-5{x}^{6})}^{8}$

c) $\displaystyle f(x)=\frac{1}{{({x}^{2}-2)}^{3}}$

d) $\displaystyle f(x)=\sqrt{1-{x}^{2}}$

e) $\displaystyle f(x)=\sqrt{\frac{1}{x}}$

f) $\displaystyle f(x)=\frac{1}{\sqrt{x-{x}^{3}}}$

g) $\displaystyle f(x)={(\sin (x))}^{6}$

h) $\displaystyle f(x)=\sin ({x}^{2})$

i) $\displaystyle f(x)=\frac{1}{{(\cos x)}^{2}}$

j) $\displaystyle f(x)=\sqrt{\sin (3x)}$

k) $\displaystyle f(x)=\tan (1-3x)$

l) $\displaystyle f(x)=\frac{1}{\sqrt{\cos ({x}^{2})}}$

m) $\displaystyle f(x)={\mathrm{e}}^{-{x}^{2}}$

n) $\displaystyle f(t)=\cos (A\pi t)$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $\displaystyle f'(x)=5{({x}^{2}-4x)}^{4}(2x-4)$

b) $\displaystyle f'(x)=8{({x}^{3}-5{x}^{6})}^{7}(3{x}^{2}-30{x}^{5})$

c) $\displaystyle f'(x)=-3\frac{1}{{({x}^{2}-2)}^{4}}2x$

d) $\displaystyle f'(x)=\frac{1}{2\sqrt{1-{x}^{2}}}(-2x)$

e) $\displaystyle f'(x)=\frac{1}{2\sqrt{\frac{1}{x}}}(-\frac{1}{{x}^{2}})$

f) $\displaystyle f'(x)=-\frac{1}{2}\frac{1}{{\sqrt{x-{x}^{3}}}^{3}}(1-3{x}^{2})$

g) $\displaystyle f'(x)=6{(\sin (x))}^{5}\cos x$

h) $\displaystyle f'(x)=\cos ({x}^{2})2x$

i) $\displaystyle f'(x)=-2\frac{1}{{(\cos x)}^{3}}(-\sin x)$

j) $\displaystyle f'(x)=\frac{1}{2\sqrt{\sin (3x)}}\cdot\cos (3x)\cdot3$

k) $\displaystyle f'(x)=\frac{1}{{(\cos (1-3x))}^{2}}\cdot(-3)$

l) $\displaystyle f'(x)=-\frac{1}{2{\sqrt{\cos ({x}^{2})}}^{3}}(-\sin ({x}^{2}))2x$

m) $\displaystyle f'(x)={e}^{-{x}^{2}}(-2x)$

n) $\displaystyle f'(t)=(-\sin (A\pi t))A\pi$

```{dropdown} Lösungsweg
a)

$$f'(x)=5{({x}^{2}-4x)}^{4}(2x-4)$$

b)

$$f'(x)=8{({x}^{3}-5{x}^{6})}^{7}(3{x}^{2}-30{x}^{5})$$

c)

$$f'(x)=-3\frac{1}{{({x}^{2}-2)}^{4}}2x$$

d)

$$f'(x)=\frac{1}{2\sqrt{1-{x}^{2}}}(-2x)$$

e)

$$f'(x)=\frac{1}{2\sqrt{\frac{1}{x}}}(-\frac{1}{{x}^{2}})$$

f)

$$f'(x)=-\frac{1}{2}\frac{1}{{\sqrt{x-{x}^{3}}}^{3}}(1-3{x}^{2})$$

g)

$$f'(x)=6{(\sin (x))}^{5}\cos x$$

h)

$$f'(x)=\cos ({x}^{2})2x$$

i)

$$f'(x)=-2\frac{1}{{(\cos x)}^{3}}(-\sin x)$$

j)

$$f'(x)=\frac{1}{2\sqrt{\sin (3x)}}\cdot\cos (3x)\cdot3$$

k)

$$f'(x)=\frac{1}{{(\cos (1-3x))}^{2}}\cdot(-3)$$

l)

$$f'(x)=-\frac{1}{2{\sqrt{\cos ({x}^{2})}}^{3}}(-\sin ({x}^{2}))2x$$

m)

$$f'(x)={e}^{-{x}^{2}}(-2x)$$

n)

$$f'(t)=(-\sin (A\pi t))A\pi$$
```
````

```{admonition} Übung 10.5
:class: miniexercise
Berechnen Sie die Ableitung $f'(x)$.

a) $\displaystyle f(x)=\frac{1}{{x}^{2}}$

b) $\displaystyle f(x)=\frac{3}{{x}^{5}}$

c) $\displaystyle f(x)=2{x}^{2}+\frac{10}{{x}^{4}}$

d) $\displaystyle f(x)=\frac{\sin (x)}{{x}^{2}}$

e) $\displaystyle f(x)=\frac{\cot(x)}{3{x}^{3}}$

f) $\displaystyle f(x)=\frac{4}{5{x}^{5}}+2\cos (x)$

Hinweis: $\cot(x)=\dfrac{1}{\tan(x)}$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $\displaystyle f'(x)=\frac{-2}{{x}^{3}}$

b) $\displaystyle f'(x)=\frac{-15}{{x}^{6}}$

c) $\displaystyle f'(x)=4x-\frac{40}{{x}^{5}}$

d) $\displaystyle f'(x)=\frac{x\cdot\cos x-2\sin x}{{x}^{3}}$

e)

$$
\begin{aligned}
(\cot x)'&=-\frac{1}{{\sin }^{2}x} \\
f'(x)&=-\frac{1}{3}\frac{1}{{x}^{4}}(\frac{x}{{\sin }^{2}x}+3\cot x)
\end{aligned}
$$

f) $\displaystyle f'(x)=-\frac{4}{{x}^{6}}-2\sin (x)$

```{dropdown} Lösungsweg
a)

$$f'(x)=\frac{-2}{{x}^{3}}$$

b)

$$f'(x)=\frac{-15}{{x}^{6}}$$

c)

$$f'(x)=4x-\frac{40}{{x}^{5}}$$

d)

$$f'(x)=\frac{x\cdot\cos x-2\sin x}{{x}^{3}}$$

e)

$$(\cot x)'=-\frac{1}{{\sin }^{2}x}\quad\Rightarrow\quad f'(x)=-\frac{1}{3}\frac{1}{{x}^{4}}\left( \frac{x}{{\sin }^{2}x}+3\cot x \right)$$

f)

$$f'(x)=-\frac{4}{{x}^{6}}-2\sin (x)$$
```
````

```{admonition} Übung 10.6
:class: miniexercise
Berechnen Sie die ersten beiden Ableitungen $f'(x)$ und $f''(x)$.

a) $\displaystyle f(x)={x}^{2}-x+2$

b) $\displaystyle f(x)=\frac{{x}^{2}-x+2}{{x}^{2}+x+2}$

c) $\displaystyle f(x)=\sin x\cdot\cos x$

d) $\displaystyle f(x)={(\sin x)}^{2}+{(\cos x)}^{2}$
```

````{admonition} Lösung
:class: miniexercise, toggle

a)

$$
\begin{aligned}
f'(x)&=2x-1 \\
f''(x)&=2
\end{aligned}
$$

b)

$$
\begin{aligned}
f'(x)&=\frac{(2x-1)({x}^{2}+x+2)-({x}^{2}-x+2)(2x+1)}{{({x}^{2}+x+2)}^{2}} \\
&=\frac{2x(2x)-({x}^{2}+x+2)-({x}^{2}-x+2)}{{({x}^{2}+x+2)}^{2}} \\
&=\frac{2{x}^{2}-4}{{({x}^{2}+x+2)}^{2}} \\
f''(x)&=\frac{(4x){({x}^{2}+x+2)}^{2}-(2{x}^{2}-4)2({x}^{2}+x+2)(2x+1)}{{({x}^{2}+x+2)}^{4}} \\
&=\frac{(4x)({x}^{2}+x+2)-(2{x}^{2}-4)2(2x+1)}{{({x}^{2}+x+2)}^{3}} \\
&=\frac{-4{x}^{3}+24x+8}{{({x}^{2}+x+2)}^{3}}
\end{aligned}
$$

c)

$$
\begin{aligned}
f(x)&=\sin x\cdot\cos x=\frac{1}{2}\sin (2x) \\
f'(x)&=\cos (2x) \\
f''(x)&=-2\sin (2x)
\end{aligned}
$$

d)

$$
\begin{aligned}
f(x)&={(\sin x)}^{2}+{(\cos x)}^{2}=1 \\
f'(x)&=0 \\
f''(x)&=0
\end{aligned}
$$

```{dropdown} Lösungsweg
a)

$$
\begin{aligned}
f'(x)&=2x-1 \\
f''(x)&=2
\end{aligned}
$$

b)

$$
\begin{aligned}
f'(x)&=\frac{(2x-1)({x}^{2}+x+2)-({x}^{2}-x+2)(2x+1)}{{({x}^{2}+x+2)}^{2}} \\
&=\frac{2x(2x)-({x}^{2}+x+2)-({x}^{2}-x+2)}{{({x}^{2}+x+2)}^{2}} \\
&=\frac{2{x}^{2}-4}{{({x}^{2}+x+2)}^{2}} \\
f''(x)&=\frac{(4x){({x}^{2}+x+2)}^{2}-(2{x}^{2}-4)2({x}^{2}+x+2)(2x+1)}{{({x}^{2}+x+2)}^{4}} \\
&=\frac{(4x)({x}^{2}+x+2)-(2{x}^{2}-4)2(2x+1)}{{({x}^{2}+x+2)}^{3}} \\
&=\frac{-4{x}^{3}+24x+8}{{({x}^{2}+x+2)}^{3}}
\end{aligned}
$$

c)

$$
\begin{aligned}
f(x)&=\sin x\cdot\cos x=\frac{1}{2}\sin (2x) \\
f'(x)&=\cos (2x) \\
f''(x)&=-2\sin (2x)
\end{aligned}
$$

d)

$$
\begin{aligned}
f(x)&={(\sin x)}^{2}+{(\cos x)}^{2}=1 \\
f'(x)&=0 \\
f''(x)&=0
\end{aligned}
$$
```
````
