# Exercícios — Conversão Eletromecânica de Energia

> Lista autoral por tópico. $\mu_0 = 4\pi\times10^{-7}\ \text{H/m}$. Soluções do Fitzgerald em `Bibliografia/Solutions/`.

---

## 1. Circuitos magnéticos

**1.1** Um núcleo de comprimento médio 0,4 m, seção 4 cm² e $\mu_r = 2000$ tem um entreferro de 1 mm. A bobina tem 200 espiras e conduz 1 A. Calcule as relutâncias, o fluxo, a densidade de fluxo e a indutância (despreze espraiamento).

<details><summary>Gabarito</summary>

$\mathcal R_c = \dfrac{l}{\mu_r\mu_0A} = 3{,}98\times10^5\ \text{A/Wb}$; $\mathcal R_g = \dfrac{g}{\mu_0A} = 1{,}99\times10^6\ \text{A/Wb}$

$\mathcal R = 2{,}39\times10^6$ → $\Phi = NI/\mathcal R = 83{,}8\ \mu\text{Wb}$; $B = 0{,}209\ \text{T}$; $L = N^2/\mathcal R = 16{,}8\ \text{mH}$.

Note que 1 mm de ar "pesa" 5× mais que 40 cm de ferro.

</details>

**1.2** Por que se coloca entreferro em indutores de filtro de fontes chaveadas, mesmo reduzindo a indutância?

<details><summary>Gabarito</summary>

O entreferro lineariza o circuito magnético e evita a saturação do núcleo com a componente CC da corrente, além de concentrar a energia armazenada ($W \propto B^2/\mu$ é maior no ar).

</details>

---

## 2. Transformador monofásico

**2.1** Um transformador de 10 kVA, 2200/220 V. Calcule a relação de espiras e as correntes nominais.

<details><summary>Gabarito</summary>

a = 10; $I_1 = 4{,}55\ \text{A}$; $I_2 = 45{,}5\ \text{A}$.

</details>

**2.2** Ensaios no mesmo transformador:
- Vazio (lado BT): 220 V, 2 A, 100 W.
- Curto-circuito (lado AT): 100 V, 4,55 A, 200 W.

Determine $R_{eq}$, $X_{eq}$ (referidos à AT), o rendimento a plena carga com FP 0,8 e a regulação de tensão.

<details><summary>Gabarito</summary>

$R_{eq} = 200/4{,}55^2 = 9{,}68\ \Omega$; $Z_{eq} = 100/4{,}55 = 22{,}0\ \Omega$; $X_{eq} = \sqrt{22^2 - 9{,}68^2} = 19{,}8\ \Omega$.

Rendimento: $\eta = \dfrac{8000}{8000 + 100 + 200} = 96{,}4\%$.

Regulação (aprox.): $\dfrac{I(R\cos\theta + X\,\text{sen}\,\theta)}{V} = \dfrac{4{,}55(9{,}68\cdot0{,}8 + 19{,}8\cdot0{,}6)}{2200} \approx 4{,}0\%$.

</details>

**2.3** Em que carregamento o rendimento desse transformador é máximo?

<details><summary>Gabarito</summary>

Quando perdas no cobre = perdas no ferro: $x^2\cdot200 = 100 \Rightarrow x = 0{,}707$ (70,7% da carga nominal).

</details>

---

## 3. Transformadores trifásicos

**3.1** Um transformador de 500 kVA, 13,8 kV/380 V, Δ-Y. Calcule as correntes de linha nominais em AT e BT. Para que serve o neutro na BT?

<details><summary>Gabarito</summary>

$I_{AT} = \dfrac{500\,000}{\sqrt3\cdot13\,800} = 20{,}9\ \text{A}$; $I_{BT} = 760\ \text{A}$.
O neutro acessível na estrela permite alimentar cargas monofásicas fase-neutro (220 V) e aterrar o sistema.

</details>

**3.2** O que é o deslocamento angular de 30° num transformador Δ-Y (ex.: Dyn1) e por que isso importa ao colocar dois transformadores em paralelo?

<details><summary>Gabarito</summary>

As tensões de linha do secundário ficam defasadas 30° das do primário. Transformadores em paralelo precisam do mesmo grupo de ligação (mesmo deslocamento), além de mesma relação e impedâncias percentuais próximas — senão circulam correntes elevadas entre eles.

</details>

---

## 4. Energia, coenergia e força

**4.1** Um eletroímã tem dois entreferros (polos) de 10 cm² cada, com B = 1 T. Calcule a força de atração.

<details><summary>Gabarito</summary>

Por polo: $F = \dfrac{B^2A}{2\mu_0} = \dfrac{1\cdot10^{-3}}{2\cdot4\pi\times10^{-7}} \approx 398\ \text{N}$ → total ≈ 796 N.

</details>

**4.2** Num sistema magnético linear, mostre que a força pode ser escrita como $F = \frac12 i^2\dfrac{dL}{dx}$.

<details><summary>Gabarito</summary>

Coenergia $W'_m = \frac12L(x)i^2$; $F = \left.\dfrac{\partial W'_m}{\partial x}\right|_{i\ \text{const}} = \frac12i^2\dfrac{dL}{dx}$. A força age no sentido de **aumentar a indutância** (fechar o entreferro).

</details>
