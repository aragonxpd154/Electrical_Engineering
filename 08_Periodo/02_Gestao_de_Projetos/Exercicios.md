# Exercícios — Gestão de Projetos

> Lista autoral por tópico, com exemplos de projetos de engenharia elétrica.

---

## 1. Escopo e EAP

**1.1** Monte uma EAP (estrutura analítica do projeto) em 2 níveis para "Ativar uma retransmissora de TV digital num novo abrigo".

<details><summary>Gabarito (exemplo)</summary>

1. Gestão (cronograma, outorgas/licenças, compras)
2. Infraestrutura (abrigo, energia, aterramento e SPDA, climatização)
3. Sistema irradiante (torre, antena, linha de transmissão)
4. Equipamentos (transmissor, recepção de sinal, monitoração)
5. Comissionamento (medições de MER, espectro e cobertura; documentação)

</details>

---

## 2. Cronograma e caminho crítico

**2.1** Atividades (duração em dias, predecessoras): A(3, —), B(2, A), C(4, A), D(3, B), E(2, C), F(1, D e E). Encontre o caminho crítico, a duração e as folgas.

<details><summary>Gabarito</summary>

A-B-D-F = 9 dias; **A-C-E-F = 10 dias** (crítico). Duração: 10 dias. B e D têm folga total de 1 dia; A, C, E e F têm folga zero.

</details>

**2.2 (PERT)** Uma atividade tem estimativas otimista 2, mais provável 4 e pessimista 12 dias. Calcule a duração esperada e o desvio padrão.

<details><summary>Gabarito</summary>

$t_e = (2 + 4\cdot4 + 12)/6 = 5$ dias; $\sigma = (12 - 2)/6 = 1{,}67$ dia.

</details>

---

## 3. Custos — valor agregado (EVM)

**3.1** BAC = R\$ 100 mil. Na data de controle: PV = 50 mil, EV = 40 mil, AC = 45 mil. Calcule CV, SV, CPI, SPI e a estimativa no término (EAC = BAC/CPI).

<details><summary>Gabarito</summary>

CV = −5 mil (acima do custo); SV = −10 mil (atrasado); CPI = 0,889; SPI = 0,80; EAC = R\$ 112,5 mil.

</details>

---

## 4. Riscos

**4.1** Classifique e proponha resposta para: "atraso na entrega do transmissor importado" (probabilidade média, impacto alto).

<details><summary>Gabarito (referência)</summary>

Risco alto na matriz P×I. Respostas: **mitigar** (pedido antecipado, acompanhamento do despacho/desembaraço), **transferir** parcialmente (multa contratual ao fornecedor) e plano de contingência (equipamento reserva/locação).

</details>

---

## 5. Métodos ágeis

**5.1** Quais os papéis e eventos do Scrum?

<details><summary>Gabarito</summary>

Papéis: Product Owner, Scrum Master, Developers. Eventos: Sprint, Sprint Planning, Daily Scrum, Sprint Review e Sprint Retrospective. Artefatos: Product Backlog, Sprint Backlog e Incremento.

</details>

**5.2** Monte uma matriz RACI para "atualizar o procedimento de partida do transmissor reserva" com supervisor, técnico e estagiário.

<details><summary>Gabarito (exemplo)</summary>

Redigir: técnico **R**, supervisor **A**, estagiário **C**. Testar em campo: técnico **R**, estagiário **R**, supervisor **A**. Aprovar e divulgar: supervisor **R/A**, equipe **I**.

</details>
