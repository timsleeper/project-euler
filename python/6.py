
def solve():
    sum_sq = 0
    sq_sum = 0
    for i in range(1, 101):
        sum_sq = sum_sq + i**2
        sq_sum = sq_sum + i
    print(abs(sum_sq - sq_sum**2))

if __name__ == "__main__":
    solve()