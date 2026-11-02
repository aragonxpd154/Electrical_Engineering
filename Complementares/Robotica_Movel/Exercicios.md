# Exercícios — Robótica Móvel

> Lista autoral. Trabalhos antigos (cinemática, plataforma de Stewart) em [`Materiais/`](Materiais/).

---

**1. (Cinemática diferencial)** Um robô diferencial tem rodas de raio 5 cm e distância entre rodas de 30 cm. As rodas giram a 10 rad/s (direita) e 8 rad/s (esquerda). Calcule v, ω e o raio da curva.

<details><summary>Gabarito</summary>

$v_R = 0{,}5\ \text{m/s}$, $v_L = 0{,}4\ \text{m/s}$; $v = (v_R + v_L)/2 = 0{,}45\ \text{m/s}$; $\omega = (v_R - v_L)/L = 0{,}333\ \text{rad/s}$; $R = v/\omega = 1{,}35\ \text{m}$.

</details>

**2. (Odometria)** Um encoder de 1000 pulsos/volta está numa roda de 10 cm de diâmetro. Qual a distância por pulso?

<details><summary>Gabarito</summary>

$\pi\cdot0{,}1/1000 = 0{,}314\ \text{mm}$.

</details>

**3.** Por que a odometria acumula erro e como corrigi-lo?

<details><summary>Gabarito</summary>

Escorregamento, diferenças de diâmetro e erros de integração se acumulam sem referência externa. Corrige-se com fusão de sensores (IMU, GPS, LIDAR, visão) via filtro de Kalman e com marcos (landmarks) conhecidos.

</details>
