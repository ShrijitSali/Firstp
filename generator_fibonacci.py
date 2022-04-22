# Fiboncci series using generators


def fibo(n):
    a,b=0,1
    while a<n:
        yield a
        a,b=b,a+b


x=int(input("Please enter till where you want fibonacci: "))
for i in fibo(x):
    print(i)





