def hcf(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm(a,b):
    return abs(a * b) // hcf(a, b)
a=15
b=20
print(lcm(a,b))