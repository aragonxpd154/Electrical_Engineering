# Exercícios — Cálculo Diferencial e Integral I

> Lista autoral por tópico. As listas antigas (com gabarito) estão em [`Materiais/`](Materiais/).

---

## 1. Limites e continuidade

**1.1** Calcule: (a) $\displaystyle\lim_{x\to3}\frac{x^2-9}{x-3}$; (b) $\displaystyle\lim_{x\to0}\frac{\text{sen}\,5x}{x}$; (c) $\displaystyle\lim_{x\to\infty}\left(1+\frac2x\right)^x$.

<details><summary>Gabarito</summary>

(a) $\lim (x+3) = 6$; (b) $5\cdot\lim\frac{\text{sen}\,5x}{5x} = 5$; (c) $e^2$.

</details>

**1.2** Para que valor de $k$ a função $f(x) = \begin{cases}x^2 + k, & x < 1\\ 3x - 1, & x \ge 1\end{cases}$ é contínua?

<details><summary>Gabarito</summary>

$1 + k = 2 \Rightarrow k = 1$.

</details>

---

## 2. Derivadas

**2.1** Derive: (a) $x^3e^{2x}$; (b) $\ln(\cos x)$; (c) $\arctan(x^2)$; (d) $\dfrac{x}{x^2+1}$.

<details><summary>Gabarito</summary>

(a) $e^{2x}(3x^2 + 2x^3)$; (b) $-\tan x$; (c) $\dfrac{2x}{1+x^4}$; (d) $\dfrac{1-x^2}{(x^2+1)^2}$.

</details>

**2.2** A carga num capacitor é $q(t) = 2(1-e^{-5t})$ mC. Encontre a corrente $i(t) = dq/dt$ e seu valor em $t = 0$.

<details><summary>Gabarito</summary>

$i(t) = 10e^{-5t}$ mA → $i(0) = 10\ \text{mA}$.

</details>

**2.3** Calcule $dy/dx$ por derivação implícita em $x^2 + xy + y^2 = 7$ no ponto (1, 2).

<details><summary>Gabarito</summary>

$2x + y + xy' + 2yy' = 0 \Rightarrow y' = -\dfrac{2x+y}{x+2y}$ → em (1,2): $y' = -4/5$.

</details>

---

## 3. Aplicações da derivada

**3.1 (Taxas relacionadas)** Uma escada de 5 m está apoiada numa parede. A base escorrega a 0,5 m/s. Com que velocidade o topo desce quando a base está a 3 m da parede?

<details><summary>Gabarito</summary>

$x^2 + y^2 = 25 \Rightarrow x\dot x + y\dot y = 0$. Com $x = 3$, $y = 4$: $\dot y = -\dfrac{3\cdot0{,}5}{4} = -0{,}375\ \text{m/s}$.

</details>

**3.2 (Máxima transferência de potência)** Uma fonte $V$ com resistência interna $R_{th}$ alimenta uma carga $R$. Mostre por derivada que a potência na carga é máxima em $R = R_{th}$ e calcule $P_{max}$ para $V = 12\ \text{V}$, $R_{th} = 4\ \Omega$.

<details><summary>Gabarito</summary>

$P(R) = \dfrac{V^2R}{(R+R_{th})^2}$; $P'(R) = V^2\dfrac{R_{th} - R}{(R+R_{th})^3} = 0 \Rightarrow R = R_{th}$.
$P_{max} = \dfrac{V^2}{4R_{th}} = \dfrac{144}{16} = 9\ \text{W}$.

</details>

**3.3 (Otimização)** De uma chapa quadrada de 12 cm de lado cortam-se quadrados de lado x nos cantos para formar uma caixa aberta. Qual x maximiza o volume?

<details><summary>Gabarito</summary>

$V = x(12-2x)^2$; $V' = (12-2x)(12-6x) = 0 \Rightarrow x = 2$ (x = 6 anula o volume). $V_{max} = 128\ \text{cm}^3$.

</details>

**3.4 (L'Hôpital)** Calcule $\displaystyle\lim_{x\to0}\frac{e^x - 1 - x}{x^2}$.

<details><summary>Gabarito</summary>

Forma 0/0 duas vezes: $\lim\dfrac{e^x - 1}{2x} = \lim\dfrac{e^x}{2} = \dfrac12$.

</details>

---

## 4. Integrais

**4.1** Calcule: (a) $\int xe^x\,dx$; (b) $\int_0^\pi \text{sen}\,x\,dx$; (c) $\int\text{sen}^2x\,dx$; (d) $\int\dfrac{dx}{x^2-1}$.

<details><summary>Gabarito</summary>

(a) $e^x(x - 1) + C$ (por partes); (b) 2; (c) $\dfrac x2 - \dfrac{\text{sen}\,2x}{4} + C$; (d) $\dfrac12\ln\left|\dfrac{x-1}{x+1}\right| + C$ (frações parciais).

</details>

**4.2** Calcule a área entre $y = x^2$ e $y = x$.

<details><summary>Gabarito</summary>

Interseções em 0 e 1: $\int_0^1(x - x^2)\,dx = \dfrac12 - \dfrac13 = \dfrac16$.

</details>

---

## 5. Aplicações em engenharia elétrica

**5.1 (Valor eficaz)** Mostre que o valor eficaz de $v(t) = V_m\,\text{sen}\,\omega t$ é $V_m/\sqrt2$, usando $V_{rms} = \sqrt{\frac1T\int_0^T v^2\,dt}$.

<details><summary>Gabarito</summary>

$\frac1T\int_0^T V_m^2\,\text{sen}^2(\omega t)\,dt = \frac{V_m^2}{T}\cdot\frac T2 = \frac{V_m^2}{2}$ → $V_{rms} = V_m/\sqrt2$.

</details>

**5.2 (Valor médio)** Calcule o valor médio de uma senoide retificada em meia onda, $v = V_m\,\text{sen}\,\omega t$ para $0 \le \omega t \le \pi$ e zero no restante do período.

<details><summary>Gabarito</summary>

$V_{med} = \frac{1}{2\pi}\int_0^\pi V_m\,\text{sen}\,\theta\,d\theta = \frac{2V_m}{2\pi} = \frac{V_m}{\pi} \approx 0{,}318V_m$.

</details>

**5.3 (Energia no capacitor)** Usando $W = \int v\,i\,dt$ com $i = C\,dv/dt$, mostre que a energia armazenada num capacitor carregado até V é $\frac12CV^2$.

<details><summary>Gabarito</summary>

$W = \int_0^V vC\,dv = \frac12CV^2$.

</details>
