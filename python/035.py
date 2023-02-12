import itertools


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_circular_prime(n):
    str_n = str(n)
    rotations = [int("".join(p)) for p in itertools.permutations(str_n)]
    return all(is_prime(r) for r in rotations)


def find_circular_primes():
    return sum(1 for i in range(2, 1000000) if is_circular_prime(i))


print(find_circular_primes())
