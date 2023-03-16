def is_pandigital(number):
    number_str = str(number)
    return len(number_str) == 9 and set(number_str) == set("123456789")

def concatenated_product(number, n):
    result = ""
    for i in range(1, n + 1):
        result += str(number * i)
    return int(result)

def find_largest_pandigital():
    largest_pandigital = 0
    for i in range(1, 10000):
        n = 2
        while True:
            concatenated = concatenated_product(i, n)
            if len(str(concatenated)) > 9:
                break
            if is_pandigital(concatenated):
                largest_pandigital = max(largest_pandigital, concatenated)
            n += 1
    return largest_pandigital

print(find_largest_pandigital())
