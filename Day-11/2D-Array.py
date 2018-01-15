#!/bin/python3

import sys

def fun(arr,x,y):
    res = 0    
    res +=( arr[x][y] + arr[x-1][y] + arr[x+1][y] + arr[x+1][y-1] + arr[x+1][y+1]+ arr[x-1][y+1] + arr[x-1][y-1])
    return res

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

ans = -1e10
for x in range(1,5):
    for y in range(1,5):
        ans = max(ans,fun(arr,x,y))
print(ans)
