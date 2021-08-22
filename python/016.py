val = 2**1000
val_str = str(val)

sum_n = 0

for i in range(len(val_str)):
    sum_n = sum_n + int(val_str[i])

print(sum_n)