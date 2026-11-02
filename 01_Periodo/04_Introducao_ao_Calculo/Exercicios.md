# Exercícios — Introdução ao Cálculo

> Lista autoral por tópico, com foco nas ferramentas usadas depois em Circuitos e Telecom (decibéis, trigonometria e números complexos).

---

## 1. Inequações e módulo

**1.1** Resolva $|2x - 3| \le 5$.

<details><summary>Gabarito</summary>

$-5 \le 2x - 3 \le 5 \Rightarrow -1 \le x \le 4$, ou seja, $x \in [-1, 4]$.

</details>

**1.2** Resolva $\dfrac{x - 1}{x + 2} > 0$.

<details><summary>Gabarito</summary>

Estudo de sinal: numerador zera em 1, denominador em −2. Positivo para $x < -2$ ou $x > 1$.

</details>

---

## 2. Funções

**2.1** Para $f(x) = x^2 - 4x + 3$, encontre raízes, vértice e o conjunto imagem.

<details><summary>Gabarito</summary>

Raízes 1 e 3; vértice $(2, -1)$; imagem $[-1, +\infty)$.

</details>

**2.2** Encontre a inversa de $f(x) = \dfrac{2x+1}{x-3}$ e seu domínio.

<details><summary>Gabarito</summary>

$y(x-3) = 2x+1 \Rightarrow x(y-2) = 3y+1$ → $f^{-1}(x) = \dfrac{3x+1}{x-2}$, $x \ne 2$.

</details>

**2.3** Com $f(x) = \sqrt x$ e $g(x) = x^2 + 1$, calcule $f\circ g$ e $g\circ f$, com seus domínios.

<details><summary>Gabarito</summary>

$(f\circ g)(x) = \sqrt{x^2+1}$, domínio $\mathbb R$. $(g\circ f)(x) = x + 1$, domínio $x \ge 0$.

</details>

**2.4** A tarifa de energia de uma residência é R\$ 0,85/kWh mais uma taxa fixa de R\$ 15,00. Escreva a função custo $C(E)$ e calcule o consumo que gera uma conta de R\$ 270,00.

<details><summary>Gabarito</summary>

$C(E) = 0{,}85E + 15$ → $270 = 0{,}85E + 15 \Rightarrow E = 300\ \text{kWh}$.

</details>

---

## 3. Exponencial, logaritmo e decibéis

**3.1** Resolva $2^{x+1} = 32$ e $\log_2 1024$.

<details><summary>Gabarito</summary>

$2^{x+1} = 2^5 \Rightarrow x = 4$; $\log_2 1024 = 10$.

</details>

**3.2** Um sinal decai como $v(t) = V_0e^{-t/\tau}$. Em quanto tempo cai à metade?

<details><summary>Gabarito</summary>

$e^{-t/\tau} = 0{,}5 \Rightarrow t = \tau\ln 2 \approx 0{,}693\tau$.

</details>

**3.3** Converta: (a) 2 W em dBm; (b) um ganho de potência de 100× em dB; (c) uma atenuação de 3 dB em fator de potência; (d) um ganho de tensão de 10× em dB.

<details><summary>Gabarito</summary>

(a) $10\log(2000\ \text{mW}) = 33{,}0\ \text{dBm}$; (b) 20 dB; (c) ≈ 0,5 (metade da potência); (d) $20\log 10 = 20\ \text{dB}$ (tensão usa 20·log).

</details>

**3.4** Um transmissor de 30 dBm passa por um cabo com perda de 2 dB e uma antena de ganho 6 dBi. Qual a potência irradiada equivalente (EIRP) em dBm e em watts?

<details><summary>Gabarito</summary>

$30 - 2 + 6 = 34\ \text{dBm}$ → $10^{3{,}4}\ \text{mW} \approx 2{,}51\ \text{W}$. Em dB as contas viram somas!

</details>

---

## 4. Trigonometria

**4.1** Calcule $\text{sen}\,75^\circ$ usando soma de arcos.

<details><summary>Gabarito</summary>

$\text{sen}(45^\circ+30^\circ) = \dfrac{\sqrt2}{2}\cdot\dfrac{\sqrt3}{2} + \dfrac{\sqrt2}{2}\cdot\dfrac12 = \dfrac{\sqrt6+\sqrt2}{4} \approx 0{,}966$.

</details>

**4.2** A tensão da rede é $v(t) = 311\,\text{sen}(377t)$ V. Qual a frequência, o período e o valor eficaz?

<details><summary>Gabarito</summary>

$f = 377/2\pi = 60\ \text{Hz}$; $T = 16{,}7\ \text{ms}$; $V_{rms} = 311/\sqrt2 \approx 220\ \text{V}$.

</details>

**4.3** Escreva $v(t) = 3\cos\omega t + 4\,\text{sen}\,\omega t$ na forma $A\cos(\omega t - \varphi)$.

<details><summary>Gabarito</summary>

$A = \sqrt{3^2+4^2} = 5$; $\varphi = \arctan(4/3) = 53{,}1^\circ$ → $v(t) = 5\cos(\omega t - 53{,}1^\circ)$.

</details>

---

## 5. Números complexos (base para fasores)

**5.1** Com $z_1 = 3 + 4j$ e $z_2 = 1 - j$, calcule $z_1 + z_2$, $z_1z_2$, $z_1/z_2$ e $|z_1|$.

<details><summary>Gabarito</summary>

$z_1+z_2 = 4 + 3j$; $z_1z_2 = 3 - 3j + 4j - 4j^2 = 7 + j$;
$\dfrac{z_1}{z_2} = \dfrac{(3+4j)(1+j)}{2} = \dfrac{-1 + 7j}{2} = -0{,}5 + 3{,}5j$; $|z_1| = 5$, $\angle z_1 = 53{,}13^\circ$.

</details>

**5.2** Converta $10\angle30^\circ$ para a forma retangular e $-2 + 2j$ para a forma polar.

<details><summary>Gabarito</summary>

$10\angle30^\circ = 8{,}66 + 5j$; $-2+2j = 2{,}83\angle135^\circ$.

</details>

**5.3** Calcule $(1 + j)^8$ usando a forma polar (De Moivre).

<details><summary>Gabarito</summary>

$1 + j = \sqrt2\angle45^\circ$ → $(\sqrt2)^8\angle360^\circ = 16$.

</details>

**5.4** Encontre as três raízes cúbicas de 1 e relacione com o sistema trifásico.

<details><summary>Gabarito</summary>

$1\angle0^\circ$, $1\angle120^\circ$, $1\angle240^\circ$ — exatamente as defasagens entre as fases A, B e C. Note que a soma das três é zero (por isso a corrente de neutro é nula numa carga equilibrada). O operador $a = 1\angle120^\circ$ é usado em componentes simétricas.

</details>
