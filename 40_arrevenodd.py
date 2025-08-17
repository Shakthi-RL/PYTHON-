def evodd(n):
    for num in n:
        if(num%2==0):
            print(num)

n=list(map(int,input().split()))
evodd(n)