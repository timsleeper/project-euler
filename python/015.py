import math

def pe15(n):
    n_fact = math.factorial(n)
    return math.factorial(2 * n) / n_fact / n_fact

print(pe15(20))