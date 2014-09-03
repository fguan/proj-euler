#!/usr/bin/python

"""
Find the value of the first triangle number to have over five hundred divisors.

https://projecteuler.net/problem=12
"""

import math

#primeList = [2]
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
"""
def numDivisors(number):
    numDivisors = 0
    limit = int(math.sqrt(number))
    i = 1
    while i <= limit:
        if number % i == 0:
            numDivisors += 2
        i += 1

    if limit * limit == number:
        numDivisors -= 1

    return numDivisors
"""
def numDivisors(number):
    numDivisors = 1
    primeLimit = number + 1
    
    for x in primesList:
        if number == 1:
            break
        count = 0
        while number % x == 0:
            count += 1
            number = number / x
        numDivisors = numDivisors * (count + 1)
    return numDivisors
"""
#print(numDivisors(28))
#print(numDivisors(31))
#print(numDivisors(100))

"""
for m in primes_sieve(100000000):
    primeList.append(m)
"""

number = 0
step = 1
while numDivisors(number) < 500:
    number += step
    step += 1
print(number)

