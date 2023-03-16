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

def is_truncatable_prime(n):
    if n < 10:
        return False

    str_n = str(n)
    for i in range(len(str_n)):
        left_truncated = int(str_n[i:])
        right_truncated = int(str_n[:len(str_n) - i])
        if not (is_prime(left_truncated) and is_prime(right_truncated)):
            return False

    return True

def find_truncatable_primes(limit):
    truncatable_primes = []
    i = 11
    while len(truncatable_primes) < limit:
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
        i += 2

    return truncatable_primes

def main():
    limit = 11
    truncatable_primes = find_truncatable_primes(limit)
    result = sum(truncatable_primes)
    print(f"The sum of the only {limit} truncatable primes is: {result}")

if __name__ == "__main__":
    main()
