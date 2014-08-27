#!/usr/bin/python

def calculateSum(ceiling):
    """Calculate the sum of all number divisible by 3 or 5 less than 1000."""
    sum=0;
    for i in range(1,ceiling):
        if not i % 3 or not i % 5:
            sum += i
    return sum

print(calculateSum(1000))
