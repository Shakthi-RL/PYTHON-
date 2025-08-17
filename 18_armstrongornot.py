def arm(n):
    temp=n
    total=0
    len_dig=len(str(n))

    while temp>0:
        dig=temp%10 #last dig
        total+=dig**len_dig #last dig pow len 
        temp = temp//10
    return total == n

n=152
print(arm(n))

