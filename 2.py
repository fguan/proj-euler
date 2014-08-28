#!/usr/bin/python

def calculateSum():
    """Find sum of all even numbers in the Fibonnaci sequence whose values do not exceed four million"""
    sum = 0
    n0 = 1
    n1 = 2
    while n1 <= 4000000:
        if not n1 % 2:
            sum += n1
        temp = n0 + n1
        n0 = n1
        n1 = temp
    return sum

print(calculateSum())