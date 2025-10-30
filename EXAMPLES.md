# Calculator Usage Examples 📚

This document provides detailed examples of how to use all features of the Advanced Python Calculator.

## Table of Contents
1. [Basic Operations](#basic-operations)
2. [Scientific Functions](#scientific-functions)
3. [Memory Operations](#memory-operations)
4. [History Features](#history-features)
5. [Common Use Cases](#common-use-cases)

---

## Basic Operations

### Addition (+)
Calculate the sum of two numbers.

```
➤ Enter operation or 'q' to quit: +
Enter the first number: 25
Enter the second number: 17
✅ Result: 42.0
```

### Subtraction (-)
Calculate the difference between two numbers.

```
➤ Enter operation or 'q' to quit: -
Enter the first number: 100
Enter the second number: 42
✅ Result: 58.0
```

### Multiplication (*)
Calculate the product of two numbers.

```
➤ Enter operation or 'q' to quit: *
Enter the first number: 12
Enter the second number: 8
✅ Result: 96.0
```

### Division (/)
Divide one number by another (with zero-protection).

```
➤ Enter operation or 'q' to quit: /
Enter the first number: 144
Enter the second number: 12
✅ Result: 12.0
```

### Power (^)
Raise a number to a power.

```
➤ Enter operation or 'q' to quit: ^
Enter the first number: 2
Enter the second number: 10
✅ Result: 1024.0
```

### Modulus (%)
Find the remainder of division.

```
➤ Enter operation or 'q' to quit: %
Enter the first number: 17
Enter the second number: 5
✅ Result: 2.0
```

---

## Scientific Functions

### Square Root (sqrt)
Calculate the square root of a number.

```
➤ Enter operation or 'q' to quit: sqrt
Enter number: 144
✅ Result: 12.0
```

**Use Case**: Finding the side length of a square given its area.

### Sine (sin)
Calculate sine of an angle in degrees.

```
➤ Enter operation or 'q' to quit: sin
Enter number: 30
✅ Result: 0.5
```

**Common Values**:
- sin(0°) = 0
- sin(30°) = 0.5
- sin(45°) ≈ 0.707
- sin(90°) = 1

### Cosine (cos)
Calculate cosine of an angle in degrees.

```
➤ Enter operation or 'q' to quit: cos
Enter number: 60
✅ Result: 0.5
```

**Common Values**:
- cos(0°) = 1
- cos(60°) = 0.5
- cos(90°) = 0

### Tangent (tan)
Calculate tangent of an angle in degrees.

```
➤ Enter operation or 'q' to quit: tan
Enter number: 45
✅ Result: 1.0
```

### Logarithm (log)
Calculate logarithm with custom base (default base 10).

```
➤ Enter operation or 'q' to quit: log
Enter number: 100
Enter base (press Enter for base 10): 
✅ Result: 2.0

➤ Enter operation or 'q' to quit: log
Enter number: 8
Enter base (press Enter for base 10): 2
✅ Result: 3.0
```

**Use Cases**:
- log₁₀(100) = 2 (How many 10s multiply to 100?)
- log₂(8) = 3 (How many 2s multiply to 8?)

### Natural Logarithm (ln)
Calculate natural logarithm (base e ≈ 2.71828).

```
➤ Enter operation or 'q' to quit: ln
Enter number: 2.71828
✅ Result: 1.0
```

### Factorial (!)
Calculate factorial of a number (n! = n × (n-1) × ... × 1).

```
➤ Enter operation or 'q' to quit: !
Enter number: 5
✅ Result: 120
```

**Factorials**:
- 0! = 1
- 5! = 120
- 10! = 3,628,800

### Absolute Value (abs)
Get the absolute (positive) value of a number.

```
➤ Enter operation or 'q' to quit: abs
Enter number: -42
✅ Result: 42
```

---

## Memory Operations

Memory operations allow you to store and manipulate values across calculations.

### Memory Store (ms)
Store a value in memory.

```
➤ Enter operation or 'q' to quit: ms
Enter value: 100
✅ Stored 100 in memory
```

### Memory Recall (mr)
Retrieve the value from memory.

```
➤ Enter operation or 'q' to quit: mr
✅ Memory value: 100
```

### Memory Add (m+)
Add a value to the current memory.

```
➤ Enter operation or 'q' to quit: m+
Enter value: 50
✅ Added 50 to memory. Current memory: 150
```

### Memory Subtract (m-)
Subtract a value from the current memory.

```
➤ Enter operation or 'q' to quit: m-
Enter value: 30
✅ Subtracted 30 from memory. Current memory: 120
```

### Memory Clear (mc)
Clear all memory.

```
➤ Enter operation or 'q' to quit: mc
✅ Memory cleared
```

### Memory Workflow Example
```
1. Calculate: 25 + 75 = 100
2. Store: ms → 100
3. Calculate: 50 × 2 = 100  
4. Add to memory: m+ → 100 (memory now = 200)
5. Recall: mr → 200
```

---

## History Features

### View History (hist)
Display all calculations from the current session.

```
➤ Enter operation or 'q' to quit: hist

📜 Calculation History:
------------------------------------------------------------
1. [2025-10-31 14:30:15] 25 + 17 = 42.0
2. [2025-10-31 14:30:45] 100 - 42 = 58.0
3. [2025-10-31 14:31:20] √144 = 12.0
4. [2025-10-31 14:31:50] sin(30°) = 0.5
------------------------------------------------------------
```

### Export History (export)
Save calculation history to a JSON file.

```
➤ Enter operation or 'q' to quit: export
✅ History exported to calculator_history.json
```

**JSON Format**:
```json
[
  {
    "timestamp": "2025-10-31 14:30:15",
    "operation": "25 + 17",
    "result": 42.0
  },
  {
    "timestamp": "2025-10-31 14:30:45",
    "operation": "100 - 42",
    "result": 58.0
  }
]
```

### Clear History (clear)
Remove all calculation history.

```
➤ Enter operation or 'q' to quit: clear
✅ History cleared
```

---

## Common Use Cases

### 1. Calculate Circle Area
**Formula**: Area = π × r²

```
# For radius = 5
➤ Enter operation: ^
Enter the first number: 5
Enter the second number: 2
✅ Result: 25.0

# Then multiply by pi (≈ 3.14159)
➤ Enter operation: *
Enter the first number: 25
Enter the second number: 3.14159
✅ Result: 78.53975
```

### 2. Calculate Triangle Height (Trigonometry)
If you know the hypotenuse and angle:

```
# Height = hypotenuse × sin(angle)
# For hypotenuse = 10, angle = 30°

➤ Enter operation: sin
Enter number: 30
✅ Result: 0.5

➤ Enter operation: *
Enter the first number: 10
Enter the second number: 0.5
✅ Result: 5.0
```

### 3. Compound Interest Calculation
Store principal, add interest repeatedly:

```
# Starting principal: $1000, Interest rate: 10%

➤ Enter operation: ms
Enter value: 1000
✅ Stored 1000 in memory

# Add 10% interest
➤ Enter operation: *
Enter the first number: 1000
Enter the second number: 0.10
✅ Result: 100.0

➤ Enter operation: m+
Enter value: 100
✅ Added 100 to memory. Current memory: 1100

➤ Enter operation: mr
✅ Memory value: 1100
```

### 4. Statistical Calculations
Calculate average (mean):

```
# Numbers: 10, 20, 30, 40, 50
# Average = Sum / Count

➤ Enter operation: +
Enter the first number: 10
Enter the second number: 20
✅ Result: 30.0

# Continue adding...
# Final sum: 150

➤ Enter operation: /
Enter the first number: 150
Enter the second number: 5
✅ Result: 30.0
```

### 5. Percentage Calculations
Calculate what percentage one number is of another:

```
# What percentage is 15 of 60?
# Formula: (part / whole) × 100

➤ Enter operation: /
Enter the first number: 15
Enter the second number: 60
✅ Result: 0.25

➤ Enter operation: *
Enter the first number: 0.25
Enter the second number: 100
✅ Result: 25.0
```

---

## Error Handling Examples

### Division by Zero
```
➤ Enter operation: /
Enter the first number: 10
Enter the second number: 0
✅ Result: Error: Division by zero is not allowed!
```

### Invalid Input
```
➤ Enter operation: +
Enter the first number: abc
❌ Invalid input! Please enter numeric values.
```

### Negative Square Root
```
➤ Enter operation: sqrt
Enter number: -4
✅ Result: Error: Cannot calculate square root of negative number!
```

### Invalid Operation
```
➤ Enter operation: xyz
❌ Invalid operation! Please choose a valid operation from the list.
```

---

## Tips & Tricks 💡

1. **Use Memory for Complex Calculations**: Store intermediate results to avoid recalculating.

2. **Export History Before Quitting**: Save your work with the `export` command.

3. **Check History for Errors**: Use `hist` to review past calculations.

4. **Calculator Shortcuts**:
   - Use `q` to quit quickly
   - Press Enter for default log base (10)
   - Use negative numbers for subtraction in memory

4. **Precision**: Results are displayed as floats; for exact integers, ignore `.0`

5. **Trigonometry**: Remember that all angles are in DEGREES, not radians.

---

**Happy Calculating! 🧮**
