tc =int(input())
while tc>0:
    str = input()
    F = ""
    S = ""
    for ind in range(len(str)):
        if ind&1:
            S += str[ind]
        else:
            F += str[ind]
    print(F+" "+S)
    tc-=1
