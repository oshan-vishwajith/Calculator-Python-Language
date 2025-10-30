"""
Python Calculator 🧮
A simple command-line calculator for basic arithmetic operations.
Author: ChatGPT (example)
Requirements: Python 3.x
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed!"
    return x / y
def calculator():
    print("🧮 Welcome to Python Calculator 🧮")
    print("Available operations: +  -  *  /")
    print("Type 'q' to quit.\n")

    while True:
        operation = input("Enter operation (+, -, *, /) or 'q' to quit: ").strip()
        if operation.lower() == 'q':
            print("Goodbye! 👋")
            break

        if operation not in ['+', '-', '*', '/']:
            print("❌ Invalid operation! Please choose one of +, -, *, /")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter numeric values.")
            continue
