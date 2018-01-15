#!/bin/python3
import sys
n = int(input().strip())
count = 0
ans = 0
while n > 0 :
    temp = (n%2)
    if temp+count == count :
        ans = max(ans,count)
        count = 0
    else:
        count += 1
    n = n//2
    
print(max(ans,count))
