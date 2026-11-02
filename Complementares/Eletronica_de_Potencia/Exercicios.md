# Exercícios — Eletrônica de Potência

> Lista autoral. Provas e relatórios antigos (ELT313, simulações PLECS) em [`Materiais/`](Materiais/). Solucionário do Rashid em `Bibliografia/Solutions/`.

---

**1. (Retificador trifásico)** Qual a tensão média na saída de uma ponte de 6 pulsos não controlada alimentada por 380 V (linha)?

<details><summary>Gabarito</summary>

$V_{dc} = \dfrac{3\sqrt2}{\pi}V_L = 1{,}35\cdot380 \approx 513\ \text{V}$ — é o barramento CC típico de inversores de frequência em 380 V.

</details>

**2. (Buck)** Um conversor buck converte 12 V em 5 V a 100 kHz com L = 47 µH. Calcule o ciclo de trabalho e o ripple de corrente no indutor (modo contínuo).

<details><summary>Gabarito</summary>

$D = 5/12 = 0{,}417$; $\Delta I_L = \dfrac{(V_i - V_o)D}{f_sL} = \dfrac{7\cdot0{,}417}{100\text{k}\cdot47\mu} \approx 0{,}62\ \text{A}$.

</details>

**3. (Boost)** Que ciclo de trabalho eleva 12 V para 24 V num boost ideal?

<details><summary>Gabarito</summary>

$V_o = V_i/(1 - D)$ → D = 0,5.

</details>

**4. (Retificador controlado)** Um retificador monofásico de onda completa totalmente controlado, alimentado por 220 V eficazes com carga altamente indutiva, opera com α = 60°. Qual a tensão média?

<details><summary>Gabarito</summary>

$V_{dc} = \dfrac{2\sqrt2V}{\pi}\cos\alpha = 198\cdot0{,}5 \approx 99\ \text{V}$.

</details>

**5. (Dispositivos)** Compare SCR, MOSFET e IGBT quanto a comando, frequência de chaveamento e faixa de potência.

<details><summary>Gabarito</summary>

SCR: liga por pulso no gate, desliga só quando a corrente zera; baixa frequência, potências muito altas. MOSFET: comando por tensão, alta frequência (até MHz), baixa/média tensão. IGBT: comando por tensão, frequência média (até dezenas de kHz), média/alta tensão e corrente — padrão em inversores de motores.

</details>
