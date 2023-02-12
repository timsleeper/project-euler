def sum_of_fifth_powers(n):
    return sum(int(digit) ** 5 for digit in str(n))


def find_sum_of_numbers(power):
    return sum(n for n in range(10, 10 ** (power + 1)) if n == sum_of_fifth_powers(n))


print(find_sum_of_numbers(5))
