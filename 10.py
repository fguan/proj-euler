#!/usr/bin/python

"""
Find the sum of all the primes below two million.

https://projecteuler.net/problem=10
"""

def primes_sieve(limit):
    # Initialize the primality list
    a = [True] * limit                      
    a[0] = a[1] = False
    
    # Mark even numbers as non-prime except for 2
    for m in range(4, limit, 2):
        a[m] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, 2*i):  
                # Mark factors non-prime
                a[n] = False


sum = 0;
for x in primes_sieve(2000000):
    print(x)
    sum += x
print("--------")
print(sum)

