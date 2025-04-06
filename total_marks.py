def calculate(percentage):
    if percentage>=80:
        print("grade A")
    elif percentage>=70 and percentage<80 :print("Grade B")
    elif percentage>=60 and percentage<70:print("Grade C")
    elif percentage>=50 and percentage<60:print("Grade D")
    elif percentage<=40:print("Grade E")

print("Student mark and grade -")

s1=int(input("Enter the marks of subeject 1 -"))
s2=int(input("Enter the marks of subeject 2 -"))
s3=int(input("Enter the marks of subeject 3 -"))

tm=s1+s2+s3
percentage=tm/300*100
grade=calculate(percentage)

print("Total marks =",tm)
print("percentage =",percentage)
print("grade =",grade)