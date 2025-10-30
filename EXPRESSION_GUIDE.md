# Expression Evaluator Guide 📐

The Advanced Python Calculator now includes a powerful **Expression Evaluator** that allows you to calculate complex mathematical expressions in a single line!

## 🚀 Quick Start

Instead of calculating step-by-step, you can now enter full expressions:

```
➤ Enter operation or 'q' to quit: expr
Enter mathematical expression: 2+3*4
✅ Result: 14
```

## ✨ Features

### Basic Operations
- **Addition**: `5+3` → 8
- **Subtraction**: `10-4` → 6
- **Multiplication**: `6*7` → 42
- **Division**: `20/4` → 5
- **Power**: `2^8` or `2**8` → 256
- **Modulus**: `17%5` → 2

### Parentheses Support
Control order of operations with parentheses:
```
(2+3)*4     → 20
2+3*4       → 14
(10+5)/3    → 5
((8-2)*3)+5 → 23
```

### Scientific Functions
Use built-in scientific functions:
- **sqrt(x)**: Square root
  - `sqrt(16)` → 4
  - `sqrt(2)` → 1.414...
  
- **sin(x)**, **cos(x)**, **tan(x)**: Trigonometric functions (degrees)
  - `sin(30)` → 0.5
  - `cos(60)` → 0.5
  
- **log(x)**: Base-10 logarithm
  - `log(100)` → 2
  
- **ln(x)**: Natural logarithm
  - `ln(2.71828)` → 1
  
- **abs(x)**: Absolute value
  - `abs(-5)` → 5

### Mathematical Constants
- **pi**: π (≈ 3.14159)
  - `pi*2` → 6.283...
  - `2*pi` → 6.283...
  
- **e**: Euler's number (≈ 2.71828)
  - `e+1` → 3.718...

## 📋 Examples

### Simple Expressions
```
Expression: 10+20
Result: 30

Expression: 100-25
Result: 75

Expression: 12*12
Result: 144
```

### Complex Expressions
```
Expression: (5+3)*(10-2)
Result: 64

Expression: 2^10+100
Result: 1124

Expression: (100/2)-25
Result: 25
```

### Scientific Calculations
```
Expression: sqrt(144)+sqrt(16)
Result: 16

Expression: sin(30)+cos(60)
Result: 1.0

Expression: 2*pi
Result: 6.283185307179586

Expression: sqrt(16)*2+10
Result: 18
```

### Practical Examples

#### Calculate Circle Circumference
```
Expression: 2*pi*5
Result: 31.41592653589793
# Circumference of circle with radius 5
```

#### Pythagorean Theorem
```
Expression: sqrt(3**2 + 4**2)
Result: 5.0
# Find hypotenuse of right triangle
```

#### Compound Calculation
```
Expression: (100+50)*1.15
Result: 172.5
# Add 15% to sum
```

#### Area Calculation
```
Expression: pi*10**2
Result: 314.1592653589793
# Area of circle with radius 10
```

## ⚠️ Important Notes

### Order of Operations
The expression evaluator follows standard mathematical order (PEMDAS):
1. **P**arentheses
2. **E**xponents (^)
3. **M**ultiplication & **D**ivision (left to right)
4. **A**ddition & **S**ubtraction (left to right)

### Angle Units
- All trigonometric functions use **degrees**, not radians
- `sin(90)` = 1 (not sin(π/2))

### Power Operator
- Both `^` and `**` work for exponentiation
- `2^3` is the same as `2**3`

### Spaces
- Spaces are optional and ignored
- `2 + 3` is the same as `2+3`

## 🛡️ Safety Features

### Secure Evaluation
- Expressions are validated before evaluation
- Only safe mathematical operations allowed
- No access to system functions
- Protected against code injection

### Error Handling
Invalid expressions return helpful error messages:
```
Expression: 10/0
Result: Error: Division by zero in expression!

Expression: invalid_func(5)
Result: Error: Expression contains invalid characters!

Expression: 2++3
Result: Error: Invalid expression syntax!
```

## 💡 Tips & Tricks

1. **Use parentheses** for clarity: `(a+b)/(c+d)`
2. **Combine functions**: `sqrt(sin(45)**2 + cos(45)**2)`
3. **Use constants**: `pi` and `e` are available
4. **Test complex expressions** with simpler parts first
5. **Check history** to review past expressions

## 📊 Comparison: Old vs New

### Old Method (Step-by-Step)
```
➤ Enter operation: +
Enter first number: 2
Enter second number: 3
✅ Result: 5

➤ Enter operation: *
Enter first number: 5
Enter second number: 4
✅ Result: 20
```

### New Method (Expression)
```
➤ Enter operation: expr
Enter mathematical expression: (2+3)*4
✅ Result: 20
```

## 🎯 Use Cases

### Quick Calculations
Perfect for when you know the exact formula:
- Financial calculations: `1000*1.05**5`
- Unit conversions: `100*2.54` (inches to cm)
- Percentage: `250*0.15` (15% of 250)

### Scientific Work
Ideal for formulas and equations:
- Physics: `0.5*9.8*10**2` (free fall distance)
- Geometry: `4*pi*5**2` (sphere surface area)
- Engineering calculations

### Learning Tool
Great for students learning:
- Order of operations
- Function composition
- Mathematical expressions

## 🔄 History Integration

All expression evaluations are saved to history:
```
➤ Enter operation: hist

📜 Calculation History:
------------------------------------------------------------
1. [2025-10-31 15:30:00] 2+3*4 = 14
2. [2025-10-31 15:30:15] sqrt(16)+5 = 9.0
3. [2025-10-31 15:30:30] 2*pi = 6.283185307179586
------------------------------------------------------------
```

---

**Happy Calculating with Expressions! 🎉**
