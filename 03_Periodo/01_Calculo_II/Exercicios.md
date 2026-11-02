# Exercícios — Cálculo Diferencial e Integral II

> Lista autoral por tópico. Listas antigas com gabarito (séries e Fourier) em [`Materiais/`](Materiais/).

---

## 1. Funções de várias variáveis e derivadas parciais

**1.1** Para $f(x,y) = x^2y + 3xy^2$, calcule $f_x$, $f_y$ e $\nabla f(1, 2)$.

<details><summary>Gabarito</summary>

$f_x = 2xy + 3y^2$; $f_y = x^2 + 6xy$; $\nabla f(1,2) = (16, 13)$.

</details>

**1.2** O potencial elétrico numa região é $V(x,y,z) = x^2 - y^2 + 2z$. Calcule o campo $\mathbf E = -\nabla V$ no ponto (1, 1, 0) e a derivada direcional de V na direção $\mathbf u = (1, 0, 0)$.

<details><summary>Gabarito</summary>

$\nabla V = (2x, -2y, 2)$ → $\mathbf E(1,1,0) = (-2, 2, -2)$ V/m. $D_\mathbf uV = \nabla V\cdot\mathbf u = 2$.

</details>

**1.3** Verifique que $u(x,t) = \text{sen}(x - ct)$ satisfaz a equação da onda $u_{tt} = c^2u_{xx}$.

<details><summary>Gabarito</summary>

$u_{tt} = -c^2\,\text{sen}(x-ct)$ e $u_{xx} = -\text{sen}(x-ct)$ → $u_{tt} = c^2u_{xx}$ ✔

</details>

---

## 2. Máximos, mínimos e Lagrange

**2.1** Encontre e classifique os pontos críticos de $f(x,y) = x^2 + y^2 - 4x + 6y$.

<details><summary>Gabarito</summary>

$f_x = 2x - 4 = 0$, $f_y = 2y + 6 = 0$ → (2, −3). Hessiano: $f_{xx}f_{yy} - f_{xy}^2 = 4 > 0$, $f_{xx} > 0$ → **mínimo**, $f = -13$.

</details>

**2.2** Com 40 m de cerca, qual o retângulo de maior área? Resolva por multiplicadores de Lagrange.

<details><summary>Gabarito</summary>

Maximizar $A = xy$ com $2x + 2y = 40$: $y = 2\lambda$, $x = 2\lambda$ → $x = y = 10\ \text{m}$, $A = 100\ \text{m}^2$ (quadrado).

</details>

---

## 3. Integrais múltiplas

**3.1** Calcule $\displaystyle\int_0^1\int_0^2 (x + y)\,dy\,dx$.

<details><summary>Gabarito</summary>

$\int_0^1 (2x + 2)\,dx = 1 + 2 = 3$.

</details>

**3.2** Use coordenadas polares para calcular $\iint_D (x^2 + y^2)\,dA$, em que D é o disco de raio 2.

<details><summary>Gabarito</summary>

$\int_0^{2\pi}\int_0^2 r^2\cdot r\,dr\,d\theta = 2\pi\cdot\frac{16}{4} = 8\pi$.

</details>

**3.3** Deduza o volume de uma esfera de raio R com coordenadas esféricas.

<details><summary>Gabarito</summary>

$\int_0^{2\pi}\int_0^\pi\int_0^R r^2\,\text{sen}\,\theta\,dr\,d\theta\,d\phi = 2\pi\cdot2\cdot\frac{R^3}{3} = \frac43\pi R^3$.

</details>

**3.4** Uma carga está distribuída num cilindro de raio 1 m e altura 2 m com densidade $\rho_v = 3\rho$ (C/m³, em que $\rho$ é a distância ao eixo). Calcule a carga total.

<details><summary>Gabarito</summary>

$Q = \int_0^2\int_0^{2\pi}\int_0^1 3\rho\cdot\rho\,d\rho\,d\phi\,dz = 3\cdot\frac13\cdot2\pi\cdot2 = 4\pi\ \text{C}$.

</details>

---

## 4. Sequências e séries

**4.1** Determine se convergem: (a) $\sum_{n\ge0}(1/2)^n$; (b) $\sum_{n\ge1}1/n$; (c) $\sum_{n\ge1}1/n^2$; (d) $\sum_{n\ge1}n/3^n$.

<details><summary>Gabarito</summary>

(a) Geométrica, converge para 2; (b) harmônica, **diverge**; (c) série p com p = 2, converge ($\pi^2/6$); (d) teste da razão: $\lim\frac{n+1}{3n} = \frac13 < 1$, converge.

</details>

**4.2** Encontre o raio e o intervalo de convergência de $\sum_{n\ge1}\dfrac{x^n}{n}$.

<details><summary>Gabarito</summary>

R = 1. Em x = 1 diverge (harmônica); em x = −1 converge (alternada). Intervalo: $[-1, 1)$.

</details>

**4.3** Use o polinômio de Taylor de grau 3 para aproximar $\text{sen}(0{,}1)$ e estime o erro.

<details><summary>Gabarito</summary>

$\text{sen}\,x \approx x - x^3/6 = 0{,}1 - 0{,}000167 = 0{,}099833$. Erro $\le x^5/120 \approx 8\times10^{-8}$.

</details>

**4.4** Escreva as séries de Maclaurin de $e^x$, $\cos x$ e $\text{sen}\,x$ e deduza a fórmula de Euler $e^{j\theta} = \cos\theta + j\,\text{sen}\,\theta$.

<details><summary>Gabarito</summary>

$e^x = \sum x^n/n!$; substituindo $x = j\theta$ e separando potências pares (reais, $\cos\theta$) e ímpares (imaginárias, $j\,\text{sen}\,\theta$) obtém-se a fórmula — base de toda a análise fasorial.

</details>

---

## 5. Séries de Fourier

**5.1** Calcule a série de Fourier de $f(x) = x$ em $(-\pi, \pi)$.

<details><summary>Gabarito</summary>

Função ímpar → $a_n = 0$. $b_n = \frac1\pi\int_{-\pi}^\pi x\,\text{sen}\,nx\,dx = \frac{2(-1)^{n+1}}{n}$.
$f(x) = 2\left(\text{sen}\,x - \frac{\text{sen}\,2x}{2} + \frac{\text{sen}\,3x}{3} - \dots\right)$.

</details>

**5.2** Usando 5.1 em $x = \pi/2$, mostre que $1 - \frac13 + \frac15 - \dots = \frac\pi4$.

<details><summary>Gabarito</summary>

$\frac\pi2 = 2\left(1 - \frac13 + \frac15 - \dots\right)$, pois $\text{sen}(n\pi/2)$ vale 1, 0, −1, 0, … ✔

</details>
