def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def find_sum_of_numbers():
    factorials = [factorial(i) for i in range(10)]
    total = 0
    for i in range(3, factorials[9] * 7):
        if i == sum(factorials[int(digit)] for digit in str(i)):
            total += i
    return total


print(find_sum_of_numbers())
