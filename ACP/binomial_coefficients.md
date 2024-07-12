# Binomial Coefficients

- Número de combinações (ordem não importa) de $k$ elementos tirados de um total de $n$: ${n \choose k} = \frac{n(n-1)...(n-k+1)}{k(k-1)...1}$. Porque?
  - Pela secção anterior, há $n(n-1)...(n-k+1)$ maneiras de escolher $k$ objetos em ordem.
  - Cada escolha aparece $k!$ vezes em ordens diferentes (número de permutações)

- A fórmula acima pode ser usada não só para $n$ inteiro como também para $n$ real. Apesar de $k$ ser sempre inteiro.
- Valores de $n\choose k$ aparecem no triângulo de Pascal (1653). Primeira aparição remete à Grécia e Roma antigas.

## Propriedades

- Representação por fatorial: ${n \choose k} = \frac{n!}{k!(n-k)!}$
- Simetria: ${n \choose k} = {n \choose n-k}$
- Remoção dos parênteses: ${r \choose k} = \frac{r}{k} {r-1 \choose k-1}$, ${r \choose k} =\frac{r}{r-k} {r-1 \choose k}$
- Adição: ${r \choose k} = {r-1 \choose k}  + {r-1 \choose k-1}$
- Soma: $\sum_{k = 0}^n {r+k \choose k} = {r+n+1 \choose n}$, $\sum_{k = 0}^{n}{k\choose m} = {n+1\choose m+1}$
- Teorema Binomial (Newton): $(x+y)^r = \sum_k {r\choose k} x^k y^{r-k}$
- Negação do índice superior: ${r\choose k} = (-1)^k {k-r-1\choose k}$
- Simplificar produtos: ${r\choose m}{m\choose k} = {r\choose k}{r-k \choose m-k}$
- Soma de produtos: $\sum_k {r\choose k}{s\choose n-k} = {r+s \choose n}$

## Aplicações

- Usano a propriedade de soma ($\sum_{k = 0}^{n}{k\choose m} = {n+1\choose m+1}$), temos que ${0\choose 1} + {1 \choose 1} + ... + {n\choose 1} = {n+1 \choose 2} = \frac{(n+1)n}{2}$. Então
$$n^2 + n = 2{n+1 \choose 2}$$
$$n^2 = 2{n+1 \choose 2} - {n \choose 1}$$
$$n^2 = 2{n \choose 2} + 2 {n\choose 1} - {n \choose 1} = 2{n\choose 2} + {n\choose 1}$$
Então
$$\sum_{k = 0}^n k^2 = \sum_{k = 0}^n 2{k\choose 2} + {k\choose 1} = 2{n+1\choose 3} + {n+1\choose 2}$$

Podemos fazer isso de forma similar para qualquer$k^c$.

## Exemplos de problemas
- Solução do problema de stirling:
$$n! = a_0 + a_1n + a_2n(n-1) + a_3n(n-1)(n-2) + ...$$

- Algoritmo de Gosper-Zeilberger para identificar fórmulas fechadas caso existam.

## Generalizações
- Coeficiente multinomial
$${k_1 + k_2 + ... + k_m \choose k_1, k_2, ..., k_m} = \frac{(k_1 + k_2 + ... + k_m)!}{k_1!k_2!...k_m!}$$

Propriedade:
- $(x_1 + x_2 + ... + x_m)^n = \sum_{k_1 + k_2 + ... + k_m = n} {n \choose k_1, k_2 ..., k_m} x_1^{k_1} x_2^{k_2} ...x_m^{k_m}$
- Coeficiente multinomial = Anagrama. E.g. quantos anagramas de PARALELEPIPEDO existem?
$$\frac{14!}{3!2!1!2!3!1!1!1!} = 605404800$$
- Número de soluções inteiras não negativas da equação:
$$x_1 + x_2 + ... + x_k = n$$

Esse problema é equivalente a contar o número de maneiras de distribuir $n$ objetos em $k$ cestas diferentes. Podemos representar isso da seguinte forma:
$$\cdot \cdot | \cdot | \cdot \equiv (2,1,1)$$
em que $\cdot$ é um objeto e $|$ uma divisória entre as cestas. No exemplo acima, seria como distribuir 2 elementos na 1º cesta, 1 na 2º e 1 na 3ª.

Logo, a solução é o número de anagramas de $n$ objetos $\cdot$ e $k-1$ divisórias: $\frac{(n+k-1)!}{n!(k-1)!}$.


## Números de Stirling
- Conversão entre polinômios em potências de $x$ para polinômios em coeficientes binomiais.
- Primeiro tipo: $\genfrac{[}{]}{0pt}{}{n}{k}$ (representa o número de permutações de $n$ letras com $k$ ciclos).
  - Propriedade base: $\genfrac{[}{]}{0pt}{}{n+1}{m} = n \genfrac{[}{]}{0pt}{}{n}{m} + \genfrac{[}{]}{0pt}{}{n}{m-1}$
  -
$$x^{\underline{n}} = x(x-1)...(x-n+1) = \genfrac{[}{]}{0pt}{}{n}{n} x^n - \genfrac{[}{]}{0pt}{}{n}{n-1}n^{n-1} + ... + (-1)^n\genfrac{[}{]}{0pt}{}{n}{0} = \sum_k (-1)^{n-k}\genfrac{[}{]}{0pt}{}{n}{k}x^k$$

- Segundo tipo: $\genfrac{\{}{\}}{0pt}{}{n}{k}$ (represent o número de maneiras de particionar um conjunto de $n$ elementos em $k$ subconjuntos distintos).
  - Propriedade base: $\genfrac{\{}{\}}{0pt}{}{n+1}{m} = m \genfrac{\{}{\}}{0pt}{}{n}{m} + \genfrac{\{}{\}}{0pt}{}{n}{m-1}$
  -
$$x^n = \genfrac{\{}{\}}{0pt}{}{n}{n} x^{\underline{n}} + ... + \genfrac{\{}{\}}{0pt}{}{n}{1} x^{\underline{1}} + \genfrac{\{}{\}}{0pt}{}{n}{0} x^{\underline{0}} = \sum_k \genfrac{\{}{\}}{0pt}{}{n}{k} x^{\underline{k}}$$


## Exercício

- 10.a: Se $p$ é primo, mostre que ${n\choose p} \equiv \lfloor \frac{n}{p} \rfloor$ (modulo $p$).

**Solução**:

Lembre que ${n\choose p}$ é o número de maneiras de selecionar $p$ elementos (sem importar a ordem) de um total de $n$. Note que se a ordem importasse, para cada combinação, teríamos $p!$ possíveis permutações e, por isso, o resultado seria congruente a $0$ modulo $p$. Ou seja, $n(n-1)...(n-p+1) \equiv 0$ (modulo $p$). Faz sentido pois temos $n-(n-p) = p$ números consecutivos e, em modulo $p$, poderíamos mapeá-los à 0, 1, .., p-1, cuja multiplicação é congruente a 0 modulo $p$.

Voltando ao problema, seja $n = kp + r$, então temos

$$\frac{n...(n-p+1)}{p(p-1)...1} = \frac{(kp+r)(kp+r-1)...(kp)...(kp+r - p + 1)}{p(p-1)...1}$$

Note que cada elemento de $(kp+r)(kp+r-1)...(kp)...(kp+r - p + 1)$ pode ser mapeado a um elemento de $p(p-1)...1$ de acordo com a sua congruência. Mais, se $a\equiv b$ então $ab^{-1} \equiv 1$ (modulo $p$). Logo

$$\frac{kp+r}{r}\frac{kp+(r-1)}{r-1}...\frac{kp}{p} \equiv \frac{kp}{p}$$
$$(kp+r)(r^{-1})\frac{kp+(r-1)}{r-1}...\frac{kp}{p} \equiv \frac{kp}{p}$$


e $\frac{kp}{p} = \lfloor \frac{n}{p} \rfloor$.

