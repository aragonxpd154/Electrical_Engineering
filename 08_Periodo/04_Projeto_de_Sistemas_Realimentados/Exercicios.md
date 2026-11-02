# Exercícios — Projeto de Sistemas Realimentados

> Lista autoral por tópico. Listas antigas de Controle II (Bode, LR, controle digital) e scripts MATLAB em [`Materiais/`](Materiais/).

---

## 1. Resposta em frequência e margens

**1.1** Para $G(s) = \dfrac{10}{s(s+1)(s+10)}$ em realimentação unitária, calcule a frequência de cruzamento de ganho, a margem de fase, a frequência de cruzamento de fase e a margem de ganho.

<details><summary>Gabarito</summary>

$\omega_{cg} \approx 0{,}78\ \text{rad/s}$, **MF ≈ 47°**. Fase = −180° em $\omega = \sqrt{10} = 3{,}16\ \text{rad/s}$, onde $|G| = 1/11$ → **MG ≈ 20,8 dB** (o ganho pode ser multiplicado por 11 antes da instabilidade).

```python
import control as ct
print(ct.margin(ct.tf([10], [1, 11, 10, 0])))
```

</details>

**1.2** Qual a relação aproximada entre margem de fase e amortecimento num sistema de 2ª ordem?

<details><summary>Gabarito</summary>

$\zeta \approx MF/100$ (válida até ~60°). MF de 47° → ζ ≈ 0,47 → sobressinal ≈ 19%.

</details>

---

## 2. Critério de Nyquist

**2.1** Enuncie o critério de Nyquist (Z = N + P) e diga o que significa cada termo.

<details><summary>Gabarito</summary>

Z = nº de polos de malha fechada no semiplano direito; P = nº de polos de malha aberta no SPD; N = nº de envolvimentos (horários) do ponto −1 pelo diagrama de Nyquist de G(s)H(s). Estável se Z = 0.

</details>

---

## 3. Compensadores

**3.1** Qual o avanço de fase máximo de um compensador $C(s) = \dfrac{Ts + 1}{\alpha Ts + 1}$ com α = 0,1? Em que frequência ocorre?

<details><summary>Gabarito</summary>

$\text{sen}\,\phi_m = \dfrac{1 - \alpha}{1 + \alpha} = 0{,}818$ → $\phi_m = 54{,}9^\circ$, em $\omega_m = \dfrac{1}{T\sqrt\alpha}$.

</details>

**3.2** Quando escolher compensador de avanço e quando de atraso?

<details><summary>Gabarito</summary>

**Avanço**: melhorar a resposta transitória (margem de fase, velocidade). **Atraso**: melhorar o erro em regime (aumentar o ganho em baixas frequências) sem alterar muito o transitório.

</details>

---

## 4. Sintonia de PID

**4.1 (Ziegler-Nichols — malha fechada)** O ganho crítico é $K_u = 10$ e o período de oscilação $T_u = 2\ \text{s}$. Calcule $K_p$, $T_i$ e $T_d$ do PID.

<details><summary>Gabarito</summary>

$K_p = 0{,}6K_u = 6$; $T_i = T_u/2 = 1\ \text{s}$; $T_d = T_u/8 = 0{,}25\ \text{s}$.

</details>

**4.2 (Ziegler-Nichols — curva de reação)** Ensaio em malha aberta: ganho K = 2, atraso L = 1 s, constante T = 5 s. Calcule o PID.

<details><summary>Gabarito</summary>

$K_p = 1{,}2T/(KL) = 3$; $T_i = 2L = 2\ \text{s}$; $T_d = 0{,}5L = 0{,}5\ \text{s}$.

</details>

---

## 5. Controle digital

**5.1** Discretize $G(s) = \dfrac{1}{s + 1}$ com segurador de ordem zero e T = 0,1 s.

<details><summary>Gabarito</summary>

$G(z) = \dfrac{1 - e^{-T}}{z - e^{-T}} = \dfrac{0{,}0952}{z - 0{,}9048}$.

</details>

**5.2** Escreva a lei de controle PI discreta (forma de velocidade) para implementar num microcontrolador.

<details><summary>Gabarito</summary>

$u[k] = u[k-1] + K_p(e[k] - e[k-1]) + K_p\dfrac{T}{T_i}e[k]$, com saturação de $u$ (a forma incremental evita *windup* ao saturar).

</details>

**5.3** Onde devem estar os polos de malha fechada no plano z para estabilidade?

<details><summary>Gabarito</summary>

Dentro do círculo unitário ($|z| < 1$); o mapeamento é $z = e^{sT}$.

</details>
