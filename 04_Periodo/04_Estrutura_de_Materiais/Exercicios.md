# Exercícios — Estrutura de Materiais

> Lista autoral por tópico. Resistividades a 20 °C: Cu = 1,72×10⁻⁸ Ω·m; Al = 2,82×10⁻⁸ Ω·m. Coeficiente de temperatura do Cu: α = 0,00393 /°C.

---

## 1. Estrutura cristalina

**1.1** Quantos átomos por célula unitária e qual o fator de empacotamento das estruturas CCC (BCC) e CFC (FCC)? Cite um metal de cada.

<details><summary>Gabarito</summary>

CCC: 2 átomos, FE = 0,68 (Fe-α, Cr, W). CFC: 4 átomos, FE = 0,74 (Cu, Al, Au). Os metais CFC costumam ser mais dúcteis — bons para trefilação de fios.

</details>

**1.2** Que efeito os defeitos (impurezas, discordâncias, contornos de grão) têm sobre a condutividade de um metal? Por que se usa cobre eletrolítico de alta pureza?

<details><summary>Gabarito</summary>

Defeitos espalham os elétrons e aumentam a resistividade (regra de Matthiessen: $\rho = \rho_{térmica} + \rho_{impurezas}$). Cobre eletrolítico (≥ 99,9%) minimiza a parcela das impurezas.

</details>

---

## 2. Condutores

**2.1** Calcule a resistência de 100 m de cabo de 2,5 mm² em cobre e em alumínio.

<details><summary>Gabarito</summary>

Cu: $R = \rho L/A = 1{,}72\times10^{-8}\cdot100/2{,}5\times10^{-6} = 0{,}688\ \Omega$. Al: 1,128 Ω (~64% maior). Para a mesma resistência, o Al precisa de seção ~1,6× maior, mas é ~3× mais leve — por isso domina em linhas aéreas.

</details>

**2.2** Um enrolamento de cobre mede 10 Ω a 20 °C. Qual a resistência a 75 °C (temperatura de referência de ensaios de máquinas)?

<details><summary>Gabarito</summary>

$R = 10[1 + 0{,}00393(75-20)] = 12{,}16\ \Omega$.

</details>

---

## 3. Semicondutores

**3.1** Um silício com $n_i = 10^{10}\ \text{cm}^{-3}$ é dopado com $N_D = 10^{16}\ \text{cm}^{-3}$. Calcule n, p e a condutividade ($\mu_n = 1350\ \text{cm}^2/\text{V·s}$).

<details><summary>Gabarito</summary>

$n \approx N_D = 10^{16}$; $p = n_i^2/n = 10^4\ \text{cm}^{-3}$; $\sigma = qn\mu_n = 1{,}6\times10^{-19}\cdot10^{16}\cdot1350 \approx 2{,}16\ \text{S/cm}$.

</details>

**3.2** Por que a resistividade dos metais aumenta com a temperatura, enquanto a dos semicondutores intrínsecos diminui?

<details><summary>Gabarito</summary>

Nos metais o número de portadores é fixo e a vibração da rede aumenta o espalhamento. Nos semicondutores a temperatura gera muitos pares elétron-lacuna (aumento exponencial de portadores), dominando o efeito do espalhamento — princípio dos termistores NTC.

</details>

---

## 4. Dielétricos

**4.1** Um capacitor de 10 µF em 220 V/60 Hz tem $\tan\delta = 0{,}001$. Calcule as perdas dielétricas.

<details><summary>Gabarito</summary>

$P = V^2\omega C\tan\delta = 220^2\cdot377\cdot10^{-5}\cdot0{,}001 \approx 0{,}18\ \text{W}$.

</details>

**4.2** A rigidez dielétrica de um papel isolante é 15 kV/mm. Qual a espessura mínima para 10 kV com fator de segurança 2?

<details><summary>Gabarito</summary>

$d = 2\cdot10/15 = 1{,}33\ \text{mm}$.

</details>

**4.3** Qual a influência da umidade nos isolantes de cabos e transformadores? Que ensaio de campo avalia isso?

<details><summary>Gabarito</summary>

A água aumenta a condutividade e as perdas ($\tan\delta$) e reduz a rigidez dielétrica. Ensaio típico: **resistência de isolamento com megôhmetro** (índice de polarização) e, em transformadores, análise do óleo (teor de água e rigidez).

</details>

---

## 5. Materiais magnéticos

**5.1** Diferencie materiais magnéticos moles e duros, com uma aplicação de cada.

<details><summary>Gabarito</summary>

Moles: ciclo de histerese estreito (baixa coercividade) → núcleos de transformadores e motores (aço-silício, ferrite). Duros: ciclo largo (alta coercividade e remanência) → ímãs permanentes (NdFeB, ferrite de bário).

</details>

**5.2** Pela equação de Steinmetz $P_h = k_hfB_{max}^{1{,}6}$, quanto aumentam as perdas por histerese de um núcleo de 50 Hz operado em 60 Hz com o mesmo $B_{max}$? E se a tensão for mantida (B cai na proporção 50/60)?

<details><summary>Gabarito</summary>

Mesmo B: +20%. Mesma tensão: $B' = B\cdot50/60$ → $P'/P = 1{,}2\cdot(0{,}833)^{1{,}6} = 1{,}2\cdot0{,}747 = 0{,}90$ → cai ~10%.

</details>

**5.3** O que é a temperatura de Curie e por que é importante em ímãs de motores?

<details><summary>Gabarito</summary>

Acima dela o material perde o ferromagnetismo (vira paramagnético). Ímãs que superaquecem podem desmagnetizar de forma irreversível, reduzindo torque.

</details>
