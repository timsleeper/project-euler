# coding: utf-8

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def solve():
    largest = 0
    for i in range(999, 0, -1):
        for j in range(i-1, 0, -1):
            if is_palindrome(i * j):
                if i * j > largest:
                    largest = i * j
    print(largest)



if __name__ == "__main__":
    solve()