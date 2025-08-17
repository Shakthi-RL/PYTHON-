def checkEqual(a, b):
  
    # If lengths of array are not equal means
    # array are not equal
    if len(a) != len(b):
        return False
    return sorted(a) == sorted(b)
a=[1,2,3,4,5]
b=[5,4,7,2,1]
print(checkEqual(a,b))