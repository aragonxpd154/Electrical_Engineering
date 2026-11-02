# Exercícios — Economia da Engenharia

> Lista autoral por tópico. Use calculadora financeira, planilha (`VPL`, `TIR`, `PGTO`) ou Python (`numpy_financial`).

---

## 1. Juros e equivalência

**1.1** R\$ 10 000 aplicados a 1% a.m. por 12 meses (juros compostos). Qual o montante? Qual a taxa anual equivalente?

<details><summary>Gabarito</summary>

$M = 10\,000\cdot1{,}01^{12} = R\$\ 11\,268{,}25$; taxa anual equivalente: $1{,}01^{12} - 1 = 12{,}68\%$ a.a.

</details>

---

## 2. Financiamentos

**2.1 (Price)** Financiamento de R\$ 50 000 em 24 meses a 1,5% a.m. Qual a prestação?

<details><summary>Gabarito</summary>

$PMT = PV\dfrac{i}{1 - (1+i)^{-n}} = R\$\ 2\,496{,}21$.

</details>

**2.2 (SAC)** Mesmo financiamento pelo SAC: qual a primeira prestação e como as prestações evoluem?

<details><summary>Gabarito</summary>

Amortização constante = 50 000/24 = 2 083,33; juros do 1º mês = 750 → **R\$ 2 833,33**. As prestações caem linearmente (os juros incidem sobre o saldo, que diminui).

</details>

---

## 3. Análise de investimentos

**3.1** Um projeto custa R\$ 100 000 e gera R\$ 30 000/ano por 5 anos. Com TMA de 10% a.a., calcule VPL, TIR, payback simples e descontado. O projeto é viável?

<details><summary>Gabarito</summary>

Fator de valor presente: 3,7908 → $VPL = 30\,000\cdot3{,}7908 - 100\,000 = R\$\ 13\,724$.
TIR ≈ **15,2%** a.a. (> TMA). Payback simples: 3,33 anos. Payback descontado: ≈ 4,26 anos.
VPL > 0 e TIR > TMA → **viável**.

</details>

**3.2** Explique por que VPL e TIR podem dar ordenações diferentes ao comparar dois projetos mutuamente exclusivos. Qual critério prevalece?

<details><summary>Gabarito</summary>

Projetos com escalas ou distribuições de fluxo diferentes: a TIR pressupõe reinvestimento à própria TIR, o VPL à TMA. Para projetos mutuamente exclusivos prevalece o **VPL** (ou a TIR incremental).

</details>

---

## 4. Depreciação e substituição

**4.1** Um transmissor de R\$ 400 000 tem vida útil de 10 anos e valor residual de R\$ 40 000. Qual a depreciação linear anual?

<details><summary>Gabarito</summary>

(400 000 − 40 000)/10 = **R\$ 36 000/ano**.

</details>

**4.2** Um transmissor antigo consome R\$ 60 000/ano a mais de energia e manutenção que um novo. O novo custa R\$ 250 000 (vida 10 anos, TMA 10%). Pelo custo anual equivalente, vale a troca?

<details><summary>Gabarito</summary>

CAUE do investimento: $250\,000\cdot\dfrac{0{,}1}{1 - 1{,}1^{-10}} = R\$\ 40\,686/\text{ano}$ < R\$ 60 000 de economia → **vale a troca** (sem considerar o valor de revenda do antigo nem ganhos de confiabilidade, que reforçam a decisão).

</details>

---

## 5. Prática

**5.1** Calcule VPL e TIR do item 3.1 em Python.

<details><summary>Gabarito</summary>

```python
import numpy_financial as npf
fluxo = [-100000] + [30000]*5
print(npf.npv(0.10, fluxo), npf.irr(fluxo))   # 13723.6  0.1524
```

</details>
