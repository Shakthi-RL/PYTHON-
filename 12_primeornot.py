def primeornot(num):
    if(num%2==0):
        return True
    else:
        return False
    
num=2
if primeornot(num):
    print("prime")
else:
    print("not a prime")