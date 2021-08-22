import math



s = str(math.factorial(100))

ssum = 0
for i in range(len(s)):
    ssum = ssum + int(s[i])

print(ssum)