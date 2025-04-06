def fac(n):
    fact=1
    for i in range(2,n+1):
        fact*=i
    return fact

def ser(n):
    t=0
    for i in range(1,n+1):
        term=i/fac(i)
        if i%2==0:
            t-=term
        else:
            t+=term
    return t

n=int(input("enter the range-"))
print(ser(n))
