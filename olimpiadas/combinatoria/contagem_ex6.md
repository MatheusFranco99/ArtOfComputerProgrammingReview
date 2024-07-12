# 6

(OBM) Sejam $m$ e $n$ inteiros positivos. Quantas funções $f: \{1, 2, ..., m\} \to \{1, 2, ..., n\}$ são não decrescentes, ou seja $f(i)\leq f(j)$  $\forall 1\leq i < j \leq m$?

## Solução

Temos que $1 \leq f(1) \leq f(2) \leq ... \leq f(m) \leq n$.  Seja $d_1 = f(1)-1$, $d_2 = f(2)-f(1)$, ..., $d_{m+1} = n - f(m)$. Note que

$$d_1 + d_2 + ... + d_{m+1} = f(1)-1 + f(2)-f(1) + ... + n - f(m) = n-1$$

como $d_i$ é um inteiro não negativo, a solução do problema é o número de soluções 

$$d_1 + d_2 + ... + d_{m+1} = n-1$$

que, como vimos anteriormente, é o número de anagramas de $n-1$ objetos e $m+1-1$ divisórias
$$\frac{(n-1+m)!}{(n-1)!m!}$$

