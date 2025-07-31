# Welcome to the Basic Calculator
# This is a simple calculator that performs addition, subtraction, multiplication, and division.
# It takes two numbers and an operation as input and displays the results of these operations.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

print("Input operation:")
print("+. Add")
print("-. Subtract")
print("*. Multiply")
print("/. Divide")

while True:
    choice = input("Enter choice (+ or - or * or /): ")

    if choice in ['+', '-', '*', '/']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print("Result:", add(num1, num2))
        elif choice == '-':
            print("Result:", subtract(num1, num2))
        elif choice == '*':
            print("Result:", multiply(num1, num2))
        elif choice == '/':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        print("Thank you for using the Basic Calculator!")
        break
print("Goodbye!")
# This calculator is a fun way to practice basic arithmetic operations in Python! 🎉