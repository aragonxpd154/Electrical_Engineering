# Exercícios — Cálculo Numérico

> Lista autoral. Aulas e códigos antigos (MAT271) em [`Materiais/`](Materiais/).

---

**1. (Newton-Raphson)** Aproxime $\sqrt2$ resolvendo $x^2 - 2 = 0$ a partir de $x_0 = 1$ (3 iterações).

<details><summary>Gabarito</summary>

$x_{k+1} = x_k - \dfrac{x_k^2 - 2}{2x_k}$: 1,5 → 1,41667 → 1,414216 (erro ~2×10⁻⁶; convergência quadrática).

</details>

**2. (Bissecção)** Quantas iterações da bissecção são necessárias para achar uma raiz em [0, 1] com erro < 10⁻⁶?

<details><summary>Gabarito</summary>

$1/2^n < 10^{-6} \Rightarrow n \ge 20$.

</details>

**3. (Trapézios)** Aproxime $\int_0^1 e^x dx$ com 4 subintervalos e compare com o valor exato.

<details><summary>Gabarito</summary>

h = 0,25 → $\approx 1{,}7272$; exato $e - 1 = 1{,}7183$; erro ≈ 0,009 (cai com h²).

</details>

**4. (Euler)** Resolva $y' = -2y$, $y(0) = 1$, até t = 0,5 com h = 0,1. Compare com $e^{-1}$.

<details><summary>Gabarito</summary>

$y_{k+1} = 0{,}8y_k$ → $y(0{,}5) \approx 0{,}8^5 = 0{,}3277$; exato 0,3679 (erro de 11% — Euler é de 1ª ordem; use RK4 ou h menor).

</details>

**5. (Gauss-Seidel)** Faça 2 iterações para $4x + y = 9$, $x + 3y = 7$ a partir de (0, 0). Por que converge?

<details><summary>Gabarito</summary>

It. 1: x = 2,25, y = (7 − 2,25)/3 = 1,583. It. 2: x = (9 − 1,583)/4 = 1,854, y = (7 − 1,854)/3 = 1,715. Solução exata: (20/11, 19/11) ≈ (1,818; 1,727). Converge porque a matriz é **diagonalmente dominante**.

</details>
