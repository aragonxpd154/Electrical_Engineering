# Exercícios — Meio Ambiente, Sustentabilidade, Eficiência Energética e Energias Renováveis

> Lista autoral por tópico. Valores de tarifa e irradiação são exemplos didáticos; use dados atuais da sua distribuidora e do CRESESB/INPE em projetos reais.

---

## 1. Solar fotovoltaica

**1.1** Uma residência consome 300 kWh/mês. A irradiação local equivale a 4,5 h de sol pleno (HSP) e o desempenho global do sistema é 0,80. Dimensione a potência do gerador e o número de módulos de 550 W.

<details><summary>Gabarito</summary>

$P = \dfrac{300}{30\cdot4{,}5\cdot0{,}8} = 2{,}78\ \text{kWp}$ → 2,78/0,55 = 5,05 → **6 módulos** (3,3 kWp), ou 5 módulos (2,75 kWp) aceitando pequena diferença.

</details>

**1.2** Por que módulos FV perdem potência com o aumento da temperatura, e como isso afeta a instalação?

<details><summary>Gabarito</summary>

A tensão de circuito aberto do silício cai com a temperatura (coeficiente típico ≈ −0,3 a −0,4 %/°C na potência). Em telhados quentes a geração cai; por isso a ventilação sob os módulos importa, e a tensão máxima da string deve ser verificada na **menor** temperatura (quando a tensão é maior).

</details>

---

## 2. Eólica e hidráulica

**2.1** Uma turbina eólica tem rotor de 80 m de diâmetro, $C_p = 0{,}4$, vento de 10 m/s e $\rho = 1{,}225\ \text{kg/m}^3$. Calcule a potência. O que acontece se o vento cair para 5 m/s?

<details><summary>Gabarito</summary>

$P = \frac12\rho Av^3C_p = 0{,}5\cdot1{,}225\cdot5027\cdot1000\cdot0{,}4 \approx 1{,}23\ \text{MW}$. Com 5 m/s: 1/8 → ≈ 154 kW (potência ∝ v³). O limite teórico de $C_p$ é 0,593 (Betz).

</details>

**2.2** Uma PCH tem vazão de 20 m³/s, queda líquida de 50 m e rendimento de 90%. Qual a potência?

<details><summary>Gabarito</summary>

$P = \rho gQH\eta = 1000\cdot9{,}81\cdot20\cdot50\cdot0{,}9 \approx 8{,}83\ \text{MW}$.

</details>

---

## 3. Eficiência energética

**3.1** Troca de 100 lâmpadas fluorescentes de 40 W por LED de 18 W, funcionando 12 h/dia, 22 dias/mês, tarifa R\$ 0,85/kWh. Calcule a economia mensal.

<details><summary>Gabarito</summary>

$\Delta P = 22\ \text{W}\cdot100 = 2{,}2\ \text{kW}$ → $2{,}2\cdot12\cdot22 = 580{,}8\ \text{kWh/mês}$ → **≈ R\$ 494/mês**.

</details>

**3.2** Um motor de 30 kW (saída) opera 6000 h/ano. Compare a energia consumida com rendimento de 90% e de 94%.

<details><summary>Gabarito</summary>

Entrada: 33,33 kW × 31,91 kW → diferença 1,42 kW → **≈ 8510 kWh/ano** economizados. Em motores que operam muitas horas, o custo da energia ao longo da vida supera de longe o preço do motor.

</details>

**3.3** Cite três medidas de eficiência energética para uma sala de equipamentos/abrigo de transmissão.

<details><summary>Gabarito</summary>

(1) Confinamento de corredor quente/frio e vedação de passagens de cabos; (2) ajustar o setpoint do ar-condicionado ao limite aceito pelos equipamentos e usar equipamentos inverter; (3) substituir transmissores antigos por modelos de maior eficiência (ex.: amplificadores Doherty) e desligar equipamentos ociosos.

</details>

---

## 4. Meio ambiente

**4.1** Diferencie impacto ambiental de uma hidrelétrica a fio d'água e com reservatório.

<details><summary>Gabarito</summary>

A fio d'água tem reservatório pequeno: menor área alagada e menor capacidade de regularização (geração depende da vazão do momento). Com reservatório: grande área alagada (deslocamento de populações, perda de vegetação, emissão de metano pela decomposição), mas permite armazenar energia e regular a vazão.

</details>

**4.2** Dado um fator de emissão de 0,04 tCO₂/MWh para a rede, quantas toneladas de CO₂ a economia do item 3.2 evita por ano?

<details><summary>Gabarito</summary>

8,51 MWh × 0,04 = **0,34 tCO₂/ano**. (O fator real do SIN varia ano a ano; consulte o valor publicado pelo MCTI.)

</details>
