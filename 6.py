#!/usr/bin/python

def sumOfSquares(limit):
    sum = 0
    for i in range(1, limit + 1):
        sum += i*i
    return sum

def squareOfSums(limit):
    sum = 0
    for i in range(1, limit + 1):
        sum += i
    return sum * sum

"""Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""
print(squareOfSums(100) - sumOfSquares(100))
