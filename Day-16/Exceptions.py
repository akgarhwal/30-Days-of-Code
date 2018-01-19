#!/bin/python3
import sys

S = input().strip()
try:
    ans = int(S)
except:
    ans ="Bad String"
finally:
    print(ans)
