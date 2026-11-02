# Exercícios — Telecomunicações e Radiodifusão (trilha extra)

> Trilha complementar, fora da grade, voltada a quem trabalha com transmissão de rádio e TV. Liga Eletromagnetismo, Princípios das Comunicações e Redes Industriais à prática de campo.

---

## 1. Decibéis e cálculo de enlace

**1.1** Um transmissor de 10 kW alimenta uma linha com 2 dB de perda e uma antena com ganho de 10 dBd. Calcule a ERP em dBW e em kW.

<details><summary>Gabarito</summary>

10 kW = 40 dBW → ERP = 40 − 2 + 10 = **48 dBW ≈ 63,1 kW**. (ERP é referida ao dipolo; EIRP = ERP + 2,15 dB.)

</details>

**1.2** Converta um campo de 60 dBµV/m em 600 MHz para a potência recebida (dBm) por uma antena isotrópica de 50 Ω.

<details><summary>Gabarito</summary>

$P_r[\text{dBm}] = E[\text{dBµV/m}] - 20\log f[\text{MHz}] - 77{,}2 = 60 - 55{,}6 - 77{,}2 \approx -72{,}8\ \text{dBm}$.

</details>

---

## 2. Linhas de transmissão e casamento

**2.1** Uma carga de 75 Ω é ligada a uma linha de 50 Ω. Calcule o coeficiente de reflexão, a ROE (VSWR), a perda de retorno e a perda por descasamento.

<details><summary>Gabarito</summary>

$\Gamma = \dfrac{75 - 50}{75 + 50} = 0{,}2$; ROE = $\dfrac{1 + 0{,}2}{1 - 0{,}2} = 1{,}5$; RL = $-20\log0{,}2 = 14{,}0\ \text{dB}$; perda por descasamento = $-10\log(1 - 0{,}04) = 0{,}18\ \text{dB}$.

</details>

**2.2** Um transmissor entrega 5 kW e mede 50 W de potência refletida. Qual a ROE? Que causas investigar se ela subir de repente?

<details><summary>Gabarito</summary>

$|\Gamma| = \sqrt{50/5000} = 0{,}1$ → ROE = 1,22. Causas de aumento súbito: água/umidade na linha ou conectores, conector solto ou queimado, dano na antena (descarga atmosférica, vento), gelo, falha no combinador/filtro.

</details>

---

## 3. Propagação

**3.1** Calcule a perda no espaço livre (FSPL) em 600 MHz para 30 km.

<details><summary>Gabarito</summary>

$FSPL = 20\log d_{km} + 20\log f_{MHz} + 32{,}44 = 29{,}5 + 55{,}6 + 32{,}4 \approx 117{,}5\ \text{dB}$.

</details>

**3.2** Uma antena transmissora está a 400 m de altura efetiva e a receptora a 10 m. Estime o horizonte de rádio (fator k = 4/3).

<details><summary>Gabarito</summary>

$d \approx 4{,}12(\sqrt{h_1} + \sqrt{h_2}) = 4{,}12(20 + 3{,}16) \approx 95\ \text{km}$.

</details>

**3.3** Num enlace de 30 km em 600 MHz, qual o raio da 1ª zona de Fresnel no meio do percurso? Qual a folga recomendada?

<details><summary>Gabarito</summary>

$r_1 = 17{,}32\sqrt{\dfrac{d_1d_2}{f_{GHz}\,d}} = 17{,}32\sqrt{\dfrac{15\cdot15}{0{,}6\cdot30}} \approx 61\ \text{m}$. Recomenda-se manter pelo menos 60% da 1ª zona livre de obstáculos (≈ 37 m).

</details>

---

## 4. ISDB-T e redes SFN

**4.1** Numa SFN com modo 3 e GI 1/16 (63 µs), dois transmissores estão a 25 km um do outro. Um receptor fica ao lado de um deles. Haverá interferência intersimbólica? Como corrigir?

<details><summary>Gabarito</summary>

O atraso relativo é ≈ 25 km / c = 83 µs > 63 µs → **sim**, o eco fica fora do intervalo de guarda. Correções: ajustar o atraso estático dos transmissores (deslocar a "zona de igual atraso"), usar GI 1/8 (126 µs) ou reduzir a potência/diretividade para limitar a sobreposição.

</details>

**4.2** O que mede a MER e que valores são típicos na saída de um excitador e no receptor?

<details><summary>Gabarito</summary>

A MER (Modulation Error Ratio) compara a potência dos símbolos ideais com a do vetor de erro na constelação, em dB. Excitadores de boa qualidade costumam apresentar valores bem acima de 30 dB; no campo, o valor cai com ruído e multipercurso e precisa ficar acima do limiar exigido pela modulação/FEC em uso (64-QAM exige bem mais que QPSK).

</details>

**4.3** Por que uma SFN exige sincronismo de frequência e de tempo (GPS/1PPS e 10 MHz) e o que é o BTS de entrada?

<details><summary>Gabarito</summary>

Todos os transmissores precisam emitir o mesmo símbolo, na mesma frequência e no mesmo instante, para que os sinais se somem como ecos dentro do intervalo de guarda. O BTS (Broadcast Transport Stream) é o fluxo de 204 bytes por pacote gerado pelo remultiplexador, que já carrega a informação de camadas hierárquicas e de sincronismo (IIP) usada pelos excitadores.

</details>

---

## 5. Transport Stream MPEG-2

**5.1** Qual o tamanho de um pacote TS, o byte de sincronismo e o PID da PAT?

<details><summary>Gabarito</summary>

188 bytes; sync byte 0x47; PAT no PID 0x0000. (A PMT de cada programa tem PID indicado na PAT; 0x1FFF é o pacote nulo.)

</details>

**5.2** Um PID ocupa 500 pacotes por segundo. Qual a taxa desse PID?

<details><summary>Gabarito</summary>

500 × 188 × 8 = **752 kbit/s**.

</details>

**5.3** Para que servem os erros de prioridade 1 do ETR 290 (TR 101 290)? Cite três.

<details><summary>Gabarito</summary>

São os indicadores mais críticos de integridade do TS, que impedem a decodificação. Ex.: TS_sync_loss, Sync_byte_error, PAT_error, Continuity_count_error, PMT_error, PID_error.

</details>
