from math import *

def printDivisors (n):
    res = []
    i = 1
    while (i * i < n):
        if (n % i == 0):
            res.append(i)

        i += 1

    for i in range(int(sqrt(n)), 1, -1):
        if (n % i == 0):
            res.append(n // i)

    return res

# print(printDivisors(28))

abundant = []
for i in range(28123):
    if sum(printDivisors(i)) > i:
        abundant.append(i)
        #print(sum(printDivisors(i)))

#print(len(abundant))

sums = [0]*28124
for x in range (0, len(abundant)):
    for y in range (x, len(abundant)):
            sumOf2AbundantNums = abundant[x]+abundant[y]
            if (sumOf2AbundantNums<= 28123):
                if (sums[sumOf2AbundantNums] == 0):
                    sums[sumOf2AbundantNums] = sumOf2AbundantNums

total = 0
for x in range (1,len(sums)):
    if (sums[x] == 0):
        total +=x

print('\n', total)