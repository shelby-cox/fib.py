# Author: Shelby Cox
# GitHub username: shelby-cox
# Date: 04/22/2026
#Definition: Program returns the Fibonacci number at position n.


def fib(n):

    first = 1
    second = 1

    if n == 1:
        return 1

    for i in range(n - 1):
        next = first + second
        first = second
        second = next

    return first
