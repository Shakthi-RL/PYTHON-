def decitooct(n):
    octal=" "
    while n>0:
        octal+=int(n%8)
        n=n//8
    return octal

n=65
print(decitooct(n))