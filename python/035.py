import itertools

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_rotations(n):
    str_n = str(n)
    return [int(str_n[i:] + str_n[:i]) for i in range(len(str_n))]

def is_circular_prime(n):
    return all(is_prime(rotation) for rotation in get_rotations(n))

def count_circular_primes(limit):
    count = 0
    for num in range(2, limit):
        if is_circular_prime(num):
            count += 1
    return count

limit = 1000000
circular_primes_count = count_circular_primes(limit)
print("There are {} circular primes below one million.".format(circular_primes_count))
