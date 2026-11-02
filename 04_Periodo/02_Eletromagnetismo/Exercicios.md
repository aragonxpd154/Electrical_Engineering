# Exercícios — Eletromagnetismo

> Lista autoral por tópico. Constantes: $\varepsilon_0 = 8{,}854\times10^{-12}\ \text{F/m}$, $\mu_0 = 4\pi\times10^{-7}\ \text{H/m}$, $k = 1/(4\pi\varepsilon_0) \approx 8{,}99\times10^9$, $\eta_0 \approx 377\ \Omega$.

---

## 1. Análise vetorial

**1.1** Dados $\mathbf A = 3\hat x + 4\hat y$ e $\mathbf B = \hat x - 2\hat y + 2\hat z$, calcule $\mathbf A\cdot\mathbf B$, $\mathbf A\times\mathbf B$ e o ângulo entre eles.

<details><summary>Gabarito</summary>

$\mathbf A\cdot\mathbf B = 3 - 8 + 0 = -5$; $|\mathbf A| = 5$, $|\mathbf B| = 3$ → $\cos\theta = -1/3$ → $\theta = 109{,}5^\circ$.

$\mathbf A\times\mathbf B = (4\cdot2 - 0)\hat x - (3\cdot2 - 0)\hat y + (3\cdot(-2) - 4\cdot1)\hat z = 8\hat x - 6\hat y - 10\hat z$.

</details>

**1.2** Converta o ponto P(x = 1, y = 1, z = 2) para coordenadas cilíndricas e esféricas.

<details><summary>Gabarito</summary>

Cilíndricas: $\rho = \sqrt2$, $\phi = 45^\circ$, $z = 2$.
Esféricas: $r = \sqrt6 \approx 2{,}45$, $\theta = \arccos(2/\sqrt6) = 35{,}3^\circ$, $\phi = 45^\circ$.

</details>

**1.3** Calcule o divergente e o rotacional de $\mathbf F = x^2y\,\hat x + yz\,\hat y + xz\,\hat z$.

<details><summary>Gabarito</summary>

$\nabla\cdot\mathbf F = 2xy + z + x$

$\nabla\times\mathbf F = (0 - y)\hat x + (0 - z)\hat y + (0 - x^2)\hat z = -y\,\hat x - z\,\hat y - x^2\hat z$

</details>

---

## 2. Eletrostática

**2.1** Cargas de +2 µC (na origem) e −3 µC (em x = 3 m) estão no vácuo. Calcule a força entre elas.

<details><summary>Gabarito</summary>

$F = k\dfrac{|q_1q_2|}{r^2} = 8{,}99\times10^9\cdot\dfrac{6\times10^{-12}}{9} \approx 5{,}99\ \text{mN}$, **atrativa**.

</details>

**2.2** Use a Lei de Gauss para obter o campo de uma linha infinita com densidade $\lambda$ e, a partir dele, a capacitância por metro de um cabo coaxial (raio interno $a$, externo $b$, dielétrico $\varepsilon_r$).

<details><summary>Gabarito</summary>

Superfície gaussiana cilíndrica: $E\cdot2\pi\rho L = \lambda L/\varepsilon$ → $E = \dfrac{\lambda}{2\pi\varepsilon\rho}$.

$V = \int_a^b E\,d\rho = \dfrac{\lambda}{2\pi\varepsilon}\ln\dfrac ba$ → $C' = \dfrac{\lambda}{V} = \dfrac{2\pi\varepsilon}{\ln(b/a)}$ (F/m).

</details>

**2.3 (Aplicação — cabos de RF)** Um coaxial com polietileno ($\varepsilon_r = 2{,}25$) tem $\ln(b/a) = 1{,}875$. Calcule $C'$, $L' = \dfrac{\mu_0}{2\pi}\ln(b/a)$, a impedância característica $Z_0 = \sqrt{L'/C'}$ e a velocidade de propagação.

<details><summary>Gabarito</summary>

$C' = \dfrac{2\pi\cdot8{,}854\times10^{-12}\cdot2{,}25}{1{,}875} \approx 66{,}8\ \text{pF/m}$; $L' = 2\times10^{-7}\cdot1{,}875 = 375\ \text{nH/m}$

$Z_0 = \sqrt{375\times10^{-9}/66{,}8\times10^{-12}} \approx 75\ \Omega$ (cabo de TV/vídeo) ; $v = c/\sqrt{\varepsilon_r} = 2\times10^8\ \text{m/s}$ (fator de velocidade 0,67).

</details>

**2.4** Capacitor de placas paralelas: $A = 0{,}01\ \text{m}^2$, $d = 1\ \text{mm}$, $\varepsilon_r = 4$. Calcule C e a energia armazenada a 100 V.

<details><summary>Gabarito</summary>

$C = \varepsilon_r\varepsilon_0A/d = 354\ \text{pF}$; $W = \tfrac12CV^2 = 1{,}77\ \mu\text{J}$.

</details>

**2.5** Por que o campo elétrico é mais intenso nas pontas de um condutor? Relacione com o funcionamento do para-raios (captor tipo Franklin).

<details><summary>Gabarito</summary>

Em equilíbrio a superfície do condutor é equipotencial; regiões de menor raio de curvatura concentram mais carga por área, logo campo mais intenso ($E \propto 1/R$ para uma esfera ao mesmo potencial). Nas pontas o ar ioniza primeiro (efeito corona), favorecendo que o captor seja o ponto de conexão da descarga.

</details>

---

## 3. Magnetostática

**3.1** Um condutor longo transporta 100 A. Qual o campo magnético a 1 m? Compare com o campo terrestre (~25–65 µT).

<details><summary>Gabarito</summary>

$B = \dfrac{\mu_0I}{2\pi r} = 2\times10^{-7}\cdot100 = 20\ \mu\text{T}$ — mesma ordem de grandeza do campo terrestre.

</details>

**3.2** Um toroide de 500 espiras, raio médio 10 cm, conduz 2 A (núcleo de ar). Calcule B no interior.

<details><summary>Gabarito</summary>

Lei de Ampère: $B = \dfrac{\mu_0NI}{2\pi r} = \dfrac{4\pi\times10^{-7}\cdot1000}{2\pi\cdot0{,}1} = 2\ \text{mT}$.

</details>

**3.3** Um condutor de 0,2 m com 10 A está perpendicular a um campo de 0,5 T. Calcule a força.

<details><summary>Gabarito</summary>

$F = BIL = 0{,}5\cdot10\cdot0{,}2 = 1\ \text{N}$ (princípio do motor elétrico).

</details>

---

## 4. Indução eletromagnética

**4.1** Uma bobina de 100 espiras e área 0,05 m² está num campo que cai uniformemente de 0,2 T a 0 em 0,1 s. Calcule a fem induzida.

<details><summary>Gabarito</summary>

$\varepsilon = N\dfrac{\Delta\Phi}{\Delta t} = 100\cdot\dfrac{0{,}05\cdot0{,}2}{0{,}1} = 10\ \text{V}$ (o sentido opõe-se à variação — Lenz).

</details>

**4.2** Uma espira gira a 60 Hz num campo de 0,8 T, com área 0,02 m² e 50 espiras. Qual a tensão de pico gerada?

<details><summary>Gabarito</summary>

$e(t) = NBA\omega\,\text{sen}(\omega t)$ → $E_{pico} = 50\cdot0{,}8\cdot0{,}02\cdot377 = 301{,}6\ \text{V}$ (213 V eficazes).

</details>

**4.3** Explique por que núcleos de transformadores são laminados.

<details><summary>Gabarito</summary>

O fluxo variável induz correntes parasitas (de Foucault) no núcleo; lâminas isoladas aumentam a resistência do caminho dessas correntes, reduzindo as perdas, que crescem aproximadamente com o quadrado da espessura da lâmina e da frequência.

</details>

---

## 5. Equações de Maxwell e ondas

**5.1** Escreva as quatro equações de Maxwell na forma diferencial e diga o significado físico de cada uma.

<details><summary>Gabarito</summary>

$\nabla\cdot\mathbf D = \rho_v$ (Gauss: cargas são fontes de campo elétrico)
$\nabla\cdot\mathbf B = 0$ (não existem monopolos magnéticos)
$\nabla\times\mathbf E = -\partial\mathbf B/\partial t$ (Faraday: campo magnético variável gera campo elétrico)
$\nabla\times\mathbf H = \mathbf J + \partial\mathbf D/\partial t$ (Ampère-Maxwell: correntes e campo elétrico variável geram campo magnético)

</details>

**5.2** Calcule o comprimento de onda de um sinal de TV de 600 MHz no ar e dentro de um cabo com $\varepsilon_r = 2{,}25$. Qual o comprimento de um dipolo de meia onda nessa frequência?

<details><summary>Gabarito</summary>

Ar: $\lambda = c/f = 0{,}50\ \text{m}$; no cabo: $\lambda = 0{,}50/1{,}5 = 0{,}333\ \text{m}$. Dipolo de meia onda ≈ 0,25 m (na prática ~0,95·λ/2 ≈ 0,24 m).

</details>

**5.3** Uma onda plana no espaço livre tem $E_{rms} = 10\ \text{V/m}$. Calcule $H_{rms}$ e a densidade de potência.

<details><summary>Gabarito</summary>

$H = E/\eta_0 = 26{,}5\ \text{mA/m}$; $S = E^2/\eta_0 = 0{,}265\ \text{W/m}^2$.

</details>

**5.4** Calcule a profundidade pelicular do cobre ($\sigma = 5{,}8\times10^7\ \text{S/m}$) em 60 Hz e em 1 MHz. Que conclusão se tira para cabos de alta frequência?

<details><summary>Gabarito</summary>

$\delta = 1/\sqrt{\pi f\mu_0\sigma}$ → 60 Hz: **8,5 mm**; 1 MHz: **0,066 mm**.
Em RF a corrente circula só na "casca" do condutor; por isso usam-se condutores ocos/prateados e cabos tipo Litz — o miolo do condutor quase não conduz.

</details>
