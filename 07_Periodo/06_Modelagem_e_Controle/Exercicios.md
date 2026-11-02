# Exercícios — Modelagem e Controle

> Lista autoral por tópico. Listas antigas de Controle I e scripts MATLAB em [`Materiais/`](Materiais/).

---

## 1. Modelagem

**1.1** Obtenha a função de transferência $X(s)/F(s)$ de um sistema massa-mola-amortecedor (m, b, k).

<details><summary>Gabarito</summary>

$m\ddot x + b\dot x + kx = f$ → $\dfrac{X(s)}{F(s)} = \dfrac{1}{ms^2 + bs + k}$.

</details>

**1.2** Modele um motor CC controlado pela armadura (entrada $v_a$, saída velocidade ω), com $R_a$, $L_a$, $K_t = K_b = K$, inércia J e atrito b.

<details><summary>Gabarito</summary>

$\dfrac{\Omega(s)}{V_a(s)} = \dfrac{K}{(L_as + R_a)(Js + b) + K^2}$. Com $L_a \approx 0$, vira 1ª ordem.

</details>

**1.3** Analogia eletromecânica: a que correspondem massa, amortecedor e mola num circuito RLC série (analogia força-tensão)?

<details><summary>Gabarito</summary>

Massa ↔ indutância; amortecedor ↔ resistência; mola ↔ 1/capacitância; velocidade ↔ corrente.

</details>

---

## 2. Diagramas de blocos

**2.1** Reduza: G em malha direta com realimentação negativa H. E se houver realimentação positiva?

<details><summary>Gabarito</summary>

Negativa: $\dfrac{G}{1 + GH}$. Positiva: $\dfrac{G}{1 - GH}$.

</details>

---

## 3. Resposta transitória

**3.1** Para $G(s) = \dfrac{25}{s^2 + 6s + 25}$, calcule $\omega_n$, ζ, sobressinal, tempo de pico e tempo de acomodação (2%).

<details><summary>Gabarito</summary>

$\omega_n = 5$, $\zeta = 0{,}6$; $M_p = e^{-\pi\zeta/\sqrt{1-\zeta^2}} = 9{,}5\%$; $t_p = \pi/(\omega_n\sqrt{1-\zeta^2}) = 0{,}785\ \text{s}$; $t_s \approx 4/(\zeta\omega_n) = 1{,}33\ \text{s}$.

</details>

**3.2** A resposta ao degrau de um forno chega a 63,2% do valor final em 120 s e estabiliza em 80 °C acima da ambiente para 2 kW de entrada. Modele-o como 1ª ordem.

<details><summary>Gabarito</summary>

$G(s) = \dfrac{K}{\tau s + 1}$ com $K = 80/2 = 40\ ^\circ\text{C/kW}$ e $\tau = 120\ \text{s}$.

</details>

---

## 4. Estabilidade e erro em regime

**4.1** Para que valores de K o sistema com polinômio característico $s^3 + 2s^2 + 3s + K$ é estável (Routh-Hurwitz)?

<details><summary>Gabarito</summary>

Tabela: $s^3$: 1, 3 · $s^2$: 2, K · $s^1$: $(6-K)/2$ · $s^0$: K → **0 < K < 6**.

</details>

**4.2** Com realimentação unitária: (a) $G = \dfrac{10}{s+2}$, erro ao degrau? (b) $G = \dfrac{10}{s(s+2)}$, erro à rampa?

<details><summary>Gabarito</summary>

(a) Tipo 0: $K_p = 5$ → $e_{ss} = 1/(1+K_p) = 1/6$. (b) Tipo 1: $K_v = 5$ → $e_{ss} = 1/K_v = 0{,}2$ (erro ao degrau é zero).

</details>

---

## 5. Lugar das raízes e PID

**5.1** Para $G(s) = \dfrac{K}{s(s+4)}$, onde está o ponto de separação e qual K dá ζ = 0,707?

<details><summary>Gabarito</summary>

Separação em s = −2. Polos de malha fechada em $-2 \pm j2$ (ζ = 0,707) → $K = |s||s+4| = 2\sqrt2\cdot2\sqrt2 = 8$.

</details>

**5.2** Explique o efeito de cada ação do PID (P, I, D) na resposta.

<details><summary>Gabarito</summary>

**P**: aumenta a rapidez e reduz o erro, mas pode gerar sobressinal/instabilidade. **I**: elimina o erro em regime (aumenta o tipo do sistema), mas tende a aumentar oscilações e causar *windup*. **D**: antecipa a tendência, amortece e reduz sobressinal, mas amplifica ruído (usa-se filtro na derivada).

</details>

**5.3** Simule o sistema do item 3.1 em Python.

<details><summary>Gabarito</summary>

```python
import control as ct, matplotlib.pyplot as plt
G = ct.tf([25], [1, 6, 25])
t, y = ct.step_response(G)
print(ct.step_info(G))      # Overshoot ≈ 9.5 %, SettlingTime ≈ 1.2–1.3 s
plt.plot(t, y); plt.grid(); plt.show()
```

</details>
