# Exercícios — Circuitos Elétricos I

> Lista autoral organizada por tópico. Resolva no papel e só depois abra o **Gabarito** (clique na seta).
> Convenção: tensões em volts (V), correntes em ampères (A), resistências em ohms (Ω).

---

## 1. Lei de Ohm, potência e associação de resistores

**1.1** Um resistor de 6 Ω está em paralelo com um de 3 Ω, e o conjunto está em série com 4 Ω. Uma fonte de 12 V alimenta o circuito. Calcule a resistência equivalente, a corrente da fonte e a potência dissipada no resistor de 4 Ω.

<details><summary>Gabarito</summary>

$6 \parallel 3 = \dfrac{6\cdot 3}{6+3} = 2\ \Omega$ → $R_{eq} = 2 + 4 = 6\ \Omega$

$I = 12/6 = 2\ \text{A}$ → $P_{4\Omega} = I^2 R = 4\cdot 4 = 16\ \text{W}$

</details>

**1.2** Um divisor de tensão com $R_1 = 8\ \text{k}\Omega$ (em cima) e $R_2 = 4\ \text{k}\Omega$ (embaixo) é alimentado por 12 V. Qual a tensão de saída sobre $R_2$? O que acontece se uma carga de 4 kΩ for ligada na saída?

<details><summary>Gabarito</summary>

Sem carga: $V_o = 12\cdot\dfrac{4}{8+4} = 4\ \text{V}$.

Com carga de 4 kΩ: $R_2 \parallel R_L = 2\ \text{k}\Omega$ → $V_o = 12\cdot\dfrac{2}{8+2} = 2{,}4\ \text{V}$.
A carga "puxa" a tensão para baixo — por isso divisores resistivos só servem para cargas de alta impedância (ex.: entrada de ADC, amplificador operacional).

</details>

**1.3** Um chuveiro de 5400 W / 220 V é ligado por engano em 127 V. Considerando a resistência constante, qual a potência obtida?

<details><summary>Gabarito</summary>

$R = V^2/P = 220^2/5400 = 8{,}96\ \Omega$ → $P' = 127^2/8{,}96 = 1800\ \text{W}$ (≈ 1/3 da nominal, pois $P \propto V^2$).

</details>

---

## 2. Leis de Kirchhoff, análise nodal e de malhas

**2.1 (Nodal)** Uma fonte de 10 V em série com 2 Ω alimenta o nó A. Do nó A para a terra há 4 Ω. Entre os nós A e B há 2 Ω. Do nó B para a terra há 4 Ω, e uma fonte de corrente de 1 A injeta corrente no nó B. Determine $V_A$ e $V_B$.

<details><summary>Gabarito</summary>

Nó A: $\dfrac{V_A-10}{2} + \dfrac{V_A}{4} + \dfrac{V_A-V_B}{2} = 0 \Rightarrow 1{,}25V_A - 0{,}5V_B = 5$

Nó B: $\dfrac{V_B-V_A}{2} + \dfrac{V_B}{4} = 1 \Rightarrow -0{,}5V_A + 0{,}75V_B = 1$

Resolvendo: $V_A = 68/11 \approx 6{,}18\ \text{V}$ e $V_B = 60/11 \approx 5{,}45\ \text{V}$.

</details>

**2.2 (Malhas)** Malha 1: fonte de 12 V e resistor de 6 Ω. Malha 2: resistor de 4 Ω. As duas malhas compartilham um resistor de 4 Ω. Encontre as correntes de malha e a corrente no resistor compartilhado.

<details><summary>Gabarito</summary>

$(6+4)I_1 - 4I_2 = 12$ e $-4I_1 + (4+4)I_2 = 0$

Da segunda: $I_2 = I_1/2$ → $10I_1 - 2I_1 = 12$ → $I_1 = 1{,}5\ \text{A}$, $I_2 = 0{,}75\ \text{A}$.

Corrente no resistor compartilhado: $I_1 - I_2 = 0{,}75\ \text{A}$.

</details>

**2.3** Explique por que a soma das potências fornecidas pelas fontes é igual à soma das potências absorvidas (Teorema de Tellegen) e verifique isso no exercício 2.2.

<details><summary>Gabarito</summary>

É consequência direta das leis de Kirchhoff (conservação de carga e de energia).
Fornecida: $12 \cdot 1{,}5 = 18\ \text{W}$.
Absorvida: $6\cdot1{,}5^2 + 4\cdot0{,}75^2 + 4\cdot0{,}75^2 = 13{,}5 + 2{,}25 + 2{,}25 = 18\ \text{W}$ ✔

</details>

---

## 3. Teoremas de circuitos

**3.1 (Thévenin e máxima transferência)** Uma fonte de 24 V em série com 4 Ω alimenta um resistor de 12 Ω ligado à terra. Do nó entre eles sai um resistor série de 3 Ω até os terminais a-b. Encontre o equivalente de Thévenin visto de a-b e a potência máxima que pode ser entregue a uma carga.

<details><summary>Gabarito</summary>

$V_{th} = 24\cdot\dfrac{12}{4+12} = 18\ \text{V}$

$R_{th} = (4\parallel12) + 3 = 3 + 3 = 6\ \Omega$

Máxima transferência com $R_L = R_{th} = 6\ \Omega$: $P_{max} = \dfrac{V_{th}^2}{4R_{th}} = \dfrac{324}{24} = 13{,}5\ \text{W}$

</details>

**3.2 (Superposição)** Uma fonte de 10 V com 5 Ω em série alimenta um nó X; de X para a terra há 5 Ω, e uma fonte de corrente de 2 A injeta em X. Calcule $V_X$ por superposição.

<details><summary>Gabarito</summary>

Só a fonte de tensão (fonte de corrente aberta): $V' = 10\cdot\frac{5}{10} = 5\ \text{V}$.
Só a fonte de corrente (fonte de tensão em curto): $V'' = 2\cdot(5\parallel5) = 5\ \text{V}$.
$V_X = 5 + 5 = 10\ \text{V}$.

</details>

**3.3** Converta o equivalente de Thévenin do exercício 3.1 em equivalente de Norton.

<details><summary>Gabarito</summary>

$I_N = V_{th}/R_{th} = 18/6 = 3\ \text{A}$, com $R_N = 6\ \Omega$ em paralelo.

</details>

---

## 4. Capacitores, indutores e transitórios

**4.1** Um capacitor de 100 µF, inicialmente descarregado, é carregado por uma fonte de 12 V através de 10 kΩ. Determine a constante de tempo, a expressão $v_C(t)$ e o tempo para atingir 9 V.

<details><summary>Gabarito</summary>

$\tau = RC = 10^4 \cdot 10^{-4} = 1\ \text{s}$ → $v_C(t) = 12(1 - e^{-t})$ V

$9 = 12(1-e^{-t}) \Rightarrow e^{-t} = 0{,}25 \Rightarrow t = \ln 4 \approx 1{,}39\ \text{s}$

</details>

**4.2** Um indutor de 0,5 H em série com 10 Ω é ligado a 12 V em $t=0$. Encontre $\tau$, $i(t)$ e a energia armazenada em regime.

<details><summary>Gabarito</summary>

$\tau = L/R = 0{,}05\ \text{s}$; $i(t) = 1{,}2(1-e^{-20t})$ A; $W = \tfrac12 L I^2 = 0{,}5\cdot0{,}5\cdot1{,}44 = 0{,}36\ \text{J}$.

</details>

**4.3** Circuito RLC série com $R = 10\ \Omega$, $L = 10\ \text{mH}$ e $C = 100\ \mu\text{F}$. Classifique a resposta natural e calcule $\omega_0$, $\alpha$ e $\omega_d$.

<details><summary>Gabarito</summary>

$\omega_0 = 1/\sqrt{LC} = 1/\sqrt{10^{-6}} = 1000\ \text{rad/s}$; $\alpha = R/(2L) = 500\ \text{s}^{-1}$.

Como $\alpha < \omega_0$: **subamortecido**. $\omega_d = \sqrt{\omega_0^2-\alpha^2} = \sqrt{750\,000} \approx 866\ \text{rad/s}$.

Valor de R para amortecimento crítico: $R = 2\sqrt{L/C} = 20\ \Omega$.

</details>

**4.4** Por que a tensão no capacitor e a corrente no indutor não podem variar instantaneamente? Dê uma consequência prática ao desligar uma bobina de relé.

<details><summary>Gabarito</summary>

$i_C = C\,dv/dt$ e $v_L = L\,di/dt$: uma variação instantânea exigiria corrente (ou tensão) infinita.
Ao abrir o circuito de uma bobina, $di/dt$ muito grande gera um pico de tensão $L\,di/dt$ que pode destruir o transistor de acionamento — por isso usa-se **diodo de roda livre** (flyback) em paralelo com a bobina.

</details>

---

## 5. Regime permanente senoidal — fasores

**5.1** Uma carga RL série ($R = 10\ \Omega$, $X_L = 10\ \Omega$) é ligada a 220 V eficazes, 60 Hz. Calcule a impedância, a corrente (módulo e ângulo), a indutância e a potência ativa.

<details><summary>Gabarito</summary>

$Z = 10 + j10 = 14{,}14\angle45^\circ\ \Omega$ → $I = 220\angle0^\circ / 14{,}14\angle45^\circ = 15{,}56\angle{-45^\circ}\ \text{A}$

$L = X_L/\omega = 10/377 = 26{,}5\ \text{mH}$ ; $P = I^2R = 15{,}56^2\cdot10 \approx 2420\ \text{W}$

</details>

**5.2** Calcule a impedância equivalente de $Z_1 = 4 + j3\ \Omega$ em paralelo com $Z_2 = -j5\ \Omega$. O conjunto é indutivo ou capacitivo?

<details><summary>Gabarito</summary>

$Z = \dfrac{Z_1 Z_2}{Z_1+Z_2} = \dfrac{(4+j3)(-j5)}{4-j2} = \dfrac{15 - j20}{4-j2} = 5 - j2{,}5 = 5{,}59\angle{-26{,}6^\circ}\ \Omega$ → **capacitivo**.

</details>

**5.3** Escreva no domínio do tempo a soma $v(t) = 10\cos(\omega t) + 10\,\text{sen}(\omega t)$ usando fasores.

<details><summary>Gabarito</summary>

$10\angle0^\circ + 10\angle{-90^\circ} = 10 - j10 = 14{,}14\angle{-45^\circ}$ → $v(t) = 14{,}14\cos(\omega t - 45^\circ)$.

</details>

---

## 6. Desafio (simulação)

**6.1** Monte o circuito do exercício 3.1 em um simulador (LTspice, Falstad, PLECS ou Qucs-S), varie $R_L$ de 1 Ω a 20 Ω e trace $P_L \times R_L$. Confirme que o máximo ocorre em 6 Ω.

<details><summary>Gabarito</summary>

A curva é $P_L = \dfrac{18^2 R_L}{(6+R_L)^2}$, com pico de 13,5 W em $R_L = 6\ \Omega$. Script Python de referência:

```python
import numpy as np, matplotlib.pyplot as plt
RL = np.linspace(1, 20, 200)
P = 18**2 * RL / (6 + RL)**2
plt.plot(RL, P); plt.xlabel("R_L (Ω)"); plt.ylabel("P (W)"); plt.grid(); plt.show()
```

</details>
