def feb(n):
    a=0
    b=1
    for _ in range(n):
        print(a,end="\n")
        a,b=b,a+b

n=int(input("enter the range-"))
feb(n)