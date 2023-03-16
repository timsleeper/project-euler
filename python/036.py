def is_palindrome(s):
    return s == s[::-1]

def to_binary(n):
    return bin(n)[2:]

def main():
    total_sum = 0
    limit = 10**6

    for i in range(1, limit):
        if is_palindrome(str(i)) and is_palindrome(to_binary(i)):
            total_sum += i

    print("The sum of all numbers, less than one million, which are palindromic in base 10 and base 2 is:", total_sum)

if __name__ == "__main__":
    main()
