def is_pandigital(n, m, p):
    s = str(n) + str(m) + str(p)
    return len(s) == 9 and set(s) == set("123456789")


def find_sum_of_products():
    products = set()
    for i in range(1, 10**4):
        for j in range(i, 10**4):
            p = i * j
            if is_pandigital(i, j, p):
                products.add(p)
    return sum(products)


print(find_sum_of_products())
