def c2f(c):
    print((c*9/5)+32,"Farenhite")

def f2c(f):
    print((f-32)*5/9,"Celsius")

while True:
    print("\n1. Convert Farenhite to Celsius")
    print("\n2. Convert Celsius to Farenhite")
    print("\n3. Exit")
    ch=int(input("Enter the choice:"))

    if ch==1:
        f=float(input("Enter the temp u want to convert into Celsisus -"))
        c=f2c(f)
      
    elif ch==2:
        c=float(input("Enter the temp u want to convert into Farehnite -"))
        f=c2f(c)
      
    elif ch==3:
        print("Exiting the prog")
        break
        exit
    else:
        print("Invalid Input")