# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

def solve():
    factors = []
    n = 600851475143

    for i in range(2, int(math.ceil(math.sqrt(n)))):
        while n % i == 0:
            factors.append(i)
            n = n / i

    print(factors[-1])

if __name__ == "__main__":
    solve()