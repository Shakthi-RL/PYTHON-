# 48/18=12
# 18/12=6
# 12/6=0
def hcf(a,b):
    while b!=0:
        a,b=b,a%b
    return a
a=48
b=18
print(hcf(a,b))


# a=48
# b=18
# while b!=0:
#     t=b
#     b=a%b
#     a=t
#     print(a)