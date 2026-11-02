# Exercícios — Química Inorgânica

> Lista autoral por tópico, com foco em materiais e eletroquímica aplicados à engenharia elétrica.
> Constante de Faraday: $F = 96\,485\ \text{C/mol}$.

---

## 1. Estrutura atômica

**1.1** Faça a distribuição eletrônica do Fe (Z = 26) e do Cu (Z = 29). Qual a particularidade do cobre?

<details><summary>Gabarito</summary>

Fe: $1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,4s^2\,3d^6$.
Cu: $[\text{Ar}]\,3d^{10}\,4s^1$ — exceção à regra de Aufbau (subnível d completo é mais estável). O elétron 4s¹ fracamente ligado contribui para a alta condutividade do cobre.

</details>

---

## 2. Tabela periódica

**2.1** Ordene Na, Mg, Al e Si por raio atômico e por eletronegatividade.

<details><summary>Gabarito</summary>

Raio: Na > Mg > Al > Si (no período, a carga nuclear efetiva cresce). Eletronegatividade: Si > Al > Mg > Na.

</details>

**2.2** Por que o silício e o germânio (grupo 14) são semicondutores, e o que muda ao dopá-los com P (grupo 15) ou B (grupo 13)?

<details><summary>Gabarito</summary>

Têm 4 elétrons de valência e formam ligações covalentes com gap de energia moderado. P fornece um elétron extra (tipo **n**); B cria uma lacuna (tipo **p**).

</details>

---

## 3. Ligações químicas

**3.1** Classifique a ligação e diga se conduz eletricidade: NaCl sólido, NaCl fundido, Cl₂, H₂O pura, Cu.

<details><summary>Gabarito</summary>

NaCl sólido: iônica, não conduz (íons presos). NaCl fundido: conduz (íons móveis). Cl₂: covalente apolar, não conduz. H₂O pura: covalente polar, conduz muito pouco. Cu: metálica, conduz (mar de elétrons).

</details>

---

## 4. Estequiometria

**4.1** Balanceie $\text{Fe} + \text{O}_2 \to \text{Fe}_2\text{O}_3$ e calcule quantos gramas de óxido se formam a partir de 112 g de ferro.

<details><summary>Gabarito</summary>

$4\text{Fe} + 3\text{O}_2 \to 2\text{Fe}_2\text{O}_3$. 112 g Fe = 2 mol → 1 mol Fe₂O₃ = **159,7 g**.

</details>

**4.2** Quantos mols há em 10 g de NaOH?

<details><summary>Gabarito</summary>

M = 40 g/mol → 0,25 mol.

</details>

---

## 5. Eletroquímica

**5.1** Calcule a fem padrão da pilha de Daniell (Zn/Zn²⁺ = −0,76 V; Cu²⁺/Cu = +0,34 V) e identifique ânodo e cátodo.

<details><summary>Gabarito</summary>

$E^\circ = 0{,}34 - (-0{,}76) = 1{,}10\ \text{V}$. Ânodo (oxidação): Zn. Cátodo (redução): Cu.

</details>

**5.2** Uma eletrólise de CuSO₄ usa 2 A durante 1 h. Quantos gramas de cobre se depositam? (M = 63,55 g/mol)

<details><summary>Gabarito</summary>

$m = \dfrac{M\,I\,t}{nF} = \dfrac{63{,}55\cdot2\cdot3600}{2\cdot96\,485} \approx 2{,}37\ \text{g}$.

</details>

**5.3** Explique por que (a) se usa aço galvanizado (zincado) em estruturas de torres, (b) a conexão direta cobre-alumínio exige conector bimetálico.

<details><summary>Gabarito</summary>

(a) O zinco é mais reativo que o ferro e sofre corrosão no lugar dele (**proteção catódica/ânodo de sacrifício**). (b) Metais com potenciais diferentes em contato com umidade formam uma pilha galvânica; o alumínio (ânodo) corrói, aumentando a resistência de contato e causando aquecimento.

</details>

**5.4** Uma bateria chumbo-ácida de 12 V / 60 Ah alimenta uma carga de 5 A. Qual a autonomia ideal? Por que na prática é menor?

<details><summary>Gabarito</summary>

60/5 = 12 h. Na prática a capacidade útil cai com descarga rápida (efeito Peukert), temperatura, envelhecimento e limite de profundidade de descarga recomendada (~50% para prolongar a vida útil).

</details>
