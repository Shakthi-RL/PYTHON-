def decitibi(n):
    binary=" "
    while n>0:
        binary=str(n%2)+binary
        n=n//2
    return binary 
n=10
print(decitibi(n))