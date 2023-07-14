def is_leap_year(year):
    if year==None:
        return False
    elif (year%4==0 and year%100!=0) or year%400==0:
        return True
    else:
        return False
        
'''y= is_leap_year(1996)
print(y)
'''