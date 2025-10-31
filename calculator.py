import math
import json
import re
from datetime import datetime

# ---------------------- Console Style Setup ----------------------
# ANSI escape sequences for colorful console output
class Style:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    GRAY = "\033[90m"

# ---------------------- Global Variables ----------------------
calculator_memory = 0              # Memory register
calculation_history = []           # Stores operation history with timestamps

# ---------------------- Basic Arithmetic Functions ----------------------
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y

def divide(x, y):
    """Safely divide two numbers with zero protection"""
    if y == 0:
        return f"{Style.RED}Error: Division by zero is not allowed!{Style.RESET}"
    return x / y

def power(x, y): return x ** y

def modulus(x, y):
    """Return remainder with validation"""
    if y == 0:
        return f"{Style.RED}Error: Modulus by zero is not allowed!{Style.RESET}"
    return x % y

# ---------------------- Scientific Functions ----------------------
def square_root(x):
    """Calculate square root"""
    if x < 0:
        return f"{Style.RED}Error: Cannot calculate square root of negative number!{Style.RESET}"
    return math.sqrt(x)

def sine(x): return math.sin(math.radians(x))
def cosine(x): return math.cos(math.radians(x))
def tangent(x): return math.tan(math.radians(x))

def logarithm(x, base=10):
    """Calculate log with base (default 10)"""
    if x <= 0:
        return f"{Style.RED}Error: Log undefined for non-positive numbers!{Style.RESET}"
    if base <= 0 or base == 1:
        return f"{Style.RED}Error: Invalid log base!{Style.RESET}"
    return math.log(x, base)

def natural_log(x):
    """Calculate natural log"""
    if x <= 0:
        return f"{Style.RED}Error: Natural log undefined for non-positive numbers!{Style.RESET}"
    return math.log(x)

def factorial(x):
    """Calculate factorial for non-negative integers"""
    if x < 0:
        return f"{Style.RED}Error: Factorial undefined for negative numbers!{Style.RESET}"
    if not x.is_integer():
        return f"{Style.RED}Error: Factorial only defined for integers!{Style.RESET}"
    return math.factorial(int(x))

def absolute_value(x): return abs(x)

# ---------------------- Memory Functions ----------------------
def memory_clear():
    """Clear calculator memory"""
    global calculator_memory
    calculator_memory = 0
    return f"{Style.YELLOW}Memory cleared{Style.RESET}"

def memory_recall(): return calculator_memory

def memory_add(value):
    """Add a value to memory"""
    global calculator_memory
    calculator_memory += value
    return f"{Style.CYAN}Added {value} to memory. Current memory: {calculator_memory}{Style.RESET}"

def memory_subtract(value):
    """Subtract a value from memory"""
    global calculator_memory
    calculator_memory -= value
    return f"{Style.CYAN}Subtracted {value} from memory. Current memory: {calculator_memory}{Style.RESET}"

def memory_store(value):
    """Store a new value in memory"""
    global calculator_memory
    calculator_memory = value
    return f"{Style.CYAN}Stored {value} in memory{Style.RESET}"

# ---------------------- History Functions ----------------------
def add_to_history(operation, result):
    """Record each operation in history with timestamp"""
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "operation": operation,
        "result": result
    }
    calculation_history.append(entry)

def show_history():
    """Pretty print the calculation history"""
    if not calculation_history:
        print(f"{Style.DIM}No calculation history available.{Style.RESET}")
        return

    print(f"\n{Style.BOLD}{Style.MAGENTA}📜 Calculation History:{Style.RESET}")
    print(f"{Style.GRAY}{'-' * 60}{Style.RESET}")
    for i, entry in enumerate(calculation_history, 1):
        print(f"{Style.YELLOW}{i}. [{entry['timestamp']}] {Style.RESET}"
              f"{entry['operation']} = {Style.GREEN}{entry['result']}{Style.RESET}")
    print(f"{Style.GRAY}{'-' * 60}{Style.RESET}")

def clear_history():
    """Clear stored history"""
    global calculation_history
    calculation_history = []
    return f"{Style.YELLOW}History cleared{Style.RESET}"

def export_history(filename="calculator_history.json"):
    """Export history as JSON file"""
    if not calculation_history:
        return f"{Style.DIM}No history to export.{Style.RESET}"
    try:
        with open(filename, 'w') as f:
            json.dump(calculation_history, f, indent=2)
        return f"{Style.GREEN}History exported to {filename}{Style.RESET}"
    except Exception as e:
        return f"{Style.RED}Error exporting history: {str(e)}{Style.RESET}"

# ---------------------- Expression Evaluator ----------------------
def evaluate_expression(expression):
    """Safely evaluate mathematical expressions (supports trigonometric + log functions)"""
    try:
        expression = expression.replace('^', '**')
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
            return f"{Style.RED}Error: Expression contains invalid characters!{Style.RESET}"
        result = eval(expression, safe_namespace, {})
        if isinstance(result, (int, float)):
            return result
        else:
            return f"{Style.RED}Error: Invalid result type!{Style.RESET}"
    except ZeroDivisionError:
        return f"{Style.RED}Error: Division by zero in expression!{Style.RESET}"
    except SyntaxError:
        return f"{Style.RED}Error: Invalid expression syntax!{Style.RESET}"
    except Exception as e:
        return f"{Style.RED}Error: {str(e)}{Style.RESET}"

# ---------------------- Main Calculator Function ----------------------
def calculator():
    """Interactive calculator console UI"""
    print(f"{Style.BOLD}{Style.BLUE}{'═' * 70}{Style.RESET}")
    print(f"{Style.BOLD}{Style.CYAN}🧮 Welcome to Advanced Python Calculator 🧮{Style.RESET}")
    print(f"{Style.BOLD}{Style.BLUE}{'═' * 70}{Style.RESET}")
    
    print(f"\n{Style.YELLOW}📋 Available Operations:{Style.RESET}")
    print(f"{Style.CYAN}\nBasic: +  -  *  /  ^  %")
    print(f"Scientific: sqrt sin cos tan log ln ! abs")
    print(f"Memory: mc mr m+ m- ms")
    print(f"History: hist clear export")
    print(f"Expression Mode: expr (e.g., sqrt(16)+5)")
    print(f"Type 'q' to quit.{Style.RESET}")
    print(f"{Style.GRAY}{'=' * 70}{Style.RESET}")

    # Main interaction loop
    while True:
        operation = input(f"\n{Style.BOLD}➤ Enter operation or 'q' to quit: {Style.RESET}").strip().lower()
        if operation == 'q':
            print(f"\n{Style.GREEN}{'=' * 70}")
            print(f"{Style.BOLD}👋 Goodbye! Thanks for using Advanced Python Calculator.{Style.RESET}")
            print(f"{Style.GREEN}{'=' * 70}{Style.RESET}")
            break

        # Handle special commands
        if operation == 'hist': show_history(); continue
        elif operation == 'clear': print(f"✅ {clear_history()}"); continue
        elif operation == 'export': print(f"✅ {export_history()}"); continue

        # Expression evaluator mode
        if operation == 'expr':
            expression = input("Enter mathematical expression: ").strip()
            if expression:
                result = evaluate_expression(expression)
                print(f"{Style.GREEN}✅ Result: {result}{Style.RESET}")
                if not isinstance(result, str): add_to_history(expression, result)
            else:
                print(f"{Style.RED}❌ No expression provided!{Style.RESET}")
            continue

        # Memory operations
        if operation == 'mc': print(f"✅ {memory_clear()}"); continue
        elif operation == 'mr': print(f"✅ Memory value: {memory_recall()}"); continue
        elif operation in ['m+', 'm-', 'ms']:
            try:
                value = float(input("Enter value: "))
                if operation == 'm+': print(f"✅ {memory_add(value)}")
                elif operation == 'm-': print(f"✅ {memory_subtract(value)}")
                elif operation == 'ms': print(f"✅ {memory_store(value)}")
            except ValueError:
                print(f"{Style.RED}❌ Invalid input! Enter numeric value.{Style.RESET}")
            continue

        # Scientific operations
        if operation in ['sqrt', 'sin', 'cos', 'tan', 'ln', '!', 'abs']:
            try:
                num = float(input("Enter number: "))
                if operation == 'sqrt': result, op_str = square_root(num), f"√{num}"
                elif operation == 'sin': result, op_str = sine(num), f"sin({num}°)"
                elif operation == 'cos': result, op_str = cosine(num), f"cos({num}°)"
                elif operation == 'tan': result, op_str = tangent(num), f"tan({num}°)"
                elif operation == 'ln': result, op_str = natural_log(num), f"ln({num})"
                elif operation == '!': result, op_str = factorial(num), f"{int(num) if num.is_integer() else num}!"
                elif operation == 'abs': result, op_str = absolute_value(num), f"|{num}|"
                print(f"{Style.GREEN}✅ Result: {result}{Style.RESET}")
                if not isinstance(result, str): add_to_history(op_str, result)
            except ValueError:
                print(f"{Style.RED}❌ Invalid input! Enter numeric value.{Style.RESET}")
            continue

        # Logarithm with base
        if operation == 'log':
            try:
                num = float(input("Enter number: "))
                base = input("Enter base (default 10): ").strip()
                base = 10 if base == "" else float(base)
                result = logarithm(num, base)
                op_str = f"log_{base}({num})"
                print(f"{Style.GREEN}✅ Result: {result}{Style.RESET}")
                if not isinstance(result, str): add_to_history(op_str, result)
            except ValueError:
                print(f"{Style.RED}❌ Invalid input! Enter numeric values.{Style.RESET}")
            continue

        # Basic arithmetic operations
        if operation not in ['+', '-', '*', '/', '^', '%']:
            print(f"{Style.RED}❌ Invalid operation! Try again.{Style.RESET}")
            continue

        # Perform arithmetic
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print(f"{Style.RED}❌ Invalid input! Enter numeric values.{Style.RESET}")
            continue

        if operation == '+': result, op_str = add(num1, num2), f"{num1} + {num2}"
        elif operation == '-': result, op_str = subtract(num1, num2), f"{num1} - {num2}"
        elif operation == '*': result, op_str = multiply(num1, num2), f"{num1} × {num2}"
        elif operation == '/': result, op_str = divide(num1, num2), f"{num1} ÷ {num2}"
        elif operation == '^': result, op_str = power(num1, num2), f"{num1} ^ {num2}"
        elif operation == '%': result, op_str = modulus(num1, num2), f"{num1} % {num2}"

        print(f"{Style.GREEN}✅ Result: {result}{Style.RESET}")
        if not isinstance(result, str): add_to_history(op_str, result)

# ---------------------- Run Program ----------------------
if __name__ == "__main__":
    calculator()
