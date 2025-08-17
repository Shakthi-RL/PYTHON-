def miniMaxSum(arr):
    # Write your code here
    n=len(arr)
    i=arr[0]
    arr.sort()
    min=sum(arr[:n])
    max=sum(arr[i:])     
    return min, max
    
arr = list(map(int, input().rstrip().split()))
print(miniMaxSum(arr))
