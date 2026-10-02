# Übungen zum Selbststudium

```{admonition} Übung 5.1
:class: miniexercise
Bestimmen Sie die Geradengleichung für die Gerade durch die Punkte $A=(1,2,3)$ und $B=(4,5,6)$.
```

````{admonition} Lösung
:class: miniexercise, toggle

$$g:\vec{x}(s)=\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}+s\begin{pmatrix} 3 \\ 3 \\ 3 \end{pmatrix}$$

```{dropdown} Lösungsweg
$$g:\vec{x}(s)=\overrightarrow{OA}+s\overrightarrow{AB}=\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}+s\begin{pmatrix} 4-1 \\ 5-2 \\ 6-3 \end{pmatrix}=\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}+s\begin{pmatrix} 3 \\ 3 \\ 3 \end{pmatrix}$$
```
````

```{admonition} Übung 5.2
:class: miniexercise
Bestimmen Sie die Normalengleichung für die Ebene durch die Punkte $A=(1,2,3)$, $B=(2,4,5)$ und $C=(4,5,6)$.
```

````{admonition} Lösung
:class: miniexercise, toggle

$$E:\ -y+z=1$$

```{dropdown} Lösungsweg
Vorgehen wie in Beispiel (II) der Vorlesung.

Zunächst werden die beiden Richtungsvektoren der Ebene bestimmt

$$\vec{u}=\overrightarrow{AB}=\begin{pmatrix} 2-1 \\ 4-2 \\ 5-3 \end{pmatrix}=\begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}\qquad\vec{v}=\overrightarrow{AC}=\begin{pmatrix} 4-1 \\ 5-2 \\ 6-3 \end{pmatrix}=\begin{pmatrix} 3 \\ 3 \\ 3 \end{pmatrix}$$

Der Normalenvektor ergibt sich aus dem Kreuzprodukt beider Richtungsvektoren:

$$\vec{n}=\vec{u}\times\vec{v}=\begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}\times\begin{pmatrix} 3 \\ 3 \\ 3 \end{pmatrix}=\begin{pmatrix} 0 \\ 3 \\ -3 \end{pmatrix}$$

Die allgemeine Normalengleichung lautet (in Form der Koordinatengleichung):

$$\vec{n}\cdot\vec{x}=d$$

Anschließend kann ein beliebiger Punkt der Ebene für $\vec{x}$ eingesetzt werden, zum Beispiel der Punkt A, um $d$ zu berechnen:

$$d=\vec{n}\cdot\overrightarrow{OA}=\begin{pmatrix} 0 \\ 3 \\ -3 \end{pmatrix}\cdot\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}=3\cdot2-3\cdot3=-3$$

$d$ kann nun in die allgemeine Normalengleichung eingesetzt und das Skalarprodukt kann ausgerechnet werden:

$$
\begin{aligned}
&\Rightarrow\,\begin{pmatrix} 0 \\ 3 \\ -3 \end{pmatrix}\cdot\begin{pmatrix} x \\ y \\ z \end{pmatrix}=-3 \\
&\Rightarrow\,3y-3z=-3\qquad |:3 \\
&\Rightarrow\,-y+z=1
\end{aligned}
$$
```
````

```{admonition} Übung 5.3
:class: miniexercise
Gegeben sei eine Gerade $\vec{a}+s\cdot\vec{b}$ und der Ortsvektor $\vec{c}$ eines Punktes. Bestimmen Sie die Parametergleichung für die Ebene durch die Gerade und den Punkt.
```

````{admonition} Lösung
:class: miniexercise, toggle

$$E:\vec{x}(\lambda,\mu)=\vec{a}+\lambda\vec{b}+\mu(\vec{c}-\vec{a})$$

```{dropdown} Lösungsweg
Da bereits ein Richtungsvektor existiert, kann der zweite Richtungsvektor aus der Differenz des Stützvektors $\vec{a}$ der Ebene und des Ortsvektors des weiteren Punkts $\vec{c}$ erzeugt werden:

$$E:\vec{x}(s,t)=\vec{a}+s\cdot\vec{b}+t\cdot(\vec{c}-\vec{a})$$
```
````

```{admonition} Übung 5.4
:class: miniexercise
Zeigen Sie, dass sich die Geraden $\vec{x}(s)=(1,\,2,\,-1)+s(2,\,2,\,1)$ und $\vec{x}(t)=(-1,\,-2,\,3)+t(4,\,6,\,-3)$ schneiden. Bestimmen Sie den Schnittpunkt $S$ und den Winkel $\varphi$ zwischen den Geraden.
```

````{admonition} Lösung
:class: miniexercise, toggle

$$
\begin{aligned}
S&=(3,\,4,\,0) \\
\varphi&=43{,}5^\circ =0{,}759\,\mathrm{rad}
\end{aligned}
$$

```{dropdown} Lösungsweg
Damit ein Schnittpunkt existiert muss ein $t$ und ein $s$ (beide $\in\mathbb{R}$) existieren für die gilt:

$$\vec{x}_{1}(s)=\vec{x}_{2}(t)$$

Diese Bedingung führt zu folgendem Gleichungssystem:

$$\begin{array}{lrcll} & 1+2s & = & -1+4t & \text{ (I)} \\ & 2+2s & = & -2+6t & \text{ (II)} \\ & -1+1s & = & 3-3t & \text{ (III)} \end{array}$$

Zu beachten: Das sind 3 Gleichungen für 2 Unbekannte. Demnach dient eine Gleichung zur Probe, welche zwangsläufig durchgeführt werden muss.

(I) - (II): $1-2=-1+4t-(-2+6t)=1-2t$

$$\Rightarrow\,t=1$$

$t$ in (I) einsetzen: $s=1$

Beide Werte in (III) einsetzen: $-1+1\cdot1=3-3\cdot1$

$$\Rightarrow\,0=0$$

Auch die letzte Gleichung ist erfüllt, die Werte für s und t sind also Lösungen und damit existiert ein Schnittpunkt S. Eine dieser Lösung in die betreffenden Geradengleichung einsetzen, z.B. $t=1$ in $\vec{x}_{2}(t)$:

$$\overrightarrow{OS}=\vec{x}_{2}(1)=\begin{pmatrix} -1 \\ -2 \\ 3 \end{pmatrix}+1\cdot\begin{pmatrix} 4 \\ 6 \\ -3 \end{pmatrix}=\begin{pmatrix} 3 \\ 4 \\ 0 \end{pmatrix}$$

Der Schnittwinkel lässt sich mit Hilfe der Richtungsvektoren $\vec{u}_{1}=(2,\,2,\,1)$ und $\vec{u}_{2}=(4,\,6,\,-3)$ bestimmen.

$$
\begin{aligned}
\cos (\varphi)&=\frac{\vec{u}_{1}\cdot\vec{u}_{2}}{\left|\vec{u}_{1}\right|\left|\vec{u}_{2}\right|}=\frac{\begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix}\cdot\begin{pmatrix} 4 \\ 6 \\ -3 \end{pmatrix}}{\sqrt{{2}^{2}+{2}^{2}+{1}^{2}}\sqrt{{4}^{2}+{6}^{2}+{(-3)}^{2}}}=\frac{17}{\sqrt{9}\sqrt{16+36+9}}=\frac{17}{3\sqrt{61}} \\
&\Rightarrow\,\varphi=43{,}5^\circ =0{,}759\,\mathrm{rad}
\end{aligned}
$$
```
````

```{admonition} Übung 5.5
:class: miniexercise
Eine Gerade $L$ verläuft durch die Punkte $A=(5,1,7)$ und $B=(6,0,8)$ und eine Gerade $M$ verläuft durch die Punkte $C=(3,1,3)$ und $D=(-1,3,3)$. Bestimmen Sie den Abstand der Geraden.
```

````{admonition} Lösung
:class: miniexercise, toggle

$$d=\sqrt{6}$$

```{dropdown} Lösungsweg
$$
\begin{aligned}
\vec{L}(s)&=\overrightarrow{OA}+s\overrightarrow{AB} \\
&=\begin{pmatrix} 5 \\ 1 \\ 7 \end{pmatrix}+s\begin{pmatrix} 6-5 \\ 0-1 \\ 8-7 \end{pmatrix} \\
&=\begin{pmatrix} 5 \\ 1 \\ 7 \end{pmatrix}+s\begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} \\
&=\vec{p}_{L}+s\cdot\vec{q}_{L} \\
\vec{M}(t)&=\overrightarrow{OC}+t\overrightarrow{CD} \\
&=\begin{pmatrix} 3 \\ 1 \\ 3 \end{pmatrix}+t\begin{pmatrix} -1-3 \\ 3-1 \\ 3-3 \end{pmatrix} \\
&=\begin{pmatrix} 3 \\ 1 \\ 3 \end{pmatrix}+t\begin{pmatrix} -4 \\ 2 \\ 0 \end{pmatrix} \\
&={\vec{p}}_{M}+t\cdot{\vec{q}}_{M}
\end{aligned}
$$

An den Richtungsvektoren ${\vec{q}}_{L}$ und ${\vec{q}}_{M}$ lässt sich erkennen, dass die Geraden nicht parallel sind.

Zur Berechnung des Abstands lässt sich demnach die Formel aus der Vorlesung verwenden

$$
\begin{aligned}
d&=\frac{\left|({\vec{q}}_{L}\times{\vec{q}}_{M})\cdot(\overrightarrow{OA}-\overrightarrow{OC})\right|}{\left|{\vec{q}}_{L}\times{\vec{q}}_{M}\right|} \\
&=\frac{\left|\begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}\times\begin{pmatrix} -4 \\ 2 \\ 0 \end{pmatrix}\cdot\begin{pmatrix} 5-3 \\ 1-1 \\ 7-3 \end{pmatrix}\right|}{\left|\begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}\times\begin{pmatrix} -4 \\ 2 \\ 0 \end{pmatrix}\right|} \\
&=\frac{\left|\begin{pmatrix} -2 \\ -4 \\ -2 \end{pmatrix}\cdot\begin{pmatrix} 2 \\ 0 \\ 4 \end{pmatrix}\right|}{\left|\begin{pmatrix} -2 \\ -4 \\ -2 \end{pmatrix}\right|} \\
&=\frac{\left|-4-8\right|}{\sqrt{{(-2)}^{2}+{(-4)}^{2}+{(-2)}^{2}}} \\
&=\frac{12}{\sqrt{24}} \\
&=\frac{12}{\sqrt{4\cdot6}} \\
&=\frac{12}{2\sqrt{6}} \\
&=\frac{6}{\sqrt{6}} \\
&=\frac{\sqrt{6}\sqrt{6}}{\sqrt{6}} \\
&=\sqrt{6}
\end{aligned}
$$
```
````

```{admonition} Übung 5.6
:class: miniexercise
Berechnen Sie die Fläche des Dreiecks mit den Eckpunkten $(1,1,0)$, $(1,0,1)$ und $(0,1,1)$.
```

````{admonition} Lösung
:class: miniexercise, toggle

$${A}_{\text{Dreieck}}=\frac{\sqrt{3}}{2}$$

```{dropdown} Lösungsweg
$$
\begin{aligned}
{A}_{\text{Dreieck}}&=\frac{1}{2}\left|\overrightarrow{AB}\times\overrightarrow{AC}\right| \\
&=\frac{1}{2}\left|\begin{pmatrix} 1-1 \\ 0-1 \\ 1-0 \end{pmatrix}\times\begin{pmatrix} 0-1 \\ 1-1 \\ 1-0 \end{pmatrix}\right| \\
&=\frac{1}{2}\left|\begin{pmatrix} 0 \\ -1 \\ 1 \end{pmatrix}\times\begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix}\right| \\
&=\frac{1}{2}\left|\begin{pmatrix} -1 \\ -1 \\ -1 \end{pmatrix}\right| \\
&=\frac{1}{2}\sqrt{{(-1)}^{2}+{(-1)}^{2}+{(-1)}^{2}}=\frac{\sqrt{3}}{2}
\end{aligned}
$$
```
````

```{admonition} Übung 5.7
:class: miniexercise
Gegeben seien die Punkte $P=(3,1,2)$ und $Q=(1,-2,-4)$.

a) Bestimmen Sie die Normalengleichung der Ebene, die durch $Q$ verläuft und die senkrecht auf dem Vektor $\overrightarrow{PQ}$ steht.

b) Bestimmen Sie den Abstand ${d}_{R}$ des Punktes $R=(-1,1,1)$ zu dieser Ebene.
```

````{admonition} Lösung
:class: miniexercise, toggle

a) $E:2x+3y+6z=-28$

b) ${d}_{R}=5$

```{dropdown} Lösungsweg
a)

Der Vektor $\overrightarrow{PQ}$ ist auch sofort der Normalenvektor der Ebene: $\vec{n}=\overrightarrow{PQ}=\begin{pmatrix} 1 \\ -2 \\ -4 \end{pmatrix}-\begin{pmatrix} 3 \\ 1 \\ 2 \end{pmatrix}=\begin{pmatrix} -2 \\ -3 \\ -6 \end{pmatrix}$

Allgemeine Form der Normalengleichung: $\vec{n}\cdot\vec{x}=d$

Einsetzen von Q in die allgemeine Normalengleichung: $d=-2(1)-3(-2)-6(-4)=28$

Somit lautet die Normalengleichung für die Ebene:

$$\begin{array}{lrcl} & -2x-3y-6z & = & 28 \\ \Rightarrow & 2x+3y+6z & = & -28 \end{array}$$

b)

Aus der Vorlesung kennen Sie die Formel

$$d=\vec{n}\cdot\overrightarrow{RQ}$$

für die Berechnung des Abstands d. Dazu muss $\vec{n}$ ein Einheitsvektor sein.

Also normieren wir $\vec{n}$:

$$\left|\vec{n}\right|=\sqrt{{2}^{2}+{3}^{2}+{6}^{2}}=\sqrt{4+9+36}=\sqrt{49}=7$$

Also ist

$$
\begin{aligned}
d&=\vec{n}\cdot\overrightarrow{RQ}=\frac{1}{7}\begin{pmatrix} 2 \\ 3 \\ 6 \end{pmatrix}\cdot\left( R-Q \right)=\frac{1}{7}\begin{pmatrix} 2 \\ 3 \\ 6 \end{pmatrix}\cdot\left[ \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}-\begin{pmatrix} 1 \\ -2 \\ -4 \end{pmatrix} \right]=\frac{1}{7}\begin{pmatrix} 2 \\ 3 \\ 6 \end{pmatrix}\cdot\begin{pmatrix} -2 \\ 3 \\ 5 \end{pmatrix} \\
&=\frac{1}{7}(-4+9+30)=\frac{1}{7}(35)=5
\end{aligned}
$$
```
````

```{admonition} Übung 5.8
:class: miniexercise
Bestimmen Sie die Schnittlinie der Ebenen $x+y+z=5$ und $4x+y+2z=15$.
```

````{admonition} Lösung
:class: miniexercise, toggle

$${g}_{S}:\vec{x}=\begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix}+s\cdot\begin{pmatrix} 1 \\ 2 \\ -3 \end{pmatrix}$$

```{dropdown} Lösungsweg
Die allgemeine Geradengleichung lautet:

$$\vec{x}(s)=\vec{p}+s\cdot\vec{u}$$

Die Schnittlinie steht senkrecht auf den Normalenvektoren der beiden Ebenen:

$$\vec{u}=\vec{n}_{1}\times\vec{n}_{2}=\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}\times\begin{pmatrix} 4 \\ 1 \\ 2 \end{pmatrix}=\begin{pmatrix} 1 \\ 2 \\ -3 \end{pmatrix}$$

Jetzt wird ein Schnittpunkt beider Ebenen benötigt. Es werden also $(x,y,z)$ gesucht, die beide Ebenengleichungen erfüllen:

$$
\begin{aligned}
4x+y+2z&=15 \\
x+y+z&=5
\end{aligned}
$$

Sie können zur Lösung zum Beispiel in der ersten Gleichung auf beiden Seiten 15 subtrahieren, und in der zweiten Gleichung auf beiden Seiten 5.

Dann können sie die beiden linken Seiten gleichsetzen:

$$x+y+z-5=4x+y+2z-15$$

also:

$$-3x-z+10=0$$

Wähle zum Beispiel $x=3$, dann ist $z=1$.

Berechne $y$ aus der ersten Gleichung zu $y=15-2\cdot1-4\cdot3=1$.

Probe in zweiter Gleichung: $3+1+1=5$.

Mit $x=3$, $y=1$ und $z=1$ wurde ein Schnittpunkt beider Ebenen gefunden. Somit:

$$\vec{x}=\begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix}+s\cdot\begin{pmatrix} 1 \\ 2 \\ -3 \end{pmatrix}$$
```
````

```{admonition} Übung 5.9
:class: miniexercise
Bestimmen Sie den Winkel zwischen den Ebenen $2x+y-2z=5$ und $3x-6y-2z=7$.
```

````{admonition} Lösung
:class: miniexercise, toggle

$$\varphi=\arccos \left( \frac{4}{21} \right)=79^\circ =1{,}38\,\mathrm{rad}$$

```{dropdown} Lösungsweg
Der Winkel zwischen Ebenen ist auch der Winkel zwischen den Normalenvektoren.

Also Normalenvektoren ablesen:

$$\vec{n}_{1}=\begin{pmatrix} 2 \\ 1 \\ -2 \end{pmatrix}\qquad\vec{n}_{2}=\begin{pmatrix} 3 \\ -6 \\ -2 \end{pmatrix}$$

Winkel aus dem Skalarprodukt:

$$
\begin{aligned}
\cos (\varphi)&=\frac{\vec{n}_{1}\cdot\vec{n}_{2}}{\left|\vec{n}_{1}\right|\cdot\left|\vec{n}_{2}\right|}=\frac{\begin{pmatrix} 2 \\ 1 \\ -2 \end{pmatrix}\cdot\begin{pmatrix} 3 \\ -6 \\ -2 \end{pmatrix}}{\sqrt{{2}^{2}+{1}^{2}+{2}^{2}}\cdot\sqrt{{3}^{2}+{6}^{2}+{2}^{2}}}=\frac{4}{\sqrt{9}\cdot\sqrt{49}}=\frac{4}{3\cdot7} \\
\varphi&=\arccos \left( \frac{4}{21} \right)=79^\circ =1{,}38\,\mathrm{rad}
\end{aligned}
$$
```
````
