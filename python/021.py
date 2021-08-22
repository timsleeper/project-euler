def sum_factors(n):  
     result = []
     for i in range(1, int(n**0.5) + 1):
         if n % i == 0:
             result.extend([i, n//i])
     return sum(set(result)-set([n]))

def amicable_pair(number):
    result = []
    for x in range(1,number+1):
        y = sum_factors(x)
        if sum_factors(y) == x and x != y:
            result.append(tuple(sorted((x,y))))
    return set(result)

res = 0
for i in amicable_pair(10000):
    res = res + i[0] + i[1]

print(res)