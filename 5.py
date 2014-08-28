#!/usr/bin/python

def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

def lcm(a,b):
    return a * b / gcd(a,b)

def calculateLCM(): 
    """Find the smallest number that is evenly divisible by all of the numbers from 1 to 20"""
    n = 1
    for i in range(1, 21):
        n = lcm(n, i)
    return n
        
print(calculateLCM())
