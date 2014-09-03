#!/usr/bin/python

"""
Find the smallest number that is evenly divisible by all of the numbers from 1 to 20

https://projecteuler.net/problem=5
"""

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def lcm(a,b):
    return a * b / gcd(a,b)

def calculateLCM(): 
    n = 1
    for i in range(1, 21):
        n = lcm(n, i)
    return n
        
print(calculateLCM())
