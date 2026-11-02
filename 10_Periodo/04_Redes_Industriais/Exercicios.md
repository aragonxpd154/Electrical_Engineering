# Exercícios — Redes Industriais de Computadores

> Lista autoral por tópico. Material antigo de Automação (arquitetura, redes, programas de CLP) em [`Materiais/`](Materiais/).

---

## 1. Endereçamento IP

**1.1** Divida 192.168.10.0/24 em 4 sub-redes iguais. Dê máscara, endereço de rede, faixa de hosts e broadcast da primeira.

<details><summary>Gabarito</summary>

/26 → máscara 255.255.255.192, 62 hosts por sub-rede.
1ª: rede 192.168.10.0, hosts .1 a .62, broadcast .63. (As demais começam em .64, .128 e .192.)

</details>

**1.2** Por que separar a rede de equipamentos de transmissão da rede administrativa (VLANs/firewall)?

<details><summary>Gabarito</summary>

Segurança (reduz a superfície de ataque aos equipamentos críticos), contenção de broadcast/multicast e de falhas, e QoS para o tráfego de controle e vídeo.

</details>

---

## 2. Ethernet industrial: VLAN, STP e IGMP

**2.1** Quantas VLANs o 802.1Q permite e por quê?

<details><summary>Gabarito</summary>

O campo VID tem 12 bits → 4096 valores, com 0 e 4095 reservados → **4094 VLANs** utilizáveis.

</details>

**2.2** Como o STP elege a ponte raiz e por que a reconvergência lenta é um problema em redes de vídeo/TS?

<details><summary>Gabarito</summary>

A raiz é o switch com menor Bridge ID (prioridade + MAC). No STP clássico a reconvergência leva até ~30–50 s; no RSTP, poucos segundos ou menos. Durante a reconvergência, fluxos multicast de Transport Stream são interrompidos ou inundam a rede — numa SFN, isso tira transmissores do ar.

</details>

**2.3** O que faz o IGMP snooping e o que acontece sem ele numa rede com fluxos multicast de vídeo?

<details><summary>Gabarito</summary>

O switch "escuta" as mensagens IGMP e encaminha cada grupo multicast apenas às portas com assinantes. Sem ele, o multicast é tratado como broadcast e inunda todas as portas, podendo saturar enlaces e equipamentos. É preciso ainda um **IGMP querier** ativo na VLAN.

</details>

---

## 3. Protocolos de campo

**3.1** No Modbus, quais as funções 03, 06 e 16? A que registrador corresponde o endereço 40001?

<details><summary>Gabarito</summary>

03: ler holding registers; 06: escrever um registrador; 16 (0x10): escrever múltiplos registradores. 40001 é o primeiro holding register (endereço 0 no quadro).

</details>

**3.2** Diferencie Modbus RTU e Modbus TCP.

<details><summary>Gabarito</summary>

RTU: serial (RS-485), mestre-escravo, com endereço de escravo e CRC-16. TCP: sobre Ethernet (porta 502), cabeçalho MBAP no lugar do CRC (o TCP já garante integridade), cliente-servidor.

</details>

**3.3** Quais operações e portas do SNMP? O que é uma MIB?

<details><summary>Gabarito</summary>

GET, GETNEXT/GETBULK, SET (porta UDP 161) e TRAP/INFORM (porta UDP 162). A MIB é a base hierárquica de objetos (OIDs) que descreve o que o agente expõe.

</details>

---

## 4. CLPs

**4.1** Quais as cinco linguagens da IEC 61131-3?

<details><summary>Gabarito</summary>

Ladder (LD), Diagrama de Blocos Funcionais (FBD), Texto Estruturado (ST), Lista de Instruções (IL — descontinuada na 3ª edição) e Sequenciamento Gráfico de Funções (SFC).

</details>

**4.2** Escreva em Texto Estruturado a lógica de selo de um motor (liga, desliga, térmico).

<details><summary>Gabarito</summary>

```iecst
Motor := (BtnLiga OR Motor) AND NOT BtnDesliga AND NOT Termico;
```

</details>

**4.3** Descreva as camadas da pirâmide da automação.

<details><summary>Gabarito</summary>

Campo (sensores/atuadores) → Controle (CLPs, controladores) → Supervisão (SCADA/IHM) → Gestão da produção (MES) → Gestão corporativa (ERP).

</details>
