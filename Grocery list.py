grocery_lsit=[]

def add_item():
    A_item=input("Enter the Item u want to add in the grocery list - ")
    grocery_lsit.append(A_item)

def view_list():
    print("The List is as follow -\n")
    print(grocery_lsit)

def remove_item():
    view_list()
    R_item=int(input("Enter the item u want to remove -"))-1
    grocery_lsit.pop(R_item)
    print("The item has been removed")

print("Welcome to the Grocery list")

while True:
    print("\n1.Add an item in grocery list")
    print("\n2.View the items from grocery list")
    print("\n3.Remove an item from grocery list")
    print("\n4.Exit")

    ch=int(input("Enter choice (1-4) -"))
    if(ch==1):
        add_item()
    elif(ch==2):
        view_list()
    elif(ch==3):
        remove_item()
    elif(ch==4):
        print("Exit")
        exit