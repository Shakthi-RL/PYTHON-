n=int(input())
arr=list(map(int,input().split()))
def plusMinus(arr):
    # Write your code here
    n=len(arr)
    neg=0
    pos=0
    zero=0
    for i in arr:
        if i>0:
            pos+=1
        elif i<0:
            neg+=1
        else:
            zero+=1
    print(f"{neg:.6f}")
    print(f"{pos:.6f}")
    print(f"{zero:.6f}")

plusMinus(arr)
