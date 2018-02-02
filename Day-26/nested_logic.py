def is_leap(year):
    leap = False
    if year%4==0 :
        if year%100 == 0 and year%400 ==0:
            leap = True
        elif year%100 != 0:
            leap = True    
    return leap

def no_of_days(month,year):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year):
        days[1] = 29
    return days[month-1]


d,m,y = map(int,input().split())
ed,em,ey = map(int,input().split())


if y > ey :
    print("10000")
elif y == ey and m > em :
    print((m-em)*500)
    
elif y==ey and m==em and d > ed:
    print((d-ed)*15)
    
else:
    print(0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
