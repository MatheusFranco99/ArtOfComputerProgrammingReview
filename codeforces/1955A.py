from timeit import default_timer as timer
from unittest.mock import patch
import matplotlib.pyplot as plt
import scienceplots

def fastest_solution():
    """ Complexity: O(t) (each test case: O(1)) """

    t = int(input())

    times = []

    while t > 0:
        start = timer()
        n, a, b = list(map(int,input().split(" ")))

        if a * 2 <= b:
            print(a * n)
        else:
            print(b * int(n/2) + a * int(n%2))
        t-=1
        end = timer()
        times.append(end-start)

    return times

def slow_solution():
    """ Complexity: O(t * n) (each test case: O(n)) """

    t = int(input())

    times = []

    while t > 0:
        start = timer()
        n, a, b = list(map(int,input().split(" ")))

        cost = 0
        while n > 0:
            if n == 1:
                cost += a
            else:
                if a * 2 <= b:
                    cost += a * 2
                else:
                    cost += b
                n -= 2
        print(cost)
        t-=1
        end = timer()
        times.append(end-start)

    return times

def complexity_analysis():
    fast_solution_times = []
    slow_solution_times = []

    max_order = 8
    input = [str(max_order)]
    x = []
    for order in range(1, max_order+1):
        input.append(f"{pow(10,order)} 2 3")
        x.append(pow(10,order))

    with patch('builtins.input', side_effect=input):
        fast_solution_times = fastest_solution()
    with patch('builtins.input', side_effect=input):
        slow_solution_times = slow_solution()

    print(fast_solution_times, slow_solution_times)

    with plt.style.context(['science', 'nature']):

        plt.figure(figsize=(8, 5))

        plt.plot(x, slow_solution_times, linestyle = "--", marker = "o", label = "Slow solution")
        plt.plot(x, fast_solution_times, linestyle = "--", marker = "s", label = "Fast solution")
        plt.grid()
        plt.xlabel("$n$", fontsize = 12)
        plt.ylabel("Time($s$)", fontsize = 12)
        # plt.xscale("log")
        plt.legend(fontsize = 12)
        plt.show()


if __name__ == "__main__":
    # fastest_solution()
    complexity_analysis()



