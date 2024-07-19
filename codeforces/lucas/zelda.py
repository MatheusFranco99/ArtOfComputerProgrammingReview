test_n = int(input())
while test_n > 0:

    L,R = map(lambda x: int(x), (input().strip()).split(' '))

    ln = len(str(R))
    n = pow(10,ln)
    R = R + n
    L = L + n
    
    R = str(R)
    L = str(L)

    _bool = False
    #A partir de _bool = True, todas as casas podem ser uma diferença entre 9 e 0

    cnt = 1
    #Contagem para percorrer toda a extnsão dos números

    total = 0
    #Contagem da força da arma

    while cnt < len(R):
        if _bool:
            #todas as casas seguintes contam como 9
            total += 9 * (len(R)- cnt)
            break

        else: 
            if int(R[cnt]) > int(L[cnt]):
            #encontramos a primeira casa decimal onde existe uma diferença

                _bool = True
                total += int(R[cnt])- int(L[cnt])
                cnt += 1
            
            else:
                cnt += 1

    print(total)
    test_n -= 1
