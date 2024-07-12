# Sums and Products

For sums like $a_1 + ... + a_n$, we use the notation
$$\sum_{j = 1}^{n} a_j \text{ or } \sum_{1\leq j\leq n} a_j$$

More general:
$$\sum_{R(j)} a_j$$
where $R(j)$ is some condition the integer $j$.

Notation was introduced by Fourier in 1820.

For infinite sums:
$$\sum_{R(j)} a_j = \left( \lim_{n\to\infty} \sum_{R(j), 0\leq j < n} \right) + \left( \lim_{n\to\infty} \sum_{R(j), -n \leq j < 0} \right)$$
If the limits exist, it's convergent. Else, divergent.


## Operations

- Distributive: $\sum_{R(i)}a_i \sum_{S(j)}b_j = \sum_{R(i)}\sum_{S(j)} a_i b_j$
- Change of variable: $\sum_{R(i)} a_i = \sum_{R(j)} a_j = \sum_{R(p(j))} a_{p(j)}$ (cases: rename and permutation (i.e. $p(j) = i$ for all i that satisfies $R(i)$)) (the permutation change can't be applied in all cases for infinite sums)
-  Interchanging order: $\sum_{R(i)}\sum_{S(j)}a_{ij} = \sum_{S(j)}\sum_{R(i)}a_{ij}$
-  Manipulating the domain: $\sum_{R(j)} a_j + \sum_{S(j)}a_j = \sum_{R(j)\text{ or }S(j)} a_j + \sum_{R(j)\text{ and }S(j)} a_j$


### Examples

- Gemoetric progression
$$a + ax + ... + ax^n = \sum_{0 \leq j \leq n} a x^j$$
$$= a + \sum_{1 \leq j \leq n} ax^j$$
$$= a + x\sum_{1 \leq j \leq n} ax^{j-1}$$
$$= a + x\sum_{0 \leq j \leq n-1} ax^{j}$$
$$= a + x\sum_{0 \leq j \leq n} ax^{j} - ax^{n+1}$$


$$(1-x) \sum_{0\leq j \leq n} ax^j = a - ax^{n+1}$$
$$\sum_{0\leq j \leq n} ax^j = a\left(\frac{1 - x^{n+1}}{1-x}\right)$$
- Example 2 in the book


## Bracket notation

$\text{[statement]}$ = 1 if the statement is true, 0 otherwise

$$\sum_{R(j)}a_j = \sum_{j}a_j[R(j)]$$

**Kronecker delta**: $\delta_{ij} = 1$ if $i = j$, 0 if $i \neq j$.

## Products

We use $\Pi$ instead of $\sum$. Operations b, c and d apply.


## Problems

Problema 15: Compute a soma $1 * 2 + 2 * 2^2 + 3 * 2^3 + ... + n * 2^n$.
- Primeiro, vamos ver os casos iniciais
$$1 * 2 = 2$$
$$1 * 2 + 2 * 2^2 = 10$$
$$1 * 2 + 2 * 2^2 + 3 * 2^3 = 34$$
$$1 * 2 + 2 * 2^2 + 3 * 2^3 + 4 * 2^4 = 98$$
$$\text{...}$$

$$\sum_{1 \leq i \leq n} i*2^i = 2\sum_{1 \leq i \leq n} i*2^{i-1}$$
$$= 2\sum_{1 \leq i \leq n} (i-1+1)*2^{i-1}$$
$$= 2\sum_{1 \leq i \leq n} (i-1)*2^{i-1} + 2 * \sum_{1 \leq i \leq n} 2^{i-1}$$
$$= 2\sum_{0 \leq j \leq n-1} j *2^{j} + 2 * \sum_{0 \leq j \leq n-1} 2^j$$
$$= 0 + 2\sum_{1 \leq j \leq n-1} j *2^{j} + 2 * \sum_{0 \leq j \leq n-1} 2^j$$
$$= 2\sum_{1 \leq j \leq n} j *2^{j} - 2 * n * 2^n + 2 * \sum_{0 \leq j \leq n-1} 2^j$$
i.e.

$$ S_n = 2 * S_n - 2 * n * 2^n + 2 * \sum_{0 \leq j \leq n-1} 2^j$$
$$ S_n = 2 * n * 2^n - 2 * \sum_{0 \leq j \leq n-1} 2^j$$
$$ S_n = 2 * n * 2^n - 2 * \frac{1-2^n}{1-2}$$
$$ S_n = 2 * n * 2^n + 2 * (1-2^n)$$
$$ S_n = 2 * 2^n * (n - 1) + 2 $$
$$ S_n = 2^{n+1} * (n - 1) + 2 $$


So,

$$S_1 = 2^{2} * (1 - 1) + 2 = 2$$
$$S_2 = 2^{3} * (2 - 1) + 2 = 10$$
$$S_3 = 2^{4} * (3 - 1) + 2 = 16 * 2 + 2 = 34$$
$$S_4 = 2^{5} * (4 - 1) + 2 = 32 * 3 + 2 = 96 + 2 = 98$$