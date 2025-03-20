str=input("Enter the string -")
rev=""
for i in str:
    rev=i+rev

if str==rev:
    print("The String is palindrome!")
else:
    print("The string is not palindrome!")