# Exercícios — Eletrônica Digital

> Lista autoral por tópico. Material antigo (Sistemas Digitais, com relatórios e provas) em [`Materiais/`](Materiais/).

---

## 1. Sistemas de numeração e códigos

**1.1** Converta 156₁₀ para binário e hexadecimal; 0x3F para decimal; 47₁₀ para BCD.

<details><summary>Gabarito</summary>

156 = 1001 1100₂ = 0x9C; 0x3F = 63; 47 = 0100 0111 (BCD).

</details>

**1.2** Represente −45 em complemento de 2 com 8 bits e some com +20.

<details><summary>Gabarito</summary>

+45 = 0010 1101 → inverte e soma 1: **1101 0011**. Somando 0001 0100 (20): 1110 0111 = −25 ✔

</details>

**1.3** Por que se usa código Gray em encoders de posição?

<details><summary>Gabarito</summary>

Valores consecutivos diferem em apenas 1 bit, então a leitura durante uma transição nunca gera um valor muito errado (em binário, de 0111 para 1000 todos os bits mudam e leituras intermediárias espúrias podem aparecer).

</details>

---

## 2. Álgebra booleana e Karnaugh

**2.1** Simplifique $F = \bar AB + AB + A\bar B$.

<details><summary>Gabarito</summary>

$\bar AB + AB = B$; $B + A\bar B = A + B$. **F = A + B** (porta OU).

</details>

**2.2** Simplifique por mapa de Karnaugh $F(A,B,C,D) = \sum m(0, 2, 5, 7, 8, 10, 13, 15)$.

<details><summary>Gabarito</summary>

Os 4 cantos (0, 2, 8, 10) formam $\bar B\bar D$; o bloco central (5, 7, 13, 15) forma $BD$.
$F = \bar B\bar D + BD = \overline{B\oplus D}$ (XNOR).

</details>

**2.3** Aplique De Morgan para implementar $F = AB + CD$ só com portas NAND.

<details><summary>Gabarito</summary>

$F = \overline{\overline{AB}\cdot\overline{CD}}$ → duas NAND de entrada (AB e CD) seguidas de uma NAND de saída.

</details>

---

## 3. Circuitos combinacionais

**3.1** Escreva as equações de saída de um somador completo (entradas A, B, Cᵢₙ).

<details><summary>Gabarito</summary>

$S = A\oplus B\oplus C_{in}$; $C_{out} = AB + C_{in}(A\oplus B)$.

</details>

**3.2** Implemente $F(A,B,C) = \sum m(1, 2, 6, 7)$ com um MUX 4:1 usando A e B como seletores.

<details><summary>Gabarito</summary>

AB = 00 → mintermos 0,1: F = C → I₀ = C. AB = 01 → 2,3: F = $\bar C$ → I₁ = $\bar C$. AB = 10 → 4,5: F = 0 → I₂ = 0. AB = 11 → 6,7: F = 1 → I₃ = 1.

</details>

---

## 4. Sequenciais: flip-flops, registradores e contadores

**4.1** Um flip-flop JK tem J = K = 1. O que ele faz a cada borda de clock? Qual a frequência na saída para clock de 1 MHz?

<details><summary>Gabarito</summary>

Modo *toggle* (inverte a saída) → divide a frequência por 2: 500 kHz.

</details>

**4.2** Quantos flip-flops são necessários para um contador módulo 10? Se o clock é 1 MHz, qual a frequência do bit mais significativo / da saída de "carry"?

<details><summary>Gabarito</summary>

$\lceil\log_210\rceil = 4$ flip-flops. A saída de carry ocorre uma vez a cada 10 pulsos → 100 kHz.

</details>

**4.3** Escreva em Verilog um contador de 4 bits síncrono com reset assíncrono.

<details><summary>Gabarito</summary>

```verilog
module contador4 (input clk, input rst, output reg [3:0] q);
  always @(posedge clk or posedge rst)
    if (rst) q <= 4'd0;
    else     q <= q + 4'd1;
endmodule
```

</details>

---

## 5. Máquinas de estado

**5.1** Projete uma máquina de Moore que detecta a sequência **101** numa entrada serial (com sobreposição). Liste os estados e transições.

<details><summary>Gabarito</summary>

S0 (nada) — x=1 → S1; x=0 → S0.
S1 (viu "1") — x=0 → S2; x=1 → S1.
S2 (viu "10") — x=1 → S3; x=0 → S0.
S3 (viu "101", **saída = 1**) — x=0 → S2 (o "1" final reaproveita); x=1 → S1.

</details>

---

## 6. Interface com o mundo analógico

**6.1** Qual a resolução de um ADC de 10 bits e de um de 12 bits com referência de 3,3 V?

<details><summary>Gabarito</summary>

10 bits: 3,3/1024 = 3,22 mV. 12 bits: 3,3/4096 = 0,806 mV.

</details>

**6.2** Um DAC R-2R de 8 bits com $V_{ref} = 5\ \text{V}$ recebe o código 1000 0000. Qual a tensão de saída?

<details><summary>Gabarito</summary>

$V = 5\cdot128/256 = 2{,}5\ \text{V}$.

</details>
