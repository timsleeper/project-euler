# Largest collatz sequence - Ends at 4, 2, 1

def size_collatz(n):
    lst = []
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            lst.append(n)
        else:
            n = 3 * n + 1
            lst.append(n)
    return len(lst)

largest = 1
largest_i = 1

for i in range(1, 1000000):
    res = size_collatz(i)
    if res > largest:
        largest = res
        largest_i = i

print(largest)
print(largest_i)