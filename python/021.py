def proper_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors


def is_amicable(n):
    m = sum(proper_divisors(n))
    return n != m and n == sum(proper_divisors(m))


def sum_of_amicable_numbers(limit):
    amicable_numbers = []
    for i in range(1, limit):
        if is_amicable(i) and i not in amicable_numbers:
            amicable_numbers.append(i)
            amicable_numbers.append(sum(proper_divisors(i)))
    return sum(amicable_numbers)


print(sum_of_amicable_numbers(10000))
