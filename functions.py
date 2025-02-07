# Built-In Functions/Standard Library Functions

y = max(67, 43, 89, 90, 23)
print("The maximum value is", y)

x = min(23, 34, 56, 99, 90)
print("The minimum value is", x)

#User-defined functions
def name ():
    print("Calvin")

name() # Calling a function

def multiply(a,b):
    return a * b
results = multiply(4,5)
print(results)

# Parameter/Variable and arguments/Value
def add(a, b):
    print(a + b)
add(1,4)
add(2,6)

def employee(name, gender, age, position, salary ):
    print(name, gender, age, position, salary)
employee("Calvin","Male",22,"CEO",200000)
employee("James","Male",27,"Secretary",100000)
employee("Arnold","Male",32,"Market Director",180000)
employee("Alex","Male",30,"HR",150000)

# Write a program that displays details of 5 students.
# Use a user-defined function with the help of parameters and arguments.
# Fullname, age, course, gender

def student(Fullname, age, course, gender):
    print(Fullname, age, course, gender)
student("Ian Jackson",18,"MIT","Male")
student("Sand Cheeks",17,"Cyber Security","Female")
student("Squidward",18,"Cyber Security","Male")
student("Diana Halid",20,"MIT","Female")
student("Spenser Liam",22,"Cyber Security","Male")





