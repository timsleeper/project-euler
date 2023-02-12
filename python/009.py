# coding: utf-8

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def pythagorean_triplet(sum_of_triplet):
    for a in range(1, sum_of_triplet):
        for b in range(a + 1, sum_of_triplet - a):
            c = sum_of_triplet - a - b
            if a * a + b * b == c * c:
                return a * b * c


print(pythagorean_triplet(1000))
