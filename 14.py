#!/usr/bin/python

d = {}
d[1] = 1

def sizeOfCollatzSeq(number):
    if not number in d:
        if number % 2 == 0:
            d[number] = 1 + sizeOfCollatzSeq(number // 2)
        else:
            d[number] = 1 + sizeOfCollatzSeq(3 * number + 1)
    #print(str(number) + "\t" + str(d[number]))
    return d[number]

highest, highest_i = 1, 1
for i in range(1, 1000001):
    #print("Starting " + str(i))
    s = sizeOfCollatzSeq(i)
    if s > highest:
        highest, highest_i = s, i

print(highest_i)
