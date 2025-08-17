def fib(n):
    n1=0
    n2=1
    for i in range (1,n):
        print(n1, end=" ")
        temp=n1+n2
        n1=n2
        n2=temp
n=9

fib(n)