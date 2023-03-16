from itertools import permutations
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def largest_pandigital_prime():
    for n in range(9, 0, -1):
        digits = [str(i) for i in range(1, n + 1)]
        pandigital_numbers = sorted(permutations(digits), reverse=True)
        for number_tuple in pandigital_numbers:
            number = int("".join(number_tuple))
            if is_prime(number):
                return number

print(largest_pandigital_prime())