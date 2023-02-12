def diagonal_sum(side_length):
    sum = 1
    current_number = 1
    for i in range(3, side_length + 1, 2):
        for j in range(4):
            current_number += i - 1
            sum += current_number
    return sum


print(diagonal_sum(1001))
