def isPrime(n):
    if n<=1:
        return 0
    elif n<=3:
        return 1
    elif not(n%2 and n%3) :
        return 0
    lim = int(n ** 0.5) + 2
    for x in range(5,lim):
        if not(n%x and n%(x+2)):
            return 0
    return 1    
    

n = int(input())
while n:
    num = int(input())
    if isPrime(num):
        print("Prime")
    else:
        print("Not prime")
    n-=1
