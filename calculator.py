import math
import json
import re
from datetime import datetime
import atexit
import os

# -------------------------
# Smart Advanced Calculator
# - Preserves original logic and safety
# - Adds: exp, log2, deg, rad
# - Improved expression evaluator and validation
# - Cleaner terminal UI
# - Auto-saves history on exit
# -------------------------

# Global variables for calculator memory and history
calculator_memory = 0.0
calculation_history = []
HISTORY_AUTOSAVE_FILENAME = "calculator_history_autosave.json"

# ----------- Basic Arithmetic Functions -----------
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

def power(x, y):
    return x ** y

def modulus(x, y):
    if y == 0:
        return "Error: Modulus by zero is not allowed!"
    return x % y

# ----------- Scientific Functions -----------
def square_root(x):
    if x < 0:
        return "Error: Cannot calculate square root of negative number!"
    return math.sqrt(x)

# NOTE: For user-friendliness, sin/cos/tan expect degrees (keeps original behavior)
def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    # handle large values that are effectively undefined in degrees (e.g., 90 + k*180)
    try:
        return math.tan(math.radians(x))
    except Exception:
        return "Error: Tangent undefined for this input"

def logarithm(x, base=10):
    if x <= 0:
        return "Error: Logarithm undefined for non-positive numbers!"
    if base <= 0 or base == 1:
        return "Error: Invalid logarithm base!"
    return math.log(x, base)

def natural_log(x):
    if x <= 0:
        return "Error: Natural log undefined for non-positive numbers!"
    return math.log(x)

def log2(x):
    if x <= 0:
        return "Error: log2 undefined for non-positive numbers!"
    return math.log2(x)

def exponential(x):
    return math.exp(x)

def factorial(x):
    if x < 0:
        return "Error: Factorial undefined for negative numbers!"
    # Accept floats that are whole numbers (e.g., 5.0)
    if isinstance(x, float) and not x.is_integer():
        return "Error: Factorial only defined for integers!"
    return math.factorial(int(x))

def absolute_value(x):
    return abs(x)

# Utility small converters
def deg(radians_value):
    """Convert radians -> degrees"""
    return math.degrees(radians_value)

def rad(degrees_value):
    """Convert degrees -> radians"""
    return math.radians(degrees_value)

# ----------- Memory Functions -----------
def memory_clear():
    global calculator_memory
    calculator_memory = 0.0
    return "Memory cleared"

def memory_recall():
    return calculator_memory

def memory_add(value):
    global calculator_memory
    calculator_memory += value
    return f"Added {value} to memory. Current memory: {calculator_memory}"

def memory_subtract(value):
    global calculator_memory
    calculator_memory -= value
    return f"Subtracted {value} from memory. Current memory: {calculator_memory}"

def memory_store(value):
    global calculator_memory
    calculator_memory = value
    return f"Stored {value} in memory"

# ----------- History Functions -----------
def add_to_history(operation, result):
    global calculation_history
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "operation": operation,
        "result": result
    }
    calculation_history.append(entry)


def show_history():
    if not calculation_history:
        print("No calculation history available.")
        return

    print("\n Calculation History:")
    print("-" * 60)
    for i, entry in enumerate(calculation_history, 1):
        print(f"{i}. [{entry['timestamp']}] {entry['operation']} = {entry['result']}")
    print("-" * 60)


def clear_history():
    global calculation_history
    calculation_history = []
    return "History cleared"

def export_history(filename="calculator_history.json"):
    if not calculation_history:
        return "No history to export."

    try:
        with open(filename, 'w') as f:
            json.dump(calculation_history, f, indent=2)
        return f"History exported to {filename}"
    except Exception as e:
        return f"Error exporting history: {str(e)}"

# Auto-save history at program exit
def autosave_history():
    if calculation_history:
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{os.path.splitext(HISTORY_AUTOSAVE_FILENAME)[0]}_{timestamp}.json"
            with open(filename, 'w') as f:
                json.dump(calculation_history, f, indent=2)
            print(f"\n Auto-saved history to {filename}")
        except Exception as e:
            print(f"\n Failed to auto-save history: {e}")

atexit.register(autosave_history)

# ----------- Expression Evaluator -----------
def evaluate_expression(expression):
    """
    Safely evaluate a mathematical expression.
    Supports +, -, *, /, **, %, parentheses, and common functions.
    New functions added: exp, log2, deg, rad
    """
    try:
        # Normalize power symbol
        expression = expression.replace('^', '**')

        # Allowed characters check: digits, letters, operators, parentheses, dot, comma, underscore, spaces
        allowed_pattern = r'^[0-9a-zA-Z_+\-*/%()\.\s,\*\*]+$'
        if not re.match(allowed_pattern, expression):
            return "Error: Expression contains invalid characters!"

        # Safe namespace: provide only allowed functions/constants
        safe_namespace = {
            'sqrt': math.sqrt,
            'sin': lambda x: math.sin(math.radians(x)),
            'cos': lambda x: math.cos(math.radians(x)),
            'tan': lambda x: math.tan(math.radians(x)),
            'log': lambda x, b=10: math.log(x, b) if b != 1 else (_ for _ in ()).throw(ValueError('Invalid base')),
            'ln': math.log,
            'log2': math.log2,
            'exp': math.exp,
            'abs': abs,
            'pi': math.pi,
            'e': math.e,
            'deg': deg,
            'rad': rad,
        }

        # Evaluate with restricted globals and safe_namespace as locals
        result = eval(expression, {"__builtins__": None}, safe_namespace)

        if isinstance(result, (int, float)):
            return result
        else:
            return f"Error: Invalid result type!"
    except ZeroDivisionError:
        return "Error: Division by zero in expression!"
    except SyntaxError:
        return "Error: Invalid expression syntax!"
    except Exception as e:
        return f"Error: {str(e)}"

# ----------- Terminal UI Helpers -----------
def sep():
    print("=" * 70)

def header():
    sep()
    print(" Smart Advanced Python Calculator ")
    sep()

# ----------- Main Calculator Function -----------
def calculator():
    header()
    print("\n Available operations:")
    print("\n  Basic Operations:")
    print("    + : Addition              - : Subtraction")
    print("    * : Multiplication        / : Division")
    print("    ^ : Power                 % : Modulus")
    print("\n  Scientific Functions:")
    print("    sqrt : Square Root        sin : Sine (degrees)")
    print("    cos  : Cosine (degrees)   tan : Tangent (degrees)")
    print("    log  : Logarithm (base optional)           ln  : Natural Log")
    print("    log2 : Log base 2          exp : e^x")
    print("    !    : Factorial          abs : Absolute Value")
    print("    deg  : radians->degrees   rad : degrees->radians")
    print("\n  Expression Mode:")
    print("    expr : Evaluate full expressions (e.g., '2+3*4', 'sqrt(16)+5', 'exp(2)')")
    print("\n  Memory Functions:")
    print("    mc   : Memory Clear       mr  : Memory Recall")
    print("    m+   : Memory Add         m-  : Memory Subtract")
    print("    ms   : Memory Store")
    print("\n  History Functions:")
    print("    hist : Show History       clear : Clear History")
    print("    export : Export History")
    print("\n  Type 'q' to quit\n")
    sep()

    while True:
        operation = input("\n➤ Enter operation or 'q' to quit: ").strip().lower()

        if operation == 'q':
            print("\n Goodbye! Thanks for using Smart Advanced Calculator.")
            # autosave will run via atexit
            break

        if operation == 'hist':
            show_history()
            continue
        elif operation == 'clear':
            print(f" {clear_history()}")
            continue
        elif operation == 'export':
            filename = input("Enter filename (press Enter for default 'calculator_history.json'): ").strip()
            filename = filename if filename else "calculator_history.json"
            print(f" {export_history(filename)}")
            continue

        if operation == 'expr':
            expression = input("Enter mathematical expression: ").strip()
            if expression:
                result = evaluate_expression(expression)
                print(f" Result: {result}")
                if not isinstance(result, str):
                    add_to_history(expression, result)
            else:
                print(" No expression provided!")
            continue

        if operation == 'mc':
            print(f" {memory_clear()}")
            continue
        elif operation == 'mr':
            result = memory_recall()
            print(f"Memory value: {result}")
            continue
        elif operation in ['m+', 'm-', 'ms']:
            try:
                value = float(input("Enter value: "))
                if operation == 'm+':
                    print(f" {memory_add(value)}")
                elif operation == 'm-':
                    print(f" {memory_subtract(value)}")
                elif operation == 'ms':
                    print(f" {memory_store(value)}")
            except ValueError:
                print(" Invalid input! Please enter a numeric value.")
            continue

        # Single-number scientific operations
        if operation in ['sqrt', 'sin', 'cos', 'tan', 'ln', '!', 'abs', 'exp', 'log2', 'deg', 'rad']:
            try:
                num = float(input("Enter number: "))

                if operation == 'sqrt':
                    result = square_root(num)
                    op_str = f"√{num}"
                elif operation == 'sin':
                    result = sine(num)
                    op_str = f"sin({num}°)"
                elif operation == 'cos':
                    result = cosine(num)
                    op_str = f"cos({num}°)"
                elif operation == 'tan':
                    result = tangent(num)
                    op_str = f"tan({num}°)"
                elif operation == 'ln':
                    result = natural_log(num)
                    op_str = f"ln({num})"
                elif operation == '!':
                    result = factorial(num)
                    op_str = f"{int(num) if float(num).is_integer() else num}!"
                elif operation == 'abs':
                    result = absolute_value(num)
                    op_str = f"|{num}|"
                elif operation == 'exp':
                    result = exponential(num)
                    op_str = f"exp({num})"
                elif operation == 'log2':
                    result = log2(num)
                    op_str = f"log2({num})"
                elif operation == 'deg':
                    result = deg(num)
                    op_str = f"deg({num})"
                elif operation == 'rad':
                    result = rad(num)
                    op_str = f"rad({num})"

                print(f" Result: {result}")
                if not isinstance(result, str):
                    add_to_history(op_str, result)
            except ValueError:
                print(" Invalid input! Please enter a numeric value.")
            continue

        # Validate basic binary operation
        if operation not in ['+', '-', '*', '/', '^', '%']:
            print(" Invalid operation! Please choose a valid operation from the list.\n")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print(" Invalid input! Please enter numeric values.\n")
            continue

        if operation == '+':
            result = add(num1, num2)
            op_str = f"{num1} + {num2}"
        elif operation == '-':
            result = subtract(num1, num2)
            op_str = f"{num1} - {num2}"
        elif operation == '*':
            result = multiply(num1, num2)
            op_str = f"{num1} × {num2}"
        elif operation == '/':
            result = divide(num1, num2)
            op_str = f"{num1} ÷ {num2}"
        elif operation == '^':
            result = power(num1, num2)
            op_str = f"{num1} ^ {num2}"
        elif operation == '%':
            result = modulus(num1, num2)
            op_str = f"{num1} % {num2}"

        print(f" Result: {result}")
        if not isinstance(result, str):
            add_to_history(op_str, result)


if __name__ == "__main__":
    calculator()
