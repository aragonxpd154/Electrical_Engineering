# Exercícios — Instalações Elétricas Residenciais (NBR 5410)

> Lista autoral por tópico. Os critérios citados seguem a ABNT NBR 5410 — consulte sempre a versão vigente da norma e as tabelas completas de capacidade de condução. Resistividade do cobre usada: 0,0172 Ω·mm²/m.

---

## 1. Previsão de cargas

**1.1** Uma sala de 3 × 4 m. Calcule a carga mínima de iluminação e o número mínimo de tomadas de uso geral (TUG).

<details><summary>Gabarito</summary>

Área 12 m²: 100 VA nos primeiros 6 m² + 60 VA para cada 4 m² inteiros adicionais (6 m² → 1 incremento) = **160 VA**.
Perímetro 14 m: 1 TUG a cada 5 m ou fração → **3 TUGs** de 100 VA.

</details>

**1.2** Uma cozinha de 3 × 3 m. Quantas TUGs e qual a potência mínima?

<details><summary>Gabarito</summary>

Perímetro 12 m: 1 a cada 3,5 m ou fração → 12/3,5 = 3,43 → **4 TUGs**. Potência: 600 VA para as 3 primeiras e 100 VA para as demais → **1900 VA**.

</details>

---

## 2. Divisão de circuitos

**2.1** Por que chuveiro, ar-condicionado e forno elétrico devem ter circuitos independentes (TUE)?

<details><summary>Gabarito</summary>

Correntes altas e contínuas: circuitos dedicados permitem dimensionar condutor e proteção para aquela carga, evitam sobrecarga dos circuitos de tomadas e limitam o efeito de uma falha a um só equipamento.

</details>

---

## 3. Dimensionamento de condutores

**3.1** Chuveiro de 5400 W em 220 V (circuito com 2 condutores carregados, método B1, sem fatores de correção). Calcule a corrente de projeto e escolha condutor e disjuntor.

<details><summary>Gabarito</summary>

$I_B = 5400/220 = 24{,}5\ \text{A}$. Condutor de **4 mm²** ($I_z$ = 32 A em B1). Disjuntor que atenda $I_B \le I_n \le I_z$: **25 A ou 32 A**. Verifique ainda queda de tensão e o fator de agrupamento se houver outros circuitos no mesmo eletroduto.

</details>

**3.2 (Queda de tensão)** Um circuito monofásico de 127 V, 30 m, alimenta 20 A. Verifique a queda com 2,5 mm² e escolha a seção que atenda o limite de 4%.

<details><summary>Gabarito</summary>

$\Delta V = \dfrac{2\rho LI}{S}$:
2,5 mm²: 8,26 V (6,5%) ✗ · 4 mm²: 5,16 V (4,1%) ✗ · **6 mm²**: 3,44 V (2,7%) ✔

</details>

**3.3** Quais as seções mínimas de condutores para circuitos de iluminação e de tomadas?

<details><summary>Gabarito</summary>

Iluminação: 1,5 mm². Força (tomadas): 2,5 mm² (cobre).

</details>

---

## 4. Proteção

**4.1** Para que serve o dispositivo DR de 30 mA e onde ele é obrigatório?

<details><summary>Gabarito</summary>

Detecta corrente de fuga (diferença entre fase e neutro) e desliga antes que um choque seja fatal (**proteção de pessoas**). Exigido em circuitos de banheiros, cozinhas, lavanderias, áreas externas e tomadas em áreas molhadas, entre outros casos da norma.

</details>

**4.2** Diferencie disjuntor termomagnético, DR e DPS.

<details><summary>Gabarito</summary>

Disjuntor: protege **condutores** contra sobrecarga (térmico) e curto-circuito (magnético). DR: protege **pessoas** contra choques (fuga à terra). DPS: protege **equipamentos** contra surtos (descargas atmosféricas e manobras), desviando-os para a terra.

</details>

---

## 5. Aterramento

**5.1** Descreva os esquemas TN-S, TN-C-S e TT.

<details><summary>Gabarito</summary>

**TN-S**: neutro e proteção (PE) separados em toda a instalação, ponto da alimentação aterrado. **TN-C-S**: PEN combinado num trecho (ex.: rede da concessionária) e separado dentro da instalação. **TT**: alimentação aterrada e massas ligadas a um eletrodo de aterramento próprio, independente — exige DR para a proteção contra choques.

</details>

**5.2** Por que é proibido usar o neutro como condutor de proteção dentro de uma residência (ligando a carcaça ao neutro na tomada)?

<details><summary>Gabarito</summary>

Se o neutro romper, a carcaça fica energizada pela fase através da carga; além disso, a corrente normal de neutro produz tensão na carcaça. O PE não deve conduzir corrente em operação normal.

</details>
