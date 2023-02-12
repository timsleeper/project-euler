def recurring_cycle_length(d):
    # Check if d is divisible by 2 or 5, which will result in a non-recurring decimal
    if d % 2 == 0 or d % 5 == 0:
        return 0
    # Calculate the length of the recurring cycle
    n = 1
    for i in range(1, d):
        n = (n * 10) % d
        if n == 1:
            return i
    return 0


def longest_recurring_cycle(limit):
    max_length = 0
    d_with_max_length = 0
    for d in range(2, limit):
        length = recurring_cycle_length(d)
        if length > max_length:
            max_length = length
            d_with_max_length = d
    return d_with_max_length


print(longest_recurring_cycle(1000))
