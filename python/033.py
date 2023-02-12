def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def simplify_fraction(n, d):
    g = gcd(n, d)
    return n // g, d // g


def find_denominator():
    numerator_product = 1
    denominator_product = 1
    for denominator in range(11, 100):
        for numerator in range(10, denominator):
            n1, d1 = simplify_fraction(numerator, denominator)
            n2, d2 = simplify_fraction(numerator % 10, denominator % 10)
            if numerator // 10 == denominator // 10 and n1 == n2 and d1 == d2:
                numerator_product *= numerator
                denominator_product *= denominator
    return denominator_product // gcd(numerator_product, denominator_product)


print(find_denominator())
