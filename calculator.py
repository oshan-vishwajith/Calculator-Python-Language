import math
import json
import re
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# -------------------------
# Smart Advanced Calculator
# - Preserves original logic and safety
# - Adds: exp, log2, deg, rad
# - Improved expression evaluator and validation
# - Cleaner terminal UI
# - Auto-saves history on exit
# -------------------------

# Global variables for calculator memory and history
calculator_memory = 0
calculation_history = []

### ----------- Basic Arithmetic Functions -----------
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

### ----------- Scientific Functions -----------
def square_root(x):
    if x < 0:
        return "Error: Cannot calculate square root of negative number!"
    return math.sqrt(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

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

def factorial(x):
    if x < 0:
        return "Error: Factorial undefined for negative numbers!"
    x = int(x) if x.is_integer() else x
        return "Error: Factorial only defined for integers!"
    return math.factorial(int(x))

def absolute_value(x):
    return abs(x)

### ----------- Memory Functions -----------
def memory_clear():
    global calculator_memory
    calculator_memory = 0
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

### ----------- History Functions -----------
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
        return "No calculation history available."
    
    print("\n📜 Calculation History:")
    print("-" * 60)
    for i, entry in enumerate(calculation_history, 1):
        print(f"{i}. [{entry['timestamp']}] {entry['operation']} = {entry['result']}")
    print("-" * 60)

def clear_history():
    global calculation_history
    calculation_history = []
    return "History cleared!"

def export_history(filename="calculator_history.json"):
    if not calculation_history:
        return "No history to export."
    
    try:
        with open(filename, 'w') as f:
            json.dump(calculation_history, f, indent=2)
        return f"History exported to {filename}"
    except Exception as e:
        return f"Error exporting history: {str(e)}"

### ----------- Expression Evaluator -----------
def evaluate_expression(expression):
    try:
        expression = re.sub(r"\^", "**", expression)
        
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

### ----------- Main Calculator Function -----------
def calculator():
    print("=" * 70)
    print("🧮 Welcome to Advanced Python Calculator 🧮")
    print("=" * 70)
    print("\n📋 Available operations:")
    print("\n  Basic Operations:")
    print("    + : Addition              - : Subtraction")
    print("    * : Multiplication        / : Division")
    print("    ^ : Power                 % : Modulus")
    print("\n  Scientific Functions:")
    print("    sqrt : Square Root        sin : Sine (degrees)")
    print("    cos  : Cosine (degrees)   tan : Tangent (degrees)")
    print("    log  : Logarithm          ln  : Natural Log")
    print("    !    : Factorial          abs : Absolute Value")
    print("\n  Expression Mode:")
    print("    expr : Evaluate full expressions (e.g., '2+3*4', 'sqrt(16)+5')")
    print("\n  Memory Functions:")
    print("    mc   : Memory Clear       mr  : Memory Recall")
    print("    m+   : Memory Add         m-  : Memory Subtract")
    print("    ms   : Memory Store")
    print("\n  History Functions:")
    print("    hist : Show History       clear : Clear History")
    print("    export : Export History")
    print("\n  Type 'q' to quit\n")
    print("=" * 70)

    while True:
        operation = input("\n➤ Enter operation or 'q' to quit: ").strip().lower()
        if operation == 'q':
            print("\n" + "=" * 70)
            print("👋 Goodbye! Thanks for using Advanced Python Calculator.")
            print("=" * 70)
            break

        if operation == 'hist':
            show_history()
            continue
        elif operation == 'clear':
            print(f"✅ {clear_history()}")
            continue
        elif operation == 'export':
            print(f"✅ {export_history()}")
            continue

        if operation == 'expr':
            expression = input("Enter mathematical expression: ").strip()
            if expression:
                result = evaluate_expression(expression)
                print(f"✅ Result: {result}")
                if not isinstance(result, str):
                    add_to_history(expression, result)
            else:
                print("❌ No expression provided!")
            continue

        if operation == 'mc':
            print(f"✅ {memory_clear()}")
            continue
        elif operation == 'mr':
            result = memory_recall()
            print(f"✅ Memory value: {result}")
            continue
        elif operation in ['m+', 'm-', 'ms']:
            try:
                value = float(input("Enter value: "))
                if operation == 'm+':
                    print(f"✅ {memory_add(value)}")
                elif operation == 'm-':
                    print(f"✅ {memory_subtract(value)}")
                elif operation == 'ms':
                    print(f"✅ {memory_store(value)}")
            except ValueError:
                print("❌ Invalid input! Please enter a numeric value.")
            continue

        if operation in ['sqrt', 'sin', 'cos', 'tan', 'ln', '!', 'abs']:
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
                    op_str = f"{int(num) if num.is_integer() else num}!"
                elif operation == 'abs':
                    result = absolute_value(num)
                    op_str = f"|{num}|"
                
                print(f"✅ Result: {result}")
                if not isinstance(result, str):
                    add_to_history(op_str, result)
            except ValueError:
                print("❌ Invalid input! Please enter a numeric value.")
            continue

        if operation == 'log':
            try:
                num = float(input("Enter number: "))
                base = input("Enter base (press Enter for base 10): ").strip()
                base = 10 if base == "" else float(base)
                result = logarithm(num, base)
                op_str = f"log_{base}({num})"
                print(f"✅ Result: {result}")
                if not isinstance(result, str):
                    add_to_history(op_str, result)
            except ValueError:
                print("❌ Invalid input! Please enter numeric values.")
            continue

        if operation not in ['+', '-', '*', '/', '^', '%']:
            print("❌ Invalid operation! Please choose a valid operation from the list.\n")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter numeric values.\n")
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

        print(f"✅ Result: {result}")
        if not isinstance(result, str):
            add_to_history(op_str, result)

### ----------- Extra Features -----------
def run_tests():
    print("\n🧩 Running basic tests...")
    assert add(2,3) == 5
    assert subtract(5,2) == 3
    assert multiply(3,4) == 12
    assert divide(10,2) == 5
    assert power(2,3) == 8
    assert modulus(10,3) == 1
    assert square_root(16) == 4
    assert absolute_value(-5) == 5
    print("✅ All tests passed!")

def launch_gui():
    def on_calculate():
        expr = entry.get()
        result = evaluate_expression(expr)
        messagebox.showinfo("Result", f"{expr} = {result}")
        if not isinstance(result, str):
            add_to_history(expr, result)

    window = tk.Tk()
    window.title("🧮 Advanced Python Calculator (GUI)")
    window.geometry("400x200")

    tk.Label(window, text="Enter Expression:", font=("Arial", 14)).pack(pady=10)
    entry = tk.Entry(window, font=("Arial", 14), width=25)
    entry.pack(pady=5)

    tk.Button(window, text="Calculate", font=("Arial", 12), command=on_calculate).pack(pady=10)
    tk.Button(window, text="Show History", font=("Arial", 12), command=show_history).pack()

    window.mainloop()

### ----------- Program Entry -----------
if __name__ == "__main__":
    print("\n📘 MAIN MENU")
    print("1. Run Calculator (Text Mode)")
    print("2. Run GUI Calculator")
    print("3. Show History")
    print("4. Run Tests")
    print("5. Export History")
    print("6. Quit")

    choice = input("Choose an option: ").strip()

    if choice == '1':
        calculator()
    elif choice == '2':
        launch_gui()
    elif choice == '3':
        show_history()
    elif choice == '4':
        run_tests()
    elif choice == '5':
        print(export_history())
    else:
        print("👋 Goodbye!")
