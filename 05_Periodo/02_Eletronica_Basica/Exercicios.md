# Exercícios — Eletrônica Básica

> Lista autoral por tópico. Modelo do diodo de silício: queda de 0,7 V. $V_{BE} = 0{,}7\ \text{V}$.

---

## 1. Diodos e junção PN

**1.1** Uma fonte de 12 V alimenta um diodo de silício em série com 1 kΩ. Calcule a corrente e a potência no diodo.

<details><summary>Gabarito</summary>

$I = (12 - 0{,}7)/1000 = 11{,}3\ \text{mA}$; $P_D = 0{,}7\cdot11{,}3\text{m} = 7{,}9\ \text{mW}$.

</details>

**1.2** Qual o resistor para acender um LED (2 V, 20 mA) a partir de 5 V?

<details><summary>Gabarito</summary>

$R = (5-2)/0{,}02 = 150\ \Omega$; potência no resistor 60 mW (1/4 W serve).

</details>

---

## 2. Retificadores e filtros

**2.1** Um transformador entrega 12 V eficazes a um retificador de meia onda. Calcule o pico e o valor médio na carga (ideal e com 0,7 V de queda).

<details><summary>Gabarito</summary>

$V_p = 16{,}97\ \text{V}$; ideal $V_{dc} = V_p/\pi = 5{,}40\ \text{V}$; com diodo: $(16{,}97 - 0{,}7)/\pi = 5{,}18\ \text{V}$.

</details>

**2.2** Ponte retificadora (2 diodos conduzem por vez) a partir de 12 V eficazes, 60 Hz, com capacitor de 2200 µF e carga de 0,5 A. Calcule o pico, o ripple e a tensão média aproximada.

<details><summary>Gabarito</summary>

$V_p = 16{,}97 - 1{,}4 = 15{,}57\ \text{V}$; $V_r = \dfrac{I}{fC} = \dfrac{0{,}5}{120\cdot2200\mu} = 1{,}89\ \text{V}$ (onda completa → 120 Hz); $V_{dc} \approx V_p - V_r/2 = 14{,}6\ \text{V}$.

</details>

**2.3** Qual a tensão reversa de pico (PIV) nos diodos da ponte e num retificador de onda completa com center-tap (cada metade com 12 V eficazes)?

<details><summary>Gabarito</summary>

Ponte: ≈ $V_p$ = 17 V. Center-tap: ≈ $2V_p$ = 34 V.

</details>

---

## 3. Zener e regulação

**3.1** Um Zener de 5,1 V é alimentado por 12 V através de R. A carga consome 20 mA e o Zener precisa de pelo menos 5 mA. Escolha R comercial e calcule a potência máxima no Zener (pior caso: carga desligada).

<details><summary>Gabarito</summary>

$R \le \dfrac{12 - 5{,}1}{0{,}025} = 276\ \Omega$ → **270 Ω**. Sem carga: $I_Z = 6{,}9/270 = 25{,}6\ \text{mA}$ → $P_Z = 130\ \text{mW}$ (use Zener de 0,5 W).

</details>

---

## 4. Transistor bipolar (TBJ)

**4.1** Polarização por divisor: $V_{CC} = 12\ \text{V}$, $R_1 = 10\ \text{k}\Omega$, $R_2 = 2{,}2\ \text{k}\Omega$, $R_E = 1\ \text{k}\Omega$, $R_C = 3{,}3\ \text{k}\Omega$, $\beta = 100$. Calcule $I_C$ e $V_{CE}$ (análise exata com Thévenin).

<details><summary>Gabarito</summary>

$V_{th} = 12\cdot\frac{2{,}2}{12{,}2} = 2{,}16\ \text{V}$; $R_{th} = 1{,}80\ \text{k}\Omega$
$I_B = \dfrac{2{,}16 - 0{,}7}{1{,}80\text{k} + 101\cdot1\text{k}} = 14{,}2\ \mu\text{A}$ → $I_C = 1{,}42\ \text{mA}$
$V_{CE} = 12 - 1{,}42\cdot3{,}3 - 1{,}44\cdot1 \approx 5{,}9\ \text{V}$ → região ativa.

</details>

**4.2 (TBJ como chave)** Um GPIO de 3,3 V deve acionar um relé de 12 V / 60 mA com um transistor de $\beta_{min} = 50$. Dimensione $R_B$ com fator de saturação 2 e diga qual componente não pode faltar.

<details><summary>Gabarito</summary>

$I_B = 2\cdot60\text{m}/50 = 2{,}4\ \text{mA}$ → $R_B = (3{,}3-0{,}7)/2{,}4\text{m} = 1{,}08\ \text{k}\Omega$ → **1 kΩ**. Obrigatório o **diodo de roda livre** em antiparalelo com a bobina.

</details>

---

## 5. MOSFET

**5.1** Um MOSFET canal N tem $V_t = 2\ \text{V}$ e $k = 2\ \text{mA/V}^2$ (com $i_D = \frac k2(V_{GS}-V_t)^2$ em saturação). Para $V_{GS} = 5\ \text{V}$, calcule $i_D$ e o mínimo $V_{DS}$ para estar saturado.

<details><summary>Gabarito</summary>

$i_D = 1\cdot(3)^2 = 9\ \text{mA}$; saturação exige $V_{DS} \ge V_{GS} - V_t = 3\ \text{V}$.

</details>

**5.2** Para chavear 10 A com um MOSFET, compare $R_{DS(on)}$ de 10 mΩ e 50 mΩ quanto à dissipação. Por que preferir MOSFET a TBJ em chaves de potência de baixa tensão?

<details><summary>Gabarito</summary>

$P = I^2R$: 1 W contra 5 W. O MOSFET é comandado por tensão (corrente de gate ~0 em regime), chaveia mais rápido e tem perda de condução baixa — o TBJ exige corrente de base contínua e tem $V_{CE(sat)}$ fixo.

</details>
