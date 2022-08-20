def factorial(x,y):
    fact=1
    while y>0 and x>0:
        fact=fact*x
        y=y-1
        x=x-1
    return fact
print(factorial(4,3))