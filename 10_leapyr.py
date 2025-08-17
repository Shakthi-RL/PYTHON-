def leapyr(yr):
    if(yr%4==0):
        if(yr%100!=0 or yr%400==0):
            return True
    return False
yr=2003
if leapyr(yr):
    print("leapyr")
else:
    print("not leapyr")