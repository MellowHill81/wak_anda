# Function for addition
from random import choice


def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Main Function
def calculator():
    print("Select operator:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

# Taking user input
choice = input("Enter choice (1/2/3/4): ")

# Checking if the input is valid
if choice in ['1','2','3','4']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Performing operation based on choice
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num2} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid Input")

# Calling the calculator function
if calculator() == "_main_":
    calculator()



