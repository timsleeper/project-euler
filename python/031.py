def coin_combinations(total, coins):
    ways = [1] + [0] * total
    for coin in coins:
        for i in range(coin, total + 1):
            ways[i] += ways[i - coin]
    return ways[total]


print(coin_combinations(200, [1, 2, 5, 10, 20, 50, 100, 200]))
