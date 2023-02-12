def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_coefficient_product(expression):
    max_primes = 0
    a_b_product = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            while is_prime(eval(expression.format(n=n, a=a, b=b))):
                n += 1
            if n > max_primes:
                max_primes = n
                a_b_product = a * b
    return a_b_product


expression = "n**2 + {a} * n + {b}"
print(prime_coefficient_product(expression))
