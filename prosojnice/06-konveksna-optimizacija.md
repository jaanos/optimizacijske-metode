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

---

# Konveksne funkcije

Konveksne funkcije so "obrnjene navzgor", npr $f(x) = x^2$.

<span class="center">

![](slike/konveksna_funkcija.png)

</span>

---

# Definicija

<span class="small">

* Naj bo $K \subseteq \mathbb{R}^n$ konveksna množica.
* Funkcija $f : K \to \mathbb{R}$ je _konveksna_, če velja

  $$
  \forall x, y \in K \ \forall \lambda \in [0, 1]: f((1 - \lambda) x + \lambda y) \le (1 - \lambda) f(x) + \lambda f(y)
  $$

  Torej: graf funkcije leži pod zveznicami točk na grafu.

* Funkcija $f : K \to \mathbb{R}$ je _konkavna_, če velja

  $$
  \forall x, y \in K \ \forall \lambda \in [0, 1]: f((1 - \lambda) x + \lambda y) \ge (1 - \lambda) f(x) + \lambda f(y)
  $$

  Torej: $f$ je konkavna $\Longleftrightarrow$ $-f$ je konveksna.

* Funkcija $f : K \to \mathbb{R}$ je _strogo konveksna_, če velja

  $$
  \forall x, y \in K \ \forall \lambda \in (0, 1): f((1 - \lambda) x + \lambda y) < (1 - \lambda) f(x) + \lambda f(y)
  $$

* Funkcija $f : K \to \mathbb{R}$ je _strogo konkavna_, če velja

  $$
  \forall x, y \in K \ \forall \lambda \in (0, 1): f((1 - \lambda) x + \lambda y) > (1 - \lambda) f(x) + \lambda f(y)
  $$

</span>

---

# Primeri

* Množica $K \subseteq \mathbb{R}$ je konveksna natanko tedaj, ko je množica $K$ interval.
* Trdimo: $f(x) = x^2$ je konveksna funkcija (za vsak interval $K$).

  $$
  \begin{aligned}
  & f((1 - \lambda) x + \lambda y) \stackrel{?}{\le} (1 - \lambda) f(x) + \lambda f(y) \\[2ex]
  & ((1 - \lambda) x + \lambda y)^2 - ((1 - \lambda) x^2 + \lambda y^2) \\
  &= (1 - \lambda)^2 x^2 + 2(1 - \lambda) \lambda xy + \lambda^2 y^2 - (1 - \lambda) x^2 - \lambda y^2 \\
  &= (1 - \lambda)(1 - \lambda - 1) x^2 + 2(1 - \lambda) \lambda xy + \lambda (\lambda - 1) y^2 \\
  &= -\lambda(1 - \lambda) (x^2 - 2xy + y^2) = -\lambda(1 - \lambda) (x - y)^2 \le 0
  \end{aligned}
  $$

---

# Primeri (2)

* _Afina funkcija_ $f(x_1, x_2, \dots, x_n) = a_1 x_1 + a_2 x_2 + \dots + a_n x_n + b$ (ali $f(x) = a^\top x + b$) je konveksna:

  $$
  \begin{aligned}
  f((1 - \lambda) x + \lambda y)
  &= a^\top ((1 - \lambda) x + \lambda y) + b \\
  &= (1 - \lambda) a^\top x + \lambda a^\top y + (1 - \lambda) b + \lambda b \\
  &= (1 - \lambda) f(x) + \lambda f(y)
  \end{aligned}
  $$

* Funkcija $f$ je tudi konkavna.
* Da se dokazati, da je funkcija konveksna in konkavna natanko tedaj, ko je afina.

---

# Primeri (3)

* _Norma_ $\Vert \cdot \Vert : \mathbb{R}^n \to \mathbb{R}$ je funkcija s sledečimi lastnostmi:
   - $\Vert x \Vert \ge 0$, $\Vert x \Vert = 0 \Rightarrow x = 0$
   - $\Vert \lambda x \Vert = \vert \lambda \vert \Vert x \Vert$
   - $\Vert x + y \Vert \le \Vert x \Vert + \Vert y \Vert$ (_trikotniška neenakost_)

* Primer: dolžina vektorja $\Vert x \Vert = \sqrt{x^\top x} = \sqrt{x_1^2 + x_2^2 + \dots + x_n^2}$

* Norma je konveksna:

  $$
  \Vert (1 - \lambda) x + \lambda y \Vert \le \Vert (1 - \lambda) x \Vert + \Vert \lambda y \Vert = (1 - \lambda) \Vert x \Vert + \lambda \Vert y \Vert
  $$

---

# Lastnosti konveksnih funkcij

<span class="small numbers">

* **_Trditev._** Naj bo $K \subseteq \mathbb{R}^n$ konveksna množica ter $f, g: K \to \mathbb{R}$ konveksni funkciji. Potem velja sledeče.

  1. Če $c \ge 0$, potem je $c \cdot f$ konveksna funkcija.
  2. Funkcija $f + g$ je konveksna.
  3. Če je funkcija $f$ afina, je slika $f(K)$ konveksna množica.

* **_Trditev._** Naj bo $K \subseteq \mathbb{R}^n$ konveksna množica ter $f: K \to \mathbb{R}$ in $g: \operatorname{conv}(f(K)) \to \mathbb{R}$ konveksni funkciji. Denimo, da velja vsaj eno od sledečega.

  - Funkcija $f$ je afina, ali
  - funkcija $g$ je naraščajoča.

  Potem je kompozitum $g \circ f$ konveksna funkcija.

</span>

---

# Dokaz

* 1\.

  $$
  (c \cdot f)((1 - \lambda) x + \lambda y) \le c ((1 - \lambda) f(x) + \lambda f(y)) = ((1 - \lambda) (c \cdot f)(x) + \lambda (c \cdot f)(y))
  $$

* 2\.

  $$
  \begin{aligned}
  (f + g)((1 - \lambda) x + \lambda y)
  &= f((1 - \lambda) x + \lambda y) + g((1 - \lambda) x + \lambda y) \\
  &\le (1 - \lambda) f(x) + \lambda f(y) + (1 - \lambda) g(x) + \lambda g(y) \\
  &= (1 - \lambda) (f + g)(x) + \lambda (f + g)(y)
  \end{aligned}
  $$

* 3\. Funkcija $f(x) = a^\top x + b$ je konveksna in konkavna, za $x, y \in K$ velja $f(x), f(y) \in f(K)$. Ker je $(1 - \lambda) x + \lambda y \in K$, velja

  $$
  (1 - \lambda) f(x) + \lambda f(y) = f((1 - \lambda) x + \lambda y) \in f(K).
  $$

---

# Dokaz (2)

* Trdimo, da velja

  $$
  \begin{aligned}
  f((1 - \lambda) x + \lambda y) &\le (1 - \lambda) f(x) + \lambda f(y) \\
  g(f((1 - \lambda) x + \lambda y)) &\le g((1 - \lambda) f(x) + \lambda f(y)) \\
  &\le (1 - \lambda) (g \circ f)(x) + \lambda (g \circ f)(y)
  \end{aligned}
  $$

* Prva neenakost velja zaradi konveksnosti funkcije $f$.
* Če je funkcija $g$ naraščajoča, potem velja tudi druga neenakost.
* Če pa je funkcija $f$ afina, velja enakost v prvi in posledično tudi v drugi neenakosti.
* V obeh primerih zadnja neenakost sledi zaradi konveksnosti funkcije $g$.

---

# Neprimeri

* Produkt konveksnih funkcij ni nujno konveksna funkcija: $f(x) = x$, $g(x) = -x$, $(f \cdot g)(x) = -x^2$.
* Kompozitum konveksnih funkcij ni nujno konveksna funkcija: $f(x) = x^2$, $g(x) = -x$, $(g \circ f)(x) = -x^2$.
* Slika konveksne množice s konveksno funkcijo ni nujno konveksna množica:

  $$
  \begin{aligned}
  f:&\ [0, 1] \to \mathbb{R} \\
  f(x) &= \begin{cases}
  0 & \text{če } 0 \le x < 1 \\
  1 & \text{če } x = 1
  \end{cases} \\
  f([0, 1]) &= \lbrace 0, 1 \rbrace
  \end{aligned}
  $$

---

# Konveksne funkcije in optimizacija

* **_Definicija._** Naj bo $A \subseteq \mathbb{R}^n$ in $f: A \to \mathbb{R}$. Funkcija $f$ ima v točki $x^\ast \in A$:

  * _globalni maksimum_, če $\forall x \in A: f(x) \le f(x^\ast)$;
  * _globalni minimum_, če $\forall x \in A: f(x) \ge f(x^\ast)$;
  * _lokalni maksimum_, če $\exists \epsilon > 0 \ \forall x \in A: (\Vert x - x^\ast \Vert < \epsilon \Rightarrow f(x) \le f(x^\ast))$; in
  * _lokalni minimum_, če $\exists \epsilon > 0 \ \forall x \in A: (\Vert x - x^\ast \Vert < \epsilon \Rightarrow f(x) \ge f(x^\ast))$.

* **_Trditev._** Naj bo $K \subseteq \mathbb{R}^n$ konveksna množica ter $f: K \to \mathbb{R}$ konveksna funkcija. Če ima $f$ v $x^\ast \in K$ lokalni minimum, ima v $x^\ast$ tudi globalni minimum.

---

# Dokaz

* Naj bo $\epsilon > 0$ tak, da velja $\forall x \in K: (\Vert x - x^\ast \Vert < \epsilon \Rightarrow f(x) \ge f(x^\ast))$.
* Če $x^\ast$ ni globalni minimum, potem obstaja tak $y \in K$, da velja $f(y) < f(x^\ast)$.
* Tedaj za vsak $\lambda \in (0, 1]$ velja

  $$
  f((1 - \lambda) x^\ast + \lambda y) \le (1 - \lambda) f(x^\ast) + \lambda f(y) < (1 - \lambda) f(x^\ast) + \lambda f(x^\ast) = f(x^\ast) .
  $$

* Za dovolj majhen $\lambda$ je $(1 - \lambda) x^\ast + \lambda y$ poljubno blizu $x^\ast$:

  $$
  \Vert (1 - \lambda) x^\ast + \lambda y - x^\ast \Vert = \Vert \lambda (y - x^\ast) \Vert = \lambda \Vert y - x^\ast \Vert < \epsilon, \text{ če } \lambda < {\epsilon \over \Vert y - x^\ast \Vert}
  $$

* Torej: če je $\lambda \in \left(0, {\epsilon \over \Vert y - x^\ast \Vert}\right)$, je $\Vert (1 - \lambda) x^\ast + \lambda y - x^\ast \Vert < \epsilon$ in tedaj $f((1 - \lambda) x^\ast + \lambda y) \ge f(x^\ast)$, protislovje.

---

# Odvodi

* Preverjanje konveksnosti po definiciji je v splošnem težko. Večinoma je lažje preverjati konveksnost z odvodi.

* Naj bo $f: (a, b) \to \mathbb{R}$ konveksna funkcija. Njen graf potem leži nad vsako tangento (**kriterij 1. odvoda**), torej
$f(y) \ge f(x) + (y-x) f'(x)$ za vsaka $x, y \in (a, b)$.

* **_Primer._** Naj bo $f(x) = x^2$. Preverimo, ali za vsaka $x, y \in \mathbb{R}$ velja

  $$
  y^2 \stackrel{?}{\ge} x^2 + (y-x) \cdot 2x .
  $$

  * Res:

    $$
    y^2 - x^2 - 2xy + 2x^2 = y^2 - 2xy + x^2 = (x-y)^2 \ge 0.
    $$

---

# Odvodi (2)

* Smerni koeficienti tangent na graf konveksne funkcije $f$ naraščajo - njen odvod $f'$ je torej naraščajoča funkcija, torej $f''(x) \ge 0$ za vsak $x \in (a, b)$ (**kriterij 2. odvoda**).

* **_Primer._** Naj bo $f(x) = x^2$. Potem je $f''(x) = 2 \ge 0$.

---

# Kriterij 1. odvoda

* Naj bo $K \subseteq \mathbb{R}^n$ odprta konveksna množica, ter $f: K \to \mathbb{R}$ funkcija, ki ima vse parcialne odvode ${\partial f \over \partial x_i}$ ($1 \le i \le n$).
  - Parcialne odvode zapišemo v _gradient_ $\nabla f(x) = \left({\partial f \over \partial x_i}(x)\right)_{i=1}^n$.
* Potem je funkcija $f$ konveksna natanko tedaj, ko za vsaka $x, y \in K$ velja $f(y) \ge f(x) + (\nabla f(x))^\top (y - x)$.

---

# Dokaz ($\Longleftarrow$)

* Naj bodo $x, y \in K$ in $\lambda \in [0, 1]$ poljubni ter pišimo $z := (1 - \lambda) x + \lambda y$.
* Potem velja:

  $$
  \begin{aligned}
  f(x) &\ge f(z) + (\nabla f(z))^\top (x - z) &&/ \cdot (1 - \lambda) \\
  f(y) &\ge f(z) + (\nabla f(z))^\top (y - z) &&/ \cdot \lambda \\
  \hline
  (1 - \lambda) f(x) + \lambda f(y) &\ge f(z) + (\nabla f(z))^\top ((1 - \lambda) x + \lambda y - z) \\
  &= f((1 - \lambda) x + \lambda y)
  \end{aligned}
  $$

* Funkcija $f$ je torej konveksna.

---

# Dokaz ($\Longrightarrow$)

* Za fiksna $x, y \in K$ je $g_{x, y}(\lambda) = f((1 - \lambda) x + \lambda y)$ funkcija v $\lambda$ - zanima nas njen odvod pri $\lambda = 0$.
*  Funkcija $g_{x, y}$ je definirana na $(-\epsilon, 1]$ za nek $\epsilon > 0$.
*  Naj bo $\delta > 0$ tak, da je množica $K(x, \delta) = \lbrace y \in \mathbb{R}^n \mid \Vert x - y \Vert \le \delta \rbrace$ (tj., krogla s središčem v $x$ in polmerom $\delta$) vsebovana v $K$.
* Zadostuje, da za vse $\lambda \in (-\epsilon, 0]$ velja

  $$
  \Vert (1 - \lambda) x + \lambda y - x \Vert = \Vert \lambda y - \lambda x \Vert = \vert \lambda \vert \Vert y - x \Vert < \delta.
  $$

* Vzamemo lahko torej $\epsilon := {\delta \over \Vert y - x \Vert}$.

---

# Dokaz ($\Longrightarrow$, 2)

* Izračunajmo $g'_{x, y}(\lambda)$.

  $$
  \begin{aligned}
  g'_{x, y}(\lambda)
  &= {d \over d \lambda} f((1 - \lambda) x + \lambda y) \\
  &= {d \over d \lambda} f((1 - \lambda) x_1 + \lambda y_1, \dots, (1 - \lambda) x_n + \lambda y_n) \\
  &= {\partial f \over \partial x_1}((1 - \lambda) x + \lambda y) \cdot (y_1 - x_1) + \dots + {\partial f \over \partial x_n}((1 - \lambda) x + \lambda y) \cdot (y_n - x_n) \\
  &= (\nabla f((1 - \lambda) x + \lambda y))^\top (y - x)
  \end{aligned}
  $$

* Velja torej $g'_{x, y}(0) = (\nabla f(x))^\top (y - x)$.

---

# Dokaz ($\Longrightarrow$, 3)

* Po definiciji odvoda nadalje velja

  $$
  \begin{aligned}
  g'_{x, y}(0)
  &= \lim_{\lambda \to 0} {g_{x, y}(\lambda) - g_{x, y}(0) \over \lambda} \\
  &= \lim_{\lambda \to 0} {f((1 - \lambda) x + \lambda y) - f(x) \over \lambda} \\
  &= \lim_{\lambda \searrow 0} {f((1 - \lambda) x + \lambda y) - f(x) \over \lambda} \\ 
  &\le \lim_{\lambda \searrow 0} {(1 - \lambda) f(x) + \lambda f(y) - f(x) \over \lambda} & \text{(ker $\lambda > 0$)} \\
  &= f(y) - f(x).
  \end{aligned}
  $$

* Velja torej $f(y) \ge f(x) + (\nabla f(x))^\top (y - x)$.

---

# Kriterij 2. odvoda za funkcije ene spremenljivke

<span class="small">

* Naj bo $f: (a, b) \to \mathbb{R}$ dvakrat odvedljiva funkcija.
* Potem je funkcija $f$ konveksna natanko tedaj, ko za vsak $x \in (a, b)$ velja $f''(x) \ge 0$.

* _Dokaz ($\Longrightarrow$)._ Naj bo $x \in (a, b)$ in $h > 0$ tak, da $x \pm h \in (a, b)$.
  * Zaradi konveksnosti funkcije $f$ potem velja:

    $$
    f(x) = f\left({1 \over 2} (x + h) + {1 \over 2} (x - h)\right) \le {1 \over 2} f(x + h) + {1 \over 2} f(x - h)
    $$

  * Z dvakratno uporabo L'Hôpitalovega pravila potem izpeljemo

    $$
    \begin{aligned}
    0 \le \lim_{h \to 0} {f(x + h) + f(x - h) - 2f(x) \over h^2} &= \lim_{h \to 0} {f'(x + h) - f'(x - h) \over 2h} \\
    &= \lim_{h \to 0} {f''(x + h) + f''(x - h) \over 2} = f''(x).
    \end{aligned}
    $$

</span>

---

# Dokaz ($\Longleftarrow$)

* Naj bosta $x, y \in (a, b)$ (brez škode za splošnost privzamemo $x < y$) ter $\lambda \in (0, 1)$. Postavimo $z = (1 - \lambda) x + \lambda y \in (x, y)$.
* Po Lagrangeevem izreku velja

  $$
  \begin{aligned}
  \exists \xi_1 &\in (x, z): & {f(z) - f(x) \over z - x} &= f'(\xi_1) \\
  \exists \xi_2 &\in (z, y): & {f(y) - f(z) \over y - z} &= f'(\xi_2) \\
  \exists \xi_3 &\in (\xi_1, \xi_2): & {f'(\xi_2) - f'(\xi_1) \over \xi_2 - \xi_1} &= f''(\xi_3)
  \end{aligned}
  $$

---

# Dokaz ($\Longleftarrow$, 2)

* Ker velja $f''(\xi_3) \ge 0$ in $\xi_1 < \xi_2$, sledi $f'(\xi_1) \le f'(\xi_2)$ (tj., funkcija $f'$ narašča, ker je njen odvod nenegativen).
* Velja torej:

  $$
  \begin{aligned}
  {f(z) - f(x) \over z - x} &\le {f(y) - f(z) \over y - z} & / \cdot (z - x)(y - z) \\
  (y - z)(f(z) - f(x)) &\le (z - x)(f(y) - f(z)) \\
  (y - z + z - x) f(z) &\le (y - z) f(x) + (z - x) f(y) \\
  (y - x) f(z) &\le (1 - \lambda)(y - x) f(x) + \lambda (y - x) f(y) \\
  f((1 - \lambda) x + \lambda y) &\le (1 - \lambda) f(x) + \lambda f(y)
  \end{aligned}
  $$

---

# Lastni vektorji in vrednosti

* Pri Algebri 1 se naučite: $x \in \mathbb{C}^n \setminus \lbrace 0 \rbrace$ je _lastni vektor_ matrike $A \in \mathbb{R}^{n \times n}$, če obstaja _lastna vrednost_ $\lambda \in \mathbb{C}$, da velja $Ax = \lambda x$.
* Matrika $A$ je _diagonalizabilna_, če obstaja $n$ linearno neodvisnih lastnih vektorjev.

* **_Primer._** Matrika $A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ ni diagonalizabilna:

  $$
  \begin{gathered}
  \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}
  \begin{bmatrix} x \\ y \end{bmatrix} =
  \begin{bmatrix} y \\ 0 \end{bmatrix} =
  \lambda \begin{bmatrix} x \\ y \end{bmatrix} \\
  \begin{aligned}
  \lambda &= 0: & y &= 0, & x &\ne 0 \\
  \lambda &\ne 0: & y &= 0, & x &= 0 & \text{ni lastni vektor}
  \end{aligned}
  \end{gathered}
  $$

  - Imamo torej samo en linearno neodvisen lastni vektor.

---

# Diagonalizacija

* Lastne vrednosti poiščemo kot ničle karakterističnega polinoma $\det(A - \lambda I)$. Lastni vektorji so neničelne rešitve enačbe $(A - \lambda I) x = 0$ za lastne vrednosti $\lambda$.

* Realna matrika ima lahko kompleksne lastne vrednosti in lastne vektorje:

  $$
  A = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix} \qquad
  \begin{vmatrix} -\lambda & 1 \\ -1 & -\lambda \end{vmatrix} = \lambda^2 + 1, \quad
  \lambda = \pm i
  $$

* Če je $A$ diagonalizabilna matrika, jo lahko zapišemo kot $A = PDP^{-1}$, kjer je $P$ obrnljiva matrika, katere stolpci so linearno neodvisni lastni vektorji, $D$ pa diagonalna matrika z ustreznimi lastnimi vrednostmi na diagonali.

---

# Simetrične matrike


* **_Definicija._** Matrika $A \in \mathbb{R}^{n \times n}$ je _simetrična_, če velja $A^\top = A$.

* **_Izrek._** Simetrična matrika $A \in \mathbb{R}^{n \times n}$ ima realne lastne vrednosti in je diagonalizabilna v ortonormirani bazi (tj., lastni vektorji imajo normo $1$ in so drug na drugega pravokotni).
  - Tedaj lahko pišemo $A = UDU^\top$, kjer je $U$ ortogonalna matrika (tj., $U^\top U = I$ oziroma $U^{-1} = U^\top$) z lastnimi vektorji v stolpcih.

---

# Definitnost

**_Definicija._** Naj bo $A \in \mathbb{R}^{n \times n}$ simetrična matrika.

* $A$ je _pozitivno semidefinitna_ ($A \ge 0$), če ima same nenegativne lastne vrednosti.
* $A$ je _pozitivno definitna_ ($A > 0$), če ima same pozitivne lastne vrednosti.
* $A$ je _negativno semidefinitna_ ($A \le 0$), če ima same nepozitivne lastne vrednosti.
* $A$ je _negativno definitna_ ($A < 0$), če ima same negativne lastne vrednosti.
* $A$ je _nedefinitna_, če ima tako pozitivne kot negativne lastne vrednosti.

---

# Kvadratne forme

<span class="small">

* **_Definicija._** Naj bo $A = (a_{ij})_{i,j=1}^n \in \mathbb{R}^{n \times n}$ simetrična matrika. _Kvadratna forma_, ki pripada $A$, je

  $$
  f(x) = x^\top A x = [x_1 \ x_2 \ \dots \ x_n] \begin{bmatrix}
  a_{11} x_1 + a_{12} x_2 + \dots a_{1n} x_n \\
  a_{21} x_1 + a_{22} x_2 + \dots a_{2n} x_n \\
  \vdots \\
  a_{n1} x_1 + a_{n2} x_2 + \dots a_{nn} x_n
  \end{bmatrix} = \sum_{i=1}^n \sum_{j=1}^n a_{ij} x_i x_j
  $$

* **_Primera._**

  * Kvadratna forma za matriko $A = \begin{bmatrix} 3 & 1 \\ 1 & -2 \end{bmatrix}$ je $f(x_1, x_2) = 3 x_1^2 + 2 x_1 x_2 - 2 x_2^2$.
  * Kvadratna forma $f(x_1, x_2, x_3) = 4 x_1^2 - 2 x_1 x_2 + 3 x_1 x_3 - x_2^2 + x_3^2$ ustreza matriki
    $$
    A = \begin{bmatrix} 4 & -1 & {3 \over 2} \\ -1 & -1 & 0 \\ {3 \over 2} & 0 & 1 \end{bmatrix}.
    $$

</span>

---

# Definitnost in kvadratne forme

**_Trditev._**

- $A \ge 0 \Longleftrightarrow \forall x \in \mathbb{R}^n: \ x^\top A x \ge 0$,
- $A > 0 \Longleftrightarrow \forall x \in \mathbb{R}^n \setminus \lbrace 0 \rbrace: \ x^\top A x > 0$,
- $A \le 0 \Longleftrightarrow \forall x \in \mathbb{R}^n: \ x^\top A x \le 0$,
- $A < 0 \Longleftrightarrow \forall x \in \mathbb{R}^n \setminus \lbrace 0 \rbrace: \ x^\top A x < 0$,
- $A$ je nedefinitna natanko tedaj, ko $x^\top A x$ doseže tako pozitivne kot negativne vrednosti.

---

# Dokaz

* Vzemimo $x \in \mathbb{R}^n$ in diagonalizirajmo $A = UDU^\top$.
* Če je $x = 0$, potem je $x^\top A x = 0$. Sicer pišimo $\tilde{x} = U^\top x$, posledično velja tudi $x = U \tilde{x}$.
* Potem velja

  $$
  x^\top A x = x^\top UDU^\top x = \tilde{x}^\top D \tilde{x} = \sum_{i=1}^n \lambda_i \tilde{x}_i^2.
  $$

* Matrika $A$ ima tako vse lastne vrednosti nenegativne/pozitivne/nepozitivne/negativne natanko tedaj, ko je za vsak $x \in \mathbb{R}^n \setminus \lbrace 0 \rbrace$ zgornja vrednost $\ge/>/\le/< 0$.

---

# Primer

<span class="small">

* Naj bo $A$ simetrična matrika dimenzij $2 \times 2$: $\quad A = \begin{bmatrix} a & b \\ b & c \end{bmatrix}$

* Potem velja:

  $$
  \begin{alignedat}{8}
  A \ge 0 \quad &\Leftrightarrow &\quad \lambda_1, \lambda_2 &\ge 0 \quad \Leftrightarrow &\quad \lambda_1 + \lambda_2 &\ge 0 &\quad &\Leftrightarrow &\quad \operatorname{tr} A &=&\ a + c &\ge 0 \\
  &&&& \lambda_1 \lambda_2 &\ge 0 &&& \det A &=&\ ac - b^2 &\ge 0 \\[1ex]
  A > 0 \quad &\Leftrightarrow &\quad \lambda_1, \lambda_2 &> 0 \quad \Leftrightarrow &\quad \lambda_1 + \lambda_2 &> 0 &\quad &\Leftrightarrow &&&\ a + c &> 0 &\quad &\Leftrightarrow & a &> 0 \\
  &&&& \lambda_1 \lambda_2 &> 0 &&&&& ac - b^2 &> 0 &&& ac - b^2 &> 0 \\[1ex]
  A \le 0 \quad &\Leftrightarrow &\quad \lambda_1, \lambda_2 &\le 0 \quad \Leftrightarrow &\quad \lambda_1 + \lambda_2 &\le 0 &\quad &\Leftrightarrow &&&\ a + c &\le 0 \\
  &&&& \lambda_1 \lambda_2 &\ge 0 &&&&& ac - b^2 &\ge 0 \\[1ex]
  A < 0 \quad &\Leftrightarrow &\quad \lambda_1, \lambda_2 &< 0 \quad \Leftrightarrow &\quad \lambda_1 + \lambda_2 &< 0 &\quad &\Leftrightarrow &&&\ a + c &< 0 &\quad &\Leftrightarrow & a &< 0 \\
  &&&& \lambda_1 \lambda_2 &> 0 &&&&& ac - b^2 &> 0 &&& ac - b^2 &> 0 \\[1ex]
  A \text{ nedefinitna} \quad &\Leftrightarrow &\quad \lambda_1 &> 0 \quad \Leftrightarrow &\quad \lambda_1 \lambda_2 &< 0 &\quad &\Leftrightarrow &&& ac - b^2 &< 0 \\
  && \lambda_2 &< 0
  \end{alignedat}
  $$

---

# Preverjanje definitnosti

* **_Definicija._** _Glavne poddeterminante_ matrike $A = (a_{ij})_{i,j=1}^n \in \mathbb{R}^{n \times n}$ so vrednosti $\det (a_{ij})_{i,j=1}^\ell$ ($1 \le \ell \le n$).

* **_Trditev._** Naj bo $A \in \mathbb{R}^{n \times n}$ simetrična matrika. Potem velja:

  - $A > 0$ natanko tedaj, ko so vse glavne poddeterminante pozitivne.
  - $A < 0$ natanko tedaj, ko glavne poddeterminante alternirajo med negativnimi in pozitivnimi vrednostmi.

---

# Hessejeva matrika

* **_Definicija._** Naj bo $\Omega \subseteq \mathbb{R}^n$ odprta množica in $f: \Omega \to \mathbb{R}$ funkcija, za katero obstajajo vsi drugi parcialni odvodi ${\partial^2 f \over \partial x_j \partial x_i}$ ($1 \le i, j \le n$).
* _Hessejeva matrika_ funkcije $f$ je $H_f(x) = \left({\partial^2 f \over \partial x_j \partial x_i}(x)\right)_{i,j=1}^n$.
  * Če so vsi drugi parcialni odvodi **zvezni** ($f \in \mathcal{C}^2(\Omega)$), velja $\forall i, j: {\partial^2 f \over \partial x_j \partial x_i} = {\partial^2 f \over \partial x_i \partial x_j}$, torej je $H_f(x)$ simetrična.

---

# Kriterij 2. odvoda

* Naj bo $K \subseteq \mathbb{R}^n$ odprta konveksna množica, ter $f: K \to \mathbb{R}$ funkcija iz $\mathcal{C}^2(K)$.
* Potem je funkcija $f$ konveksna natanko tedaj, ko za vsak $x \in K$ velja $H_f(x) \ge 0$.

* _Dokaz._ Trdimo, da je funkcija $f$ konveksna natanko tedaj, ko za vsaka $x, y \in K$ obstaja tak $\epsilon$, da je funkcija $h_{x,y}: (-\epsilon, 1+\epsilon) \to \mathbb{R}$, $h_{x,y}(t) = f((1 - t) x + ty)$ konveksna in $h_{x,y} \in \mathcal{C}^2(-\epsilon, 1+\epsilon)$.
  - Dokažimo najprej to trditev.

---

# Dokaz ($\Longrightarrow$)

* Ker je množica $K$ odprta, obstaja tak $\epsilon$, da je funkcija z zgornjim predpisom dobro definirana.
* Ker velja $f \in \mathcal{C}^2(K)$, velja tudi $h_{x,y} \in \mathcal{C}^2(-\epsilon, 1+\epsilon)$.
* Dokažimo še, da je $h_{x,y}$ konveksna funkcija.
* Vzemimo torej poljubne $s, t \in (-\epsilon, 1+\epsilon)$ in $\lambda \in [0, 1]$.
* Ker je $f$ konveksna, velja:

  $$
  \begin{aligned}
  f((1 - \lambda)((1 - t) x + ty) + \lambda ((1 - s) x + sy)) &\le (1 - \lambda) f((1 - t) x + ty) + \lambda f((1 - s) x + sy) \\
  f((1 - (1 - \lambda) t - \lambda s) x + ((1 - \lambda) t + \lambda s) y) &\le (1 - \lambda) f((1 - t) x + ty) + \lambda f((1 - s) x + sy) \\
  h_{x,y}((1 - \lambda) t + \lambda s) &\le (1 - \lambda) h_{x,y}(t) + \lambda h_{x,y}(s)
  \end{aligned}
  $$

---

# Dokaz ($\Longleftarrow$)

* Ker je za vsaka $x, y \in K$ funkcija $h_{x,y}$ konveksna, za vsak $\lambda \in [0, 1]$ velja:

  $$
  \begin{aligned}
  h_{x,y}(\lambda) = h_{x,y}((1 - \lambda) \cdot 0 + \lambda \cdot 1) &\le (1 - \lambda) h_{x,y}(0) + \lambda h_{x,y}(1) \\
  f((1 - \lambda) x + \lambda y) &\le (1 - \lambda) f(x) + \lambda f(y)
  \end{aligned}
  $$

* Funkcija $f$ je torej konveksna.

---

# Dokaz (nadaljevanje)

Za poljubna $x, y \in K$ lahko torej zapišemo:

$$
\begin{aligned}
h_{x,y}(t) &= f((1 - t) x + ty) \\
&= f((1 - t) x_1 + ty_1, \dots, (1 - t) x_n + ty_n) \\[2ex]
h'_{x,y}(t) &= {\partial f \over \partial x_1}((1 - t) x + ty) \cdot (y_1 - x_1) + \dots + {\partial f \over \partial x_n}((1 - t) x + ty) \cdot (y_n - x_n) \\
&= (\nabla f((1 - t) x + ty))^\top (y - x) \\[2ex]
h''_{x,y}(t) &= {\partial^2 f \over \partial x_1 \partial x_1}((1 - t) x + ty) \cdot (y_1 - x_1)(y_1 - x_1) + \dots + {\partial^2 f \over \partial x_n \partial x_1}((1 - t) x + ty) \cdot (y_n - x_n)(y_1 - x_1) \\
&+ \dots \\
&+ {\partial^2 f \over \partial x_1 \partial x_n}((1 - t) x + ty) \cdot (y_1 - x_1)(y_n - x_n) + \dots + {\partial^2 f \over \partial x_n \partial x_n}((1 - t) x + ty) \cdot (y_n - x_n)(y_n - x_n) \\
&= \sum_{i=1}^n \sum_{j=1}^n {\partial^2 f \over \partial x_j \partial x_i}((1 - t) x + ty) \cdot (y_j - x_j)(y_i - x_i) \\
&= (y - x)^\top H_f((1 - t) x + ty) (y - x)
\end{aligned}
$$

---

# Dokaz (zaključek)

* Velja torej:

  $$
  \begin{aligned}
  \forall x, y \in K \ \forall t \in [0, 1]: h''_{x,y}(t) \ge 0 &\iff
  \forall x, y \in K \ \forall t \in [0, 1]: H_f((1 - t) x + ty) \ge 0 \\
  &\iff \forall x \in K: H_f(x) \ge 0
  \end{aligned}
  $$

* **Opomba.** Taylorjev razvoj funkcije več spremenljivk lahko zapišemo kot

  $$
  f(y) = f(x) + (\nabla f(x))^\top (y - x) + {1 \over 2} (y - x)^\top H_f(x) (y - x) + \text{členi višjega reda}
  $$

  - Če je v $x$ lokalni minimum, potem velja $H_f(x) \ge 0$, $\nabla f(x) = 0$.
  - Če velja $H_f(x) > 0$ in $\nabla f(x) = 0$, potem je v $x$ lokalni minimum.

---

# Stroga konveksnost in ekstremne točke

* Iz dokazov za kriterij 2. odvoda lahko ugotovimo, da če za vsak $x \in K$ velja $H_f(x) > 0$, potem je $f$ strogo konveksna.
  - Obratno ne velja v splošnem (npr. $f(x) = x^4$).

* **_Trditev._** Naj bo $K \subseteq \mathbb{R}^n$ konveksna množica, ter $f: K \to \mathbb{R}$ strogo konveksna funkcija. Če je $x^\ast \in K$ globalni maksimum funkcije $f$, potem je $x^\ast$ ekstremna točka za $K$.

* _Dokaz._ Predpostavimo, da $x^\ast$ ni ekstremna točka, torej obstajajo $x, y \in K, \ x \ne y$ ter $\lambda \in (0, 1)$, da velja $x^\ast = (1 - \lambda) x + \lambda y$. Potem velja

  $$
  f(x^\ast) = f((1 - \lambda) x + \lambda y) < (1 - \lambda) f(x) + \lambda f(y) \le (1 - \lambda) f(x^\ast) + \lambda f(x^\ast) = f(x^\ast),
  $$

  protislovje.

---

# Neprimer

* Naj bo $K = [-1, 1] \times \mathbb{R}$ in $f: K \to \mathbb{R}$, $f(x, y) = x^2$.
* Funkcija $f$ je konveksna, saj velja $H_f(x, y) = \begin{bmatrix} 2 & 0 \\ 0 & 0 \end{bmatrix} \ge 0$ (lastni vrednosti sta $0$ in $2$).
* Funkcija $f$ ni strogo konveksna, saj za vse $\lambda \in (0, 1)$ velja

  $$
  1 = f(1, \lambda) = f((1 - \lambda) (1, 0) + \lambda (1, 1)) = (1 - \lambda) f(1, 0) + \lambda f(1, 1) = 1
  $$

* Globalni maksimumi funkcije $f$ so doseženi v točkah iz $\lbrace -1, 1 \rbrace \times \mathbb{R}$.
* Množica $K$ nima ekstremnih točk.
