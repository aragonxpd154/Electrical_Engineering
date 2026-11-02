# Exercícios — Projeto Integrador em Engenharia II

> Propostas de miniprojetos integrando o que foi visto até o 6º período (circuitos, eletrônica, digital, instrumentação e sinais). Cada uma tem critérios de aceitação — o "gabarito" é uma solução de referência resumida.

---

## Projeto A — Monitor de temperatura e tensão com alarme

**Requisitos**: medir temperatura (NTC ou DS18B20) e tensão de uma fonte de 0–30 V com ESP32; acender LED e enviar mensagem quando T > 35 °C ou V fora de ±10%.

**Critérios de aceitação**: erro de tensão < 2%; alarme em < 5 s; registro com data/hora.

<details><summary>Solução de referência</summary>

- Divisor de tensão 30 V → 3,0 V: R1 = 27 kΩ, R2 = 3 kΩ (corrente ≈ 1 mA; use capacitor de 100 nF na entrada do ADC).
- Calibrar o ADC do ESP32 (não linear nas extremidades) com 2 pontos de referência.
- Filtro média móvel/exponencial (ver Sinais e Sistemas, 4.3).
- Publicar via MQTT/HTTP; usar NTP para data/hora.

</details>

---

## Projeto B — Fonte linear regulada 0–12 V / 1 A

**Requisitos**: transformador + ponte + filtro + regulador ajustável (LM317) com proteção.

**Critérios**: ripple < 50 mV a 1 A; dissipador dimensionado.

<details><summary>Solução de referência</summary>

- Trafo 15 V eficazes → pico ≈ 19,8 V após a ponte.
- Capacitor: para ripple de 2 V antes do regulador, $C = I/(f V_r) = 1/(120\cdot2) \approx 4700\ \mu\text{F}$.
- LM317: $V_o = 1{,}25(1 + R_2/R_1)$, com R1 = 240 Ω e R2 = potenciômetro de 2,2 kΩ.
- Pior caso de dissipação (saída próxima de 0 V a 1 A): ≈ 18 W → dissipador com $R_{sa}$ ≲ 3 °C/W (ver Fenômenos de Transporte, 4.1) ou limitar a corrente em baixa tensão.

</details>

---

## Projeto C — Analisador de espectro de áudio com FFT

**Requisitos**: amostrar um microfone a 8 kHz e exibir o espectro em tempo real.

<details><summary>Solução de referência</summary>

Filtro anti-aliasing passa-baixas (~3,5 kHz, Sallen-Key), ADC a 8 kHz, janela de Hann + FFT de 256 pontos (resolução 31,25 Hz), módulo em dB. Validar com tom puro de gerador de sinais.

</details>
