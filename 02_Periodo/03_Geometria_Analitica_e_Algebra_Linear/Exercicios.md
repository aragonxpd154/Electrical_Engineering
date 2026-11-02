# Exercícios — Geometria Analítica e Álgebra Linear

> Lista autoral por tópico. Listas antigas com gabarito em [`Materiais/`](Materiais/).

---

## 1. Matrizes, determinantes e sistemas lineares

**1.1** Resolva por escalonamento: $x + y + z = 6$; $2x - y + z = 3$; $x + 2y - z = 2$.

<details><summary>Gabarito</summary>

$x = 1$, $y = 2$, $z = 3$ (sistema possível e determinado).

</details>

**1.2** Calcule $\det\begin{bmatrix}2&1&3\\0&-1&4\\1&2&0\end{bmatrix}$.

<details><summary>Gabarito</summary>

$2(0 - 8) - 1(0 - 4) + 3(0 + 1) = -16 + 4 + 3 = -9$.

</details>

**1.3** Encontre a inversa de $\begin{bmatrix}4&7\\2&6\end{bmatrix}$.

<details><summary>Gabarito</summary>

$\det = 10$ → $\dfrac1{10}\begin{bmatrix}6&-7\\-2&4\end{bmatrix}$.

</details>

**1.4 (Aplicação — análise de malhas)** As equações de malha de um circuito são $10I_1 - 4I_2 = 12$ e $-4I_1 + 8I_2 = 0$. Resolva pela Regra de Cramer.

<details><summary>Gabarito</summary>

$D = 80 - 16 = 64$; $D_1 = 96$; $D_2 = 48$ → $I_1 = 1{,}5\ \text{A}$, $I_2 = 0{,}75\ \text{A}$.

</details>

**1.5** Para que valores de k o sistema $x + ky = 1$, $kx + y = 1$ é impossível?

<details><summary>Gabarito</summary>

$\det = 1 - k^2 = 0 \Rightarrow k = \pm1$. Com k = 1 as equações são idênticas (infinitas soluções); com **k = −1** fica $x - y = 1$ e $x - y = -1$ → **impossível**.

</details>

---

## 2. Vetores

**2.1** Com $\mathbf u = (1, 2, 2)$ e $\mathbf v = (3, 0, 4)$: calcule $\mathbf u\cdot\mathbf v$, o ângulo entre eles, $\mathbf u\times\mathbf v$ e a área do paralelogramo formado.

<details><summary>Gabarito</summary>

$\mathbf u\cdot\mathbf v = 11$; $\cos\theta = 11/15 \Rightarrow \theta = 42{,}8^\circ$.
$\mathbf u\times\mathbf v = (8, 2, -6)$; área $= \sqrt{104} \approx 10{,}2$.

</details>

**2.2** Calcule a projeção de $\mathbf u$ sobre $\mathbf v$ do item 2.1.

<details><summary>Gabarito</summary>

$\text{proj}_\mathbf v\mathbf u = \dfrac{\mathbf u\cdot\mathbf v}{|\mathbf v|^2}\mathbf v = \dfrac{11}{25}(3, 0, 4) = (1{,}32;\ 0;\ 1{,}76)$.

</details>

---

## 3. Retas e planos

**3.1** Encontre a equação do plano que passa por A(1,0,0), B(0,2,0) e C(0,0,3), e a distância da origem a ele.

<details><summary>Gabarito</summary>

$\dfrac x1 + \dfrac y2 + \dfrac z3 = 1 \Rightarrow 6x + 3y + 2z = 6$. Distância: $\dfrac{6}{\sqrt{36+9+4}} = \dfrac67$.

</details>

**3.2** Escreva a equação paramétrica da reta que passa por P(1, 2, 3) com direção (2, −1, 1) e verifique se Q(5, 0, 5) pertence a ela.

<details><summary>Gabarito</summary>

$(x,y,z) = (1+2t,\ 2-t,\ 3+t)$. Para t = 2: (5, 0, 5) ✔ — Q pertence à reta.

</details>

---

## 4. Espaços vetoriais

**4.1** Verifique se (1,1,0), (0,1,1) e (1,0,1) são LI e se formam base de $\mathbb R^3$.

<details><summary>Gabarito</summary>

Determinante da matriz formada = 2 ≠ 0 → LI e base de $\mathbb R^3$.

</details>

**4.2** O conjunto $W = \{(x,y,z): x + y + z = 0\}$ é subespaço de $\mathbb R^3$? Qual a dimensão e uma base?

<details><summary>Gabarito</summary>

Sim (contém o zero e é fechado para soma e produto por escalar). Dimensão 2; base: $\{(1,-1,0),\ (1,0,-1)\}$.

</details>

---

## 5. Transformações lineares, autovalores e autovetores

**5.1** Encontre autovalores e autovetores de $A = \begin{bmatrix}4&1\\2&3\end{bmatrix}$.

<details><summary>Gabarito</summary>

$\lambda^2 - 7\lambda + 10 = 0 \Rightarrow \lambda = 5, 2$. $\lambda=5$: $\mathbf v = (1,1)$; $\lambda=2$: $\mathbf v = (1,-2)$.

</details>

**5.2** A transformação $T(x,y) = (x + 2y,\ 3x - y)$ é inversível? Calcule $T^{-1}$.

<details><summary>Gabarito</summary>

$\det\begin{bmatrix}1&2\\3&-1\end{bmatrix} = -7 \ne 0$ → inversível. $T^{-1}(x,y) = \left(\dfrac{x+2y}{7},\ \dfrac{3x-y}{7}\right)$.

</details>

**5.3** Escreva a matriz de rotação de 30° no plano e aplique-a ao vetor (1, 0). Que relação isso tem com fasores?

<details><summary>Gabarito</summary>

$R = \begin{bmatrix}\cos30^\circ&-\text{sen}\,30^\circ\\\text{sen}\,30^\circ&\cos30^\circ\end{bmatrix}$ → $R(1,0) = (0{,}866;\ 0{,}5)$.
Multiplicar um fasor por $1\angle30^\circ$ é exatamente essa rotação no plano complexo.

</details>

**5.4** Na transformada de Clarke (usada em controle de motores), por que interessa diagonalizar matrizes? Dê a ideia em uma frase.

<details><summary>Gabarito</summary>

Mudar para a base de autovetores desacopla as equações — cada nova variável evolui independentemente, o que simplifica a análise (ex.: as componentes αβ/dq desacoplam as três fases).

</details>
