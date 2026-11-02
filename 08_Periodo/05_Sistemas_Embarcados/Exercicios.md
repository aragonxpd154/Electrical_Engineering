# Exercícios — Sistemas Embarcados

> Lista autoral por tópico (C para microcontroladores, Linux embarcado e IoT). Projetos antigos de Automação em Tempo Real (C#) em [`Materiais/`](Materiais/).

---

## 1. Temporizadores e interrupções

**1.1** Um AVR a 16 MHz usa prescaler 64. (a) Quanto tempo leva o estouro de um timer de 8 bits? (b) Que valor de comparação (modo CTC, timer de 16 bits) gera interrupção a cada 1 ms?

<details><summary>Gabarito</summary>

Tick = 64/16 MHz = 4 µs. (a) 256 × 4 µs = 1,024 ms. (b) 1 ms/4 µs = 250 ticks → **OCR = 249**.

</details>

**1.2** Liste três boas práticas ao escrever rotinas de interrupção (ISR).

<details><summary>Gabarito</summary>

(1) Ser curta — só sinalizar/copiar dados e deixar o processamento para o laço principal; (2) variáveis compartilhadas declaradas `volatile` e acessadas de forma atômica; (3) não usar funções bloqueantes (printf, delay) dentro da ISR.

</details>

---

## 2. ADC e PWM

**2.1** Um ADC de 12 bits com referência de 3,3 V lê 2048. Qual a tensão? Projete um divisor para medir 0–30 V.

<details><summary>Gabarito</summary>

$V = 2048\cdot3{,}3/4096 = 1{,}65\ \text{V}$. Divisor 30 V → 3,0 V (margem): R1 = 27 kΩ, R2 = 3 kΩ → fator 10.

</details>

**2.2** Um PWM de 8 bits deve ter ciclo de trabalho de 25%. Que valor carregar no registrador de comparação?

<details><summary>Gabarito</summary>

0,25 × 256 = **64**.

</details>

---

## 3. Comunicação serial

**3.1** Quantos bytes por segundo trafegam numa UART a 115 200 baud, 8N1?

<details><summary>Gabarito</summary>

Cada byte usa 10 bits (start + 8 + stop) → 11 520 B/s.

</details>

**3.2** Compare UART, I2C e SPI (fios, endereçamento, velocidade).

<details><summary>Gabarito</summary>

UART: 2 fios (TX/RX), ponto a ponto, assíncrona. I2C: 2 fios (SDA/SCL) com pull-up, vários dispositivos por endereço, 100 kHz–1 MHz típicos. SPI: 4 fios (MOSI/MISO/SCK/CS), um CS por escravo, full-duplex, dezenas de MHz.

</details>

---

## 4. Software embarcado

**4.1** Implemente um buffer circular (FIFO) em C para bytes recebidos pela UART.

<details><summary>Gabarito</summary>

```c
#define TAM 64                       /* potência de 2 */
static volatile uint8_t buf[TAM];
static volatile uint8_t ini = 0, fim = 0;

int fifo_put(uint8_t b) {            /* chamada na ISR */
    uint8_t prox = (fim + 1) & (TAM - 1);
    if (prox == ini) return -1;      /* cheio */
    buf[fim] = b; fim = prox; return 0;
}
int fifo_get(uint8_t *b) {           /* chamada no laço principal */
    if (ini == fim) return -1;       /* vazio */
    *b = buf[ini]; ini = (ini + 1) & (TAM - 1); return 0;
}
```

</details>

**4.2** Escreva um debounce de botão por software (leitura a cada 1 ms, estável por 20 ms).

<details><summary>Gabarito</summary>

```c
uint8_t estado = 0, cont = 0;
void tick_1ms(void) {
    uint8_t leitura = ler_pino();
    if (leitura != estado) {
        if (++cont >= 20) { estado = leitura; cont = 0; }
    } else cont = 0;
}
```

</details>

---

## 5. RTOS e concorrência

**5.1** O que é inversão de prioridade e como a herança de prioridade a resolve?

<details><summary>Gabarito</summary>

Uma tarefa de alta prioridade espera um mutex detido por uma de baixa prioridade, que por sua vez é preemptada por uma de prioridade média — a alta fica bloqueada indefinidamente. Com herança de prioridade, a tarefa que detém o mutex herda temporariamente a prioridade da que espera e libera o recurso rápido.

</details>

---

## 6. IoT e energia

**6.1** Um nó sensor com bateria de 2000 mAh consome 80 mA ativo durante 1% do tempo e 50 µA dormindo. Estime a autonomia.

<details><summary>Gabarito</summary>

$I_{med} = 0{,}01\cdot80 + 0{,}99\cdot0{,}05 = 0{,}85\ \text{mA}$ → 2000/0,85 ≈ 2354 h ≈ **98 dias**.

</details>

**6.2** Proponha uma estrutura de tópicos MQTT para telemetria de vários abrigos de transmissão e diga qual QoS usar para alarmes.

<details><summary>Gabarito</summary>

`transmissao/<abrigo>/<equipamento>/<grandeza>` — ex.: `transmissao/fonte-grande/tx1/potencia_refletida`. Alarmes com **QoS 1** (entrega garantida ao menos uma vez) e mensagem *retained* para o último estado; *Last Will* para detectar nó offline.

</details>

**6.3** Para que serve o watchdog e qual o erro comum ao usá-lo?

<details><summary>Gabarito</summary>

Reinicia o sistema se o software travar. Erro comum: "alimentar" o watchdog dentro de uma ISR de timer — ele continua sendo alimentado mesmo com o laço principal travado.

</details>
