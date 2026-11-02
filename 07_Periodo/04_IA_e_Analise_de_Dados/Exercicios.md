# Exercícios — Inteligência Artificial e Análise de Dados

> Lista autoral por tópico, em Python (pandas, scikit-learn). Relatórios antigos de Inteligência Computacional em [`Materiais/`](Materiais/).

---

## 1. Manipulação e visualização de dados

**1.1** Um CSV de telemetria tem colunas `timestamp`, `abrigo`, `temperatura`, `potencia_refletida`. Calcule por abrigo a média e o máximo de temperatura e plote a série de um abrigo.

<details><summary>Gabarito</summary>

```python
import pandas as pd
df = pd.read_csv("telemetria.csv", parse_dates=["timestamp"])
print(df.groupby("abrigo")["temperatura"].agg(["mean", "max"]))
df[df.abrigo == "Fonte Grande"].set_index("timestamp")["temperatura"].plot()
```

</details>

**1.2** Detecte leituras anômalas com z-score > 3.

<details><summary>Gabarito</summary>

```python
z = (df.temperatura - df.temperatura.mean()) / df.temperatura.std()
anomalias = df[z.abs() > 3]
```
(Para dados com tendência/sazonalidade, aplique sobre os resíduos de uma média móvel.)

</details>

---

## 2. Regressão

**2.1** Escreva a solução de mínimos quadrados em forma matricial e aplique aos pontos (1; 2,1), (2; 3,9), (3; 6,2), (4; 7,8).

<details><summary>Gabarito</summary>

$\boldsymbol\beta = (X^TX)^{-1}X^T\mathbf y$, com $X = [\mathbf 1\ \mathbf x]$ → $\beta_0 = 0{,}15$, $\beta_1 = 1{,}94$.

</details>

**2.2** O que é sobreajuste (overfitting) e como detectá-lo?

<details><summary>Gabarito</summary>

O modelo decora o ruído do treino e generaliza mal. Detecta-se pelo erro baixo no treino e alto na validação/teste; combate-se com mais dados, regularização, modelos mais simples e validação cruzada.

</details>

---

## 3. Classificação e métricas

**3.1** Um classificador de falhas teve: VP = 40, FP = 10, FN = 5, VN = 45. Calcule acurácia, precisão, revocação (recall) e F1.

<details><summary>Gabarito</summary>

Acurácia = 85/100 = 0,85; precisão = 40/50 = 0,80; recall = 40/45 = 0,889; F1 = 0,842.

</details>

**3.2** Num problema em que 1% dos equipamentos falha, um modelo que sempre diz "sem falha" tem 99% de acurácia. Por que ele é inútil e que métrica revela isso?

<details><summary>Gabarito</summary>

Recall = 0 (não detecta nenhuma falha). Para classes desbalanceadas, use recall, precisão, F1, curva PR/ROC.

</details>

**3.3** Treine uma árvore de decisão com scikit-learn usando divisão treino/teste 80/20.

<details><summary>Gabarito</summary>

```python
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=0)
clf = DecisionTreeClassifier(max_depth=4).fit(Xtr, ytr)
print(classification_report(yte, clf.predict(Xte)))
```

</details>

---

## 4. Agrupamento

**4.1** Execute uma iteração do k-means (k = 2) para os pontos 1, 2, 9, 10, 11 com centroides iniciais 1 e 2.

<details><summary>Gabarito</summary>

Atribuição: {1} → c₁; {2, 9, 10, 11} → c₂. Novos centroides: c₁ = 1; c₂ = 8. Na próxima iteração: {1, 2} e {9, 10, 11} → centroides 1,5 e 10 (converge).

</details>

---

## 5. Redes neurais

**5.1** Um neurônio tem pesos $\mathbf w = (0{,}5;\ -1)$, viés b = 0,2 e ativação sigmoide. Calcule a saída para $\mathbf x = (2;\ 1)$.

<details><summary>Gabarito</summary>

$z = 0{,}5\cdot2 - 1\cdot1 + 0{,}2 = 0{,}2$ → $\sigma(0{,}2) = 1/(1 + e^{-0{,}2}) = 0{,}550$.

</details>

**5.2** Faça um passo de gradiente descendente para $J(w) = (w - 3)^2$ partindo de w = 0 com taxa 0,1.

<details><summary>Gabarito</summary>

$J'(w) = 2(w-3) = -6$ → $w_1 = 0 - 0{,}1(-6) = 0{,}6$.

</details>
