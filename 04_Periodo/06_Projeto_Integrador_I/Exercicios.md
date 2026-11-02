# Exercícios — Projeto Integrador em Engenharia I

> Atividades de planejamento de projeto com respostas de referência. Para miniprojetos completos, veja [Projeto Integrador II](../../06_Periodo/05_Projeto_Integrador_II/Exercicios.md).

---

**1.** Escreva requisitos funcionais e não funcionais para um "medidor de consumo de energia com ESP32 para uma tomada".

<details><summary>Gabarito (exemplo)</summary>

Funcionais: medir tensão, corrente, potência e energia acumulada; exibir no celular; registrar histórico.
Não funcionais: erro < 2% na faixa de 0,1–10 A; isolação galvânica entre a rede e o microcontrolador; atualização a cada 1 s; custo < R\$ 150.

</details>

**2.** Que sensor de corrente usar nesse projeto e por quê?

<details><summary>Gabarito (exemplo)</summary>

Um sensor isolado: TC não invasivo (ex.: SCT-013) ou sensor de efeito Hall — garantem isolação da rede. Alternativa: CI medidor dedicado (ex.: HLW8032/ADE7753), que já calcula potência ativa e fator de potência.

</details>

**3.** Monte um cronograma de 8 semanas com marcos.

<details><summary>Gabarito (exemplo)</summary>

S1 requisitos e pesquisa · S2 esquemático e lista de materiais · S3 compra/montagem em protoboard · S4 firmware de leitura · S5 calibração · S6 interface/app · S7 testes e ajustes · S8 relatório e apresentação. Marcos: protótipo funcionando (S4), calibração validada (S5), entrega (S8).

</details>
