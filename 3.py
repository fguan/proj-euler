#!/usr/bin/python

def calculateLargestPrimeFactor(number):
    """Calculate the largest prime factor of 600851475143."""
    i = 2
    while i * i < number:
        while number % i == 0:
            number = number / i
        i += 1
    return number

print(calculateLargestPrimeFactor(600851475143))
