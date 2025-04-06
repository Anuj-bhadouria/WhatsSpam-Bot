def fac(n):
    fact=1
    for i in range(2,n+1):
        fact*=i
    print(fact)

n=int(input("enter the range-"))
fac(n)