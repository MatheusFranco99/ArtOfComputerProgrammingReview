def yogurt() -> None:
    test_case_n = int(input())

    for _ in range(test_case_n):
        n, a, b = map(lambda x: int(x), (input().strip()).split(' '))

        #Promoção vantajosa
        if b < 2*a:
            #n par
            if n % 2 == 0:
                out = (n/2)*b
            #n ímpar
            else:
                out = (n//2)*b + a

        #Promoção não vantajosa ou indiferente
        else:
            out = n*a
        
        print(int(out))

def brute_yogurt() -> None:

    test_case_n = int(input())

    for _ in range(test_case_n):
        n, a, b = map(lambda x: int(x), (input().strip()).split(' '))
        brute_list = []

        for i in range((n//2)+1): #1 loop para cada combinação n/2 + 1
            qa = (n-(2*i))*a
            qb = i*b

            brute_list.append(qa+qb)
        
        print(sorted(brute_list)[0])

if __name__ == '__main__':
    yogurt()
    brute_yogurt()