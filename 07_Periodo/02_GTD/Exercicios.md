# Exercícios — Geração, Transmissão e Distribuição de Energia Elétrica

> Lista autoral por tópico. Listas e relatórios antigos em [`Materiais/`](Materiais/).

---

## 1. Geração

**1.1** Uma usina de 100 MW gerou 438 GWh no ano. Qual o fator de capacidade? Compare com valores típicos de eólica, solar e térmica de base.

<details><summary>Gabarito</summary>

$FC = 438\ \text{GWh}/(100\ \text{MW}\cdot8760\ \text{h}) = 50\%$. Típicos: solar 20–30%, eólica no Nordeste 40–55%, térmica de base 80–90%.

</details>

**1.2** Quantos polos um gerador hidráulico de 60 Hz deve ter para girar a 180 rpm?

<details><summary>Gabarito</summary>

$p = 120f/n = 120\cdot60/180 = 40$ polos.

</details>

---

## 2. Parâmetros de linhas

**2.1** Uma linha trifásica tem condutores de raio 1,5 cm e espaçamento médio geométrico de 5 m. Calcule a indutância por fase (H/km), a reatância a 60 Hz e a capacitância por fase.

<details><summary>Gabarito</summary>

$r' = 0{,}7788r = 1{,}168\ \text{cm}$; $L = 2\times10^{-7}\ln(D/r') = 1{,}21\ \text{mH/km}$; $X_L = 0{,}457\ \Omega/\text{km}$.
$C = \dfrac{2\pi\varepsilon_0}{\ln(D/r)} = 9{,}58\ \text{nF/km}$.

</details>

**2.2** Por que linhas de EAT usam feixes de condutores (bundles)?

<details><summary>Gabarito</summary>

Aumentam o raio equivalente: reduzem o gradiente de campo na superfície (menos corona, ruído e perdas) e a reatância série (maior capacidade de transmissão).

</details>

---

## 3. Modelos de linha e regulação

**3.1** Linha curta de 69 kV, 20 km, $z = 0{,}2 + j0{,}45\ \Omega/\text{km}$, alimenta 10 MW com FP 0,9 indutivo a 69 kV no receptor. Calcule a corrente, a tensão no transmissor, a regulação e as perdas.

<details><summary>Gabarito</summary>

$Z = 4 + j9\ \Omega$; $I = \dfrac{10\text{M}}{\sqrt3\cdot69\text{k}\cdot0{,}9} = 93{,}0\ \text{A}$ a −25,8°.
$V_s = V_r + IZ$ (por fase) → $V_{s,linha} \approx 70{,}2\ \text{kV}$ → regulação ≈ **1,8%**.
Perdas: $3I^2R = 3\cdot93^2\cdot4 \approx 104\ \text{kW}$ (1% da carga).

</details>

**3.2** Uma linha de 500 kV tem impedância de surto de 250 Ω. Calcule a potência natural (SIL) e diga o que acontece com a tensão no receptor quando a carga é menor que a SIL.

<details><summary>Gabarito</summary>

$SIL = V^2/Z_c = 1000\ \text{MW}$. Abaixo da SIL a linha gera mais reativo (capacitivo) do que consome → a tensão **sobe** ao longo da linha (efeito Ferranti), exigindo reatores em derivação.

</details>

**3.3** Mantida a potência transmitida, o que acontece com as perdas se a tensão for dobrada?

<details><summary>Gabarito</summary>

A corrente cai à metade → perdas $I^2R$ caem para **1/4**.

</details>

---

## 4. Distribuição

**4.1** Num conjunto com 1000 consumidores, ocorreram no mês: interrupção A (2 h, 300 consumidores) e B (0,5 h, 800 consumidores). Calcule DEC e FEC do mês.

<details><summary>Gabarito</summary>

$DEC = \dfrac{\sum C_a\cdot t}{C_s} = \dfrac{300\cdot2 + 800\cdot0{,}5}{1000} = 1{,}0\ \text{h}$; $FEC = \dfrac{300 + 800}{1000} = 1{,}1$ interrupções.

</details>

**4.2** Compare topologias radial, anel aberto e reticulado (network) quanto a custo e confiabilidade.

<details><summary>Gabarito</summary>

Radial: mais barata, menor confiabilidade (falha desliga tudo a jusante). Anel aberto: permite remanejar carga por chaves de manobra após isolar o defeito. Reticulado: alta confiabilidade (centros urbanos densos), custo e complexidade de proteção elevados.

</details>
