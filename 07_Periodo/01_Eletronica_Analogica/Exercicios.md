# Exercícios — Eletrônica Analógica

> Lista autoral por tópico. Amp-op ideal, salvo indicação. Trabalhos antigos (filtros, Sallen-Key) em [`Materiais/`](Materiais/) e em `04_Periodo/01_Circuitos_Eletricos_II/Materiais/`.

---

## 1. Amplificadores com transistores (pequenos sinais)

**1.1** Um amplificador emissor comum com $I_C = 1\ \text{mA}$, $\beta = 100$, $R_C = 3{,}3\ \text{k}\Omega$, carga de 10 kΩ e emissor desacoplado. Calcule $g_m$, $r_\pi$ e o ganho de tensão (despreze $r_o$, $V_T = 25\ \text{mV}$).

<details><summary>Gabarito</summary>

$g_m = I_C/V_T = 40\ \text{mS}$; $r_\pi = \beta/g_m = 2{,}5\ \text{k}\Omega$
$A_v = -g_m(R_C\parallel R_L) = -0{,}04\cdot2{,}48\text{k} \approx -99$.

</details>

**1.2** Que configuração (EC, BC, CC) você usaria como *buffer* entre um estágio de alta impedância e uma carga de baixa impedância? Por quê?

<details><summary>Gabarito</summary>

Coletor comum (seguidor de emissor): ganho ≈ 1, alta impedância de entrada e baixa de saída.

</details>

---

## 2. Amplificador operacional

**2.1** Inversor com $R_f = 100\ \text{k}\Omega$ e $R_{in} = 10\ \text{k}\Omega$. Qual o ganho e a saída para 0,5 V na entrada? E um não inversor com os mesmos resistores?

<details><summary>Gabarito</summary>

Inversor: −10 → −5 V. Não inversor: $1 + 100/10 = 11$ → 5,5 V.

</details>

**2.2** Projete um somador inversor que produza $v_o = -(2v_1 + v_2)$ com $R_f = 20\ \text{k}\Omega$.

<details><summary>Gabarito</summary>

$R_1 = 10\ \text{k}\Omega$ (ganho 2) e $R_2 = 20\ \text{k}\Omega$ (ganho 1).

</details>

**2.3** Um integrador inversor tem R = 10 kΩ e C = 100 nF. Para entrada de +1 V constante, qual a taxa de variação da saída? Por que na prática se coloca um resistor em paralelo com C?

<details><summary>Gabarito</summary>

$dv_o/dt = -V_{in}/RC = -1000\ \text{V/s}$ (−1 V/ms). O resistor limita o ganho em DC; sem ele, o offset do amp-op é integrado e satura a saída.

</details>

**2.4** Um amplificador de instrumentação tem ganho $G = 1 + 2R/R_g$ com R = 25 kΩ. Que $R_g$ dá ganho 100?

<details><summary>Gabarito</summary>

$R_g = 2R/(G-1) = 50\text{k}/99 \approx 505\ \Omega$.

</details>

---

## 3. Limitações reais

**3.1** Um amp-op tem GBW = 1 MHz. Qual a banda com ganho 100? Quantos estágios de ganho 10 seriam necessários para ter ganho 100 com banda maior?

<details><summary>Gabarito</summary>

GBW/G = 10 kHz. Dois estágios de ganho 10 → cada um com 100 kHz (a banda total fica ≈ 64 kHz, pois $\sqrt{2^{1/2}-1}\cdot100\text{k}$).

</details>

**3.2** Com slew rate de 0,5 V/µs, qual a maior frequência para uma senoide de 10 V de pico sem distorção?

<details><summary>Gabarito</summary>

$f_{max} = SR/(2\pi V_p) = 0{,}5\times10^6/(2\pi\cdot10) \approx 7{,}96\ \text{kHz}$.

</details>

---

## 4. Filtros ativos e osciladores

**4.1** Sallen-Key passa-baixas de ganho unitário com R₁ = R₂ = 10 kΩ, C₁ (realimentação) = 20 nF, C₂ (terra) = 10 nF. Calcule $f_c$ e Q.

<details><summary>Gabarito</summary>

$f_c = \dfrac{1}{2\pi R\sqrt{C_1C_2}} \approx 1{,}13\ \text{kHz}$; $Q = \frac12\sqrt{C_1/C_2} = 0{,}707$ → **Butterworth**.

</details>

**4.2** Oscilador em ponte de Wien com R = 10 kΩ e C = 16 nF. Qual a frequência e o ganho mínimo do amplificador?

<details><summary>Gabarito</summary>

$f = 1/(2\pi RC) \approx 995\ \text{Hz}$; ganho = 3 (critério de Barkhausen).

</details>

**4.3** Um comparador Schmitt não inversor alimentado com ±12 V tem $R_1 = 10\ \text{k}\Omega$ (entrada) e $R_2 = 100\ \text{k}\Omega$ (realimentação). Calcule os limiares.

<details><summary>Gabarito</summary>

$V_{th} = \pm V_{sat}\dfrac{R_1}{R_2} = \pm1{,}2\ \text{V}$ → histerese de 2,4 V.

</details>

---

## 5. Fontes e reguladores

**5.1** Um regulador linear reduz 12 V para 5 V a 1 A. Calcule a dissipação e o rendimento. Compare com um conversor buck de 90%.

<details><summary>Gabarito</summary>

Linear: $P_{diss} = 7\ \text{W}$, $\eta = 5/12 = 41{,}7\%$. Buck: perdas ≈ 0,56 W. Linear ganha em ruído e simplicidade; buck em eficiência.

</details>
