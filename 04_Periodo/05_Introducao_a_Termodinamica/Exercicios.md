# Exercícios — Introdução à Termodinâmica

> Lista autoral por tópico. Calor específico da água: 4186 J/(kg·K).

---

## 1. Temperatura, calor e dilatação

**1.1** Converta 25 °C para K e °F.

<details><summary>Gabarito</summary>

298,15 K; 77 °F.

</details>

**1.2** Um cabo de alumínio ($\alpha = 23\times10^{-6}\ /^\circ\text{C}$) tem 1 km entre torres. Quanto ele se alonga com aumento de 40 °C? Qual a consequência na flecha?

<details><summary>Gabarito</summary>

$\Delta L = \alpha L\Delta T = 23\times10^{-6}\cdot1000\cdot40 = 0{,}92\ \text{m}$. O cabo fica mais longo e a flecha aumenta — por isso as distâncias de segurança ao solo são verificadas na temperatura máxima de operação do condutor.

</details>

**1.3** Quanto tempo um aquecedor de 2 kW leva para aquecer 1 L de água de 20 °C a 100 °C (sem perdas)?

<details><summary>Gabarito</summary>

$Q = mc\Delta T = 1\cdot4186\cdot80 = 334{,}9\ \text{kJ}$ → $t = 167\ \text{s} \approx 2{,}8\ \text{min}$.

</details>

---

## 2. Primeira lei

**2.1** Um gás recebe 500 J de calor e realiza 200 J de trabalho. Qual a variação de energia interna?

<details><summary>Gabarito</summary>

$\Delta U = Q - W = 300\ \text{J}$.

</details>

**2.2** Um mol de gás ideal sofre compressão isotérmica a 300 K de 20 L para 10 L. Calcule o trabalho e o calor trocado.

<details><summary>Gabarito</summary>

$W = nRT\ln(V_f/V_i) = 1\cdot8{,}314\cdot300\cdot\ln0{,}5 = -1729\ \text{J}$ (trabalho feito sobre o gás). Isotérmico → $\Delta U = 0$ → $Q = -1729\ \text{J}$ (calor cedido).

</details>

---

## 3. Gases ideais

**3.1** Um pneu tem 2,2 bar (manométrica) a 20 °C. Qual a pressão a 50 °C, com volume constante? (Use pressão absoluta.)

<details><summary>Gabarito</summary>

$P_1 = 3{,}21\ \text{bar abs}$ → $P_2 = 3{,}21\cdot323/293 = 3{,}54\ \text{bar abs} = 2{,}53\ \text{bar manométrica}$.

</details>

---

## 4. Segunda lei e máquinas térmicas

**4.1** Qual o rendimento máximo (Carnot) de uma máquina entre 800 K e 300 K?

<details><summary>Gabarito</summary>

$\eta = 1 - 300/800 = 62{,}5\%$.

</details>

**4.2** Uma termelétrica gera 500 MW elétricos com rendimento global de 40%. Qual a potência do combustível e o calor rejeitado ao ambiente?

<details><summary>Gabarito</summary>

$P_{comb} = 500/0{,}4 = 1250\ \text{MW}$; rejeitado: 750 MW (pelo condensador/torre de resfriamento).

</details>

**4.3** Um ar-condicionado retira 3,5 kW de calor de uma sala de equipamentos consumindo 1,1 kW. Calcule o COP e o calor rejeitado para fora.

<details><summary>Gabarito</summary>

COP = 3,5/1,1 = 3,18; calor rejeitado = 3,5 + 1,1 = 4,6 kW.

</details>

**4.4** Toda a potência elétrica consumida por um transmissor que não é irradiada vira calor no abrigo. Um transmissor consome 12 kW e entrega 5 kW à antena. Que carga térmica o ar-condicionado precisa remover? Expresse em BTU/h (1 W ≈ 3,412 BTU/h).

<details><summary>Gabarito</summary>

$12 - 5 = 7\ \text{kW}$ → $\approx 23\,900\ \text{BTU/h}$ (mais a carga dos demais equipamentos e da insolação).

</details>
