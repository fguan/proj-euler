#!/usr/bin/python

"""
Find the sum of the digits in the number 100!

https://projecteuler.net/problem=20
"""

product = 1
for i in range(1, 101):
    product *= i

sum = 0
for j in str(product):
    sum += int(j)

print(sum)
