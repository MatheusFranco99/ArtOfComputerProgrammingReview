# Fibonacci Numbers

Sequência definida por
$$F_0 = 0; \,\, F_1 = 1;\,\, F_{n+2} = F_{n+1} + F_n, \,\, n\geq 0$$

$$0,\, 1,\, 1,\, 2,\, 3,\, 5,\, 8,\, 13,\, 21,\, 34,\, 55,\, 89$$

## History

Aparece no problema de Leonardo Pisano (1202): "How many pairs of rabbits can be produced from a single pair in a year's time?"
- Cada par produz um novo par todo mês.
- Cada novo par se torna fértil depois de 1 mês.
- Os coelhos nunca morrem

De fato:
- No começo temos 1 par, ainda inférteis.
- No primeiro mes, ainda teremos 1 par. Mas, pro próximo, esse par já vai estar fértil.
- No segundo mês, temos 1 par do mês anterior + 1 par produzido. Então, 2 pares.
- No terceiro, teremos 2 pares do segundo (que continuam vivos) + 1 par gerado pelos férteis do penúltimo mês.
- Em regra geral, no mês $n$, temos $F_{n-1}$ do último mês que continuam vivos + $F_{n-2}$ que são gerados pelos férteis do mês $n-2$.

Também aparece em:
- Acadêmicos da Índia que estudavam padrões rítimicos (1150)
- Johannes Kepler (1611)
- Eficiência do algoritmo de euclides (1837)
- $\phi$ : "extreme and mean ratio" segundo Euclides (pois a razão de A e B é a razão de A+B e A, se a razão de A e B for $\phi$); Renascimento: chamavam de proporção divina e razão de ouro.

## GCD Theorem

Note que temos

$$F_{n+2} = F_{n+1} + F_{n}$$
$$F_{n+3} = F_{n+2} + F_{n+1} = 2F_{n+1} + F_{n}$$
$$F_{n+4} = F_{n+3} + F_{n+2} = 3F_{n+1} + 2F_{n}$$
$$F_{n+5} = F_{n+4} + F_{n+3} = 5F_{n+1} + 3F_{n}$$
$$F_{n+6} = F_{n+5} + F_{n+4} = 8F_{n+1} + 5F_{n}$$
$$...$$
$$F_{n+m} = F_m F_{n+1} + F_{m-1} F_n$$

**Teorema**: Um número divide $F_m$ e $F_n$ $\iff$ divide $F_d$, onde $d = gcd(m,n)$. Em particular:
$$gcd(F_m,F_n) = F_{gcd(m,n)}$$

**Prova**:
Pela equação acima, $d|F_m,F_n \implies d|F_{n+m}$. Também, $d|F_{n+m},F_n \implies d|F_m F_{n+1}$. Mas $F_{n+1}$ é coprimo com $F_{n}$, então $d|F_m$ pois $d\nmid F_{n+1}$. Portanto $d|F_m,F_n \iff d|F_{m+n},F_n$.

Por indução em $k$, segue também que $d|F_m,F_n \iff d|F_{m+kn},F_n$. Logo, $d|F_{m \mod n},F_n \iff d|F_{m},F_n$. Ou seja, o conjunto de divisores comuns de $\{F_{r}, F_n\}$ são os mesmos de $\{F_m,F_n\}$. Pelo algoritmo de euclides, teremos que o conjunto de divisores comuns de $\{F_m,F_n\}$ também será igual ao de $\{F_{gcd(m,n)},0\}$. Logo $gcd(F_m,F_n) = F_{gcd(m,n)}$.

## Closed Formula

Seja a soma
$$G(z) = F_0 + F_1 z + F_2 z^2 + ...$$
Chamamos essa soma de a função geradora de $F_n$. Vamos supor que essa soma exista e então podemos fazer:
$$zG(z) = F_0z + F_1 z^2 + F_2 z^3 + ...$$
$$z^2G(z) = F_0z^2 + F_1 z^3 + F_2 z^4 + ...$$
E temos
$$(1-z-z^2)G(z) = F_0 + (F_1 - F_0)z + (F_2-F_1-F_0)z^2 + (F_3-F_2-F_1)z^3 + ... = F_0 = 1*z$$
Ou seja
$$G(z) = \frac{z}{1-z-z^2}$$

As raízes de $1-z-z^2$ são $\frac{\sqrt{5}-1}{2}$ e $\frac{-\sqrt{5}-1}{2}$ ($-\phi$ e $-\hat{\phi}$). De fato,

$$(z-\frac{\sqrt{5}-1}{2}) * (z - \frac{-\sqrt{5}-1}{2}) = z^2 + z + \frac{(-1)^2-5}{4} = z^2 + z - 1 = (-1) * (-z^2 - z + 1) $$

Pode-se re-escrever:

$$G(z) = \frac{1}{\sqrt{5}}\left( \frac{1}{1-\phi z} - \frac{1}{1-\hat{\phi}z}\right)$$

e, novamente, re-escrever como a série geométria infinita

$$G(z) = \frac{1}{\sqrt{5}} (1 + \phi z + \phi^2 z^2 + ... -1 -\hat{\phi}z - \hat{\phi}^2 z^2 - ...)$$

O coeficient de $z^n$ (que é $F_n$) é então:

$$\frac{1}{\sqrt{5}}(\phi^n - \hat{\phi}^n)$$

Quando $n$ tende à infinito, temos que $\hat{\phi}^n \to 0$ e $F_n \approx \phi^n /\sqrt{5}$. Além disso,

$$\lim_{n\to\infty} \frac{F_{n+1}}{F_n} = \lim_{n\to\infty} \frac{\phi^{n+1}-\hat{\phi}^{n+1}}{\phi^{n}-\hat{\phi}^{n}}$$
$$= \lim_{n\to\infty} \frac{\phi^{n+1}}{\phi^{n}} = \phi$$


## Problema

18) Is $F_n^2 + F_{n+1}^2$ always a Fibonacci number?

**Solução**:

Já vimos anteriormente que
$$F_{n+m} = F_m F_{n+1} + F_{m-1} F_n$$

Basta tomar $m = n+1$ donde teremos que:
$$F_{2n+1} = F_{n+1}^2 + F_{n}^2$$

donde $F_{n+1}^2 + F_{n}^2$ é $F_{2n+1}$ para qualquer $n$ pelo que é um número de Fibonacci.

20) Express $\sum_{k = 0}^n F_k$ in terms of Fibonacci numbers.

**Solução**:

Temos que:

$$\sum_{k = 0}^n F_k = F_0 + F_1 + \sum_{k = 2}^n F_k$$
$$= F_0 + F_1 + \sum_{k = 2}^n (F_{k-1} + F_{k-2})$$
$$= F_0 + F_1 + \sum_{k = 2}^n (F_{k-1} - F_{k-2} + 2F_{k-2})$$
$$= F_0 + F_1 + \sum_{k = 2}^n (F_{k-1} - F_{k-2}) + 2 \sum_{k = 2}^n F_{k-2}$$
$$= F_0 + F_1 + F_{n-1} - F_{0} + 2 \sum_{k = 2}^n F_{k-2}$$

Então

$$\sum_{k = 0}^n F_k - 2 \sum_{k = 2}^n F_{k-2} = F_1 + F_{n-1}$$
$$\sum_{k = 0}^n F_k - 2 \sum_{k = 0}^n F_{k} + 2F_{n-1} + 2F_n = F_1 + F_{n-1}$$
$$- \sum_{k = 0}^n F_{k} + 2F_{n-1} + 2F_n = F_1 + F_{n-1}$$
$$ 2F_{n-1} + 2F_n - F_1 - F_{n-1} = \sum_{k = 0}^n F_{k}$$
$$ \sum_{k = 0}^n F_{k} =  2F_n + F_{n-1} - F_1$$