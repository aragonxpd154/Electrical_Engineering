# Exercícios — Mecânica Técnica

> Lista autoral por tópico, com aplicações em torres, mastros e suportes. Vídeos e listas resolvidas (FIS233) em [`Materiais/`](Materiais/).

---

## 1. Forças e momentos

**1.1** Duas forças atuam num ponto: 300 N a 0° e 400 N a 90°. Calcule a resultante (módulo e direção).

<details><summary>Gabarito</summary>

$R = \sqrt{300^2 + 400^2} = 500\ \text{N}$ a $\arctan(400/300) = 53{,}1^\circ$.

</details>

**1.2** Uma chave de 0,5 m aplica 200 N perpendicularmente. Qual o momento? E se a força fizer 60° com a chave?

<details><summary>Gabarito</summary>

$M = Fd = 100\ \text{N·m}$; a 60°: $M = 200\cdot0{,}5\cdot\text{sen}\,60^\circ = 86{,}6\ \text{N·m}$.

</details>

---

## 2. Equilíbrio de corpos rígidos

**2.1** Uma viga biapoiada de 6 m recebe uma carga de 12 kN a 2 m do apoio A. Calcule as reações.

<details><summary>Gabarito</summary>

$\Sigma M_A = 0$: $6R_B = 12\cdot2 \Rightarrow R_B = 4\ \text{kN}$; $R_A = 8\ \text{kN}$.

</details>

**2.2** A mesma viga recebe carga distribuída de 2 kN/m em todo o vão. Calcule reações e momento fletor máximo.

<details><summary>Gabarito</summary>

$R_A = R_B = 6\ \text{kN}$; $M_{max} = wL^2/8 = 9\ \text{kN·m}$ (no meio do vão).

</details>

**2.3 (Mastro estaiado)** Um mastro vertical de 10 m recebe força horizontal de vento de 2 kN no topo. Um estai vai do topo até um ponto no solo a 7,5 m da base, do lado oposto ao vento. Calcule a tração no estai e a compressão adicional no mastro (base articulada).

<details><summary>Gabarito</summary>

Comprimento do estai: $\sqrt{10^2 + 7{,}5^2} = 12{,}5\ \text{m}$.
Componente horizontal da tração = 2 kN → $T = 2\cdot\dfrac{12{,}5}{7{,}5} = 3{,}33\ \text{kN}$.
Componente vertical (comprime o mastro): $T\cdot\dfrac{10}{12{,}5} = 2{,}67\ \text{kN}$.

</details>

---

## 3. Treliças

**3.1** Uma treliça triangular tem vão de 4 m e altura de 2 m (nó superior no meio). Uma carga de 10 kN atua no nó superior. Calcule as reações e os esforços nas barras (tração/compressão).

<details><summary>Gabarito</summary>

Reações: 5 kN em cada apoio. As barras inclinadas fazem 45°: $F\,\text{sen}\,45^\circ = 5 \Rightarrow F = 7{,}07\ \text{kN}$ (**compressão**). Banzo inferior: $7{,}07\cos45^\circ = 5\ \text{kN}$ (**tração**).

</details>

**3.2** Quando usar o método dos nós e quando usar o método das seções?

<details><summary>Gabarito</summary>

Nós: quando se quer o esforço em todas as barras (percorre-se nó a nó). Seções (Ritter): quando se quer o esforço em poucas barras específicas no meio da treliça — corta-se e aplica-se equilíbrio de momentos.

</details>

---

## 4. Centroides e momentos de inércia

**4.1** Calcule o centroide de uma seção em L formada por dois retângulos: 100×20 mm (horizontal, na base) e 20×80 mm (vertical, sobre o lado esquerdo do primeiro).

<details><summary>Gabarito</summary>

Retângulo 1: A = 2000 mm², centro (50; 10). Retângulo 2: A = 1600 mm², centro (10; 60).
$\bar x = \dfrac{2000\cdot50 + 1600\cdot10}{3600} = 32{,}2\ \text{mm}$; $\bar y = \dfrac{2000\cdot10 + 1600\cdot60}{3600} = 32{,}2\ \text{mm}$.

</details>

**4.2** Calcule o momento de inércia de um retângulo 100 × 200 mm em relação ao eixo centroidal horizontal. O que acontece se a peça for "deitada"?

<details><summary>Gabarito</summary>

$I = bh^3/12 = 0{,}1\cdot0{,}2^3/12 = 6{,}67\times10^{-5}\ \text{m}^4$. Deitada (h = 0,1): $1{,}67\times10^{-5}\ \text{m}^4$ — 4 vezes menor; por isso vigas são usadas "em pé".

</details>
