

def solve_case(l: str, r: str) -> int:
    if len(l) < len(r):
            # if:
            #   r = [r_n ... r_k ... r_0]
            #   l = [        l_k ... l_0]
            #   we can simply choose:
            #   A = [r_n 0 ... 0 ... 0]
            #   B = [0   9 ... 9 ... 9]
            # Notice that l <= B < A <= r
            return int(r[0]) + 9 * (len(r)-1)
    else:
        # if:
        #   r = [r_n ... r_k ... r_0]
        #   l = [l_n ... l_k ... l_0]
        # let's say that r_i = l_i from n until k+1.
        # Notice that we can't change these digits, otherwise
        # we would be out of the [l,r] interval.
        # Thus, these gotta be fixed and we can look at the problem:
        #   r = [       r_k ... r_0]
        #   l = [       l_k ... l_0]
        # with r_k > l_k. Notice that we can choose:
        #   A = [ r_k 0 ... 0]
        #   B = [ l_k 9 ... 9]
        # which provides us the best differences for indices 0 to k-1 and also for index k.
        # Notice that l <= B <= A <= r

        for i in range(len(r)):
            if r[i] == l[i]:
                continue
            else:
                return (int(r[i])-int(l[i])) + 9 * (len(r)-(i+1))
        return 0


def main():
    t = int(input())

    for _ in range(t):
        l, r = input().split()

        ans = solve_case(l,r)
        print(ans)


if __name__ == "__main__":
    main()