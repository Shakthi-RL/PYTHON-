def decitooct(n):
    hexa=" "
    while n>0:
        hexa+=str(n%16)
        n=n//16
    return hexa

n=65
print(decitooct(n))