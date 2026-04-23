# Author: Shelby Cox
# GitHub username: shelby-cox
# Date: 04/22/2026
#Definition: Program returns the Fibonacci number at position n.


def fib(n)

    first = 1
    second = 1

    for i in range(n - 2):
        next_num = first + second
        first = second
        second = next_num

    return second