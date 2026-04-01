---
marp: true
style: "@import url('style.css')"
plugins: mathjax
---

# Konveksna optimizacija

* **_Definicija._** Množica $A \subseteq \mathbb{R}^m$ je _konveksna_, če za vsaka $x, y \in A$ in vsak $\lambda \in [0, 1]$ velja $(1 - \lambda) x + \lambda y \in A$.

* Torej: množica $A$ je konveksna, če je vsaka daljica s krajišči v množici $A$ v celoti vsebovana v $A$.

* **_Trditev._** Presek konveksnih množic je konveksen: $A_i$ ($i \in I$) konveksne $\Rightarrow \bigcap_{i \in I} A_i$ konveksna.

* _Dokaz._ Preveriti moramo: za vsaka $x, y \in \bigcap_{i \in I} A_i$ in vsak $\lambda \in [0, 1]$ velja $\forall i \in I: (1-\lambda) x + \lambda y \in A_i$. To je res, ker so množice $A_i$ ($i \in I$) konveksne.

---

# Konveksne kombinacije

* **_Definicija._** Vektor $\lambda_1 x_1 + \lambda_2 x_2 + \dots + \lambda_n x_n$, kjer $\lambda_1, \lambda_2, \dots, \lambda_n \ge 0$, $\lambda_1 + \lambda_2 + \dots + \lambda_n = 1$, je _konveksna kombinacija_ vektorjev $x_1, x_2, \dots, x_n$.

* Za $n = 2$ pišemo $\lambda := \lambda_2$, $\lambda_1 = 1 - \lambda$, torej $\lambda_1 x_1 + \lambda_2 x_2 = (1 - \lambda) x_1 + \lambda x_2$.

* **_Trditev._** Množica $A$ je konveksna natanko tedaj, ko je v $A$ vsaka konveksna kombinacija vektorjev iz $A$.

---

# Dokaz

<span class="small">

* ($\Longleftarrow$) Očitno.
* ($\Longrightarrow$) Naj bo $x = \lambda_1 x_1 + \lambda_2 x_2 + \dots + \lambda_n x_n$ konveksna kombinacija vektorjev $x_1, x_2, \dots, x_n \in A$. Naredimo indukcijo na $n$.
  * $n = 1$: $x = 1 \cdot x_1 = x_1 \in A$.
  * $n = 2$: po definiciji.
  * $n > 2$: če $\lambda_n = 1$, potem $\lambda_1 = \lambda_2 = \dots = \lambda_{n-1} = 0$ in $x = 1 \cdot x_n = x_n \in A$. Sicer $\lambda_n < 1$ - tedaj naj bo

    $$
    y := {\lambda_1 x_1 + \lambda_2 x_2 + \dots + \lambda_{n-1} x_{n-1} \over 1 - \lambda_n} .
    $$

    * Ker je ${\lambda_1 \over 1 - \lambda_n}, {\lambda_2 \over 1 - \lambda_n}, \dots, {\lambda_{n-1} \over 1 - \lambda_n} \ge 0$ in ${\lambda_1 \over 1 - \lambda_n} + {\lambda_2 \over 1 - \lambda_n} + \dots + {\lambda_{n-1} \over 1 - \lambda_n} = 1$, je $y$ konveksna kombinacija vektorjev $x_1, x_2, \dots, x_{n-1} \in A$.
    * Po indukcijski predpostavki je $y \in A$, torej je tudi $x = (1 - \lambda_n) y + \lambda_n x_n \in A$.

</span>

---

# Konveksna ogrinjača

* **_Definicija._** Množica $\operatorname{conv}(A) := \bigcap_{\substack{K \supseteq A \\ K \text{ konveksna}}} K$ je _konveksna ogrinjača_ (ali _konveksna ovojnica_) množice $A \subseteq \mathbb{R}^m$.

* **Opomba.** Primerjaj z linearno ogrinjačo $\operatorname{Lin}(A) = \bigcap_{\substack{V \supseteq A \\ V \text{ podprostor}}} V$.

---

# Lastnosti konveksne ogrinjače

**_Trditev._** Naj bosta $A, B \subseteq \mathbb{R}^m$ množici, pri čemer je množica $B$ konveksna. Potem velja sledeče.

<span class="numbers nobullet">

* 1\. $A \subseteq \operatorname{conv}(A)$.
* 2\. $\operatorname{conv}(A)$ je konveksna množica.
* 3\. $A \subseteq B \Rightarrow \operatorname{conv}(A) \subseteq B$.
* 4\. Če je $A$ konveksna množica, potem $\operatorname{conv}(A) = A$.
* 5\.

  $$
  \begin{multlined}
  \operatorname{conv}(A) = \lbrace \lambda_1 x_1 + \lambda_2 x_2 + \dots + \lambda_n x_n \mid \\
  n \in \mathbb{N}, x_1, x_2, \dots, x_n \in A, \lambda_1, \lambda_2, \dots, \lambda_n \ge 0, \lambda_1 + \lambda_2 + \dots + \lambda_n = 1 \rbrace
  \end{multlined}
  $$

  \- tj., množica konveksnih kombinacij vektorjev iz $A$.

</span>

---

# Dokaz

<span class="numbers nobullet">

* 1\. $\operatorname{conv}(A) = \bigcap_{\substack{K \supseteq A \\ K \text{ konveksna}}} K \supseteq A$
* 2\. Presek konveksnih množic je konveksen.
* 3\. Ker je $B$ konveksna, sledi iz definicije konveksne ogrinjače.
* 4\. Po 3. je $\operatorname{conv}(A) \subseteq A \subseteq \operatorname{conv}(A)$.

</span>

---

# Dokaz (2)

<span class="small">

5\. Naj bo $C$ množica konveksnih kombinacij vektorjev iz $A$. Dokažimo $\operatorname{conv}(A) = C$.
* ($\subseteq$) Po 3. velja $\operatorname{conv}(A) \subseteq C$, saj:
  * $A = \lbrace 1 \cdot x \mid x \in A \rbrace \subseteq C$;
  * $C$ je konveksna, ker je vsaka konveksna kombinacija vektorjev $x, y \in C$

    $$
    \begin{aligned}
    z &= (1 - \lambda) x + \lambda y \\
      &= (1 - \lambda)(\mu_1 x_1 + \dots + \mu_k x_k) + \lambda (\nu_1 y_1 + \dots + \nu_\ell y_\ell) \\
      &= (1 - \lambda) \mu_1 x_1 + \dots + (1 - \lambda) \mu_k x_k + \lambda \nu_1 y_1 + \dots + \lambda \nu_\ell y_\ell
    \end{aligned}
    $$

    tudi konveksna kombinacija vektorjev $x_1, \dots, x_k, y_1, \dots, y_\ell \in A$, saj $(1-\lambda) \mu_i, \lambda \nu_j \ge 0$ ($1 \le i \le k$, $1 \le j \le \ell$) in $\sum_{i=1}^k (1 - \lambda) \mu_i + \sum_{j=1}^\ell \lambda \nu_j = (1 - \lambda) + \lambda = 1$, torej $z \in C$.
* ($\supseteq$) Ker je vsak $x \in C$ konveksna kombinacija vektorjev $x_1, x_2, \dots, x_n \in A$, za vsako konveksno množico $K \supseteq A$ velja $x_1, x_2, \dots, x_n \in K$, torej $x \in K$ in zato $x \in \operatorname{conv}(A)$. Sledi $\operatorname{conv}(A) \supseteq C$.

</span>

---

# Ekstremne točke

* **_Definicija._** Naj bo $A$ konveksna množica. Točka $a \in A$ je _ekstremna točka_, če velja $\forall x, y \in A \ \forall \lambda \in (0, 1): (a = (1 - \lambda) x + \lambda y \Rightarrow x = y = a)$ (tj., $a$ ne leži v notranjosti nobene daljice med različnima točkama iz $A$).

* **_Primer._** Ekstremne točke so prikazane z rdečo barvo.

<span class="columns col3 nobullet">

<span>

* ![h:250px](slike/ekstremne1.png)

</span>

<span>

* ![h:250px](slike/ekstremne2.png)

</span>

<span>

* ![h:250px](slike/ekstremne3.png)

  Ni ekstremnih točk!

</span>

</span>

---

# Afine množice in kombinacije

* **_Definicija._** Množica $A \ne \emptyset$ je _afina_, če velja $\forall x, y \in A \ \forall \lambda \in \mathbb{R}: (1 - \lambda) x + \lambda y \in A$ (tj., vsaka premica skozi različni točki iz $A$ je vsebovana v $A$).

* **_Definicija._** Vektor $\lambda_1 x_1 + \lambda_2 x_2 + \dots + \lambda_n x_n$, kjer je $\lambda_1 + \lambda_2 + \dots + \lambda_n = 1$, je _afina kombinacija_ vektorjev $x_1, x_2, \dots, x_n$.

---

# Lastnosti afinih množic

* **_Trditev._** Naj bo $A \subseteq \mathbb{R}^m$ neprazna množica. Sledeče trditve so ekvivalentne.

  <span class="nobullet numbers">

  * 1\. Množica $A$ je afina.
  * 2\. Vsaka afina kombinacija točk iz $A$ je v $A$.
  * 3\. $\exists v \in \mathbb{R}^m$, $\exists V \le \mathbb{R}^m$ linearen podprostor: $A = v + V = \lbrace v + x \mid x \in V \rbrace$.

  </span>

* **Opomba.** Primeri afinih množic so premica v $\mathbb{R}^m$, ravnina v $\mathbb{R}^m$, ... - rečemo jim tudi _afini podprostori_. Definiramo lahko tudi dimenzijo afinega podprostora.

---

# Dokaz (1. $\Rightarrow$ 2.)

<span class="small">

Naj bo $x = \lambda_1 x_1 + \lambda_2 x_2 + \dots + \lambda_n x_n$ afina kombinacija vektorjev $x_1, x_2, \dots, x_n \in A$. Naredimo indukcijo na $n$.
  * $n = 1$: $x = 1 \cdot x_1 = x_1 \in A$.
  * $n = 2$: po definiciji.
  * $n > 2$: brez škode za splošnost vzamemo $\lambda_n \ne 1$ - tedaj naj bo

    $$
    y := {\lambda_1 x_1 + \lambda_2 x_2 + \dots + \lambda_{n-1} x_{n-1} \over 1 - \lambda_n} .
    $$

    * Ker je ${\lambda_1 \over 1 - \lambda_n} + {\lambda_2 \over 1 - \lambda_n} + \dots + {\lambda_{n-1} \over 1 - \lambda_n} = 1$, je $y$ afina kombinacija vektorjev $x_1, x_2, \dots, x_{n-1} \in A$.
    * Po indukcijski predpostavki je $y \in A$, torej je tudi $x = (1 - \lambda_n) y + \lambda_n x_n \in A$.

</span>

---

# Dokaz (2. $\Rightarrow$ 3. $\Rightarrow$ 1.)

* (2. $\Rightarrow$ 3.) Naj bo $v \in A$ poljuben vektor. Potem je $V := A - v$ linearen podprostor, saj za vsake $x, y \in A$ ter $\mu, \nu \in \mathbb{R}$ velja
  
  $$
  \begin{aligned}
  \mu (x - v) + \nu (y - v) &= \mu x + \nu y - \mu v - \nu v \\
  &= \mu x + \nu y + (1 - \mu - \nu) v - v \in V,
  \end{aligned}
  $$

  saj $x, y, v \in A$ ter $\mu + \nu + (1 - \mu - \nu) = 1$. Velja torej $A = V + v$.

* (3. $\Rightarrow$ 1.) Poljubna vektorja iz $A$ lahko zapišemo kot $x+v$ in $y+v$, kjer $x, y \in V$. Za poljuben $\lambda \in \mathbb{R}$ velja

  $$
  (1 - \lambda) (x + v) + \lambda (y + v) = (1 - \lambda) x + \lambda y + v \in A.
  $$

---

# Konveksni stožci in Farkaseva lema

* **_Definicija._** Množica $A \subseteq \mathbb{R}^m$ je _konveksen stožec_, če velja $\forall x, y \in A \ \forall \lambda, \mu \ge 0: \lambda x + \mu y \in A$.

* **Opomba.** Če za vsaka $x, y \in A$ velja

  - $\forall \lambda, \mu: \lambda x + \mu y \in A$, potem je $A$ linearen podprostor;
  - $\forall \lambda, \mu \ge 0: \lambda x + \mu y \in A$, potem je $A$ konveksen stožec;
  - $\forall \lambda, \mu: (\lambda + \mu = 1 \Rightarrow \lambda x + \mu y \in A)$, potem je množica $A$ afina; in
  - $\forall \lambda, \mu \ge 0: (\lambda + \mu = 1 \Rightarrow \lambda x + \mu y \in A)$, potem je množica $A$ konveksna.

  Vsak konveksen stožec je konveksna množica; obratno ne velja.

---

# Konveksen stožec, napet na vektorjih

* **_Definicija._** Množica

  $$
  S(a_1, a_2, \dots, a_n) := \lbrace \lambda_1 a_1 + \lambda_2 a_2 + \dots \lambda_n a_n \mid \lambda_1, \lambda_2, \dots, \lambda_n \ge 0 \rbrace
  $$

  je _konveksen stožec, napet na vektorjih_ $a_1, a_2, \dots, a_n$.

* **_Trditev._** Množica $S(a_1, a_2, \dots, a_n)$ je konveksen stožec.

* _Dokaz._ Naj bodo $\lambda, \lambda_1, \dots, \lambda_n, \mu, \mu_1, \dots, \mu_n \ge 0$. Potem velja

  $$
  \begin{multlined}
  \lambda (\lambda_1 a_1 + \dots + \lambda_n a_n) + \mu (\mu_1 a_1 + \dots + \mu_n a_n) = \\
  (\lambda \lambda_1 + \mu \mu_1) a_1 + \dots + (\lambda \lambda_n + \mu \mu_n) a_n \in S(a_1, \dots, a_n),
  \end{multlined}
  $$

  saj $\lambda \lambda_i + \mu \mu_i \ge 0$ ($1 \le i \le n$).

---

# Primeri

<span class="columns col2">

<span>

* $S(a_1)$:
  ![h:350px](slike/stozec1.png)

</span>

<span>

* $S(a_1, a_2)$:
  ![h:350px](slike/stozec2.png)
</span>

</span>

---

# Primeri (2)

$S(a_1, a_2, a_3)$:

<span class="center">

![](slike/stozec3.png)

</span>

---

# Dualni stožec

<span class="columns col2 nobullet">

<span>

* **_Definicija._** Naj bo $A \subseteq \mathbb{R}^m$. Množici

  $$
  A^\ast := \lbrace x \in \mathbb{R}^m \mid \forall a \in A: a^\top x \ge 0 \rbrace
  $$

  (tj., množici vektorjev, ki tvorijo ostri kot z vsemi vektorji iz $A$) pravimo _dualni stožec_ množice $A$.

</span>

<span class="center">

* ![h:400px](slike/dualni_stozec.png)

</span>

</span>

---

# Lastnosti dualnega stožca

* **_Trditev._** Dualni stožec $A^\ast$ množice $A$ je konveksen stožec.

* _Dokaz._ Vzemimo poljubne $x, y \in A^\ast$ in $\lambda, \mu \ge 0$. Potem za vsak $a \in A$ velja

  $$
  a^\top (\lambda x + \mu y) = \lambda \, a^\top x + \mu \, a^\top y \ge 0,
  $$

  torej $\lambda x + \mu y \in A^\ast$.

* **_Trditev._** $A \subseteq A^{\ast\ast}$.

* **Opomba.** V splošnem ne velja $A = A^{\ast\ast}$ (npr. če $A$ ni konveksen stožec).

* _Dokaz._ Vzemimo poljuben $x \in A$. Potem za vsak $y \in A^\ast$ velja $x^\top y \ge 0$, torej velja tudi $x \in A^{\ast\ast}$.

---

# Farkaseva lema

* **_Izrek (Farkaseva lema - geometrijska oblika)._** $S^{\ast\ast}(a_1, a_2, \dots, a_n) = S(a_1, a_2, \dots, a_n)$.

* _Dokaz._

  * ($\supseteq$) Po prejšnji trditvi.
  * ($\subseteq$) Naj bo $A = [a_1 \, a_2 \, \dots \, a_n]$ matrika s stolpci $a_1, a_2, \dots, a_n$ in $b \in S^{\ast\ast}(a_1, a_2, \dots, a_n)$. Definirajmo linearni program $\Pi$ in njegov dual $\Pi'$:

    <span class="columns col2">

    <span>

    $$
    \begin{aligned}
    \Pi: \quad \max \ 0^\top x \\[1ex]
    \text{p.p.} \quad A x &= b \\
    x &\ge 0
    \end{aligned}
    $$

    </span>

    <span>

    $$
    \begin{aligned}
    \Pi': \quad \min \ b^\top y \\[1ex]
    \text{p.p.} \quad A^\top y &\ge 0 \\
    \phantom{}
    \end{aligned}
    $$

    </span>

    </span>

---

# Dokaz (2)

* Ker je $y = 0$ dopustna rešitev $\Pi'$, je ta dopusten; pokazali bomo, da je tudi omejen.
* Naj bo $y$ dopustna rešitev za $\Pi'$, torej velja $A^\top y \ge 0$ oziroma

  $$
  \forall i \in \lbrace 1, 2, \dots, n \rbrace: \ a_i^\top y \ge 0.
  $$

* Potem za poljubne $\lambda_1, \lambda_2, \dots, \lambda_n \ge 0$ velja

  $$
  (\lambda_1 a_1 + \lambda_2 a_2 + \dots + \lambda_n a_n)^\top y = \lambda_1 \, a_1^\top y + \lambda_2 \, a_2^\top y + \dots + \lambda_n \, a_n^\top y \ge 0
  $$

* Vektor $y$ torej tvori ostri kot z vsemi vektorji iz $S(a_1, a_2, \dots, a_n)$ in zato $y \in S^\ast(a_1, a_2, \dots, a_n)$.

---

# Dokaz (3)

* Ker velja $b \in S^{\ast\ast}(a_1, a_2, \dots, a_n)$, sledi $b^\top y \ge 0$, torej je $\Pi'$ omejen in zato optimalen.
* Po krepkem izreku o dualnosti je tudi $\Pi$ optimalen, torej $\exists x \ge 0: Ax = b$ oziroma

  $$
  \exists x_1, x_2, \dots, x_n \ge 0: \ x_1 a_1 + x_2 a_2 + \dots + x_n a_n = b,
  $$

  iz česar sledi $b \in S(a_1, a_2, \dots, a_n)$.

* **Opomba.** Farkasevo lemo se da dokazati tudi neposredno, krepki izrek o dualnosti sledi iz nje. Imamo torej ekvivalenco Farkas $\Leftrightarrow$ KID.

---

# Farkaseva lema - algebraična oblika


1. $\exists x \ge 0: \ Ax = b \ \Longleftrightarrow \ \forall y: \ (A^\top y \ge 0 \Rightarrow b^\top y \ge 0)$
2. $\exists x \ge 0: \ Ax \le b \ \Longleftrightarrow \ \forall y \ge 0: \ (A^\top y \ge 0 \Rightarrow b^\top y \ge 0)$
3. $\exists x: \ Ax = b \ \Longleftrightarrow \ \forall y: \ (A^\top y = 0 \Rightarrow b^\top y \ge 0)$
4. $\exists x: \ Ax \le b \ \Longleftrightarrow \ \forall y \ge 0: \ (A^\top y = 0 \Rightarrow b^\top y \ge 0)$

* _Dokaz._

  <span class="numbers">

  1\. Naj bodo $a_1, a_2, \dots, a_n$ stolpci matrike $A$. Potem je izjava ekvivalentna izjavi $b \in S(a_1, a_2, \dots, a_n) \Longleftrightarrow b \in S^{\ast\ast}(a_1, a_2, \dots, a_n)$, ki sledi iz geometrijske oblike Farkaseve leme.

  </span>

---

# Dokaz (nadaljevanje)

<span class="columns col2 numbers">

<span class="nobullet">

Obravnavamo linearna programa:

* 2\.

  <span class="columns col2">

  <span>

  $$
  \begin{aligned}
  \Pi: \quad \max \ 0^\top x \\[1ex]
  \text{p.p.} \quad A x &\le b \\
  x &\ge 0
  \end{aligned}
  $$

  </span>

  <span>

  $$
  \begin{aligned}
  \Pi': \quad \min \ b^\top y \\[1ex]
  \text{p.p.} \quad A^\top y &\ge 0 \\
  y &\ge 0
  \end{aligned}
  $$

  </span>

  </span>

* 3\.

  <span class="columns col2">

  <span>

  $$
  \begin{aligned}
  \Pi: \quad \max \ 0^\top x \\[1ex]
  \text{p.p.} \quad A x &= b
  \end{aligned}
  $$

  </span>

  <span>

  $$
  \begin{aligned}
  \Pi': \quad \min \ b^\top y \\[1ex]
  \text{p.p.} \quad A^\top y &= 0
  \end{aligned}
  $$

  </span>

  </span>

</span>

<span>

<span class="nobullet">

* 4\.

  <span class="columns col2">

  <span>

  $$
  \begin{aligned}
  \Pi: \quad \max \ 0^\top x \\[1ex]
  \text{p.p.} \quad A x &\le b \\
  \phantom{}
  \end{aligned}
  $$

  </span>

  <span>

  $$
  \begin{aligned}
  \Pi': \quad \min \ b^\top y \\[1ex]
  \text{p.p.} \quad A^\top y &= 0 \\
  y &\ge 0
  \end{aligned}
  $$

  </span>

  </span>

</span>

<span class="small">

* V vseh primerih ekvivalenco dokažemo tako:

  * ($\Longrightarrow$) Sledi iz šibkega izreka o dualnosti.
  * ($\Longleftarrow$) Dualni linearni program $\Pi'$ ima dopustno rešitev $y = 0$, po predpostavki pa je to tudi optimalna rešitev. Po krepkem izreku o dualnosti je tudi $\Pi$ optimalen, torej ima dopustno rešitev.

</span>

</span>

</span>

---

# Primeri

<span class="small">

1\. Ali obstaja nenegativna rešitev sistema linearnih enačb $Ax = b$?
* Če obstaja, jo zapišemo. Če ne obstaja, poiščemo $y$, da velja $A^\top y \ge 0$, $b^\top y < 0$.

  $$
  \begin{aligned}
  x_1 - x_2 + 2 x_3 &= 1 & / \cdot 1 \\
  -x_1 - x_2 + x_3 &= 2 & / \cdot (-1) \\ \hline
  2 x_1 + x_3 &= -1
  \end{aligned}
  $$

* Dokažimo, da zgornji sistem nima nenegativnih rešitev.

  $$
  \begin{aligned}
  A &= \begin{bmatrix}
  1 & -1 & 2 \\ -1 & -1 & 1
  \end{bmatrix}, \quad
  b = \begin{bmatrix} 1 \\ 2 \end{bmatrix}, \quad
  y = \begin{bmatrix} 1 \\ -1 \end{bmatrix} \\
  A^\top y &= \begin{bmatrix}
  1 & -1 \\ -1 & -1 \\ 2 & 1
  \end{bmatrix}
  \begin{bmatrix} 1 \\ -1 \end{bmatrix}
  = \begin{bmatrix} 2 \\ 0 \\ 1 \end{bmatrix} \ge 0, \quad
  b^\top y = -1 < 0
  \end{aligned}
  $$
   
* Ustrezen $x$ oziroma $y$ lahko poiščemo s simpleksno metodo.

</span>

---

# Primeri (2)

2\. Pokažimo, da linearni program nima dopustne rešitve.

<span class="nobullet">

* 
  $$
  \begin{aligned}
  x_1 - x_2 &\le -1 & / \cdot 1 \\
  -x_1 - x_2 &\le -3 & / \cdot 3 \\
  2 x_1 + x_2 &\le 2 & / \cdot 4 \\
  x_1, x_2 &\ge 0 \\ \hline
  6 x_1 &\le -2
  \end{aligned}
  $$

* 
  $$
  \begin{aligned}
  A &= \begin{bmatrix}
  1 & -1 \\ -1 & -1 \\ 2 & 1
  \end{bmatrix}, \quad
  b = \begin{bmatrix} -1 \\ -3 \\ 2 \end{bmatrix},  \quad
  y = \begin{bmatrix} 1 \\ 3 \\ 4 \end{bmatrix} \ge 0 \\
  A^\top y &= \begin{bmatrix} 6 \\ 0 \end{bmatrix} \ge 0, \quad
  b^\top y = -2 < 0
  \end{aligned}
  $$

</span>

---

# Primeri (3)

3\. Enakovredna izjava: $\exists x: \ Ax = b \ \Longleftrightarrow \ \forall y: \ (A^\top y = 0 \Rightarrow b^\top y = 0)$.

* Pri linearni algebri $\lnot \exists x: \ Ax = b$ dokazujemo z Gaussovo eliminacijo.

<span class="nobullet">

* 
  $$
  \begin{aligned}
  x_1 - 2 x_2 &= 3 & / \cdot 1 \\
  -x_1 + 2 x_2 &= 1 & / \cdot 1 \\ \hline
  0 &= 4
  \end{aligned}
  $$

* 
  $$
  \begin{aligned}
  A &= \begin{bmatrix}
  1 & -2 \\ -1 & 2
  \end{bmatrix}, \quad
  b = \begin{bmatrix} 3 \\ 1 \end{bmatrix}, \quad
  y = \begin{bmatrix} 1 \\ 1 \end{bmatrix} \\
  A^\top y &= \begin{bmatrix} 0 \\ 0 \end{bmatrix}, \quad
  b^\top y = 4
  \end{aligned}
  $$

</span>

---

# Opomba

<span class="columns col2">

<span>

* Ekvivalentna trditev Farkasevi lemi:

  $$
  b \not\in S(a_1, a_2, \dots, a_n) \Longleftrightarrow b \not\in S^{\ast\ast}(a_1, a_2, \dots, a_n).
  $$

* Torej ($\Longrightarrow$): če $b$ ni v konveksnem stožcu, napetem na $a_1, a_2, \dots, a_n$, potem $b$ ne tvori ostrega kota z $y \in S^\ast(a_1, a_2, \dots, a_n)$ - med $b$ in $S(a_1, a_2, \dots, a_n)$ je tako neka hiperravnina.

</span>

<span class="nobullet">

* ![](slike/farkas.png)

</span>

</span>