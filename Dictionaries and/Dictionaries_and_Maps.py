n = int(input())
q = n
phone_book = {}
while n > 0:
    name,phone = map(str,input().split())
    n-=1
    phone_book[name] = phone
    
while q > 0:
    name = input()
    if name in phone_book:
        print(name+"="+phone_book[name])
    else:
        print("Not found")
    q -= 1
