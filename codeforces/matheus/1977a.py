

def main():

    t = int(input())

    while t > 0:

        n,m = map(int, input().split(" "))

        if n < m:
            print("No")
        else:
            if (m-n)%2 == 0:
                print("Yes")
            else:
                print("No")

        t-=1


if __name__ == "__main__":
    main()