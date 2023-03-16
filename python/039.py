def count_right_angle_triangles(p):
    count = 0
    for a in range(1, p // 2):
        for b in range(a, (p - a) // 2):
            c = p - a - b
            if a * a + b * b == c * c:
                count += 1
    return count

def find_max_solutions(limit):
    max_solutions = 0
    max_p = 0

    for p in range(1, limit + 1):
        solutions = count_right_angle_triangles(p)
        if solutions > max_solutions:
            max_solutions = solutions
            max_p = p

    return max_p

limit = 1000
result = find_max_solutions(limit)
print(f"The value of p for which the number of solutions is maximized (p ≤ {limit}): {result}")
