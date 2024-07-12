# Integer Functions and Elementary Number Theory

## Floor and ceil
- $\lfloor x \rfloor$ = greatest integer less than or equal to $x$
- $\lceil x \rceil$ = least integer greater than or equal to $x$

**Formulas**
- $\lceil x \rceil = \lfloor x \rfloor$ se inteiro
- $\lceil x \rceil = \lfloor x \rfloor + 1$ se não inteiro
- $\lfloor -x \rfloor = - \lceil x \rceil$
- $x-1 < \lfloor x \rfloor \leq x \leq \lceil x \rceil < x+1$


## Modulus (remainder)
- $x$ mod $y = x - y \lfloor x/y \rfloor$ se $y \neq 0$; $x$ mod $0 = x$.
- congruence $x \equiv y$ (modulo z)
- $gcd(m,n)$. $m\perp n$ se $gcd(m,n) = 1$

**Laws**
- $a \equiv b$ and $x \equiv y \implies a \pm x \equiv b\pm y$ and $ax \equiv by$ (modulo m)
- $ax \equiv by$ and $a\equiv b$ and $a \perp m \implies x\equiv y$ (modulo m)
- $a\equiv b$ (modulo m) $\iff an \equiv bn$ (modulo mn), when $n \neq 0$
- $r \perp s \implies a \equiv b$ (modulo rs) $\iff a\equiv b$ (modulo r) and $a \equiv b$ (modulo s)


## Fermat's Theorem (1640)

**Teorema**: $p$ prime $\implies a^p \equiv a$ (modulo p) for all integers $a$

Prova:
- Se a é multiplo de p, $a^p \equiv a \equiv 0$
- Se não, $a \perp p$ pois $p$ é primo. Considerando

$$0\,\,\text{mod p}, a\,\,\text{mod p}, 2a\,\,\text{mod p},\,\,\text{..., }\,\,(p-1)a\,\,\text{mod p}$$

- Esses números são todos distintos pois $a\perp p$ e se $ax\equiv ay$ então $x\equiv y$.
- Logo, $a \cdot 2a \cdot ...\cdot ((p-1)a) \equiv 1 \cdot 2 \cdot ... \cdot (p-1)$ (modulo p)
- Multiplicando cada lado por $a$: $a^p (1*2*...*(p-1)) \equiv a(1*2*...*(p-1))$ (modulo p) e $a^p \equiv a$ pois 1, 2, ..., p-1 são co-primos com $p$.




## Exercícios

**Euler's totient function**: $\phi(n) = |\{a : a\in \{0, 1, ..., n-1\} \wedge a\perp n\}|$

E.g. $\phi(1) = 1, \phi(2) = 1, \phi(3) = 2, \phi(4) = 2$.

- $\phi(p) = p-1$ quando $p$ é primo.
- $\phi(p^k) = p^k - p^{k-1}$ quando $p$ é primo.

**Função multiplicativa**: toda função que $f(ab) = f(a)f(b)$ sempre que $a\perp b$.

Problema 30: Mostre que $\phi(n)$ é multiplicativa.
- Queremos mostrar que $\phi(m)\phi(n) = \phi(mn)$ quando $m\perp n$.
- Por exemplo, $\phi(12) = \phi(4)\phi(3)$. De fato, $\phi(12) = |\{1, 5, 7, 11\}| = 4$ e $\phi(4) = |\{1, 3\}| = 2$ e $\phi(3) = |\{1,2\}| = 2$.
- Seja $A$ o conjunto de coprimos menores que $m$, $B$ o conjunto pra $n$ e $C$ o conjunto pra $mn$. É suficiente provar que há uma bijeção $f: C \to (A,B)$. Por que?
- A bijeção mostra que cada elemento de $C$ pode ser unicamente identificado por um par de $A$ e $B$. Como consequência dessa bijeção, há $|A|*|B|$ pares e portanto $|C| = |A|*|B|$, ou seja $\phi(m)\phi(n) = \phi(mn)$.
- Vamos provar que $f(k) = (k \mod m, k \mod n)$ é a bijeção que queremos. Nota que $gcd(k,mn) = 1 \implies gcd(k, m) = 1, gcd(k,n) = 1$. E $gcd(k,m) = 1 \implies gcd(k \mod m, m) = 1$. Portanto, se $k\in C$, então $gcd(k,mn) = 1$ e o par $(k \mod m, k \mod n) \in A\times B$.
- Como provar que $f$ é bijetiva?
- Pelo teorema chines dos restos, o sistema de congruências: $x\equiv a_1 \mod n_1$, ..., $x\equiv a_N \mod n_N$ have a unique solution $\mod n_1*...*n_N$ given that $gcd(n_i, n_j) = 1$ (are co-prime).
- Portanto, tomando $a \in A$ e $b\in B$, o sistema para encontrar $k\in C$ tal que $k\equiv a \mod m$ e $k\equiv b \mod n$ tem solução e é única. Logo, $f$ é tanto injetiva como sobrejetiva, e logo é bijetiva.
