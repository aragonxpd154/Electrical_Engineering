# Exercícios — Fenômenos de Transporte

> Lista autoral por tópico. Água: ρ = 1000 kg/m³, μ = 10⁻³ Pa·s. Ar: ρ = 1,2 kg/m³, $c_p$ = 1005 J/(kg·K). σ = 5,67×10⁻⁸ W/(m²·K⁴).

---

## 1. Estática dos fluidos

**1.1** Qual a pressão manométrica no fundo de uma caixa d'água de 10 m de profundidade?

<details><summary>Gabarito</summary>

$p = \rho gh = 1000\cdot9{,}81\cdot10 = 98{,}1\ \text{kPa}$ (≈ 1 bar).

</details>

**1.2** Por que transformadores de potência têm tanque de expansão (conservador) e relé Buchholz?

<details><summary>Gabarito</summary>

O óleo dilata com a temperatura; o conservador acomoda a variação de volume mantendo o tanque principal cheio. O relé Buchholz, entre os dois, detecta acúmulo de gás (falhas internas incipientes) e fluxo brusco de óleo (falha severa).

</details>

---

## 2. Escoamento: continuidade e Bernoulli

**2.1** Água escoa a 2 m/s num tubo de 100 mm que se reduz para 50 mm. Qual a velocidade no trecho estreito?

<details><summary>Gabarito</summary>

$v_2 = v_1(D_1/D_2)^2 = 2\cdot4 = 8\ \text{m/s}$.

</details>

**2.2** No item 2.1, se a pressão no trecho largo é 200 kPa (mesma cota, sem perdas), qual a pressão no estreito?

<details><summary>Gabarito</summary>

$p_2 = p_1 + \frac12\rho(v_1^2 - v_2^2) = 200 + 0{,}5(4 - 64) = 170\ \text{kPa}$.

</details>

**2.3** Calcule o número de Reynolds para água a 2 m/s num tubo de 100 mm. O escoamento é laminar ou turbulento?

<details><summary>Gabarito</summary>

$Re = \rho vD/\mu = 1000\cdot2\cdot0{,}1/10^{-3} = 2\times10^5$ → **turbulento** (> ~4000).

</details>

---

## 3. Transferência de calor

**3.1 (Condução)** Uma parede de 10 m², 20 cm de espessura e k = 0,8 W/(m·K) tem 20 °C de diferença entre as faces. Qual o fluxo de calor?

<details><summary>Gabarito</summary>

$q = kA\Delta T/L = 0{,}8\cdot10\cdot20/0{,}2 = 800\ \text{W}$.

</details>

**3.2 (Convecção)** Uma superfície de 0,5 m² está 40 °C acima do ar, com h = 25 W/(m²·K). Calcule o calor trocado.

<details><summary>Gabarito</summary>

$q = hA\Delta T = 500\ \text{W}$.

</details>

**3.3 (Radiação)** Uma placa de 1 m² com ε = 0,9 está a 350 K num ambiente a 300 K. Calcule a troca líquida por radiação.

<details><summary>Gabarito</summary>

$q = \varepsilon\sigma A(T_s^4 - T_{amb}^4) \approx 352\ \text{W}$.

</details>

---

## 4. Aplicações eletrônicas

**4.1 (Dissipador)** Um transistor dissipa 20 W. $T_{j,max} = 150\ ^\circ\text{C}$, $T_a = 40\ ^\circ\text{C}$, $R_{jc} = 1{,}5\ ^\circ\text{C/W}$, $R_{cs} = 0{,}5\ ^\circ\text{C/W}$ (pasta térmica). Qual a máxima resistência térmica do dissipador?

<details><summary>Gabarito</summary>

$R_{total} \le (150 - 40)/20 = 5{,}5\ ^\circ\text{C/W}$ → $R_{sa} \le 5{,}5 - 1{,}5 - 0{,}5 = 3{,}5\ ^\circ\text{C/W}$ (use margem: escolha ≤ 3 °C/W).

</details>

**4.2 (Ventilação de transmissor)** Um transmissor dissipa 5 kW em calor. Que vazão de ar é necessária para limitar a elevação de temperatura do ar a 15 °C?

<details><summary>Gabarito</summary>

$\dot m = \dfrac{P}{c_p\Delta T} = \dfrac{5000}{1005\cdot15} = 0{,}332\ \text{kg/s}$ → $\dot V = 0{,}276\ \text{m}^3/\text{s} \approx 995\ \text{m}^3/\text{h}$.

</details>
