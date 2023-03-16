def get_fractional_digit(n):
    num_digits, count = 1, 9
    while n > num_digits * count:
        n -= num_digits * count
        num_digits += 1
        count *= 10
    quotient, remainder = divmod(n - 1, num_digits)
    return int(str(quotient + 10 ** (num_digits - 1))[remainder])

def product_of_fractional_digits(digits_list):
    product = 1
    for digit_position in digits_list:
        product *= get_fractional_digit(digit_position)
    return product

digits_list = [1, 10, 100, 1000, 10000, 100000, 1000000]
result = product_of_fractional_digits(digits_list)

print("The value of the expression is:", result)
