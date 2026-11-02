# Exercícios — Acionamento e Proteção de Sistemas Elétricos

> Lista autoral por tópico. Para eletrônica de potência (retificadores, conversores, inversores), veja também [`Complementares/Eletronica_de_Potencia`](../../Complementares/Eletronica_de_Potencia/).

---

## 1. Comandos elétricos

**1.1** Descreva o circuito de comando de partida direta com selo (botoeiras liga/desliga, contator K1 e relé térmico F1).

<details><summary>Gabarito</summary>

Em série: contato NF do relé térmico (95-96) → botão desliga (NF) → botão liga (NA) → bobina K1. Em paralelo com o botão liga: contato auxiliar NA de K1 (**selo**), que mantém a bobina energizada após soltar o botão. O desliga ou a atuação do térmico interrompem o circuito.

</details>

**1.2** O que é intertravamento numa reversão de motor e como é feito?

<details><summary>Gabarito</summary>

Impede que os contatores de sentido horário e anti-horário sejam acionados ao mesmo tempo (curto entre fases). Faz-se com contatos auxiliares NF de um contator em série com a bobina do outro (intertravamento elétrico) e, idealmente, intertravamento mecânico.

</details>

**1.3** Como ajustar o relé de sobrecarga de um motor de 21,9 A nominais?

<details><summary>Gabarito</summary>

Na corrente nominal do motor (21,9 A), ou até o fator de serviço indicado na placa.

</details>

---

## 2. Partidas e inversores

**2.1** Na partida estrela-triângulo, por que não se deve comutar para triângulo cedo demais?

<details><summary>Gabarito</summary>

Se o motor ainda estiver longe da velocidade nominal, a comutação gera um pico de corrente quase igual ao da partida direta, anulando a vantagem. Comuta-se perto de 90% da rotação.

</details>

**2.2** Cite vantagens do inversor de frequência sobre o soft-starter.

<details><summary>Gabarito</summary>

Controle contínuo de velocidade (economia em bombas e ventiladores, pois $P \propto n^3$), torque nominal desde baixa rotação, rampas de aceleração e frenagem, proteções integradas. O soft-starter só reduz a tensão na partida.

</details>

---

## 3. Proteção

**3.1** O que significam as funções ANSI 50, 51, 50N/51N, 27, 59 e 87?

<details><summary>Gabarito</summary>

50: sobrecorrente instantânea; 51: sobrecorrente temporizada; 50N/51N: idem para neutro/terra; 27: subtensão; 59: sobretensão; 87: diferencial.

</details>

**3.2** Um relé de curva IEC normalmente inversa, $t = TMS\cdot\dfrac{0{,}14}{(I/I_s)^{0{,}02} - 1}$, tem TMS = 0,1. Qual o tempo de atuação para corrente de 10 vezes o ajuste?

<details><summary>Gabarito</summary>

$t = 0{,}1\cdot\dfrac{0{,}14}{10^{0{,}02} - 1} = 0{,}1\cdot\dfrac{0{,}14}{0{,}0471} \approx 0{,}30\ \text{s}$.

</details>

**3.3** O que é seletividade e qual o intervalo de coordenação típico entre relés em cascata?

<details><summary>Gabarito</summary>

Seletividade: atua apenas a proteção mais próxima do defeito, isolando o menor trecho possível. O intervalo de coordenação entre curvas costuma ficar em 0,2–0,4 s (tempo do disjuntor + margem).

</details>

**3.4** Por que se especifica a classe de exatidão do TC de proteção (ex.: 10P20) diferente do TC de medição?

<details><summary>Gabarito</summary>

O TC de proteção precisa manter a exatidão (10% no exemplo) até 20 vezes a corrente nominal, durante curtos; o TC de medição precisa ser exato perto da corrente nominal e é projetado para saturar em correntes altas, protegendo os medidores.

</details>
