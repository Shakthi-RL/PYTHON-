a=list(map(int,input().split()))
lenth_a=len(a)
for i in range(lenth_a):
    i+=a[i]
print(i)