# Exercícios — Instalações Elétricas Industriais

> Lista autoral por tópico. Relatórios antigos de Qualidade de Energia (simulações Simulink) em [`Materiais/`](Materiais/).

---

## 1. Demanda e transformador

**1.1** Uma indústria tem 800 kW instalados, fator de demanda 0,8 e FP 0,92. Dimensione o transformador (potências padronizadas: 500, 750, 1000 kVA).

<details><summary>Gabarito</summary>

Demanda: 640 kW → 640/0,92 = 696 kVA → **750 kVA**.

</details>

---

## 2. Correção do fator de potência

**2.1** Uma carga de 500 kW tem FP 0,80. Que banco de capacitores leva o FP a 0,92?

<details><summary>Gabarito</summary>

$Q_c = P(\tan\varphi_1 - \tan\varphi_2) = 500(0{,}75 - 0{,}426) \approx 162\ \text{kvar}$.

</details>

**2.2** Por que bancos de capacitores em redes com muitos harmônicos precisam de reatores de dessintonia?

<details><summary>Gabarito</summary>

O capacitor com a indutância da rede forma um circuito ressonante; se a ressonância cair perto de uma harmônica presente (5ª, 7ª), as correntes e tensões harmônicas são amplificadas, queimando capacitores. O reator desloca a ressonância para abaixo da 5ª (ex.: 189 Hz).

</details>

---

## 3. Curto-circuito

**3.1** Um transformador de 750 kVA, 380 V, impedância 5%. Calcule a corrente nominal e a corrente de curto trifásico nos terminais de BT (rede de MT considerada infinita).

<details><summary>Gabarito</summary>

$I_n = \dfrac{750\,000}{\sqrt3\cdot380} = 1140\ \text{A}$; $I_{cc} = I_n/0{,}05 \approx 22{,}8\ \text{kA}$. A capacidade de interrupção dos disjuntores do QGBT deve superar esse valor.

</details>

---

## 4. Qualidade de energia

**4.1** Uma corrente tem fundamental de 100 A, 5ª harmônica de 20 A e 7ª de 14 A. Calcule a DHT de corrente e o valor eficaz total.

<details><summary>Gabarito</summary>

$DHT_i = \sqrt{20^2 + 14^2}/100 = 24{,}4\%$; $I_{rms} = \sqrt{100^2 + 20^2 + 14^2} = 102{,}9\ \text{A}$.

</details>

**4.2** Por que o condutor neutro pode sobreaquecer em instalações com muitas fontes chaveadas monofásicas?

<details><summary>Gabarito</summary>

As harmônicas de ordem múltipla de 3 (3ª, 9ª…) estão em fase nas três fases e **somam-se** no neutro em vez de se cancelar — a corrente de neutro pode superar a das fases.

</details>

**4.3** Diferencie afundamento de tensão (sag), interrupção e flicker.

<details><summary>Gabarito</summary>

Afundamento: redução momentânea (0,1–0,9 pu) por ciclos a segundos, típica de curtos na rede ou partidas de motores. Interrupção: tensão abaixo de 0,1 pu. Flicker: flutuação repetitiva da tensão que causa cintilação luminosa perceptível (fornos a arco, soldas).

</details>

---

## 5. SPDA

**5.1** Quais os raios da esfera rolante para as classes de SPDA I a IV (NBR 5419)? Que classe é típica de estruturas de telecomunicação?

<details><summary>Gabarito</summary>

Classe I: 20 m; II: 30 m; III: 45 m; IV: 60 m. Estações de telecomunicação e radiodifusão costumam exigir níveis elevados (I ou II), definidos pela análise de risco da norma.

</details>

**5.2** Por que todas as massas e o aterramento do sistema irradiante de uma torre devem ser equipotencializados no mesmo barramento?

<details><summary>Gabarito</summary>

Durante uma descarga, a corrente eleva o potencial da malha; se partes estiverem em referências diferentes, surgem diferenças de potencial perigosas entre elas (centelhamento, danos a equipamentos e risco a pessoas). A equipotencialização faz tudo subir junto.

</details>
