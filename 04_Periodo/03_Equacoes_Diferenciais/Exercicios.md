# Exercícios — Equações Diferenciais

> Lista autoral por tópico, com aplicações em circuitos e sistemas físicos.

---

## 1. EDOs de 1ª ordem

**1.1 (Separável)** Resolva $\dfrac{dy}{dx} = xy$, com $y(0) = 1$.

<details><summary>Gabarito</summary>

$\dfrac{dy}{y} = x\,dx \Rightarrow \ln|y| = \dfrac{x^2}{2} + C$ → $y = e^{x^2/2}$.

</details>

**1.2 (Linear)** Resolva $y' + 2y = 4$, $y(0) = 0$.

<details><summary>Gabarito</summary>

Fator integrante $e^{2t}$: $(ye^{2t})' = 4e^{2t}$ → $y = 2 + Ce^{-2t}$ → $y(t) = 2(1 - e^{-2t})$.

</details>

**1.3 (Exata)** Resolva $(2xy + 3)\,dx + (x^2 - 1)\,dy = 0$.

<details><summary>Gabarito</summary>

$M_y = 2x = N_x$ → exata. $\psi = x^2y + 3x - y$ → solução implícita: $x^2y + 3x - y = C$, ou $y = \dfrac{C - 3x}{x^2 - 1}$.

</details>

**1.4 (Circuito RL)** Um circuito RL série recebe tensão constante V em $t=0$. Escreva e resolva a EDO para $i(t)$.

<details><summary>Gabarito</summary>

$L\dfrac{di}{dt} + Ri = V$, $i(0) = 0$ → $i(t) = \dfrac VR\left(1 - e^{-Rt/L}\right)$.

</details>

**1.5 (Resfriamento de Newton — transformador)** Um transformador desligado está a 90 °C num ambiente a 30 °C. Após 1 h está a 70 °C. Quanto tempo leva (a partir do desligamento) para chegar a 40 °C?

<details><summary>Gabarito</summary>

$T(t) = 30 + 60e^{-kt}$; $70 = 30 + 60e^{-k}$ → $k = \ln(1{,}5) = 0{,}405\ \text{h}^{-1}$.
$40 = 30 + 60e^{-kt}$ → $t = \ln 6/0{,}405 \approx 4{,}4\ \text{h}$.

</details>

---

## 2. EDOs lineares de 2ª ordem

**2.1** Resolva $y'' + 5y' + 6y = 0$.

<details><summary>Gabarito</summary>

$r^2 + 5r + 6 = 0 \Rightarrow r = -2, -3$ → $y = c_1e^{-2t} + c_2e^{-3t}$ (superamortecido).

</details>

**2.2** Resolva $y'' + 4y = 0$, $y(0) = 1$, $y'(0) = 2$.

<details><summary>Gabarito</summary>

$r = \pm 2j$ → $y = c_1\cos2t + c_2\,\text{sen}\,2t$; $c_1 = 1$, $2c_2 = 2$ → $y = \cos 2t + \text{sen}\,2t$.

</details>

**2.3** Resolva $y'' + 2y' + 5y = 0$ e classifique o amortecimento.

<details><summary>Gabarito</summary>

$r = -1 \pm 2j$ → $y = e^{-t}(c_1\cos2t + c_2\,\text{sen}\,2t)$ — **subamortecido** ($\zeta = 1/\sqrt5 \approx 0{,}447$).

</details>

**2.4 (Coeficientes indeterminados)** Encontre uma solução particular de $y'' - y = e^{2t}$.

<details><summary>Gabarito</summary>

$y_p = Ae^{2t}$ → $4A - A = 1$ → $A = 1/3$ → $y_p = e^{2t}/3$. Geral: $y = c_1e^t + c_2e^{-t} + e^{2t}/3$.

</details>

**2.5 (Ressonância)** Encontre a solução particular de $y'' + y = \cos t$ e explique o comportamento.

<details><summary>Gabarito</summary>

A forçante tem a mesma frequência natural, logo tenta-se $y_p = t(A\cos t + B\,\text{sen}\,t)$ → $y_p = \dfrac{t\,\text{sen}\,t}{2}$. A amplitude cresce linearmente com o tempo: **ressonância** sem amortecimento.

</details>

**2.6 (Variação de parâmetros)** Resolva $y'' + y = \sec t$.

<details><summary>Gabarito</summary>

$y_1 = \cos t$, $y_2 = \text{sen}\,t$, $W = 1$.
$u_1 = -\int \text{sen}\,t\sec t\,dt = \ln|\cos t|$; $u_2 = \int \cos t\sec t\,dt = t$.
$y = c_1\cos t + c_2\,\text{sen}\,t + \cos t\ln|\cos t| + t\,\text{sen}\,t$.

</details>

---

## 3. Transformada de Laplace

**3.1** Resolva $y'' + 3y' + 2y = 2$, com $y(0) = y'(0) = 0$.

<details><summary>Gabarito</summary>

$Y(s) = \dfrac{2}{s(s+1)(s+2)} = \dfrac1s - \dfrac{2}{s+1} + \dfrac{1}{s+2}$ → $y(t) = 1 - 2e^{-t} + e^{-2t}$.

</details>

**3.2** Calcule $\mathcal L\{t\,e^{-3t}\}$ e $\mathcal L^{-1}\left\{\dfrac{s+2}{s^2+4s+13}\right\}$.

<details><summary>Gabarito</summary>

$\mathcal L\{te^{-3t}\} = \dfrac{1}{(s+3)^2}$.
$\dfrac{s+2}{(s+2)^2 + 9}$ → $e^{-2t}\cos 3t$.

</details>

**3.3** Use o Teorema do Valor Final para obter $\lim_{t\to\infty} y(t)$ em 3.1, sem inverter a transformada.

<details><summary>Gabarito</summary>

$\lim_{s\to0} sY(s) = \lim_{s\to0}\dfrac{2}{(s+1)(s+2)} = 1$ ✔ (válido porque os polos de $sY(s)$ estão no semiplano esquerdo).

</details>

---

## 4. Sistemas de EDOs

**4.1** Resolva $\mathbf x' = \begin{bmatrix}0 & 1\\ -2 & -3\end{bmatrix}\mathbf x$.

<details><summary>Gabarito</summary>

$\lambda^2 + 3\lambda + 2 = 0 \Rightarrow \lambda = -1, -2$.
$\lambda=-1$: $\mathbf v = (1, -1)$; $\lambda = -2$: $\mathbf v = (1, -2)$.
$\mathbf x(t) = c_1e^{-t}\begin{bmatrix}1\\-1\end{bmatrix} + c_2e^{-2t}\begin{bmatrix}1\\-2\end{bmatrix}$ — nó estável.

</details>

**4.2** Escreva o circuito RLC série ($v_C$ e $i_L$ como estados, entrada $v_s$) na forma de espaço de estados $\mathbf x' = A\mathbf x + Bu$.

<details><summary>Gabarito</summary>

$\dfrac{dv_C}{dt} = \dfrac{i_L}{C}$; $\dfrac{di_L}{dt} = \dfrac{v_s - Ri_L - v_C}{L}$

$A = \begin{bmatrix}0 & 1/C\\ -1/L & -R/L\end{bmatrix}$, $B = \begin{bmatrix}0\\1/L\end{bmatrix}$.

</details>

---

## 5. Prática computacional

**5.1** Resolva numericamente o PVI 3.1 em Python e compare com a solução analítica.

<details><summary>Gabarito</summary>

```python
import numpy as np
from scipy.integrate import solve_ivp
f = lambda t, y: [y[1], 2 - 3*y[1] - 2*y[0]]
t = np.linspace(0, 5, 50)
sol = solve_ivp(f, (0, 5), [0, 0], t_eval=t)
exata = 1 - 2*np.exp(-t) + np.exp(-2*t)
print("erro máximo:", np.max(np.abs(sol.y[0] - exata)))  # da ordem de 1e-4 ou menor
```

</details>
