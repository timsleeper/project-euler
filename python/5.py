# coding: utf-8

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def solve():
    n = 20
    d = 0
    while (True):
        d = 0
        for i in range(1, 21):
            if n % i != 0:
                d = 1
        if d == 0:
            print(n)
            exit()
        else:
            n = n + 20


if __name__ == "__main__":
    solve()