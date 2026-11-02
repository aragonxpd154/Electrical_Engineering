# Exercícios — Introdução à Programação de Computadores (Python)

> Lista autoral com problemas de engenharia elétrica. Material antigo (INF100/INF101 em Python) em [`Materiais/`](Materiais/).

---

## 1. Variáveis, entrada e saída

**1.1** Leia tensão e corrente e imprima resistência e potência com 2 casas decimais.

<details><summary>Gabarito</summary>

```python
v = float(input("Tensão (V): "))
i = float(input("Corrente (A): "))
print(f"R = {v/i:.2f} Ω  |  P = {v*i:.2f} W")
```

</details>

---

## 2. Decisão

**2.1** Classifique a tensão medida numa tomada de 127 V conforme faixas: adequada (117–133 V), precária (110–117 ou 133–135 V) ou crítica (fora disso).

<details><summary>Gabarito</summary>

```python
v = float(input("V: "))
if 117 <= v <= 133:
    print("adequada")
elif 110 <= v < 117 or 133 < v <= 135:
    print("precária")
else:
    print("crítica")
```
(As faixas são exemplos didáticos; os limites oficiais estão no PRODIST, Módulo 8, da ANEEL.)

</details>

---

## 3. Repetição

**3.1** Aproxime $\pi$ pela série $\sum_{n=1}^{N}1/n^2 = \pi^2/6$ e mostre quantos termos são necessários para errar menos de 0,001.

<details><summary>Gabarito</summary>

```python
import math
s, n = 0.0, 0
while True:
    n += 1
    s += 1/n**2
    if abs(math.sqrt(6*s) - math.pi) < 1e-3:
        break
print(n, math.sqrt(6*s))   # 955 termos: a série converge devagar (erro ≈ 0,95/N)
```

</details>

---

## 4. Funções

**4.1** Escreva `paralelo(*rs)` que devolve a resistência equivalente de qualquer número de resistores em paralelo, e `serie(*rs)`.

<details><summary>Gabarito</summary>

```python
def serie(*rs):
    return sum(rs)

def paralelo(*rs):
    return 1 / sum(1/r for r in rs)

print(serie(4, paralelo(6, 3)))   # 6.0
```

</details>

**4.2** Escreva `codigo_cores(c1, c2, c3)` que recebe as cores das 3 faixas de um resistor e devolve o valor em ohms.

<details><summary>Gabarito</summary>

```python
CORES = ["preto","marrom","vermelho","laranja","amarelo",
         "verde","azul","violeta","cinza","branco"]

def codigo_cores(c1, c2, c3):
    d1, d2, m = (CORES.index(c) for c in (c1, c2, c3))
    return (10*d1 + d2) * 10**m

print(codigo_cores("amarelo", "violeta", "vermelho"))   # 4700
```

</details>

---

## 5. Listas, dicionários e strings

**5.1** Dada uma lista de temperaturas de um abrigo, imprima média, máxima, mínima e quantas leituras passaram de 35 °C.

<details><summary>Gabarito</summary>

```python
t = [28.5, 30.1, 36.2, 34.8, 37.0, 29.9]
print(sum(t)/len(t), max(t), min(t), sum(1 for x in t if x > 35))
```

</details>

**5.2** Conte quantos alarmes de cada tipo existem numa lista como `["VSWR", "TEMP", "VSWR", "FONTE"]`.

<details><summary>Gabarito</summary>

```python
from collections import Counter
print(Counter(["VSWR", "TEMP", "VSWR", "FONTE"]))   # {'VSWR': 2, 'TEMP': 1, 'FONTE': 1}
```

</details>

---

## 6. Arquivos e bibliotecas científicas

**6.1** Um arquivo `amostras.csv` tem uma coluna `tensao` com amostras de uma senoide. Calcule o valor eficaz (RMS) e o valor de pico.

<details><summary>Gabarito</summary>

```python
import numpy as np, pandas as pd
v = pd.read_csv("amostras.csv")["tensao"].to_numpy()
print("RMS =", np.sqrt(np.mean(v**2)), " Pico =", np.max(np.abs(v)))
```

</details>

**6.2** Plote a carga de um capacitor (R = 10 kΩ, C = 100 µF, V = 12 V) de 0 a 5τ e marque o ponto $t = \tau$.

<details><summary>Gabarito</summary>

```python
import numpy as np, matplotlib.pyplot as plt
R, C, V = 10e3, 100e-6, 12
tau = R*C
t = np.linspace(0, 5*tau, 500)
vc = V*(1 - np.exp(-t/tau))
plt.plot(t, vc); plt.plot(tau, V*(1-np.exp(-1)), "o")   # 63,2% de V
plt.xlabel("t (s)"); plt.ylabel("v_C (V)"); plt.grid(); plt.show()
```

</details>
