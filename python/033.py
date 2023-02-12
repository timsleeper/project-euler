def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_cancelling_fraction(n, d):
    n_digits = [int(x) for x in str(n)]
    d_digits = [int(x) for x in str(d)]
    common = set(n_digits) & set(d_digits)
    if len(common) != 1:
        return False
    digit = common.pop()
    if digit == 0:
        return False
    n_digits.remove(digit)
    d_digits.remove(digit)
    if d_digits[0] == 0:
        return False
    reduced_n = n_digits[0]
    reduced_d = d_digits[0]
    return n / d == reduced_n / reduced_d


numerator_product = 1
denominator_product = 1
for numerator in range(10, 100):
    for denominator in range(numerator + 1, 100):
        if is_cancelling_fraction(numerator, denominator):
            numerator_product *= numerator
            denominator_product *= denominator

print(denominator_product // gcd(numerator_product, denominator_product))
