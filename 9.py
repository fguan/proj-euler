#!/usr/bin/python

"""
https://projecteuler.net/problem=9
"""

for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000-a-b
        if c > 0:
            if c*c == a*a + b*b:
                print(a*b*c)
