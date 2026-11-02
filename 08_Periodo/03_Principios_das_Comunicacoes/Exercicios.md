# Exercícios — Princípios das Comunicações

> Lista autoral por tópico. Soluções do Haykin em `Bibliografia/Solutions/`. Para RF aplicada e TV digital, veja também a trilha [`Complementares/Telecom_e_Radiodifusao`](../../Complementares/Telecom_e_Radiodifusao/).

---

## 1. Decibéis e espectro

**1.1** Converta: 1 W, 10 kW e 1 µW para dBm e dBW.

<details><summary>Gabarito</summary>

1 W = 30 dBm = 0 dBW; 10 kW = 70 dBm = 40 dBW; 1 µW = −30 dBm = −60 dBW.

</details>

---

## 2. Modulação em amplitude

**2.1** Um transmissor AM tem portadora de 100 W e índice de modulação 0,8 (tom senoidal). Calcule a potência total, a potência nas bandas laterais e a eficiência.

<details><summary>Gabarito</summary>

$P_t = P_c(1 + m^2/2) = 132\ \text{W}$; bandas laterais: 32 W; eficiência = 32/132 = 24,2% — a portadora não carrega informação.

</details>

**2.2** Qual a banda ocupada por AM-DSB, DSB-SC e SSB para áudio de 5 kHz?

<details><summary>Gabarito</summary>

AM e DSB-SC: 10 kHz; SSB: 5 kHz.

</details>

---

## 3. Modulação em frequência

**3.1** Uma rádio FM tem desvio máximo de 75 kHz e áudio até 15 kHz. Calcule o índice de modulação e a banda pela regra de Carson.

<details><summary>Gabarito</summary>

β = 75/15 = 5; $B = 2(\Delta f + f_m) = 180\ \text{kHz}$ (o canal FM tem 200 kHz).

</details>

**3.2** Por que o FM é mais imune a ruído que o AM?

<details><summary>Gabarito</summary>

A informação está na frequência, não na amplitude; o limitador remove variações de amplitude (onde está grande parte do ruído) e, acima do limiar, o ganho de SNR cresce com β² à custa de mais banda.

</details>

---

## 4. Ruído

**4.1** Qual a potência de ruído térmico numa banda de 6 MHz a 290 K?

<details><summary>Gabarito</summary>

$N = kTB$ → $-174\ \text{dBm/Hz} + 10\log(6\times10^6) = -106{,}2\ \text{dBm}$.

</details>

**4.2** Um LNA (G = 20 dB, NF = 1 dB) é seguido de um misturador com NF = 10 dB. Calcule a figura de ruído total (Friis).

<details><summary>Gabarito</summary>

$F = F_1 + \dfrac{F_2 - 1}{G_1} = 1{,}259 + \dfrac{9}{100} = 1{,}349$ → **1,30 dB**. O primeiro estágio domina — por isso o LNA fica junto da antena.

</details>

---

## 5. Comunicação digital

**5.1** Um sinal de voz de 4 kHz é amostrado a 8 kHz com 8 bits. Qual a taxa de bits e a SQNR teórica?

<details><summary>Gabarito</summary>

64 kbit/s; $SQNR \approx 6{,}02n + 1{,}76 = 49{,}9\ \text{dB}$.

</details>

**5.2** Uma modulação 64-QAM opera a 5 Mbaud. Qual a taxa bruta? Por que aumentar a ordem da QAM exige mais SNR?

<details><summary>Gabarito</summary>

6 bits/símbolo → 30 Mbit/s. Os pontos da constelação ficam mais próximos para a mesma potência média; menos ruído basta para levar a decisão ao ponto vizinho.

</details>

**5.3** Qual a capacidade de Shannon de um canal de 6 MHz com SNR de 20 dB?

<details><summary>Gabarito</summary>

$C = B\log_2(1 + SNR) = 6\times10^6\log_2(101) \approx 39{,}9\ \text{Mbit/s}$.

</details>

---

## 6. OFDM e ISDB-T

**6.1** No ISDB-T modo 3 o espaçamento entre portadoras é 250/252 kHz. Calcule a duração útil do símbolo, o intervalo de guarda para GI = 1/8 e 1/16, e a máxima diferença de percurso tolerada numa rede SFN.

<details><summary>Gabarito</summary>

$T_u = 1/\Delta f = 1008\ \mu\text{s}$. GI 1/8: 126 µs → $c\cdot126\mu = 37{,}8\ \text{km}$. GI 1/16: 63 µs → 18,9 km.

</details>

**6.2** Calcule a taxa útil de **um segmento** ISDB-T modo 3 (384 portadoras de dados), 64-QAM, FEC 3/4, GI 1/16, considerando o Reed-Solomon 188/204. Qual seria a taxa com 13 segmentos nessa configuração?

<details><summary>Gabarito</summary>

Bits por símbolo OFDM por segmento: $384\cdot6\cdot\frac34\cdot\frac{188}{204} = 1592{,}5$.
Duração total do símbolo: $1008\cdot(1 + 1/16) = 1071\ \mu\text{s}$ → **≈ 1,487 Mbit/s por segmento** → ×13 ≈ **19,3 Mbit/s**.
(Confira: DQPSK, FEC 1/2, GI 1/4 dá 280,9 kbit/s por segmento, o valor da tabela ARIB.)

</details>
