#!/usr/bin/python

"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26. 
What is the sum of the digits of the number 2^1000?

https://projecteuler.net/problem=16
"""

a = 2**1000
length = len(str(a))
sum = 0
for i in range(0, length):
    sum += int(str(a)[i])
print(sum)
