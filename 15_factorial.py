def factorial(num):
    fact=1
    for i in range(1,num):
        fact=fact*i
    return fact
num=5
print(factorial(num))