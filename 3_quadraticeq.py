a=2
b=4
c=8

d=(b**2)-(4*a*c)

# d>0 both real
# d==0 one is real
# d<0 no real root
if (d>0):
    r1=(-b + (d)**0.5)/2*a
    r2=(-b - (d)**0.5)/2*a
    print(r1,"is real root")
elif(d==0):
    root=-b/2*a
    print("both are real",root)
else:
    print("no real root")

