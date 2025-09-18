import math

"""
Write a script that lists all the prime numbers between 1 and 10000.
(A prime number is an integer greater or equal to 2 which has no divisors except 1 and itself). 
Hint: Write an is_factor helper function.
"""

import math

def is_factor(d, n):
    """True iff (if and only if) d is a divisor of n."""
    return n % d == 0

def is_prime(n):
    for d in range(2, int(math.sqrt(n)+1)):
        if is_factor(d, n):
            # n is not prime
            return False
    return True

list_of_primes = []
for n in range(2, 10001):
    if is_prime(n):
        list_of_primes.append(n)

print(list_of_primes)
