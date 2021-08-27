def fibonacci_sequence():
    a,b = 1,1
    while True:
        yield a
        a,b = b, a+b

f = fibonacci_sequence()
a = next(f)
i = 1
while(len(str(a)) < 1000):
    # print(a)
    a = next(f)
    i += 1
print(i)