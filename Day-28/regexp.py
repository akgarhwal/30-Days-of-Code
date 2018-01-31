#!/bin/python3

import sys
import re

N = int(input().strip())
res = []
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if re.search('\w+@gmail.com',emailID):
        res.append(firstName)
        
res.sort()
for name in res:
    print(name)

