# Exercícios — Probabilidade e Estatística

> Lista autoral por tópico, com aplicações em medição, confiabilidade e manutenção.

---

## 1. Estatística descritiva

**1.1** Cinco medições de tensão: 12,1; 11,9; 12,0; 12,3; 11,7 V. Calcule média, variância amostral e desvio padrão.

<details><summary>Gabarito</summary>

$\bar x = 12{,}0\ \text{V}$; desvios: 0,1; −0,1; 0; 0,3; −0,3 → $s^2 = 0{,}20/4 = 0{,}05\ \text{V}^2$; $s = 0{,}224\ \text{V}$.

</details>

**1.2** Por que a variância amostral divide por $n - 1$ e não por $n$?

<details><summary>Gabarito</summary>

Porque a média amostral já foi estimada a partir dos mesmos dados (perde-se um grau de liberdade); dividir por $n-1$ torna o estimador **não viesado**.

</details>

---

## 2. Probabilidade e Bayes

**2.1** Um sensor detecta 95% dos defeitos reais e dá alarme falso em 3% dos equipamentos bons. A taxa de defeito é 2%. Dado um alarme, qual a probabilidade de haver defeito?

<details><summary>Gabarito</summary>

$P(D|A) = \dfrac{0{,}95\cdot0{,}02}{0{,}95\cdot0{,}02 + 0{,}03\cdot0{,}98} = \dfrac{0{,}019}{0{,}0484} \approx 39{,}3\%$.
Mesmo com sensor "bom", a maioria dos alarmes é falsa quando o defeito é raro.

</details>

**2.2** Dois links redundantes falham independentemente com probabilidade 0,05 e 0,08. Qual a probabilidade de perder o serviço (ambos falharem)? E de pelo menos um falhar?

<details><summary>Gabarito</summary>

Ambos: $0{,}05\cdot0{,}08 = 0{,}004$. Pelo menos um: $1 - 0{,}95\cdot0{,}92 = 0{,}126$.

</details>

---

## 3. Variáveis aleatórias

**3.1 (Binomial)** Um lote tem 10 componentes, cada um com 10% de chance de falha. Calcule P(nenhuma falha) e P(no máximo uma falha).

<details><summary>Gabarito</summary>

$0{,}9^{10} = 0{,}349$; $0{,}349 + 10\cdot0{,}1\cdot0{,}9^9 = 0{,}736$.

</details>

**3.2 (Poisson)** Um abrigo de transmissão registra em média 3 falhas por mês. Qual a probabilidade de um mês sem falhas? E de 2 ou mais?

<details><summary>Gabarito</summary>

$P(0) = e^{-3} = 0{,}050$; $P(\ge2) = 1 - e^{-3}(1 + 3) = 0{,}801$.

</details>

**3.3 (Exponencial — confiabilidade)** Um transmissor tem MTBF de 50 000 h. Qual a probabilidade de operar 1 ano (8760 h) sem falhar?

<details><summary>Gabarito</summary>

$R(t) = e^{-t/\text{MTBF}} = e^{-0{,}175} = 0{,}839$ (83,9%).

</details>

**3.4 (Normal)** Resistores de 100 Ω têm desvio padrão de 2 Ω. Que fração está entre 98 e 102 Ω? E dentro da tolerância de ±5%?

<details><summary>Gabarito</summary>

±1σ → 68,3%. ±5 Ω = ±2,5σ → 98,8%.

</details>

---

## 4. Inferência

**4.1** 25 medições da tensão de um barramento deram média 220,5 V e s = 2 V. Construa o IC de 95% para a média.

<details><summary>Gabarito</summary>

$t_{24;\,0{,}025} = 2{,}064$ → $220{,}5 \pm 2{,}064\cdot\frac{2}{5} = 220{,}5 \pm 0{,}83$ → **[219,7; 221,3] V**.

</details>

**4.2** O fabricante garante tensão média de 220 V. Com os dados de 4.1, ao nível de 5%, há evidência de que a média é diferente?

<details><summary>Gabarito</summary>

$t = \dfrac{220{,}5 - 220}{2/5} = 1{,}25 < 2{,}064$ → **não** se rejeita $H_0$ (o IC contém 220 V).

</details>

---

## 5. Confiabilidade de sistemas e regressão

**5.1** Três equipamentos em série, cada um com R = 0,95. Qual a confiabilidade do sistema? E de dois equipamentos iguais em paralelo (redundância)?

<details><summary>Gabarito</summary>

Série: $0{,}95^3 = 0{,}857$. Paralelo: $1 - 0{,}05^2 = 0{,}9975$.

</details>

**5.2** Ajuste uma reta $y = a + bx$ aos pontos (1; 2,1), (2; 3,9), (3; 6,2), (4; 7,8).

<details><summary>Gabarito</summary>

$\bar x = 2{,}5$, $\bar y = 5{,}0$, $S_{xy} = 9{,}7$, $S_{xx} = 5$ → $b = 1{,}94$, $a = 0{,}15$ → $y = 0{,}15 + 1{,}94x$.

```python
import numpy as np
print(np.polyfit([1,2,3,4], [2.1,3.9,6.2,7.8], 1))   # [1.94 0.15]
```

</details>
