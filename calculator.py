import math
import json
import re
from datetime import datetime

# ---------------- Global variables ----------------
calculator_memory = 0
calculation_history = []

# ==================================================
#               BASIC ARITHMETIC FUNCTIONS
# ==================================================
def add(x, y):
    """Return sum of x and y"""
    return x + y

def subtract(x, y):
    """Return difference of x and y"""
    return x - y

def multiply(x, y):
    """Return product of x and y"""
    return x * y

def divide(x, y):
    """Return division of x by y, handle division by zero"""
    if y == 0:
        return "Error: Division by zero is not allowed!"
    return x / y

def power(x, y):
    """Return x raised to y"""
    return x ** y

def modulus(x, y):
    """Return modulus of x and y, handle zero divisor"""
    if y == 0:
        return "Error: Modulus by zero is not allowed!"
    return x % y

# ==================================================
#               SCIENTIFIC FUNCTIONS
# ==================================================
def square_root(x):
    """Calculate square root of x"""
    if x < 0:
        return "Error: Cannot calculate square root of negative number!"
    return math.sqrt(x)

def sine(x):
    """Calculate sine of x in degrees"""
    return math.sin(math.radians(x))

def cosine(x):
    """Calculate cosine of x in degrees"""
    return math.cos(math.radians(x))

def tangent(x):
    """Calculate tangent of x in degrees"""
    return math.tan(math.radians(x))

def logarithm(x, base=10):
    """Calculate logarithm of x with optional base"""
    if x <= 0:
        return "Error: Logarithm undefined for non-positive numbers!"
    if base <= 0 or base == 1:
        return "Error: Invalid logarithm base!"
    return math.log(x, base)

def natural_log(x):
    """Calculate natural logarithm (base e)"""
    if x <= 0:
        return "Error: Natural log undefined for non-positive numbers!"
    return math.log(x)

def factorial(x):
    """Calculate factorial of x if integer and non-negative"""
    if x < 0:
        return "Error: Factorial undefined for negative numbers!"
    if not x.is_integer():
        return "Error: Factorial only defined for integers!"
    return math.factorial(int(x))

def absolute_value(x):
    """Return absolute value of x"""
    return abs(x)

# ==================================================
#               MEMORY FUNCTIONS
# ==================================================
def memory_clear():
    """Clear calculator memory"""
    global calculator_memory
    calculator_memory = 0
    return "Memory cleared"

def memory_recall():
    """Return value from memory"""
    return calculator_memory

def memory_add(value):
    """Add value to memory"""
    global calculator_memory
    calculator_memory += value
    return f"Added {value} to memory. Current memory: {calculator_memory}"

def memory_subtract(value):
    """Subtract value from memory"""
    global calculator_memory
    calculator_memory -= value
    return f"Subtracted {value} from memory. Current memory: {calculator_memory}"

def memory_store(value):
    """Store a new value in memory"""
    global calculator_memory
    calculator_memory = value
    return f"Stored {value} in memory"

# ==================================================
#               HISTORY FUNCTIONS
# ==================================================
def add_to_history(operation, result):
    """Record operation and result in history"""
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "operation": operation,
        "result": result
    }
    calculation_history.append(entry)

def show_history():
    """Display calculation history"""
    if not calculation_history:
        return "No calculation history available."
    print("\nCalculation History:")
    print("-" * 60)
    for i, entry in enumerate(calculation_history, 1):
        print(f"{i}. [{entry['timestamp']}] {entry['operation']} = {entry['result']}")
    print("-" * 60)

def clear_history():
    """Clear calculation history"""
    global calculation_history
    calculation_history = []
    return "History cleared"

def export_history(filename="calculator_history.json"):
    """Export calculation history to JSON file"""
    if not calculation_history:
        return "No history to export."
    try:
        with open(filename, 'w') as f:
            json.dump(calculation_history, f, indent=2)
        return f"History exported to {filename}"
    except Exception as e:
        return f"Error exporting history: {str(e)}"

# ==================================================
#               EXPRESSION EVALUATOR
# ==================================================
def evaluate_expression(expression):
    """Safely evaluate a mathematical expression."""
    try:
        expression = expression.replace('^', '**')  # Convert ^ to ** for power

        # Define safe math environment
        safe_namespace = {
            'sqrt': math.sqrt,
            'sin': lambda x: math.sin(math.radians(x)),
            'cos': lambda x: math.cos(math.radians(x)),
            'tan': lambda x: math.tan(math.radians(x)),
            'log': math.log10,
            'ln': math.log,
            'abs': abs,
            'pi': math.pi,
            'e': math.e,
            '__builtins__': {}
        }

        allowed_pattern = r'^[\d+\-*/().,\s^*sqrtincoalgbe]+$'
        if not re.match(allowed_pattern, expression, re.IGNORECASE):
            return "Error: Expression contains invalid characters!"

        result = eval(expression, safe_namespace, {})
        return result if isinstance(result, (int, float)) else "Error: Invalid result type!"
    except ZeroDivisionError:
        return "Error: Division by zero in expression!"
    except SyntaxError:
        return "Error: Invalid expression syntax!"
    except Exception as e:
        return f"Error: {str(e)}"

# ==================================================
#               MAIN CALCULATOR FUNCTION
# ==================================================
def calculator():
    """Interactive calculator main loop"""
    print("=" * 70)
    print("Welcome to Advanced Python Calculator")
    print("=" * 70)
    print("\nAvailable operations:")
    print("  +  -  *  /  ^  %   --> Basic operations")
    print("  sqrt sin cos tan log ln abs !  --> Scientific functions")
    print("  expr  --> Evaluate expressions (e.g., sqrt(16)+2^3)")
    print("  mc mr m+ m- ms  --> Memory functions")
    print("  hist clear export  --> History functions")
    print("  q  --> Quit\n")
    print("=" * 70)

    # Main loop
    while True:
        operation = input("\nEnter operation or 'q' to quit: ").strip().lower()

        if operation == 'q':
            print("\n" + "=" * 70)
            print("Goodbye! Thanks for using Advanced Python Calculator.")
            print("=" * 70)
            break

        # --- History operations ---
        if operation == 'hist':
            show_history(); continue
        elif operation == 'clear':
            print(f"{clear_history()}"); continue
        elif operation == 'export':
            print(f"{export_history()}"); continue

        # --- Expression evaluation ---
        if operation == 'expr':
            expr = input("Enter mathematical expression: ").strip()
            if not expr:
                print("No expression provided!"); continue
            result = evaluate_expression(expr)
            print(f"Result: {result}")
            if not isinstance(result, str):
                add_to_history(expr, result)
            continue

        # --- Memory operations ---
        if operation == 'mc':
            print(f"{memory_clear()}"); continue
        elif operation == 'mr':
            print(f"Memory value: {memory_recall()}"); continue
        elif operation in ['m+', 'm-', 'ms']:
            try:
                value = float(input("Enter value: "))
                msg = (memory_add(value) if operation == 'm+' else
                       memory_subtract(value) if operation == 'm-' else
                       memory_store(value))
                print(f"{msg}")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
            continue

        # --- Scientific single-number operations ---
        if operation in ['sqrt', 'sin', 'cos', 'tan', 'ln', '!', 'abs']:
            try:
                num = float(input("Enter number: "))
                if operation == 'sqrt': result, op = square_root(num), f"√{num}"
                elif operation == 'sin': result, op = sine(num), f"sin({num}°)"
                elif operation == 'cos': result, op = cosine(num), f"cos({num}°)"
                elif operation == 'tan': result, op = tangent(num), f"tan({num}°)"
                elif operation == 'ln': result, op = natural_log(num), f"ln({num})"
                elif operation == '!': result, op = factorial(num), f"{int(num)}!"
                elif operation == 'abs': result, op = absolute_value(num), f"|{num}|"
                print(f"Result: {result}")
                if not isinstance(result, str): add_to_history(op, result)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
            continue

        # --- Logarithm special case ---
        if operation == 'log':
            try:
                num = float(input("Enter number: "))
                base_in = input("Enter base (press Enter for base 10): ").strip()
                base = 10 if base_in == "" else float(base_in)
                result = logarithm(num, base)
                print(f"Result: {result}")
                if not isinstance(result, str):
                    add_to_history(f"log_{base}({num})", result)
            except ValueError:
                print("Invalid input! Please enter numeric values.")
            continue

        # --- Basic arithmetic operations ---
        if operation not in ['+', '-', '*', '/', '^', '%']:
            print("Invalid operation! Please choose a valid operation.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        # Map operator to corresponding function
        operations = {
            '+': (add, f"{num1} + {num2}"),
            '-': (subtract, f"{num1} - {num2}"),
            '*': (multiply, f"{num1} × {num2}"),
            '/': (divide, f"{num1} ÷ {num2}"),
            '^': (power, f"{num1} ^ {num2}"),
            '%': (modulus, f"{num1} % {num2}")
        }

        func, op_str = operations[operation]
        result = func(num1, num2)
        print(f"Result: {result}")
        if not isinstance(result, str): add_to_history(op_str, result)

# ==================================================
#               NEW WRAPPER FUNCTION
# ==================================================
def run_calculator():
    """
    Wrapper function to run the calculator.
    Allows importing this module elsewhere without auto-start.
    """
    calculator()

# ==================================================
#               PROGRAM ENTRY POINT
# ==================================================
if __name__ == "__main__":
    run_calculator()
