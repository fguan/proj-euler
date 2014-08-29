#!/usr/bin/python

"""
Find the sum of the digits in the number 100!

https://projecteuler.net/problem=20
"""

product = 1
for i in range(1, 101):
    product *= i

length = len(str(product))

sum = 0
for j in range(0, length):
    sum += int(str(product)[j])

print(sum)
