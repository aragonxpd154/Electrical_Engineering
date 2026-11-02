# Exercícios — Robótica Industrial

> Lista autoral por tópico. Material antigo (listas, trabalhos e aulas) em [`Materiais/`](Materiais/).

---

## 1. Rotações e transformações homogêneas

**1.1** Escreva $R_z(90^\circ)$ e aplique ao ponto (1, 0, 0).

<details><summary>Gabarito</summary>

$R_z(90^\circ) = \begin{bmatrix}0&-1&0\\1&0&0\\0&0&1\end{bmatrix}$ → (0, 1, 0).

</details>

**1.2** Um sistema {B} está rotacionado 90° em z e transladado (2, 0, 0) em relação a {A}. Escreva $^AT_B$ e calcule as coordenadas em {A} do ponto $^Bp = (1, 0, 0)$.

<details><summary>Gabarito</summary>

$^AT_B = \begin{bmatrix}0&-1&0&2\\1&0&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}$ → $^Ap = (2, 1, 0)$.

</details>

---

## 2. Cinemática direta

**2.1** Um braço planar 2R tem $L_1 = 1\ \text{m}$, $L_2 = 0{,}5\ \text{m}$, $\theta_1 = 30^\circ$, $\theta_2 = 45^\circ$. Calcule a posição do efetuador.

<details><summary>Gabarito</summary>

$x = L_1\cos\theta_1 + L_2\cos(\theta_1+\theta_2) = 0{,}866 + 0{,}129 = 0{,}995\ \text{m}$
$y = L_1\,\text{sen}\,\theta_1 + L_2\,\text{sen}(\theta_1+\theta_2) = 0{,}5 + 0{,}483 = 0{,}983\ \text{m}$

</details>

**2.2** Monte a tabela de Denavit-Hartenberg do braço 2R planar.

<details><summary>Gabarito</summary>

| i | $a_{i}$ | $\alpha_{i}$ | $d_i$ | $\theta_i$ |
|---|---|---|---|---|
| 1 | $L_1$ | 0 | 0 | $\theta_1$ |
| 2 | $L_2$ | 0 | 0 | $\theta_2$ |

(Convenção DH clássica.)

</details>

---

## 3. Cinemática inversa

**3.1** Para $L_1 = L_2 = 1$, encontre $\theta_1$ e $\theta_2$ que levam o efetuador a (1, 1). Há quantas soluções?

<details><summary>Gabarito</summary>

$\cos\theta_2 = \dfrac{x^2 + y^2 - L_1^2 - L_2^2}{2L_1L_2} = 0$ → $\theta_2 = \pm90^\circ$.
Com $\theta_2 = +90^\circ$: $\theta_1 = \text{atan2}(1,1) - \text{atan2}(1, 1) = 0^\circ$. Com $\theta_2 = -90^\circ$: $\theta_1 = 90^\circ$.
**Duas soluções** (cotovelo para cima/para baixo).

</details>

---

## 4. Jacobiano e singularidades

**4.1** Escreva o jacobiano do braço 2R e encontre as configurações singulares.

<details><summary>Gabarito</summary>

$J = \begin{bmatrix}-L_1s_1 - L_2s_{12} & -L_2s_{12}\\ L_1c_1 + L_2c_{12} & L_2c_{12}\end{bmatrix}$, $\det J = L_1L_2\,\text{sen}\,\theta_2$.
Singular em $\theta_2 = 0^\circ$ (braço esticado) e $180^\circ$ (dobrado) — perde-se um grau de liberdade no espaço cartesiano.

</details>

**4.2** Qual o espaço de trabalho de um braço 2R com $L_1 = 1$ e $L_2 = 0{,}5$?

<details><summary>Gabarito</summary>

Coroa circular: $0{,}5 \le r \le 1{,}5\ \text{m}$ (sem limites de junta).

</details>

---

## 5. Aplicação e segurança

**5.1** Quantos graus de liberdade são necessários para posicionar e orientar arbitrariamente uma ferramenta no espaço? Por que robôs de paletização costumam ter só 4?

<details><summary>Gabarito</summary>

6 (3 de posição + 3 de orientação). Na paletização a ferramenta só precisa girar em torno do eixo vertical — 4 eixos bastam e o robô fica mais simples, rápido e barato.

</details>

**5.2** Cite três medidas de segurança exigidas para células robotizadas (NR-12 / ISO 10218).

<details><summary>Gabarito</summary>

Proteções físicas (grades) com intertravamento de portas; dispositivos de parada de emergência; sensores de presença (cortinas de luz, scanners) e velocidade reduzida em modo de ensino/manutenção.

</details>
