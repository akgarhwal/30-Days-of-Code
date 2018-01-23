#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
# Bubble Sort 
numSwap = 0
for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1] :
            a[j],a[j+1] = a[j+1],a[j]
            numSwap += 1

print("Array is sorted in "+str(numSwap)+" swaps.")
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[n-1]))
