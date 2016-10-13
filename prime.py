def prime(a):
    for num in range(0,a):
        for i in range(2,num):
            if (num%i==0):
                break
            else:
                print(num)
                break
n=int(input("enter a no.:"))
prime(n)
