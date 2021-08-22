from functools import reduce
def divisors(n):
    expList = []
    ctr = 0
    divisor = 2
    while divisor <= n:
        while n % divisor == 0:
            n = n/divisor
            ctr += 1
        if ctr != 0:
            expList.append(ctr+1)
        divisor += 1
        ctr = 0
    return reduce(lambda n, y: n * y, expList, 1)


def n_divisors(n):
    natural = 1
    triangular_num = 0

    while True:
        triangular_num += natural
        natural += 1
        if divisors(triangular_num) > n:
            break
    return triangular_num

print(n_divisors(5))
print(n_divisors(100))
print(n_divisors(500))