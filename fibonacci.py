def fibo(n):
    a=0
    b=1
    d=0
    while d<n:
        c=a+b
        a+=1
        b+=1
        print(c)
#test
x=int(input("enter no.:"))
fibo(x)
