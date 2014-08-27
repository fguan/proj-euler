#!/usr/bin/python

def isPalindrome(number):
    i = 0
    a = str(number)
    while i < len(a)/2:
        if a[i] != a[len(a)-i-1]:
            return False
        i += 1
    return True

def findLargestPalindrome():
    """Find the largest palindrome made from the product of two 3-digit numbers."""
    i = 999
    j = 999
    curr = 0
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            x = i * j
            if x > curr:
                if isPalindrome(x):
                    curr = x
    return curr

print(findLargestPalindrome())
