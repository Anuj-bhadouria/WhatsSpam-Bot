def add_employee(employees):
    name = input("Name: ")
    age = input("Age: ")
    salary = input("Salary: ")
    employees.append({"name": name, "age": age, "salary": salary})
    print("Employee added!")

def view_employees(employees):
    if not employees:
        print("No employees yet.")
        return
    for emp in employees:
        print(f"{emp['name']}, Age: {emp['age']}, Salary: {emp['salary']}")

def remove_employee(employees):
    name = input("Name to remove: ")
    for emp in employees:
        if emp["name"].lower() == name.lower():
            employees.remove(emp)
            print("Employee removed!")
            return
    print("Not found!")

def average_salary(employees):
    if not employees:
        print("No employees yet.")
        return
    total = sum(float(emp["salary"]) for emp in employees)
    print(f"Avg Salary: {total / len(employees):.2f}")

employees = []
while True:
    print("\n1. Add  2. View  3. Remove  4. Avg Salary  5. Exit")
    choice = input("> ")
    if choice == "1":
        add_employee(employees)
    elif choice == "2":
        view_employees(employees)
    elif choice == "3":
        remove_employee(employees)
    elif choice == "4":
        average_salary(employees)
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
