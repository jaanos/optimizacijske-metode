---
marp: true
style: "@import url('style.css')"
---

# Linearno programiranje

* **_Definicija._** _Linearni program_ (LP) je optimizacijski problem, kjer so ciljna funkcija in vsi pogoji linearni.

* **_Primer._**
    $$
    \begin{aligned}
    \min \ 2x_1 - 3x_2 + 2x_3 \\[1ex]
    \text{p.p.} \quad
    x_1 + 2x_2 - x_3 &\le 4 \\
    x_1 + 5x_2 + 2x_3 &\ge 2 \\
    2x_1 - 3x_2 - 4x_3 &= 1 \\
    x_1 &\ge 0 \\
    x_3 &\le 0
    \end{aligned}
    $$

---

# Standardna oblika

<span class="small">

* **_Definicija._** Linearni program je v _standardni obliki_, če

  - iščemo $\max$
  - so vsi pogoji $\le$
  - so vse spremenljivke $\ge 0$

* **_Trditev._** Vsak linearni program lahko ekvivalentno zapišemo v standardni obliki.

* _Dokaz._

  - $\min f(x) \to \max -f(x)$
  - $g_j(x) \ge b \to -g_j(x) \le -b$
  - $g_j(x) = b \to g_j(x) \le b$; $-g_j(x) \le -b$
  - $x_i \le 0 \to x_i = -x'_i$; $x'_i \ge 0$
  - $x_i$ neomejena $\to x_i = x^+_i - x^-_i$; $x^+_i, x^-_i \ge 0$

</span>

---

# Primer

Zapišimo prejšnji primer v standardni obliki.
$$
\begin{aligned}
\max \ -2x_1 + 3x^+_2 - 3x^-_2 + 2x'_3 \\[1ex]
\text{p.p.} \quad
x_1 + 2x^+_2 - 2x^-_2 + x'_3 &\le 4 \\
-x_1 - 5x^+_2 + 5x^-_2 + 2x'_3 &\le -2 \\
2x_1 - 3x^+_2 + 3x^-_2 + 4x'_3 &\le 1 \\
-2x_1 + 3x^+_2 - 3x^-_2 - 4x'_3 &\le -1 \\
x_1, x^+_2, x^-_2, x'_3 &\ge 0
\end{aligned}
$$

---

# Splošni zapis LP v standardni obliki

V splošnem lahko zapišemo linearni program v standardni obliki kot
$$
\begin{aligned}
\max \ c_1 x_1 + c_2 x_2 + \dots + c_n x_n \\[1ex]
\text{p.p.} \quad
a_{11} x_1 + a_{12} x_2 + \dots + a_{1n} x_n &\le b_1 \\
a_{21} x_1 + a_{22} x_2 + \dots + a_{2n} x_n &\le b_2 \\
&\ \ \vdots \\
a_{m1} x_1 + a_{m2} x_2 + \dots + a_{mn} x_n &\le b_m \\
x_1, x_2, \dots, x_n &\ge 0
\end{aligned}
$$

---

# Matrična oblika

* Definirajmo:
  $$
  x = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix},
  \quad
  c = \begin{bmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{bmatrix} \in \mathbb{R}^n,
  \quad
  b = \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_m \end{bmatrix} \in \mathbb{R}^m,
  \quad
  A = [a_{ij}]_{i,j=1}^{m,n} \in \mathbb{R}^{m \times n}
  $$

* Potem lahko zapišemo linearni program v matrični obliki:
  $$
  \begin{aligned}
  \max \ c^\top x \\[1ex]
  \text{p.p.} \quad
  A x &\le b \\
  x &\ge 0
  \end{aligned}
  $$

---

# Konveksnost

* **_Definicija._** Množica $A \subseteq \mathbb{R}^n$ je _konveksna_, če za vsaka $x, y \in A$ in vsak $\lambda \in [0, 1]$ velja $(1 - \lambda) x + \lambda y \in A$.

* $\sum_{i=1}^k \alpha_i x_i$ z $\sum_{i=1}^k \alpha_i = 1$ je _afina kombinacija_ točk $x_i$ ($1 \le i \le k$).
  - Afin prostor: "premaknjen" linearen prostor = afina kombinacija točk neke množice
* $\sum_{i=1}^k \alpha_i x_i$ z $\sum_{i=1}^k \alpha_i = 1$ in $\alpha_i \ge 0$ ($1 \le i \le k$) je _konveksna kombinacija_ točk $x_i$ ($1 \le i \le k$).

* Torej: množica $A$ je konveksna, če je vsaka daljica s krajišči v množici $A$ v celoti vsebovana v $A$.

---

# Primeri konveksnih množic

* Konveksne množice v $\mathbb{R}$: intervali
* Krogla v $\mathbb{R}^n$ je konveksna, sfera pa ne
* Polprostor v $\mathbb{R}^n$ je konveksen:
  $$
  \begin{aligned}
  a_1 x_1 + a_2 x_2 + \dots + a_n x_n &\le b &&/ \cdot (1 - \lambda) \\
  a_1 y_1 + a_2 y_2 + \dots + a_n y_n &\le b &&/ \cdot \lambda \\
  a_1 ((1-\lambda) x_1 + \lambda y_1) + \dots + a_n ((1-\lambda) x_n + \lambda y_n) &\le (1-\lambda) b + \lambda b = b
  \end{aligned}
  $$
  $\Rightarrow$ $(1-\lambda) x + \lambda y$ je tudi v polprostoru.

---

# Lastnosti konveksnih množic

* **_Trditev._** Presek konveksnih množic je konveksen: $A_i$ ($i \in I$) konveksne $\Rightarrow \bigcap_{i \in I} A_i$ konveksna.

* _Dokaz._ Preveriti moramo: za vsaka $x, y \in \bigcap_{i \in I} A_i$ in vsak $\lambda \in [0, 1]$ velja $\forall i \in I: (1-\lambda) x + \lambda y \in A_i$. To je res, ker so množice $A_i$ ($i \in I$) konveksne.

* Unija konveksnih množic **ni nujno konveksna**!

---

# Konveksnost pri linearnih programih

<span class="numbers">

* **_Trditev._** Naj bo $\Pi = (\Omega, f, \max)$ linearni program. Potem velja:

  1. $\Omega$ je konveksna množica.
  2. Množica optimalnih rešitev $\Pi$ je konveksna množica.

* _Dokaz._

  1. $\Omega$ je presek polprostorov (in hiperravnin), torej je konveksna množica.
  2. Če optimalnih rešitev ni, potem je množica optimalnih rešitev prazna, torej konveksna. Sicer naj bo $c$ optimalna vrednost. Potem je množica optimalnih rešitev enaka
     $$
     \{x \in \Omega \mid f(x) = c\}
     $$
     in je zato konveksna množica.

</span>

---

# Grafično reševanje LP z dvema spremenljivkama

<span class="columns col2">

<span>

* **_Primer._**
  $$
  \begin{aligned}
  \max \ x + y \\[1ex]
  \text{p.p.} \quad
  x + 2y &\le 6 \\
  5x + 4y &\le 20 \\
  x, y &\ge 0
  \end{aligned}
  $$

</span>

<span class="nobullet">

* ![](slike/graficno.png)

</span>

</span>

* $(x^\ast, y^\ast) = ({8 \over 3}, {5 \over 3})$ je optimalna rešitev, $z^\ast = {13 \over 3}$ je optimalna vrednost.

---

# Politop dopustnih rešitev

* Množica dopustnih rešitev $\Omega$ je **politop** (lahko neomejen).
* Množica optimalnih rešitev je **lice** tega politopa (oglišče, stranica, stranska ploskev, itd.).
* Optimalna vrednost (če obstaja) je vedno dosežena (tudi) v oglišču.

---

# Simpleksna metoda

Denimo, da imamo linearni program v standardni obliki
$$
\begin{aligned}
\max \ c^\top x \\[1ex]
\text{p.p.} \quad
A x &\le b \\
x &\ge 0
\end{aligned}
$$
kjer velja

* $A \in \mathbb{R}^{m \times n}$, $b \in \mathbb{R}^m$, $c \in \mathbb{R}^n$
* $b \ge 0$
  * če velja $b \not\ge 0$, uporabimo dvofazno simpleksno metodo, ki jo bomo spoznali kasneje

---

# Primer - kmetija

<span class="small">

* Dan je sledeči linearni program.
  $$
  \begin{aligned}
  \max &\ &  400 x_1 + 600 x_2 + 480 x_3 \\[1ex]
  \text{p.p.} && x_1 + x_2 + x_3 &\le 50 \\
  &&  60 x_1 +  80 x_2 + 100 x_3 &\le 5000 \\
  && 240 x_1 + 400 x_2 + 320 x_3 &\le 24000 \\
  && x_1, x_2, x_3 &\ge 0
  \end{aligned}
  $$

* Ciljno funkcijo in omejitve lahko skaliramo brez vpliva na pomen spremenljivk:
  $$
  \begin{aligned}
  \max &\ & 10 x_1 + 15 x_2 + 12 x_3 \\[1ex]
  \text{p.p.} && x_1 + x_2 + x_3 &\le 50 \\
  && 3 x_1 + 4 x_2 + 5 x_3 &\le 250 \\
  && 3 x_1 + 5 x_2 + 4 x_3 &\le 300 \\
  && x_1, x_2, x_3 &\ge 0
  \end{aligned}
  $$

</span>

---

# Prvi slovar

<span class="small">

* Neenakosti spremenimo v enakosti z uvedbo novih **nenegativnih** spremenljivk.

* Prvi slovar:
  $$
  \begin{aligned}
  x_4 &= 50 - x_1 - x_2 - x_3 \\
  x_5 &= 250 - 3 x_1 - 4 x_2 - 5 x_3 \\
  x_6 &= 300 - 3 x_1 - 5 x_2 - 4 x_3 \\ \hline
  z &= 10 x_1 + 15 x_2 + 12 x_3
  \end{aligned}
  $$

* V zgornjem sistemu enačb nastopajo sledeče spremenljivke:

  - _prvotne spremenljivke_: $x_1, x_2, \dots, x_n$
  - _dopolnilne spremenljivke_: $x_{n+1}, x_{n+2}, \dots, x_{n+m}$
  - _funkcional_ $z$

</span>

---

# Slovarji

* _Slovar_ je izražava $m$ izmed spremenljivk $x_1, x_2, \dots, x_{n+m}$ (_bazne spremenljivke_) in funkcionala $z$ z ostalimi izmed spremenljivk (_nebazne spremenljivke_).

* V _prvem slovarju_ velja:

  - nebazne spremenljivke so prvotne spremenljivke, in
  - bazne spremenljivke so dopolnilne spremenljivke.

* Slovar je _dopusten_, če so konstantni koeficienti baznih spremenljivk nenegativni. Prvi slovar je dopusten zaradi predpostavke $b \ge 0$.

* Dopusten slovar nam da bazno dopustno rešitev, ki jo dobimo tako, da nebaznim spremenljivkam dodelimo vrednost $0$.

---

# Vstopne in izstopne spremenljivke

* Izberemo **nebazno** spremenljivko s **pozitivnim** koeficientom pri funkcionalu $z$. Če je kandidatov več, izberemo **poljubnega**. Pogosto uporabljamo:

  - pravilo največjega koeficienta
  - pravilo najmanjšega indeksa
  - pravilo največjega povečanja

* Izbrani spremenljivki pravimo _vstopna_ spremenljivka. 

* Vrstici, ki izbrano vstopno spremenljivko **najbolj omejuje**, pravimo _pivotna_ vrstica, pripadajoči bazni spremenljivki pa _izstopna_ spremenljivka.
* Če imamo več pivotnih vrstic (tj., več baznih spremenljivk najbolj omejuje vstopno spremenljivko), potem za izstopno spremenljivko izberemo **poljubno** izmed njih.

---

# Pivotiranje

* V našem primeru za vstopno spremenljivko izberemo $x_2$ (sta pa tudi $x_1$ in $x_3$ kandidata).

  $$
  \begin{aligned}
  x_4 &= 50 - x_1 - x_2 - x_3 & \leftarrow x_2 &\le 50 \\
  x_5 &= 250 - 3 x_1 - 4 x_2 - 5 x_3 & x_2 &\le {250 \over 4} = {125 \over 2} \\
  x_6 &= 300 - 3 x_1 - 5 x_2 - 4 x_3 & x_2 &\le {300 \over 5} = 60 \\ \hline
  z &= 10 x_1 + 15 \underline{x_2} + 12 x_3
  \end{aligned}
  $$

* Edini kandidat za izstopno spremenljivko je $x_4$.

---

# Naslednji slovar

* Vstopna spremenljivka vstopi v bazo, izstopna iz nje izstopi.
* Rešimo enačbo za vstopno spremenljivko in vstavimo v enačbe za ostale bazne spremenljivke in funkcional $z$:

  $$
  \begin{aligned}
  x_2 &= 50 - x_1 - x_3 - x_4 \\
  x_5 &= 250 - 3 x_1 - 4 (50 - x_1 - x_3 - x_4) - 5 x_3 \\
  &= 50 + x_1 - x_3 + 4 x_4 \\
  x_6 &= 300 - 3 x_1 - 5 (50 - x_1 - x_3 - x_4) - 4 x_3 \\
  &= 50 + 2 x_1 + x_3 + 5 x_4 \\ \hline
  z &= 10 x_1 + 15 (50 - x_1 - x_3 - x_4) + 12 x_3 = \\
  &= 750 - 5 x_1 - 3 x_3 - 15 x_4
  \end{aligned}
  $$

---

# Nadaljevanje metode

* Če so vsi koeficienti pri funkcionalu $z$ **nepozitivni**, smo našli **optimalno rešitev** in se simpleksna metoda ustavi.
* V nasprotnem primeru ponavljamo postopek.
* Vsi slovarji, ki smo jih dobili tekom reševanja, so **dopustni**.
  * Če smo dobili kak nedopusten slovar, smo se zmotili (npr. izbrali napačno izstopno spremenljivko ali naredili računsko napako).

---

# Kaj se lahko še zgodi?

* Konstantni koeficient bazne spremenljivke je enak $0$:
  $$
  \begin{aligned}
  &\vdots \\
  x_j &= 0 + \ldots - 3 x_i + \ldots & \leftarrow x_i \le 0 \\
  &\vdots \\ \hline
  z &= 10 + \ldots + 4 \underline{x_i} + \ldots
  \end{aligned}
  $$
* Vrednost v bazni dopustni rešitvi se **ne** poveča - _izrojen_ korak.

---

# Kaj se lahko še zgodi? (2)

* Nobena vrstica na omejuje vstopne spremenljivke:
  $$
  \begin{aligned}
  &\vdots \\
  x_j &= \ldots + 3 x_i + \ldots & x_i \le \infty \\
  &\vdots \\ \hline
  z &= \ldots + 4 \underline{x_i} + \ldots
  \end{aligned}
  $$
* Tedaj je linearni program **neomejen** - končamo simpleksno metodo. 
* **Neomejeno družino** dopustnih rešitev dobimo tako, da vstopno spremenljivko pustimo kot nenegativen parameter brez zgornje meje, ostalim nebaznim spremenljivkam pa dodelimo vrednost $0$.

---

# Vse optimalne rešitve

Kako iz zadnjega slovarja za optimalni problem dobimo **vse** optimalne rešitve?

* Nebaznim spremenljivkam z negativnim koeficientom dodelimo vrednost $0$.
* Nebazne spremenljivke z **ničelnim koeficientom** pustimo kot parametre (tj., jim ne dodelimo nujno vrednosti $0$).
* Upoštevamo, da so vse bazne spremenljivke nenegativne.

---

# Primer

<span class="small">

* Denimo, da imamo sledeči zadnji slovar.
  $$
  \begin{aligned}
  x_2 &= 40 - {2 \over 3} x_1 - {4 \over 5} x_3 - {1 \over 15} x_6 \\
  x_4 &= 10 - {1 \over 3} x_1 - {1 \over 5} x_3 + {1 \over 15} x_6 \\
  x_5 &= 90 - {1 \over 3} x_1 - {9 \over 5} x_3 + {4 \over 15} x_6 \\ \hline
  z &= 200 - {1 \over 3} x_1 - {1 \over 3} x_6
  \end{aligned}
  $$

<span class="columns col2">

<span>

* Potem velja:
  - $x_1^\ast = x_6^\ast = 0$
  - $x_2^\ast = 40 - {4 \over 5} x_3^\ast \ge 0$, torej $x_3^\ast \le 50$
  - $x_4^\ast = 10 - {1 \over 5} x_3^\ast \ge 0$, torej $x_3^\ast \le 50$
  - $x_5^\ast = 90 - {9 \over 5} x_3^\ast \ge 0$, torej $x_3^\ast \le 50$

</span>

<span>

* Optimalne rešitve so torej oblike $x_1^\ast = 0$, $x_2^\ast = 40 - {4 \over 5} x_3^\ast$, $0 \le x_3^\ast \le 50$, $z^\ast = 200$.

</span>

</span>

</span>

---

# Končnost simpleksne metode

* Ali se simpleksna metoda vedno ustavi? **NE.**

* Možnih slovarjev je ${n+m \choose m}$.
  * Če se simpleksna metoda ne ustavi, pomeni, da je prišlo do "ciklanja".
  * V tem primeru so vsi koraki v ciklu izrojeni.

* Ciklanje je izjemno redko. Dokazati se da, da do ciklanja ne bo prišlo, če za vstopne in izstopne spremenljivke uporabimo pravilo najmanjšega indeksa (_Blandovo pravilo_).

---

# Časovna zahtevnost simpleksne metode

* Časovne zahtevnosti algoritmov:
  - "Hitri" algoritmi: uporabijo polinomsko mnogo operacij.
  - "Počasni" algoritmi: uporabijo eksponentno mnogo operacij.

* Ali je simpleksna metoda hitra?
  * Tipično: $\approx m \log n$ korakov
  * Najslabši primer: simpleksna metoda **ni** polinomska

---

# Klee-Mintyjeva kocka

* **_Primer._** (Klee-Minty) Za $n = 3$:
  $$
  \begin{aligned}
  \max &\ & 100 x_1 + 10 x_2 + x_3 \\[1ex]
  \text{p.p.} && x_1 &\le 1 \\
  &&  20 x_1 +  x_2 &\le 100 \\
  && 200 x_1 + 20 x_2 + x_3 &\le 10000 \\
  && x_1, x_2, x_3 &\ge 0
  \end{aligned}
  $$

  * Če uporabimo pravilo največjega koeficienta, potrebujemo $2^n - 1$ korakov.
  * Če uporabimo pravilo največjega povečanja, potrebujemo $1$ korak.

* Obstajajo algoritmi za reševanje linearnih programov, ki so dokazljivo polinomski.

---

# Dvofazna simpleksna metoda

Uporabljamo jo za linearne programe v standardni obliki, za katere ne velja $b \ge 0$.

1. faza: ugotovi, ali je linearni program dopusten - če je, nam prva faza da dopusten začetni slovar za drugo fazo.
2. faza: identična simpleksni metodi.

---

# Primer

Imamo dve vitaminski tableti, Polivit in Oligovit, ki vsebujejo različne količine vitaminov A, B in C.

|                | A |  B | C | cena za tableto |
| -------------- | - | -- | - | --------------- |
| Polivit        | 1 |  4 | 1 | 12              |
| Oligovit       | 1 |  1 | 2 | 10              |
| dnevne potrebe | 7 | 13 | 8 |

Kako najceneje zadostiti dnevnim potrebam?

---

# Linearni program

<span class="small">

* Zapišimo kot linearni program.
  $$
  \begin{aligned}
  \min &\ & 12 x_1 + 10 x_2 \\[1ex]
  \text{p.p.} && x_1 + x_2 &\ge 7 \\
  &&  4 x_1 + x_2 &\ge 13 \\
  && x_1 + 2 x_2 &\ge 8 \\
  && x_1, x_2 &\ge 0
  \end{aligned}
  $$

* Zapišimo še ekvivalentni linearni program v standardni obliki.
  $$
  \begin{aligned}
  \max &\ & -12 x_1 - 10 x_2 \\[1ex]
  \text{p.p.} && -x_1 - x_2 &\le -7 \\
  && -4 x_1 - x_2 &\le -13 \\
  && -x_1 - 2 x_2 &\le -8 \\
  && x_1, x_2 &\ge 0
  \end{aligned}
  $$

</span>

---

# Pomožni problem prve faze

* Ker v zgornjem linearnem programu velja $b \not\ge 0$, zapišimo še pomožni problem prve faze:
  $$
  \begin{aligned}
  && \min \ x_0 \\[1ex]
  \text{p.p.} && -x_1 - x_2 &\le -7 + x_0 \\
  && -4 x_1 - x_2 &\le -13 + x_0 \\
  && -x_1 - 2 x_2 &\le -8 + x_0 \\
  && x_0, x_1, x_2 &\ge 0
  \end{aligned}
  $$
* Pomožni problem je vedno dopusten ($x_0$ mora biti dovolj velik).
* Pomožni problem ima optimalno vrednost $0$ **natanko tedaj**, ko je prvotni problem dopusten.

---

# Začetni slovar za prvo fazo

* Zapišimo začetni slovar za prvo fazo - ta slovar **ni dopusten**:
  $$
  \begin{aligned}
  x_3 &= -7 + x_0 + x_1 + x_2 \\
  x_4 &= -13 + x_0 + 4 x_1 + x_2 \\
  x_5 &= -8 + x_0 + x_1 + 2 x_2 \\ \hline
  w &= -x_0
  \end{aligned}
  $$

* V prvem koraku prve faze v bazo vstopi $x_0$, izstopi pa spremenljivka z najmanjšim (najbolj negativnim) konstantnim členom - v našem primeru $x_4$:
  $$
  \begin{aligned}
  x_0 &= 13 - 4 x_1 - x_2 + x_4 & \leftarrow x_2 &\le 13  \\
  x_3 &=  6 - 3 x_1 + x_4 & x_2 &\le \infty \\
  x_5 &=  5 - 3 x_1 + x_2 + x_4 & x_2 &\le \infty \\ \hline
  w &= -13 + 4 x_1 + \underline{x_2} - x_4
  \end{aligned}
  $$

---

# Nadaljevanje prve faze

* Nadaljujemo enako kot pri osnovni simpleksni metodi.
* V našem primeru po metodi največjega povečanja izberemo $x_2$ za vstopno spremenljivko in $x_0$ za izstopno spremenljivko.
  $$
  \begin{aligned}
  x_2 &= 13 - x_0 - 4 x_1 + x_4 \\
  x_3 &=  6 - 3 x_1 + x_4 \\
  x_5 &= 18 - x_0 - 7 x_1 + 2 x_4 \\ \hline
  w &= -x_0
  \end{aligned}
  $$

---

# Začetni slovar za drugo fazo

* Optimalna vrednost pomožnega problema je $0$ - prvotni problem je torej dopusten.
* Začetni slovar druge faze dobimo tako, da v zadnjem slovarju prve faze vzamemo $x_0 = 0$ in vstavimo prvotne bazne spremenljivke v funkcional $z$:
  $$
  \begin{aligned}
  x_2 &= 13 - 4 x_1 + x_4 \\
  x_3 &=  6 - 3 x_1 + x_4 \\
  x_5 &= 18 - 7 x_1 + 2 x_4 \\ \hline
  z &= -12 x_1 - 10 (13 - 4 x_1 + x_4) \\
  &= -130 + 28 x_1 - 10 x_4
  \end{aligned}
  $$

---

# Nadaljevanje druge faze

<span class="small">

$x_1$ vstopi, $x_3$ izstopi:
$$
\begin{aligned}
x_1 &=  2 - {1 \over 3} x_3 + {1 \over 3} x_4 \\[-1ex]
x_2 &= 13 - 4 \left(2 - {1 \over 3} x_3 + {1 \over 3} x_4\right) + x_4 \\[-1ex]
&= 5 + {4 \over 3} x_3 - {1 \over 3} x_4 \\[-1ex]
x_5 &= 18 - 7 \left(2 - {1 \over 3} x_3 + {1 \over 3} x_4\right) + 2 x_4 \\[-1ex]
&= 4 + {7 \over 3} x_3 - {1 \over 3} x_4 \\ \hline
z &= -130 + 28 \left(2 - {1 \over 3} x_3 + {1 \over 3} x_4\right) - 10 x_4 \\[-1ex]
&= -74 - {28 \over 3} x_3 - {2 \over 3} x_4
\end{aligned}
$$

</span>

---

# Optimalna rešitev

Imamo zadnji slovar druge faze, preberemo optimalno rešitev:

* $x_1^\ast = 2$ tableti Polivit
* $x_2^\ast = 5$ tablet Oligovit
* cena: $-z^\ast = 74$

---

# Kaj se lahko zgodi ob koncu prve faze?

Prva faza se vedno konča, ko ne moremo več izbrati vstopne spremenljivke (ker je problem omejen).

* $w^\ast < 0$: prvotni problem je nedopusten, končamo.
* $w^\ast = 0$, $x_0$ je nebazna spremenljivka v zadnjem slovarju prve faze: nadaljujemo z drugo fazo.
* $w^\ast = 0$, $x_0$ je bazna spremenljivka v zadnjem slovarju prve faze: temu se izognemo s pravilom, da če $x_0$ lahko izstopi iz baze, jo izberemo za izstopno spremenljivko (ali pa naredimo izrojen korak, da $x_0$ izstopi).

---

# Povzetek

![h:500px](slike/dvofazna.png)

---

# Osnovni izrek linearnega programiranja

* Če ima linearni program dopustno rešitev, ima bazno dopustno rešitev.
* Če ima linearni program optimalno rešitev, ima bazno optimalno rešitev.
* Za linearni program velja natanko ena od možnosti:
  - linearni program je nedopusten,
  - linearni program je neomejen, ali
  - linearni program je optimalen.

---

# Dualnost pri linearnem programiranju

* Naj bo $\Pi$ linearni program
  $$
  \begin{aligned}
  \max &\ & 10 x_1 + 15 x_2 + 12 x_3 \\[1ex]
  \text{p.p.} && x_1 + x_2 + x_3 &\le 50 &/ \cdot y_4 \ge 0 \\
  && 3 x_1 + 4 x_2 + 5 x_3 &\le 250 &/ \cdot y_5 \ge 0 \\
  && 3 x_1 + 5 x_2 + 4 x_3 &\le 300 &/ \cdot y_6 \ge 0 \\
  && x_1, x_2, x_3 &\ge 0
  \end{aligned}
  $$

* Iščemo zgornje meje za ciljno funkcijo:
  $$
  (y_4 + 3 y_5 + 3 y_6) x_1 + (y_4 + 4 y_5 + 5 y_6) x_2 + (y_4 + 5 y_5 + 4 y_6) x_3 \le 50 y_4 + 250 y_5 + 300 y_6
  $$

---

# Zgornja meja za ciljno funkcijo

* Če velja
  $$
  \begin{aligned}
  y_4 + 3 y_5 + 3 y_6 &\ge 10, \\
  y_4 + 4 y_5 + 5 y_6 &\ge 15, \\
  y_4 + 5 y_5 + 4 y_6 &\ge 12,
  \end{aligned}
  $$
  potem
  $$
  10 x_1 + 15 x_2 + 12 x_3 \le 50 y_4 + 250 y_5 + 300 y_6.
  $$
* Hočemo čim manjšo zgornjo mejo.

---

# Dualni linearni program

_Prvotnemu_ linearnemu programu $\Pi$ dodelimo _dualni_ linearni program $\Pi'$:
$$
\begin{aligned}
\min &\ & 50 y_4 + 250 y_5 + 300 y_6 \\[1ex]
\text{p.p.} && y_4 + 3 y_5 + 3 y_6 &\ge 10 \\
&& y_4 + 4 y_5 + 5 y_6 &\ge 15 \\
&& y_4 + 5 y_5 + 4 y_6 &\ge 12 \\
&& y_4, y_5, y_6 &\ge 0
\end{aligned}
$$

---

# Definicija

**_Definicija._** Za prvotni linearni program $\Pi$ je njegov dualni linearni program $\Pi'$, kjer je

<span class="small nobullet">

* 
  <span class="columns col2">
  <span>

  $$
  \begin{aligned}
  \max \ c^\top x \\[1ex]
  \text{p.p.} \quad A x &\le b \\
  x &\ge 0
  \end{aligned}
  $$

  </span>

  <span>

  $$
  \begin{aligned}
  \min \ b^\top y \\[1ex]
  \text{p.p.} \quad A^\top y &\ge c \\
  y &\ge 0
  \end{aligned}
  $$

  </span>
  </span>

* 
  <span class="columns col2">
  <span>

  $$
  \begin{aligned}
  \max \ \sum_{j=1}^n c_j x_j \\[1ex]
  \text{p.p.} \quad \sum_{j=1}^n a_{ij} x_j &\le b_i & (1 &\le i \le m) \\
  x_j &\ge 0 & (1 &\le j \le n)
  \end{aligned}
  $$

  </span>

  <span>

  $$
  \begin{aligned}
  \min \ \sum_{i=1}^m b_i y_{n+i} \\[1ex]
  \text{p.p.} \quad \sum_{i=1}^m a_{ij} y_{n+i} &\ge c_j & (1 &\le j \le n) \\
  y_{n+i} &\ge 0 & (1 &\le i \le m)
  \end{aligned}
  $$

  </span>
  </span>

</span>

---

# Dualnost

* **_Trditev._** $\Pi'' = \Pi$.

* _Dokaz._

  <span class="columns col2">
  <span>

  * Zapišimo $\Pi'$ v standardni obliki.
    $$
    \begin{aligned}
    \max \ -b^\top y \\[1ex]
    \text{p.p.} \quad -A^\top y &\le -c \\
    y &\ge 0
    \end{aligned}
    $$

  </span>
  <span>

  * Potem je $\Pi''$ sledeči LP:
    $$
    \begin{aligned}
    \min \ -c^\top x \\[1ex]
    \text{p.p.} \quad -A x &\ge -b \\
    x &\ge 0
    \end{aligned}
    $$

  </span>
  </span>

  * Pretvorba v standardno obliko nam pokaže, da je $\Pi'' = \Pi$.

---

# Šibki izrek o dualnosti (ŠID)

* Naj bo $\Pi$ prvotni linearni program kot zgoraj in $\Pi'$ njegov dual.
* Če je $x$ dopustna rešitev za $\Pi$ in $y$ dopustna rešitev za $\Pi'$, potem velja $c^\top x \le b^\top y$.

* _Dokaz._

  $$
  \begin{aligned}
  c^\top x &\le (A^\top y)^\top x & (A^\top y &\ge c, x \ge 0) \\
  &= y^\top A x \\
  &\le y^\top b & (Ax &\le b, y \ge 0) \\
  &= b^\top y
  \end{aligned}
  $$

---

# Še en dokaz

$$
\begin{aligned}
\sum_{j=1}^n c_j x_j &\le \sum_{j=1}^n \left(\sum_{i=1}^m a_{ij} y_{n+i}\right) x_j & \Big(\forall j: \sum_{i=1}^m a_{ij} y_{n+i} &\ge c_j, x_j \ge 0\Big) \\
&= \sum_{i=1}^m \left(\sum_{j=1}^n a_{ij} x_j\right) y_{n+i} \\
&\le \sum_{i=1}^m b_i y_{n+i} & \Big(\forall i: \sum_{j=1}^n a_{ij} x_j &\le b_i, y_{n+i} \ge 0\Big) \\
\end{aligned}
$$

---

# Posledici

* **_Posledica 1._** Če sta $x$ in $y$ dopustni rešitvi za $\Pi$ oziroma $\Pi'$, za kateri velja $c^\top x = b^\top y$, potem sta $x$ in $y$ optimalni rešitvi za $\Pi$ oziroma $\Pi'$.

* _Dokaz._ $b^\top y$ je zgornja meja za $c^\top x$, to zgornjo mejo dosežemo. $c^\top x$ je spodnja meja za $b^\top y$, to spodnjo mejo dosežemo.

* **Opomba.** S to posledico lahko preverimo optimalnost ponujenih dopustnih rešitev $x$, $y$, za kateri velja $c^\top x = b^\top y$.

* **_Posledica 2._** Če je $\Pi$ neomejen problem, je $\Pi'$ nedopusten problem.

* _Dokaz._ Če je $\Pi'$ dopusten, imamo zgornjo mejo za ciljno funkcijo $\Pi$, protislovje.

---

# Krepki izrek o dualnosti (KID)

* Naj bo $\Pi$ prvotni linearni program kot zgoraj in $\Pi'$ njegov dual.
* Če je $x^\ast$ optimalna rešitev za $\Pi$, potem obstaja optimalna rešitev $y^\ast$ za $\Pi'$ in velja $c^\top x^\ast = b^\top y^\ast$.

---

# Problem kmetije

<span class="small">

* Zadnji slovar za problem kmetije:
  $$
  \begin{aligned}
  x_2 &= 50 - x_1 - x_3 - x_4 \\
  x_5 &= 50 + x_1 - x_3 + 4 x_4 \\
  x_6 &= 50 + 2 x_1 + x_3 + 5 x_4 \\ \hline
  z &= 750 - 5 x_1 - 0 x_2 - 3 x_3 - 15 x_4 - 0 x_5 - 0 x_6
  \end{aligned}
  $$

* Zadnji slovar za dual problema kmetije:
  $$
  \begin{aligned}
  y_1 &=  5 + y_2 -   y_5 - 2 y_6 \\
  y_3 &=  3 + y_2 +   y_5 -   y_6 \\
  y_4 &= 15 + y_2 - 4 y_5 - 5 y_6 \\ \hline
  z &= -750 - 0 y_1 - 50 y_2 - 0 y_3 - 0 y_4 - 50 y_5 - 50 y_6
  \end{aligned}
  $$

* Videti je, da so koeficienti dopolnilnih spremenljivk v zadnjem slovarju ravno negacija optimalne rešitve dualnega problema.

</span>

---

# Dokaz KID

* Simpleksna metoda za $\Pi$ se konča z zadnjim slovarjem z
  $$
  z = z^\ast + \sum_{j=1}^{n+m} c^\ast_j x_j = \sum_{j=1}^n c_j x^\ast_j + \sum_{j=1}^n c^\ast_j x_j + \sum_{i=1}^m c^\ast_{n+i} x_{n+i},
  $$
  kjer velja $c^\ast_j \le 0$ ($1 \le j \le n+m$) in $c^\ast_j = 0$, če je $x_j$ bazna spremenljivka.
* Naj bo $y^\ast_{n+i} = -c^\ast_{n+i}$ ($1 \le i \le m$).
* Pokazali bomo, da je $y^\ast$ optimalna rešitev $\Pi'$.

---

# Dokaz KID (2)

Velja
$$
\begin{aligned}
z &= \sum_{j=1}^n c_j x^\ast_j + \sum_{j=1}^n c^\ast_j x_j + \sum_{i=1}^m (-y^\ast_{n+i}) \left(b_i - \sum_{j=1}^n a_{ij} x_j\right) \\
&= \left(\sum_{j=1}^n c_j x^\ast_j - \sum_{i=1}^m b_i y^\ast_{n+i}\right) + \sum_{j=1}^n c^\ast_j x_j + \sum_{j=1}^n \left(\sum_{i=1}^m a_{ij} y^\ast_{n+i}\right) x_j \\
&= \left(\sum_{j=1}^n c_j x^\ast_j - \sum_{i=1}^m b_i y^\ast_{n+i}\right) + \sum_{j=1}^n \left(c^\ast_j + \sum_{i=1}^m a_{ij} y^\ast_{n+i}\right) x_j \\
\end{aligned}
$$

---

# Dokaz KID (3)

* Ker velja $z = \sum_{j=1}^n c_j x_j$, sledi
  $$
  \begin{aligned}
  \sum_{j=1}^n c_j x^\ast_j - \sum_{i=1}^m b_i y^\ast_{n+i} &= 0, \\
  c^\ast_j + \sum_{i=1}^m a_{ij} y^\ast_{n+i} &= c_j & (1 \le j \le n).
  \end{aligned}
  $$
* Ker velja $y^\ast_{n+i} = -c^\ast_{n+i} \ge 0$ ($1 \le i \le m$) in $\sum_{i=1}^m a_{ij} y^\ast_{n+i} = c_j - c^\ast_j \ge c_j$ ($1 \le j \le n$), je $y^\ast$ dopustna rešitev za $\Pi'$.
* Ker velja $c^\top x^\ast = b^\top y^\ast$, je po Posledici 1 $y^\ast$ optimalna rešitev za $\Pi'$.

---

# Povzetek

* **_ŠID:_** $x, y$ dopustni za $\Pi, \Pi' \Rightarrow c^\top x \le b^\top y$
* **_KID:_** $\Pi$ optimalen $\Rightarrow \Pi'$ optimalen z isto optimalno vrednostjo

* Imamo torej sledeče možnosti:

  | $\Pi$ \ $\Pi'$ | nedopusten | neomejen    | optimalen   |
  | -------------- | ---------- | ----------- | ----------- |
  | nedopusten     | ✔          | ✔           | ✗ (KID)     |
  | neomejen       | ✔          | ✗ (ŠID)     | ✗ (KID/ŠID) |
  | optimalen      | ✗ (KID)    | ✗ (KID/ŠID) | ✔           |

---

# Primer: nedopustni LP in dual

<span class="columns col2">

<span>

$$
\begin{aligned}
\Pi: \\[1ex]
\max &\ & 2x_1 - x_2 \\
\text{p.p.} && -x_1 + x_2 &\le -2 \\
&& x_1 - x_2 &\le 1 \\
&& x_1, x_2 &\ge 0
\end{aligned}
$$

</span>

<span>

$$
\begin{aligned}
\Pi': \\[1ex]
\min &\ & -2y_3 + y_4 \\
\text{p.p.} && -y_3 + y_4 &\ge 2 \\
&& y_3 - y_4 &\ge -1 \\
&& y_3, y_4 &\ge 0
\end{aligned}$$

</span>

</span>

* **_Izrek._** Za linearna programa $\Pi$ in $\Pi'$ velja natanko ena od sledečih možnosti:

  - oba sta optimalna,
  - oba sta nedopustna, ali
  - eden je neomejen, drugi pa nedopusten.

---

# Izrek o dualnem dopolnjevanju (IDD)

* Naj bo $\Pi$ prvotni linearni program kot zgoraj in $\Pi'$ njegov dual,
ter naj bosta $x$ in $y$ dopustni rešitvi za $\Pi$ oziroma $\Pi'$.
* Potem sta $x$ in $y$ optimalni rešitvi za $\Pi$ oziroma $\Pi'$ natanko tedaj, ko velja
  $$
  \begin{aligned}
  \forall i &\in \{1, \dots, m\}: & \Big(\sum_{j=1}^n a_{ij} x_j &= b_i &&\lor& y_{n+i} &= 0\Big) \quad \text{in} \\
  \forall j &\in \{1, \dots, n\}: & \Big(x_j &= 0 &&\lor& \sum_{i=1}^m a_{ij} y_{n+i} &= c_j\Big).
  \end{aligned}
  $$

---

# IDD - ekvivalentna oblika

Ekvivalentno: potem sta $x$ in $y$ optimalni rešitvi za $\Pi$ oziroma $\Pi'$ natanko tedaj, ko velja
$$
\begin{aligned}
\forall i &\in \{1, \dots, m\}: & \Big(\sum_{j=1}^n a_{ij} x_j &< b_i &&\Rightarrow& y_{n+i} &= 0\Big) \quad \text{in} \\
\forall j &\in \{1, \dots, n\}: & \Big(x_j &> 0 &&\Rightarrow& \sum_{i=1}^m a_{ij} y_{n+i} &= c_j\Big).
\end{aligned}
$$

---

# Dokaz IDD

$$
L = \sum_{j=1}^n c_j x_j \le \sum_{j=1}^n \left(\sum_{i=1}^m a_{ij} y_{n+i}\right) x_j = \sum_{i=1}^m \left(\sum_{j=1}^n a_{ij} x_j\right) y_{n+i} \le \sum_{i=1}^m b_i y_{n+i} = D
$$

* Po Posledici 1 in KID sta $x, y$ optimalni za $\Pi, \Pi'$ natanko tedaj, ko velja $L = D$, kar je enakovredno
  $$
  \begin{aligned}
  \forall j: c_j x_j = \left(\sum_{i=1}^m a_{ij} y_{n+i}\right) x_j &\ \land \ \forall i: \left(\sum_{j=1}^n a_{ij} x_j\right) y_{n+i} = b_i y_{n+i} \\
  \Leftrightarrow \quad
  \forall j: \left(c_j - \sum_{i=1}^m a_{ij} y_{n+i}\right) x_j = 0  &\ \land \ \forall i: \left(b_i - \sum_{j=1}^n a_{ij} x_j\right) y_{n+i} = 0
  \end{aligned}
  $$

---

# Primer

Pokaži, da je $x = (0, 50, 0)$ optimalna rešitev problema kmetije.

* 1\. korak: preverimo, da je ponujena rešitev dopustna.
  $$
  \begin{aligned}
  0 + 50 + 0 &= 50 \\
  3 \cdot 0 + 4 \cdot 50 + 5 \cdot 0 &< 250 \\
  3 \cdot 0 + 5 \cdot 50 + 4 \cdot 0 &< 300
  \end{aligned}
  $$

* 2\. korak: za vsako neenakost, ki je izpolnjena z $<$, pripadajoči dualni spremenljivki dodelimo vrednost $0$.
  $$
  y_5 = y_6 = 0
  $$

---

# Primer (2)

* 3\. korak: za vsako pozitivno vrednost v rešitvi postavimo enačaj v pripadajoči neenakosti.
  $$
  y_4 + 4 y_5 + 5 y_6 = 15
  $$

* 4\. korak: rešimo sistem iz korakov 2 in 3 ter preverimo dopustnost rešitve.
  - Če je rešitev več (parametrična rešitev), zadostuje, da poiščemo tako vrednost parametrov, da bo dobljena rešitev dopustna.
  $$
  \begin{aligned}
  y_4 = 15 \qquad y_5 &= 0 \qquad y_6 = 0 \\[1ex]
  15 + 3 \cdot 0 + 3 \cdot 0 &\ge 10 \\
  15 + 5 \cdot 0 + 4 \cdot 0 &\ge 12
  \end{aligned}
  $$

---

# Ekonomski pomen dualnih spremenljivk

* **_Primer._** Problem kmetije:
  $$
  \begin{aligned}
  x_1^\ast = 0 \qquad x_2^\ast = 50 \qquad x_3^\ast &= 0 \\[1ex]
  z^\ast = 10 \cdot 0 + 15 \cdot 50 + 12 \cdot 0 &= 750 & \text{(zaslužek v 40 €)} \\[1ex]
  0 + 50 + 0 &= 50 & \text{(zemlja v ha)} \\
  3 \cdot 0 + 4 \cdot 50 + 5 \cdot 0 &< 250 & \text{(delovna sila v 20 človek-urah)} \\
  3 \cdot 0 + 5 \cdot 50 + 4 \cdot 0 &< 300 & \text{(kapital v 80 €)}
  \end{aligned}
  $$
* Ne izplača se nam najeti več delovne sile ali vzeti kredita. Morda se nam izplača dokupiti dodatno zemljo.
  $$
  y_4^\ast = 15 \qquad y_5^\ast = 0 \qquad y_6^\ast = 0
  $$

---

# Ekonomski pomen dualnih spremenljivk (2)

<span class="small">

* **_Izrek._** Naj bo $\Pi$ prvotni linearni program kot zgoraj z neizrojeno bazno optimalno rešitvijo (tj., v pripadajočem slovarju so vsi konstantni členi pri baznih spremenljivkah pozitivni), in $\Pi'$ njegov dual. Potem obstaja $\epsilon > 0$, da velja
  $$
  |\Delta b| < \epsilon \ \Rightarrow \ \Delta z^\ast = \sum_{i=1}^m y_{n+i}^\ast \Delta b_i,
  $$
  kjer je $y^\ast$ optimalna rešitev $\Pi'$ ter sta $\Delta b$ in $\Delta z^\ast$ spremembi desne strani in optimalne vrednosti.

* V našem primeru: $\Delta z^\ast = 15 \, \Delta b_1$ za $|\Delta b| < \epsilon$. Zemljo se nam splača kupiti po ceni največ $15 \cdot 40$ €/ha = $600$ €/ha.

* Torej: optimalne vrednosti duala nam dajo "tržno"/"pošteno"/sprejemljivo ceno surovin.

</span>

---

# Dual splošnega linearnega programa

**_Izrek._** Naj bo $\Pi$ linearni program v spodnji obliki. Potem je njegov dual $\Pi'$:

<span class="columns col2">

<span>

$$
\begin{aligned}
\max \ \sum_{j=1}^n c_j x_j \\[1ex]
\text{p.p.} \quad \sum_{j=1}^n a_{ij} x_j &\le b_i & (1 &\le i \le m') \\
\sum_{j=1}^n a_{ij} x_j &= b_i & (m'+1 &\le i \le m) \\
x_j &\ge 0 & (1 &\le j \le n')
\end{aligned}
$$

</span>

<span>

$$
\begin{aligned}
\min \ \sum_{i=1}^m b_i y_{n+i} \\[1ex]
\text{p.p.} \quad \sum_{i=1}^m a_{ij} y_{n+i} &\ge c_j & (1 &\le j \le n') \\
\sum_{i=1}^m a_{ij} y_{n+i} &= c_j & (n'+1 &\le j \le n) \\
y_{n+i} &\ge 0 & (1 &\le i \le m')
\end{aligned}$$

</span>

</span>

---

# IDD za splošni linearni program

* Naj bosta $x$ in $y$ dopustni rešitvi za $\Pi$ oziroma $\Pi'$.
* Potem sta $x$ in $y$ optimalni rešitvi za $\Pi$ oziroma $\Pi'$ natanko tedaj, ko velja
  $$
  \begin{aligned}
  \forall i &\in \{1, \dots, m'\}: & \Big(\sum_{j=1}^n a_{ij} x_j &= b_i &&\lor& y_{n+i} &= 0\Big) \quad \text{in} \\
  \forall j &\in \{1, \dots, n'\}: & \Big(x_j &= 0 &&\lor& \sum_{i=1}^m a_{ij} y_{n+i} &= c_j\Big).
  \end{aligned}
  $$

* Torej:
  - neenakost $\le \quad \leftrightarrow \quad$ nenegativna spremenljivka
  - enakost $\quad \leftrightarrow \quad$ neomejena spremenljivka

---

# Primer

<span class="columns col2">

<span>

$$
\begin{aligned}
\Pi: \\[1ex]
\max \ 3 x_1 - 2 x_2 \\[1ex]
\text{p.p.} \quad x_1 + 4 x_2 &\le 5 \\
3 x_1 + x_2 &= 4 \\
x_1 &\ge 0
\end{aligned}
$$

</span>

<span>

$$
\begin{aligned}
\Pi': \\[1ex]
\min \ 5 y_3 + 4 y_4 \\[1ex]
\text{p.p.} \quad y_3 + 3 y_4 &\ge 3 \\
4 y_3 + y_4 &= -2 \\
y_3 &\ge 0
\end{aligned}$$

</span>

</span>

---

# Splošni LP v standardni obliki

$$
\begin{aligned}
\max \ \sum_{j=1}^{n'} c_j x_j + \sum_{j=n'+1}^n c_j x^+_j - \sum_{j=n'+1}^n c_j x^-_j \\
\text{p.p.} \quad \sum_{j=1}^{n'} a_{ij} x_j + \sum_{j=n'+1}^n a_{ij} x^+_j - \sum_{j=n'+1}^n a_{ij} x^-_j &\le b_i & (1 &\le i \le m') \\[-2ex]
\sum_{j=1}^{n'} a_{ij} x_j + \sum_{j=n'+1}^n a_{ij} x^+_j - \sum_{j=n'+1}^n a_{ij} x^-_j &\le b_i & (m'+1 &\le i \le m) \\[-2ex]
-\sum_{j=1}^{n'} a_{ij} x_j - \sum_{j=n'+1}^n a_{ij} x^+_j + \sum_{j=n'+1}^n a_{ij} x^-_j &\le -b_i & (m'+1 &\le i \le m) \\[-2ex]
x_j &\ge 0 & (1 &\le j \le n') \\[-1ex]
x^+_j, x^-_j &\ge 0 & (n'+1 &\le j \le n)
\end{aligned}
$$

---

# Dual splošnega linearnega programa - dokaz

Zapišimo še dual - ta je enakovreden našemu zapisu $\Pi'$:
$$
\begin{aligned}
\min \ \sum_{i=1}^{m'} b_i y_{n+i} + \sum_{i=m'+1}^m b_i y^+_{n+i} - \sum_{i=m'+1}^m b_i y^-_{n+i} \\
\text{p.p.} \quad \sum_{i=1}^{m'} a_{ij} y_{n+i} + \sum_{i=m'+1}^m a_{ij} y^+_{n+i} - \sum_{i=m'+1}^m a_{ij} y^-_{n+i} &\ge c_j & (1 &\le j \le n') \\[-2ex]
\sum_{i=1}^{m'} a_{ij} y_{n+i} + \sum_{i=m'+1}^m a_{ij} y^+_{n+i} - \sum_{i=m'+1}^m a_{ij} y^-_{n+i} &\ge c_j & (n'+1 &\le j \le n) \\[-2ex]
-\sum_{i=1}^{m'} a_{ij} y_{n+i} - \sum_{i=m'+1}^m a_{ij} y^+_{n+i} + \sum_{i=m'+1}^m a_{ij} y^-_{n+i} &\ge -c_j & (n'+1 &\le j \le n) \\[-2ex]
y_{n+i} &\ge 0 & (1 &\le i \le m') \\[-2ex]
y^+_{n+i}, y^-_{n+i} &\ge 0 & (m'+1 &\le i \le m)
\end{aligned}
$$