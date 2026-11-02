# Exercícios — Introdução aos Sistemas Elétricos de Potência

> Lista autoral por tópico. Provas e listas antigas (ELT441, com notebook Python) em [`Materiais/`](Materiais/).

---

## 1. Estrutura do setor elétrico

**1.1** Qual o papel de ANEEL, ONS, CCEE e EPE no setor elétrico brasileiro?

<details><summary>Gabarito</summary>

**ANEEL**: regula e fiscaliza (tarifas, qualidade, concessões). **ONS**: opera o Sistema Interligado Nacional (despacho da geração, segurança da rede). **CCEE**: contabiliza e liquida a compra e venda de energia. **EPE**: estudos e planejamento de longo prazo.

</details>

**1.2** Cite níveis de tensão típicos de transmissão e de distribuição no Brasil.

<details><summary>Gabarito</summary>

Transmissão (rede básica): 230, 345, 440, 500 e 765 kV (e ±600/±800 kV em CC). Subtransmissão: 69 e 138 kV. Distribuição primária: 13,8 e 34,5 kV. Secundária: 127/220 V e 220/380 V.

</details>

---

## 2. Sistema por unidade

**2.1** Base 100 MVA e 138 kV. Calcule a impedância e a corrente de base e converta $Z = 10 + j50\ \Omega$ para pu.

<details><summary>Gabarito</summary>

$Z_b = 138^2/100 = 190{,}44\ \Omega$; $I_b = 100\text{M}/(\sqrt3\cdot138\text{k}) = 418\ \text{A}$; $Z = 0{,}0525 + j0{,}263\ \text{pu}$.

</details>

**2.2** Um gerador de 50 MVA, 13,8 kV tem $X'' = 0{,}2\ \text{pu}$ na base própria. Converta para 100 MVA, 13,8 kV.

<details><summary>Gabarito</summary>

$X_{nova} = 0{,}2\cdot\dfrac{100}{50}\cdot\left(\dfrac{13{,}8}{13{,}8}\right)^2 = 0{,}4\ \text{pu}$.

</details>

**2.3** Cite duas vantagens do sistema pu.

<details><summary>Gabarito</summary>

(1) Elimina as relações de transformação dos transformadores (impedância em pu é a mesma dos dois lados). (2) Valores de equipamentos de mesmo tipo ficam em faixas estreitas, facilitando conferência e detecção de erros.

</details>

---

## 3. Fluxo de potência (introdução)

**3.1** Duas barras com $V_1 = V_2 = 1\ \text{pu}$ são ligadas por uma reatância de 0,5 pu. Que ângulo é necessário para transferir 1 pu de potência ativa? Qual o máximo teórico?

<details><summary>Gabarito</summary>

$P = \dfrac{V_1V_2}{X}\text{sen}\,\delta \Rightarrow \text{sen}\,\delta = 0{,}5 \Rightarrow \delta = 30^\circ$. Máximo (δ = 90°): 2 pu — limite de estabilidade estática.

</details>

**3.2** Classifique as barras PQ, PV e de referência (swing) quanto às grandezas conhecidas e incógnitas.

<details><summary>Gabarito</summary>

PQ (carga): conhecidos P e Q; incógnitas V e θ. PV (geração): conhecidos P e |V|; incógnitas Q e θ. Referência: conhecidos |V| e θ; incógnitas P e Q (fecha o balanço de perdas).

</details>

---

## 4. Curto-circuito trifásico simétrico

**4.1** Sistema na base 100 MVA: gerador com X = 0,4 pu, transformador 13,8/138 kV com X = 0,1 pu e linha com X = 0,2625 pu (do item 2.1). Calcule a corrente de curto trifásico no fim da linha (138 kV), em pu e em ampères, com tensão pré-falta 1 pu.

<details><summary>Gabarito</summary>

$X_{tot} = 0{,}4 + 0{,}1 + 0{,}2625 = 0{,}7625\ \text{pu}$ → $I_{cc} = 1/0{,}7625 = 1{,}31\ \text{pu}$ → $1{,}31\cdot418 \approx 549\ \text{A}$.

</details>

**4.2** Qual a potência de curto-circuito nesse ponto e para que ela é usada?

<details><summary>Gabarito</summary>

$S_{cc} = 1{,}31\cdot100 = 131\ \text{MVA}$. Usada para dimensionar a capacidade de interrupção de disjuntores, ajustar proteções e avaliar a "força" da rede (impacto de partidas de motores, harmônicos).

</details>
