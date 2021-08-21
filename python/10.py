# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def SieveOfEratosthenes(n):
    s = 0 
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    for p in range(n + 1):
        if prime[p]:
            s = s + p
    print(s)
 
# driver program
if __name__=='__main__':
    n = 2000000
    
    #Use print("Following are the prime numbers smaller") for Python 3
    print("than or equal to", n)
    #Use print("than or equal to", n) for Python 3
    SieveOfEratosthenes(n)