# Exercícios — Instrumentação Industrial

> Lista autoral por tópico. Listas antigas de Medidas Elétricas (wattímetro, TC/TP, terra) em [`Materiais/`](Materiais/).

---

## 1. Características de instrumentos

**1.1** Um termômetro de 0–200 °C tem exatidão de ±0,5% do fundo de escala. Qual o erro máximo? Qual o erro relativo ao medir 20 °C?

<details><summary>Gabarito</summary>

±1 °C em qualquer ponto da escala → a 20 °C, ±5% da leitura. Por isso se escolhe a faixa próxima do valor medido.

</details>

**1.2** Diferencie exatidão, precisão e resolução com um exemplo.

<details><summary>Gabarito</summary>

**Exatidão**: proximidade do valor verdadeiro. **Precisão**: repetibilidade (baixa dispersão). **Resolução**: menor variação detectável. Ex.: um multímetro com 4 casas decimais (alta resolução) descalibrado em +0,5 V pode ser preciso mas inexato.

</details>

**1.3** Um sensor de 1ª ordem tem τ = 5 s e recebe um degrau de 25 °C para 100 °C. O que ele indica após 10 s? Quanto tempo para indicar 99% da variação?

<details><summary>Gabarito</summary>

$T = 25 + 75(1 - e^{-2}) = 89{,}8\ ^\circ\text{C}$. 99% → $t = \tau\ln100 \approx 4{,}6\tau = 23\ \text{s}$.

</details>

---

## 2. Sinais padrão

**2.1** Um transmissor de pressão 0–10 bar tem saída 4–20 mA. Qual a pressão para 12 mA? Que corrente corresponde a 7,2 bar?

<details><summary>Gabarito</summary>

$p = (I - 4)/16\cdot10$ → 12 mA = **5 bar**. 7,2 bar → $4 + 16\cdot0{,}72 = 15{,}52\ \text{mA}$.

</details>

**2.2** Por que o padrão começa em 4 mA e não em 0 mA? E por que corrente em vez de tensão?

<details><summary>Gabarito</summary>

"Zero vivo": 0 mA indica cabo rompido/falha (detecção de defeito), e os 4 mA alimentam o próprio transmissor a 2 fios. Corrente não sofre com a queda de tensão no cabo e é mais imune a ruído em longas distâncias.

</details>

**2.3** Que resistor converte 4–20 mA em 1–5 V?

<details><summary>Gabarito</summary>

250 Ω.

</details>

---

## 3. Sensores

**3.1** Um Pt100 segue $R = 100(1 + 0{,}00385T)$. Qual a resistência a 100 °C? Que temperatura corresponde a 119,4 Ω?

<details><summary>Gabarito</summary>

138,5 Ω; $T = (119{,}4/100 - 1)/0{,}00385 = 50{,}4\ ^\circ\text{C}$.

</details>

**3.2** Por que se liga o Pt100 a 3 fios?

<details><summary>Gabarito</summary>

Para compensar a resistência dos cabos: com 3 fios iguais, a resistência de um fio fica em cada braço adjacente da ponte e o efeito se cancela.

</details>

**3.3** Um termopar tipo K (~41 µV/°C) gera 4,1 mV com junção fria a 25 °C. Qual a temperatura aproximada da junção quente?

<details><summary>Gabarito</summary>

ΔT ≈ 4,1 mV / 41 µV/°C = 100 °C → $T \approx 125\ ^\circ\text{C}$ (a compensação de junção fria soma a temperatura ambiente; em medições reais use a tabela de linearização).

</details>

---

## 4. Pontes e condicionamento

**4.1** Uma ponte de Wheatstone com três resistores de 1 kΩ e $R_x = 1{,}01\ \text{k}\Omega$ é alimentada com 10 V. Qual a tensão de saída?

<details><summary>Gabarito</summary>

$V_o = 10\left(\dfrac{1010}{2010} - \dfrac12\right) \approx 24{,}9\ \text{mV}$.

</details>

**4.2** Um strain gauge (GF = 2) num quarto de ponte com 10 V sofre deformação de 500 µε. Estime a saída.

<details><summary>Gabarito</summary>

$\Delta R/R = GF\cdot\varepsilon = 0{,}001$ → $V_o \approx V\cdot\dfrac{\Delta R/R}{4} = 2{,}5\ \text{mV}$ — precisa de amplificador de instrumentação.

</details>

---

## 5. Medidas elétricas

**5.1** Um TC 200/5 A indica 3,5 A no secundário. Qual a corrente primária? Por que nunca se deve abrir o secundário de um TC energizado?

<details><summary>Gabarito</summary>

$3{,}5\cdot40 = 140\ \text{A}$. Com o secundário aberto não há força magnetomotriz de oposição: o núcleo satura e surgem tensões de pico perigosíssimas (kV) nos terminais, com risco de choque e de destruição do TC.

</details>

**5.2** Um osciloscópio mostra uma senoide de 8 divisões pico a pico na escala de 5 V/div. Qual a tensão eficaz?

<details><summary>Gabarito</summary>

$V_{pp} = 40\ \text{V}$ → $V_p = 20\ \text{V}$ → $V_{rms} = 14{,}1\ \text{V}$.

</details>

**5.3** Descreva o método da queda de potencial (regra dos 62%) para medir a resistência de terra.

<details><summary>Gabarito</summary>

Injeta-se corrente entre o eletrodo sob teste (E) e uma haste auxiliar de corrente (C) distante. Uma haste de potencial (P) é colocada em linha a 62% da distância E–C; a resistência é $V_{EP}/I$. Deslocam-se P a ±10% para confirmar que a leitura está no "patamar" (fora das zonas de influência).

</details>
