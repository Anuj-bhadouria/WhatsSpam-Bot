def area_rectangle(l, w):
    return l * w

def area_square(s):
    return s * s

def area_circle(r):
    pi=3.14
    return pi * r * r

def area_triangle(b, h):
    return 0.5 * b * h

while True:
    print("\nArea Menu:")
    print("1. Rectangle")
    print("2. Square")
    print("3. Circle")
    print("4. Triangle")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print("Area of rectangle:", area_rectangle(l, w))
    elif choice == '2':
        s = float(input("Enter side: "))
        print("Area of square:", area_square(s))
    elif choice == '3':
        r = float(input("Enter radius: "))
        print("Area of circle:", area_circle(r))
    elif choice == '4':
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print("Area of triangle:", area_triangle(b, h))
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
