#!/usr/bin/python

def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

""" 2 is the 1st prime.  Find the 10001st prime number."""
i = 1
for x in primes_sieve(1000000):
    print(str(i) + ' ' + str(x))
    i += 1
    if i > 10001:
        break

