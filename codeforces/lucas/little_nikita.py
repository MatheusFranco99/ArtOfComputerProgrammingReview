def little_nikita() -> str:
    test_c = int(input())
    while test_c > 0:
        n,m  = map(lambda x: int(x), (input().strip()).split(' '))
        test_c -= 1

        #Não conseguimos chegar a m cubos sem pelo menos n = m ações
        if n >= m:
            if n == m: print('Yes')
            else: 
                # para ir até m, gastamos m --> para manter em m precisamos de um número par de ações restante
                if (n-m)%2 == 0: print('Yes')
                else: print('No')
        else:
            print('No')

if __name__ == '__main__':
    little_nikita()