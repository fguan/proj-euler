#!/usr/bin/python

"""
Calculate the sum of all number divisible by 3 or 5 less than 1000.

https://projecteuler.net/problem=1
"""

sum = 0;
for i in range(1, 1000):
    if not i % 3 or not i % 5:
        sum += i
    
print(sum)
