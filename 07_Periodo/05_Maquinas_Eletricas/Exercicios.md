# Exercícios — Máquinas Elétricas

> Lista autoral por tópico. Soluções do Fitzgerald em `Bibliografia/Solutions/`; material antigo (Máquinas I e II) em [`Materiais/`](Materiais/).

---

## 1. Motor de indução trifásico

**1.1** Um motor de 4 polos, 60 Hz, gira a 1750 rpm. Calcule a velocidade síncrona, o escorregamento e a frequência das correntes do rotor.

<details><summary>Gabarito</summary>

$n_s = 120\cdot60/4 = 1800\ \text{rpm}$; $s = 50/1800 = 2{,}78\%$; $f_r = sf = 1{,}67\ \text{Hz}$.

</details>

**1.2** Placa: 15 cv, 380 V, η = 90%, FP = 0,85, 1750 rpm. Calcule a corrente nominal e o torque nominal (1 cv = 735,5 W).

<details><summary>Gabarito</summary>

$P = 11{,}03\ \text{kW}$; $I = \dfrac{P}{\sqrt3V\eta\,\text{FP}} = 21{,}9\ \text{A}$; $T = P/\omega = 11030/183{,}3 = 60{,}2\ \text{N·m}$.

</details>

**1.3** O que acontece com o torque e com o escorregamento se a tensão de alimentação cair 10% com a mesma carga mecânica?

<details><summary>Gabarito</summary>

O torque para dado escorregamento cai com $V^2$ (≈ 81%). Para manter o torque da carga, o escorregamento aumenta (~1/0,81), a corrente aumenta e o motor aquece mais.

</details>

---

## 2. Partida de motores

**2.1** Compare corrente de partida e torque de partida na ligação estrela-triângulo em relação à partida direta.

<details><summary>Gabarito</summary>

Em estrela cada enrolamento recebe $V/\sqrt3$: corrente de linha e torque caem para **1/3**. Só serve para cargas que partem com torque baixo (bombas, ventiladores) e motores com 6 terminais.

</details>

**2.2** Um inversor mantém V/f constante. Com o motor do item 1.2 (380 V, 60 Hz), que tensão aplicar em 30 Hz e qual a nova velocidade síncrona?

<details><summary>Gabarito</summary>

190 V; $n_s = 900\ \text{rpm}$. Mantendo V/f, o fluxo fica constante e o motor entrega torque nominal em toda a faixa (abaixo da nominal).

</details>

---

## 3. Máquina de corrente contínua

**3.1** Um motor CC de excitação independente: $V = 220\ \text{V}$, $R_a = 0{,}5\ \Omega$, $I_a = 40\ \text{A}$ a 1500 rpm. Se a carga diminuir e $I_a$ cair para 20 A (fluxo constante), qual a nova velocidade?

<details><summary>Gabarito</summary>

$E_1 = 220 - 20 = 200\ \text{V}$; $E_2 = 220 - 10 = 210\ \text{V}$ → $n_2 = 1500\cdot210/200 = 1575\ \text{rpm}$.

</details>

**3.2** Por que um motor CC série nunca deve partir sem carga?

<details><summary>Gabarito</summary>

O fluxo depende da corrente; sem carga a corrente e o fluxo ficam pequenos e a velocidade ($n \propto E/\Phi$) dispara, podendo destruir o rotor.

</details>

---

## 4. Máquina síncrona

**4.1** Um gerador síncrono (por fase) tem $V = 1\ \text{pu}$, $X_s = 1{,}2\ \text{pu}$ e entrega $I = 1\ \text{pu}$ com FP 0,8 indutivo. Calcule a tensão interna E e o ângulo de carga δ (despreze $R_a$).

<details><summary>Gabarito</summary>

$I = 1\angle{-36{,}87^\circ} = 0{,}8 - j0{,}6$; $E = V + jX_sI = 1 + j1{,}2(0{,}8 - j0{,}6) = 1{,}72 + j0{,}96$ → $E = 1{,}97\angle29{,}2^\circ\ \text{pu}$.

</details>

**4.2** O que são as curvas V de um motor síncrono e como ele pode corrigir o fator de potência de uma indústria?

<details><summary>Gabarito</summary>

Gráficos de corrente de armadura versus corrente de campo para potência constante. Sobre-excitado, o motor fornece reativo (comporta-se como capacitor), compensando cargas indutivas — o compensador síncrono.

</details>

---

## 5. Prática computacional

**5.1** Usando o circuito equivalente do motor de indução ($R_1$, $X_1$, $X_m$, $R_2/s$, $X_2$), escreva um script que trace torque × velocidade.

<details><summary>Gabarito</summary>

```python
import numpy as np, matplotlib.pyplot as plt
V, f, p = 380/np.sqrt(3), 60, 4
R1, X1, R2, X2, Xm = 0.5, 1.2, 0.4, 1.2, 40
ws = 4*np.pi*f/p
s = np.linspace(0.001, 1, 500)
Vth = V*Xm/np.sqrt(R1**2 + (X1+Xm)**2)
Zth = (1j*Xm*(R1+1j*X1))/(R1+1j*(X1+Xm))
T = 3*Vth**2*(R2/s)/(ws*((Zth.real + R2/s)**2 + (Zth.imag + X2)**2))
plt.plot((1-s)*ws*60/(2*np.pi), T); plt.xlabel("rpm"); plt.ylabel("T (N·m)"); plt.grid(); plt.show()
```

</details>
