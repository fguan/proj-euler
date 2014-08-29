#!/usr/bin/python

"""
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

https://projecteuler.net/problem=19
"""

month = 1
year = 1
dayOfWeek = 1
count = 0

while year < 101:
    #print(str(month) + "\t" + str(year) + "\t" + str(dayOfWeek) + "\t" + str(count))
    if dayOfWeek == 0:
        count += 1

    if month == 4 or month == 6 or month == 9 or month == 11:
        dayOfWeek = (dayOfWeek + 30) % 7
    if month == 2:
        if year % 4:
            dayOfWeek = (dayOfWeek + 29) % 7 
        else:
            dayOfWeek = (dayOfWeek + 28) % 7
    else: 
        dayOfWeek = (dayOfWeek + 30) % 7

    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

print(count)
