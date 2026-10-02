# Übungen zum Selbststudium

```{admonition} Übung 8.1
:class: miniexercise
Gegeben seien die komplexen Zahlen $z_1=2-2\mathrm{i}$ und $z_2=1+\sqrt{3}\,\mathrm{i}$. Berechnen Sie

a) $z_1+z_2$

b) $z_1-z_2$

c) $z_1\cdot z_2$

d) $z_1+\overline{z}_1$

e) $|z_1|$, $|z_2|$

f) $|z_1\cdot z_2|$

g) $\dfrac{z_1}{z_2}$

h) $\overline{z}_1$, $\overline{z}_2$

i) $z_1\cdot\overline{z}_1$

j) $\left|\dfrac{z_1}{z_2}\right|$

k) $\arg(z_1)$, $\arg(z_2)$

Hierin bezeichnet $\arg(z)$ das Argument $\varphi$ von $z$.
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $3+(\sqrt{3}-2)\mathrm{i}$

b) $1-(2+\sqrt{3})\mathrm{i}$

c) $2+2\sqrt{3}+(2\sqrt{3}-2)\mathrm{i}$

d) $4$

e) $|z_1|=2\sqrt{2}$, $|z_2|=2$

f) $|z_1\cdot z_2|=4\sqrt{2}$

g) $\displaystyle\frac{z_1}{z_2}=\frac{1}{4}\left[2-2\sqrt{3}-\mathrm{i}(2+2\sqrt{3})\right]\approx-0{,}366-1{,}366\,\mathrm{i}$

h) $\overline{z}_1=2+2\mathrm{i}$, $\overline{z}_2=1-\sqrt{3}\,\mathrm{i}$

i) $8$

j) $\sqrt{2}$

k) $\arg(z_1)=\dfrac{7}{4}\pi$, $\arg(z_2)=\dfrac{\pi}{3}$

```{dropdown} Lösungsweg
a)

$${z}_{1}+{z}_{2}=2-2\mathrm{i}+1+\sqrt{3}\mathrm{i}=3+(\sqrt{3}-2)\mathrm{i}$$

b)

$${z}_{1}-{z}_{2}=2-2\mathrm{i}-(1+\sqrt{3}\mathrm{i})=1-(2+\sqrt{3})\mathrm{i}$$

c)

$${z}_{1}\cdot{z}_{2}=(2-2\mathrm{i})\cdot(1+\sqrt{3}\mathrm{i})=2-2\sqrt{3}{\mathrm{i}}^{2}+(2\sqrt{3}-2)\mathrm{i}=2+2\sqrt{3}+(2\sqrt{3}-2)\mathrm{i}$$

d)

$${z}_{1}+\overline{z}_{1}=2-2\mathrm{i}+2+2\mathrm{i}=4$$

e)

$$\left|{z}_{1}\right|=\sqrt{{2}^{2}+{(2)}^{2}}=\sqrt{8}=\sqrt{4\cdot2}=2\sqrt{2}\,,\,\left|{z}_{2}\right|=\sqrt{{1}^{2}+\sqrt{{3}^{2}}}=\sqrt{4}=2$$

f)

$$\left|{z}_{1}\cdot{z}_{2}\right|=\left|{z}_{1}\right|\cdot\left|{z}_{2}\right|=2\sqrt{2}\cdot2=4\sqrt{2}$$

g)

$$
\begin{aligned}
\frac{{z}_{1}}{{z}_{2}}&=\frac{2-2\mathrm{i}}{1+\mathrm{i}\sqrt{3}}=\frac{2-2\mathrm{i}}{1+\mathrm{i}\sqrt{3}}\cdot\frac{1-\mathrm{i}\sqrt{3}}{1-\mathrm{i}\sqrt{3}}=\frac{2-2\sqrt{3}\mathrm{i}-2\mathrm{i}+{\mathrm{i}}^{2}2\sqrt{3}}{1-{\mathrm{i}}^{2}3}=\frac{2-\mathrm{i}(2\sqrt{3}+2)-2\sqrt{3}}{1+3} \\
&=\frac{1}{4}[2-2\sqrt{3}-\mathrm{i}(2+2\sqrt{3})]\approx-0.366-1\mathrm{i}.366
\end{aligned}
$$

h)

$$\overline{z}_{1}=2+2\mathrm{i}\,,\,\overline{z}_{2}=1-\mathrm{i}\sqrt{3}$$

i)

$${z}_{1}\cdot\overline{z}_{1}=(2-2\mathrm{i})\cdot(2+2\mathrm{i})=4-{\mathrm{i}}^{2}4=4+4=8$$

j)

Mit dem Ergebnis von g):

$$
\begin{aligned}
\left|\frac{{z}_{1}}{{z}_{2}}\right|&=\sqrt{{(\frac{2}{4}-\frac{2}{4}\sqrt{3})}^{2}+{(\frac{2}{4}\sqrt{3}+\frac{2}{4})}^{2}}=\sqrt{\frac{4}{16}-\frac{8}{16}\sqrt{3}+\frac{4\cdot3}{16}+\frac{4\cdot3}{16}+\frac{8}{16}\sqrt{3}+\frac{4}{16}}= \\
&=\sqrt{\frac{8}{16}+\frac{24}{16}}=\sqrt{\frac{32}{16}}=\sqrt{2}
\end{aligned}
$$

k)

$$
\begin{aligned}
\arg(z_1)&=\varphi_1=\arctan\!\left(\frac{-2}{2}\right)+2\pi=\frac{7}{4}\pi \\
\arg(z_2)&=\varphi_2=\arctan\!\left(\frac{\sqrt{3}}{1}\right)=\frac{\pi}{3}
\end{aligned}
$$
```
````

```{admonition} Übung 8.2
:class: miniexercise
Führen Sie die Division aus. (Das Ergebnis soll Normalform haben.)

a) $\displaystyle z=\frac{1+\frac{1}{\mathrm{i}}}{1-\frac{1}{\mathrm{i}}}$

b) $\displaystyle z=\frac{\frac{1}{2}(5+\mathrm{i})}{2+\frac{1}{1-\mathrm{i}}}$

c) $\displaystyle z=\frac{(1+2\mathrm{i})(2-\mathrm{i})+1}{{(2-\mathrm{i})}^{2}-2+\mathrm{i}}$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $-\mathrm{i}$

b) $1$

c) $\dfrac{1}{5}(-2+9\mathrm{i})$

```{dropdown} Lösungsweg
a)

$$z=\frac{1+\frac{1}{\mathrm{i}}}{1-\frac{1}{\mathrm{i}}}=\frac{\frac{\mathrm{i}}{\mathrm{i}}+\frac{1}{\mathrm{i}}}{\frac{\mathrm{i}}{\mathrm{i}}-\frac{1}{\mathrm{i}}}=\frac{\frac{1+\mathrm{i}}{\mathrm{i}}}{\frac{\mathrm{i}-1}{\mathrm{i}}}=\frac{1+\mathrm{i}}{\mathrm{i}-1}=\frac{1+\mathrm{i}}{\mathrm{i}-1}\cdot\frac{\mathrm{i}+1}{\mathrm{i}+1}=\frac{1+2\mathrm{i}+{\mathrm{i}}^{2}}{{\mathrm{i}}^{2}-1}=\frac{2\mathrm{i}}{-2}=-\mathrm{i}$$

b)

$$
\begin{aligned}
z&=\frac{\frac{1}{2}(5+\mathrm{i})}{2+\frac{1}{1-\mathrm{i}}}=\frac{\frac{1}{2}(5+\mathrm{i})}{\frac{2(1-\mathrm{i})}{1-\mathrm{i}}+\frac{1}{1-\mathrm{i}}}=\frac{\frac{1}{2}(5+\mathrm{i})}{\frac{2(1-\mathrm{i})+1}{1-\mathrm{i}}}=\frac{\frac{1}{2}(5+\mathrm{i})(1-\mathrm{i})}{2(1-\mathrm{i})+1}=\frac{\frac{1}{2}(5-5\mathrm{i}+\mathrm{i}-{\mathrm{i}}^{2})}{2(1-\mathrm{i})+1}=\frac{\frac{1}{2}(5-4\mathrm{i}+1)}{2(1-\mathrm{i})+1} \\
&=\frac{\frac{1}{2}(6-4\mathrm{i})}{2(1-\mathrm{i})+1}=\frac{3-2\mathrm{i}}{3-2\mathrm{i}}=1
\end{aligned}
$$

c)

$$
\begin{aligned}
z&=\frac{(1+2\mathrm{i})(2-\mathrm{i})+1}{{(2-\mathrm{i})}^{2}-2+\mathrm{i}}=\frac{2-\mathrm{i}+4\mathrm{i}-2{\mathrm{i}}^{2}+1}{4-4\mathrm{i}+{\mathrm{i}}^{2}-2+\mathrm{i}}=\frac{2+3\mathrm{i}+2+1}{2-3\mathrm{i}-1}=\frac{5+3\mathrm{i}}{1-3\mathrm{i}}=\frac{5+3\mathrm{i}}{1-3\mathrm{i}}\frac{1+3\mathrm{i}}{1+3\mathrm{i}} \\
&=\frac{5+15\mathrm{i}+3\mathrm{i}+9{\mathrm{i}}^{2}}{1-9{\mathrm{i}}^{2}}=\frac{-4+18\mathrm{i}}{10}=\frac{1}{5}(-2+9\mathrm{i})
\end{aligned}
$$
```
````

```{admonition} Übung 8.3
:class: miniexercise
Berechnen Sie die Beträge dieser komplexen Zahlen.

a) $\displaystyle z=\frac{2+3\mathrm{i}}{1+\mathrm{i}}$

b) $\displaystyle z=\frac{\mathrm{i}}{(1+2\mathrm{i})3{\mathrm{e}}^{-\mathrm{i}}}$

c) $\displaystyle z=\frac{1-\mathrm{i}}{2{\mathrm{e}}^{\mathrm{i}\pi/3}}$

d) $\displaystyle z=\frac{1+3\mathrm{i}}{(1+\mathrm{i})(1-\mathrm{i})}$

Tipp: Es ist $\displaystyle\left|\frac{z_1}{z_2}\right|=\frac{|z_1|}{|z_2|}$.
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $\sqrt{\dfrac{13}{2}}$

b) $\dfrac{1}{3\sqrt{5}}$

c) $\dfrac{\sqrt{2}}{2}$

d) $\dfrac{\sqrt{10}}{2}$

```{dropdown} Lösungsweg
a)

$$\left|z\right|=\left|\frac{2+3\mathrm{i}}{1+\mathrm{i}}\right|=\left|\frac{2+3\mathrm{i}}{1+\mathrm{i}}\frac{1-\mathrm{i}}{1-\mathrm{i}}\right|=\left|\frac{2-2\mathrm{i}+3\mathrm{i}-3{\mathrm{i}}^{2}}{1-{\mathrm{i}}^{2}}\right|=\left|\frac{5+\mathrm{i}}{2}\right|=\sqrt{{\left( \frac{5}{2} \right)}^{2}+{\left( \frac{1}{2} \right)}^{2}}=\sqrt{\frac{26}{4}}=\sqrt{\frac{13}{2}}$$

alternativ:

$$\left|z\right|=\left|\frac{2+3\mathrm{i}}{1+\mathrm{i}}\right|=\frac{\left|2+3\mathrm{i}\right|}{\left|1+i\right|}=\frac{\sqrt{{2}^{2}+{3}^{2}}}{\sqrt{{1}^{2}+{1}^{2}}}=\sqrt{\frac{13}{2}}$$

b)

$$\left|z\right|=\left|\frac{\mathrm{i}}{(1+2\mathrm{i})3{\mathrm{e}}^{-\mathrm{i}}}\right|=\frac{\left|\mathrm{i}\right|}{\left|1+2\mathrm{i}\right|\left|3{\mathrm{e}}^{-\mathrm{i}}\right|}=\frac{1}{\sqrt{1+{2}^{2}}\cdot3}=\frac{1}{3\sqrt{5}}$$

c)

$$\left|z\right|=\left|\frac{1-\mathrm{i}}{2{\mathrm{e}}^{\mathrm{i}\pi/3}}\right|=\frac{\left|1-\mathrm{i}\right|}{\left|2\right|\cdot\left|{\mathrm{e}}^{\mathrm{i}\pi/3}\right|}=\frac{\sqrt{{1}^{2}+{1}^{2}}}{2\cdot1}=\frac{\sqrt{2}}{2}$$

d)

$$\left|z\right|=\left|\frac{1+3\mathrm{i}}{(1+\mathrm{i})(1-\mathrm{i})}\right|=\frac{\left|1+3\mathrm{i}\right|}{\left|1+\mathrm{i}\right|\cdot\left|1-\mathrm{i}\right|}=\frac{\sqrt{{1}^{2}+{3}^{2}}}{\sqrt{{1}^{2}+{1}^{2}}\sqrt{{1}^{2}+{1}^{2}}}=\frac{\sqrt{10}}{2}$$
```
````

```{admonition} Übung 8.4
:class: miniexercise
Berechnen Sie

a) $\displaystyle {(\sqrt{3}+\mathrm{i})}^{9}$

b) $\displaystyle {\left( \frac{1}{2}-\mathrm{i}\sqrt{\frac{3}{4}} \right)}^{12}$
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $-512\,\mathrm{i}$

b) $1$

```{dropdown} Lösungsweg
a)

$$
\begin{aligned}
z&=\sqrt{3}+\mathrm{i}\Rightarrow\,r=\left|z\right|=\sqrt{{\sqrt{3}}^{2}+{1}^{2}}=2,\,\varphi=\arctan (\frac{1}{\sqrt{3}})=\frac{\pi}{6}\Rightarrow\,z=2{\mathrm{e}}^{\mathrm{i}\frac{\pi}{6}} \\
&\Rightarrow\,{z}^{9}={2}^{9}{\mathrm{e}}^{9\mathrm{i}\frac{\pi}{6}}={2}^{9}{\mathrm{e}}^{3\frac{\pi}{2}\mathrm{i}}=512[\cos (\frac{3\pi}{2})+\mathrm{i}\cdot\sin (\frac{3\pi}{2})]=-512\mathrm{i}
\end{aligned}
$$

b)

$$
\begin{aligned}
z&=\frac{1}{2}-\mathrm{i}\sqrt{\frac{3}{4}}\Rightarrow\,r=\left|z\right|=\sqrt{{\left( \frac{1}{2} \right)}^{2}+{\left(\sqrt{\frac{3}{4}}\right)}^{2}}=1,\quad \\
\varphi&=\arctan \left( \frac{-\sqrt{\frac{3}{4}}}{\frac{1}{2}} \right)+2\pi=-\frac{\pi}{3}+2\pi=\frac{5\pi}{3}\Rightarrow\,z={\mathrm{e}}^{\frac{5\pi}{3}\mathrm{i}} \\
&\Rightarrow\,{z}^{12}={\mathrm{e}}^{5\frac{\pi}{3}12\mathrm{i}}={\mathrm{e}}^{20\pi\mathrm{i}}=\cos (20\pi)+\mathrm{i}\cdot\sin (20\pi)=1
\end{aligned}
$$
```
````

```{admonition} Übung 8.5
:class: miniexercise
Berechnen Sie die Lösungen der Gleichung $z^3=-2\mathrm{i}$.
```

````{admonition} Lösung
:class: miniexercise, toggle

$z_0=\sqrt[3]{2}\,\mathrm{i}$

$z_1=\sqrt[3]{2}\left(-\frac{\sqrt{3}}{2}-\frac{1}{2}\mathrm{i}\right)$

$z_2=\sqrt[3]{2}\left(\frac{\sqrt{3}}{2}-\frac{1}{2}\mathrm{i}\right)$

```{dropdown} Lösungsweg
Gesucht sind die 3. Wurzeln von $w=-2\mathrm{i}$. Umwandeln in Exponentialform:

$$r=\left|w\right|=\sqrt{{0}^{2}+{(-2)}^{2}}=\sqrt{4}=2$$

$$\varphi=\arg(w)=\frac{3\pi}{2}$$

(denn $w$ liegt auf der negativen Imaginärteil-Achse)

Die 3. Wurzeln werden berechnet mit

$${z}_{k}=\sqrt[3]{r}\cdot{\mathrm{e}}^{\mathrm{i}(\varphi+k\cdot2\pi)/3}$$

für $k=0,1,2$.

Für $k=0$:

$${z}_{0}=\sqrt[3]{2}\cdot{\mathrm{e}}^{\mathrm{i}(\frac{3\pi}{2})/3}=\sqrt[3]{2}\cdot{\mathrm{e}}^{\mathrm{i}(\frac{\pi}{2})}=\sqrt[3]{2}\cdot[\cos\frac{\pi}{2}+\mathrm{i}\cdot\sin\frac{\pi}{2}]=\sqrt[3]{2}\cdot[0+\mathrm{i}]=\sqrt[3]{2}\mathrm{i}$$

Für $k=1$:

$${z}_{1}=\sqrt[3]{2}\cdot{\mathrm{e}}^{\mathrm{i}(\frac{3\pi}{2}+2\pi)/3}=\sqrt[3]{2}\cdot{\mathrm{e}}^{\mathrm{i}(\frac{7\pi}{6})}=\sqrt[3]{2}\cdot[\cos (\frac{7\pi}{6})+\mathrm{i}\sin (\frac{7\pi}{6})]=\sqrt[3]{2}\left( -\frac{\sqrt{3}}{2}-\frac{1}{2}\mathrm{i} \right)$$

Für $k=2$:

$${z}_{2}=\sqrt[3]{2}\cdot{\mathrm{e}}^{\mathrm{i}(\frac{3\pi}{2}+2\cdot2\pi)/3}=\sqrt[3]{2}\cdot[\cos (\frac{11\pi}{6})+\mathrm{i}\sin (\frac{11\pi}{6})]=\sqrt[3]{2}\left( \frac{\sqrt{3}}{2}-\frac{1}{2}\mathrm{i} \right)$$
```
````
