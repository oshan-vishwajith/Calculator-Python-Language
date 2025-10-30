# Addition
def add(x, y):
    return x + y

# Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division with zero-division check
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed!"
    return x / y

# Power function (x raised to y)
def power(x, y):
    return x ** y

# Modulus with zero check
def modulus(x, y):
    if y == 0:
        return "Error: Modulus by zero is not allowed!"
    return x % y

# ----------- Main Calculator Function -----------
def calculator():
    print("🧮 Welcome to Python Calculator 🧮")
    print("Available operations:")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    print("^ : Power")
    print("% : Modulus")
    print("Type 'q' to quit.\n")

    while True:
        # Take operation input
        operation = input("Enter operation (+, -, *, /, ^, %) or 'q' to quit: ").strip().lower()
        
        # Exit condition
        if operation == 'q':
            print("👋 Goodbye! Thanks for using Python Calculator.")
            break

        # Validate operation
        if operation not in ['+', '-', '*', '/', '^', '%']:
            print("❌ Invalid operation! Please choose one of +, -, *, /, ^, %\n")
            continue

        # Input numbers, handle non-numeric input error
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter numeric values.\n")
            continue

        # Perform selected operation
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        elif operation == '^':
            result = power(num1, num2)
        elif operation == '%':
            result = modulus(num1, num2)

        # Display result
        print(f"✅ Result: {result}\n")

# ----------- Run program -----------
if __name__ == "__main__":
    calculator()

