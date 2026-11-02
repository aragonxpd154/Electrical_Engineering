# Exercícios — Laboratório de Física

> Lista autoral sobre tratamento de dados experimentais. Relatórios antigos (FIS224) e normas de relatório em [`Materiais/`](Materiais/).

---

## 1. Algarismos significativos e incerteza

**1.1** Escreva corretamente: (a) 12,3456 ± 0,03 V; (b) 0,004560 m; (c) 1500 Ω com 2 algarismos significativos.

<details><summary>Gabarito</summary>

(a) (12,35 ± 0,03) V — a incerteza define a última casa. (b) 4,560 × 10⁻³ m (4 significativos). (c) 1,5 × 10³ Ω.

</details>

**1.2** Um multímetro de 3½ dígitos tem exatidão ±(0,5% da leitura + 2 dígitos). Na escala de 20 V ele lê 12,00 V. Qual a incerteza?

<details><summary>Gabarito</summary>

0,5% de 12 = 0,06 V; 2 dígitos = 2 × 0,01 = 0,02 V → ±0,08 V → (12,00 ± 0,08) V.

</details>

---

## 2. Propagação de incertezas

**2.1** $R = V/I$ com $V = (5{,}00 \pm 0{,}05)\ \text{V}$ e $I = (0{,}100 \pm 0{,}002)\ \text{A}$. Calcule R e sua incerteza (soma em quadratura).

<details><summary>Gabarito</summary>

$R = 50{,}0\ \Omega$; $\dfrac{\sigma_R}{R} = \sqrt{(1\%)^2 + (2\%)^2} = 2{,}24\%$ → $R = (50{,}0 \pm 1{,}1)\ \Omega$.

</details>

**2.2** Para $P = I^2R$, qual a incerteza relativa de P se I tem 1% e R tem 2%?

<details><summary>Gabarito</summary>

$\dfrac{\sigma_P}{P} = \sqrt{(2\cdot1\%)^2 + (2\%)^2} = 2{,}8\%$ — o expoente multiplica a incerteza relativa.

</details>

---

## 3. Linearização e mínimos quadrados

**3.1** Num pêndulo simples, $T = 2\pi\sqrt{L/g}$. Mediu-se:

| L (m) | 0,20 | 0,40 | 0,60 | 0,80 |
|---|---|---|---|---|
| T² (s²) | 0,81 | 1,60 | 2,42 | 3,21 |

Linearize, ajuste a reta e obtenha g.

<details><summary>Gabarito</summary>

$T^2 = \dfrac{4\pi^2}{g}L$ → reta passando pela origem com inclinação $4\pi^2/g$. Ajuste: inclinação = 4,01 s²/m → $g = 4\pi^2/4{,}01 = 9{,}84\ \text{m/s}^2$.

```python
import numpy as np
b, a = np.polyfit([.2,.4,.6,.8], [.81,1.60,2.42,3.21], 1)
print(b, a, 4*np.pi**2/b)
```

</details>

**3.2** Na descarga de um capacitor, $V(t) = V_0e^{-t/RC}$. Que gráfico deve ser feito para obter RC por regressão linear?

<details><summary>Gabarito</summary>

$\ln V \times t$: reta com inclinação $-1/RC$ e intercepto $\ln V_0$.

</details>

---

## 4. Relatório técnico

**4.1** Liste as seções de um relatório de laboratório e o que vai em cada uma.

<details><summary>Gabarito</summary>

Título/identificação; **Objetivo**; **Fundamentação teórica** (breve); **Materiais e métodos** (equipamentos com modelo e incerteza, montagem); **Resultados** (tabelas e gráficos com unidades e barras de erro); **Discussão** (comparação com o teórico, fontes de erro); **Conclusão**; **Referências**.

</details>
