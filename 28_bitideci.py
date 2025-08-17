def bitodeci(n):
    decimal=0
    power=len(n)-1
    for dig in n:
        decimal+=int(dig) * (power ** 2)
        power-=1
    return decimal
n="1010"
print(bitodeci(n))