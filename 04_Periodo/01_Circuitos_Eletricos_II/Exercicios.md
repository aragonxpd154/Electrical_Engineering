# Exercícios — Circuitos Elétricos II

> Lista autoral organizada por tópico. Resolva antes de abrir o **Gabarito**.
> Tensões e correntes em valores **eficazes** (RMS), salvo indicação.

---

## 1. Potência em corrente alternada e fator de potência

**1.1** Uma carga de 10 kW com FP 0,80 indutivo é alimentada em 220 V, 60 Hz. Calcule a potência aparente, a reativa e a corrente. Em seguida dimensione o capacitor em paralelo para elevar o FP a 0,95.

<details><summary>Gabarito</summary>

$S = P/\text{FP} = 12{,}5\ \text{kVA}$; $Q = P\tan(\arccos 0{,}8) = 7{,}5\ \text{kvar}$; $I = S/V = 56{,}8\ \text{A}$.

Novo reativo: $Q_2 = 10\tan(\arccos0{,}95) = 3{,}29\ \text{kvar}$ → $Q_C = 7{,}5 - 3{,}29 = 4{,}21\ \text{kvar}$

$C = \dfrac{Q_C}{\omega V^2} = \dfrac{4213}{377\cdot 220^2} \approx 231\ \mu\text{F}$. A corrente cai para $10\,000/(220\cdot0{,}95) = 47{,}8\ \text{A}$.

</details>

**1.2** Por que as distribuidoras cobram excedente de reativo quando o FP fica abaixo de 0,92? Cite duas consequências técnicas de um FP baixo.

<details><summary>Gabarito</summary>

O limite de 0,92 é o de referência da regulação da ANEEL. Com FP baixo, para a mesma potência ativa circula mais corrente: (1) aumentam as perdas $I^2R$ em cabos e transformadores; (2) aumenta a queda de tensão e a capacidade de transformadores/cabos fica "ocupada" por reativo, exigindo equipamentos maiores.

</details>

**1.3** Mostre que, para uma carga $Z = R + jX$ alimentada por $V$, a potência complexa vale $S = V I^* = P + jQ$, e calcule $S$ para $V = 220\angle0^\circ$ e $Z = 10 + j10\ \Omega$.

<details><summary>Gabarito</summary>

$I = 15{,}56\angle{-45^\circ}$ → $S = 220\cdot15{,}56\angle{45^\circ} = 3423\angle45^\circ = 2420 + j2420\ \text{VA}$.

</details>

---

## 2. Circuitos trifásicos

**2.1** Uma carga equilibrada em **estrela** com $Z = 10\angle30^\circ\ \Omega$ por fase é ligada a uma rede de 380 V (tensão de linha). Calcule tensão de fase, corrente de linha, P, Q e S totais.

<details><summary>Gabarito</summary>

$V_f = 380/\sqrt3 = 219{,}4\ \text{V}$; $I_L = I_f = 21{,}94\ \text{A}$

$P = 3V_fI_f\cos30^\circ = 12{,}5\ \text{kW}$; $Q = 3V_fI_f\,\text{sen}30^\circ = 7{,}22\ \text{kvar}$; $S = 14{,}4\ \text{kVA}$.

</details>

**2.2** A mesma impedância é religada em **triângulo** na mesma rede. Calcule corrente de fase, de linha e a potência ativa. Compare com 2.1.

<details><summary>Gabarito</summary>

$I_f = 380/10 = 38\ \text{A}$; $I_L = \sqrt3\cdot38 = 65{,}8\ \text{A}$; $P = 3\cdot380\cdot38\cdot\cos30^\circ = 37{,}5\ \text{kW}$.

Em Δ a potência é **3 vezes** maior que em Y — é exatamente o princípio da partida estrela-triângulo de motores.

</details>

**2.3** No método dos dois wattímetros, as leituras foram $W_1 = 8{,}5\ \text{kW}$ e $W_2 = 4{,}0\ \text{kW}$. Calcule P, Q e o FP da carga.

<details><summary>Gabarito</summary>

$P = W_1 + W_2 = 12{,}5\ \text{kW}$; $Q = \sqrt3(W_1 - W_2) = 7{,}79\ \text{kvar}$; $\text{FP} = \cos(\arctan(Q/P)) = 0{,}849$.

</details>

**2.4** Em uma carga desequilibrada em estrela com neutro, por que a corrente de neutro não é nula? O que acontece com as tensões de fase se o neutro se romper?

<details><summary>Gabarito</summary>

A corrente de neutro é a soma fasorial $I_A + I_B + I_C$, que só é zero se as cargas forem iguais. Sem neutro, o ponto central "flutua": fases com menos carga recebem sobretensão e fases mais carregadas, subtensão — causa clássica de queima de equipamentos em instalações residenciais.

</details>

---

## 3. Frequência complexa e Laplace aplicada a circuitos

**3.1** Obtenha a função de transferência $H(s) = V_o/V_i$ de um RC passa-baixas ($R$ em série, saída no capacitor) e a resposta ao degrau unitário.

<details><summary>Gabarito</summary>

$H(s) = \dfrac{1/(sC)}{R + 1/(sC)} = \dfrac{1}{RCs+1}$. Para degrau: $V_o(s) = \dfrac{1}{s(RCs+1)}$ → $v_o(t) = 1 - e^{-t/RC}$.

</details>

**3.2** Um RLC série ($R = 2\ \Omega$, $L = 1\ \text{H}$, $C = 0{,}5\ \text{F}$) com capacitor inicialmente descarregado recebe um degrau de 10 V. Encontre $I(s)$ e $i(t)$.

<details><summary>Gabarito</summary>

$I(s) = \dfrac{10/s}{R + sL + 1/(sC)} = \dfrac{10}{s^2 + 2s + 2} = \dfrac{10}{(s+1)^2 + 1}$ → $i(t) = 10\,e^{-t}\,\text{sen}(t)$ A.

</details>

---

## 4. Resposta em frequência, Bode e filtros

**4.1** Para $H(s) = \dfrac{100}{s+100}$, determine a frequência de corte (rad/s e Hz) e o módulo (dB) e a fase em $\omega = 1000\ \text{rad/s}$.

<details><summary>Gabarito</summary>

$\omega_c = 100\ \text{rad/s}$ → $f_c = 15{,}9\ \text{Hz}$.
$|H(j1000)| = 1/\sqrt{1+100} \Rightarrow -20{,}0\ \text{dB}$; fase $= -\arctan(10) = -84{,}3^\circ$.
(Assíntota: −20 dB/década a partir de $\omega_c$.)

</details>

**4.2** Um RLC série com $R = 10\ \Omega$, $L = 10\ \text{mH}$, $C = 1\ \mu\text{F}$ é usado como passa-faixa (saída no resistor). Calcule $f_0$, Q e a largura de banda.

<details><summary>Gabarito</summary>

$\omega_0 = 1/\sqrt{LC} = 10\,000\ \text{rad/s}$ → $f_0 = 1{,}59\ \text{kHz}$
$Q = \omega_0L/R = 10$ → $B = \omega_0/Q = 1000\ \text{rad/s}$ (159 Hz).

</details>

**4.3** Esboce o diagrama de Bode assintótico de $H(s) = \dfrac{10\,(s+10)}{(s+1)(s+100)}$.

<details><summary>Gabarito</summary>

Ganho DC: $H(0) = 10\cdot10/100 = 1$ (0 dB). Polo em 1 rad/s (−20 dB/dec), zero em 10 rad/s (inclinação volta a 0), polo em 100 rad/s (−20 dB/dec).
Entre 10 e 100 rad/s o módulo fica em ≈ −20 dB; acima de 100 rad/s cai a −20 dB/dec.

</details>

---

## 5. Acoplamento magnético e transformador

**5.1** Dois indutores $L_1 = 4\ \text{mH}$ e $L_2 = 9\ \text{mH}$ têm coeficiente de acoplamento $k = 0{,}5$. Calcule M e a indutância equivalente em série aditiva e subtrativa.

<details><summary>Gabarito</summary>

$M = k\sqrt{L_1L_2} = 0{,}5\cdot6 = 3\ \text{mH}$.
Aditiva: $L_1+L_2+2M = 19\ \text{mH}$; subtrativa: $L_1+L_2-2M = 7\ \text{mH}$.

</details>

**5.2** Um transformador ideal 10:1 tem primário em 220 V e carga de 2 Ω no secundário. Calcule $V_2$, $I_2$, $I_1$ e a impedância refletida ao primário.

<details><summary>Gabarito</summary>

$V_2 = 22\ \text{V}$; $I_2 = 11\ \text{A}$; $I_1 = 1{,}1\ \text{A}$; $Z_{in} = a^2 Z_L = 100\cdot2 = 200\ \Omega$.

</details>

**5.3** Qual relação de espiras casa um alto-falante de 8 Ω com um amplificador de saída 800 Ω?

<details><summary>Gabarito</summary>

$a = \sqrt{800/8} = 10$ (10:1).

</details>

---

## 6. Quadripolos

**6.1** Determine os parâmetros Z de uma rede T com braços série $Z_a = 2\ \Omega$ (entrada) e $Z_b = 4\ \Omega$ (saída) e ramo shunt $Z_c = 6\ \Omega$.

<details><summary>Gabarito</summary>

$z_{11} = Z_a + Z_c = 8\ \Omega$; $z_{22} = Z_b + Z_c = 10\ \Omega$; $z_{12} = z_{21} = Z_c = 6\ \Omega$ (rede recíproca).

</details>

**6.2** Quais parâmetros (Z, Y, h ou ABCD) são mais convenientes para (a) associar quadripolos em cascata, (b) modelar um transistor em pequenos sinais, (c) modelar uma linha de transmissão?

<details><summary>Gabarito</summary>

(a) ABCD (multiplicam-se as matrizes); (b) h (híbridos); (c) ABCD.

</details>

---

## 7. Série de Fourier em circuitos

**7.1** Uma onda quadrada de amplitude ±A e período T tem série $v(t) = \dfrac{4A}{\pi}\sum_{n\ \text{ímpar}} \dfrac{1}{n}\,\text{sen}(n\omega_0 t)$. Qual a amplitude da 3ª e da 5ª harmônica em relação à fundamental? Calcule a DHT considerando até a 7ª harmônica.

<details><summary>Gabarito</summary>

3ª: 1/3 (33,3 %); 5ª: 1/5 (20 %); 7ª: 1/7 (14,3 %).
$\text{DHT}_7 = \sqrt{(1/3)^2+(1/5)^2+(1/7)^2} = 41{,}4\ \%$ (a DHT completa da onda quadrada é ≈ 48,3 %).

</details>

**7.2** Essa onda quadrada (A = 10 V, f₀ = 1 kHz) alimenta o passa-baixas RC do item 3.1 com $f_c = 1\ \text{kHz}$. Calcule a amplitude de saída da fundamental e da 3ª harmônica.

<details><summary>Gabarito</summary>

Fundamental: $\frac{40}{\pi}\cdot\frac{1}{\sqrt{1+1}} = 9{,}00\ \text{V}$.
3ª: $\frac{40}{3\pi}\cdot\frac{1}{\sqrt{1+9}} = 1{,}34\ \text{V}$. O filtro atenua mais as harmônicas, "arredondando" a onda.

</details>
