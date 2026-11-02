# Exercícios — Sinais e Sistemas

> Lista autoral por tópico. Soluções do Oppenheim e do Chen em `Bibliografia/Solutions/`.

---

## 1. Classificação de sinais e sistemas

**1.1** Classifique quanto a linearidade, invariância no tempo, causalidade e estabilidade (BIBO):
(a) $y(t) = x(t) + 3$; (b) $y(t) = t\,x(t)$; (c) $y[n] = x[n] + x[n-1]$; (d) $y(t) = x(t+1)$.

<details><summary>Gabarito</summary>

(a) Não linear (não passa pela origem), invariante, causal, estável.
(b) Linear, **variante** no tempo, causal, instável (t cresce sem limite).
(c) LIT, causal, estável.
(d) LIT, **não causal** (depende do futuro), estável.

</details>

**1.2** Calcule a energia de $x(t) = e^{-2t}u(t)$ e a potência média de $x(t) = 5\cos(100t)$.

<details><summary>Gabarito</summary>

$E = \int_0^\infty e^{-4t}dt = 1/4$. $P = 25/2 = 12{,}5$ (sinal de potência).

</details>

---

## 2. Convolução

**2.1** Calcule $y(t) = x(t)*h(t)$ com $x(t) = u(t)$ e $h(t) = e^{-t}u(t)$.

<details><summary>Gabarito</summary>

$y(t) = \int_0^t e^{-(t-\tau)}d\tau = (1 - e^{-t})u(t)$ — a resposta ao degrau de um sistema RC com τ = 1.

</details>

**2.2** Convolva $x[n] = \{1, 2, 3\}$ e $h[n] = \{1, 1\}$ (ambos começando em n = 0).

<details><summary>Gabarito</summary>

$y[n] = \{1, 3, 5, 3\}$. Verificação: `numpy.convolve([1,2,3],[1,1])`.

</details>

---

## 3. Série e Transformada de Fourier

**3.1** Calcule a Transformada de Fourier do pulso retangular de amplitude A e duração τ centrado na origem. Onde está o primeiro nulo?

<details><summary>Gabarito</summary>

$X(f) = A\tau\,\text{sinc}(f\tau) = A\tau\dfrac{\text{sen}(\pi f\tau)}{\pi f\tau}$. Primeiro nulo em $f = 1/\tau$ — pulsos mais curtos ocupam mais banda.

</details>

**3.2** Se $x(t) \leftrightarrow X(f)$, qual a transformada de $x(t - t_0)$ e de $x(t)\cos(2\pi f_ct)$? Interprete o segundo resultado.

<details><summary>Gabarito</summary>

$X(f)e^{-j2\pi ft_0}$ (atraso só muda a fase). $\frac12[X(f-f_c) + X(f+f_c)]$ — **modulação**: o espectro é deslocado para ±$f_c$ (base da modulação AM/DSB).

</details>

---

## 4. Laplace e Transformada Z

**4.1** Encontre a resposta ao impulso de $H(s) = \dfrac{1}{s^2 + 3s + 2}$. O sistema é estável?

<details><summary>Gabarito</summary>

$H(s) = \dfrac{1}{s+1} - \dfrac{1}{s+2}$ → $h(t) = (e^{-t} - e^{-2t})u(t)$. Polos em −1 e −2 (semiplano esquerdo) → estável.

</details>

**4.2** Para $H(z) = \dfrac{1}{1 - 0{,}5z^{-1}}$, encontre $h[n]$ e diga se é estável.

<details><summary>Gabarito</summary>

$h[n] = 0{,}5^nu[n]$. Polo em z = 0,5 (dentro do círculo unitário) → estável.

</details>

**4.3** O filtro $y[n] = 0{,}9y[n-1] + 0{,}1x[n]$ é passa-baixas ou passa-altas? Qual o ganho DC?

<details><summary>Gabarito</summary>

$H(z) = \dfrac{0{,}1}{1 - 0{,}9z^{-1}}$. Em z = 1 (DC): $0{,}1/0{,}1 = 1$. Em z = −1 (Nyquist): $0{,}1/1{,}9 \approx 0{,}053$ → **passa-baixas** (média exponencial, muito usada para suavizar leituras de sensores).

</details>

---

## 5. Amostragem

**5.1** Qual a taxa mínima para amostrar áudio de até 20 kHz? Por que o CD usa 44,1 kHz?

<details><summary>Gabarito</summary>

Nyquist: > 40 kHz. 44,1 kHz deixa uma faixa de transição para o filtro anti-aliasing real (que não é ideal).

</details>

**5.2** Um tom de 7 kHz é amostrado a 10 kHz sem filtro anti-aliasing. Em que frequência ele aparece?

<details><summary>Gabarito</summary>

$|7 - 10| = 3\ \text{kHz}$ (alias).

</details>

**5.3** Mostre numericamente o aliasing do item 5.2 em Python.

<details><summary>Gabarito</summary>

```python
import numpy as np
fs, n = 10e3, np.arange(20)
a = np.cos(2*np.pi*7e3*n/fs)
b = np.cos(2*np.pi*3e3*n/fs)
print(np.allclose(a, b))   # True: as amostras são idênticas
```

</details>
