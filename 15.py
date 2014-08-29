#!/usr/bin/python

"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner. How many such routes are there through a 20×20 grid?

https://projecteuler.net/problem=15
"""

gridSize = 20
a = [[0 for i in range(0,gridSize+1)] for j in range(0,gridSize+1)]

# initialize bottom and right most boundary to 1. 
for i in range(0,gridSize):
    a[i][gridSize] = a[gridSize][i] = 1

print(a[20][1])

# number of routes available for each point is equal to the routes(right-point) + routes(down-point)
for i in range(gridSize-1, -1, -1):
    for j in range(gridSize-1, -1, -1):
        a[i][j] = a[i+1][j] + a[i][j+1]

print(a[0][0])
