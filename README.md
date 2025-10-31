# Advanced Python Calculator 🧮

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)
![Hacktoberfest](https://img.shields.io/badge/hacktoberfest-friendly-orange)

An advanced command-line calculator built with Python, featuring basic arithmetic, scientific functions, memory operations, and calculation history tracking. Perfect for students, developers, and Hacktoberfest contributors!

## ✨ Features

### Basic Operations

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division (with zero-division protection)
- 🔺 Power (exponentiation)
- 📐 Modulus

### Scientific Functions

- √ **Square Root** - Calculate square roots
- 📊 **Trigonometry** - Sine, Cosine, Tangent (in degrees)
- 📈 **Logarithms** - Base-10 logarithm and natural logarithm
- ❗ **Factorial** - Calculate factorials
- |x| **Absolute Value** - Get absolute values

### Expression Evaluator 🆕
- 📐 **Full Expression Evaluation** - Calculate complete expressions in one go
- 🔢 **Support for**: `2+3*4`, `(10+5)/3`, `sqrt(16)+2^3`
- 🔗 **Function Chaining** - Combine multiple operations and functions
- 🎯 **Mathematical Constants** - Use `pi` and `e` in expressions
- 📖 **Full Guide**: See [EXPRESSION_GUIDE.md](EXPRESSION_GUIDE.md) for detailed usage

### Quick Calculations 🆕
- 💵 **Percentage Calculator** - Calculate percentages instantly
- 💰 **Tip Calculator** - Calculate tips and split bills
- 🏷️ **Discount Calculator** - Find final prices after discounts
- 📈 **Compound Interest** - Calculate investment growth
- ⚕️ **BMI Calculator** - Calculate Body Mass Index
- 📖 **Full Guide**: See [QUICK_CALC_GUIDE.md](QUICK_CALC_GUIDE.md) for detailed usage

### Memory Functions
- 💾 **Memory Store (MS)** - Store values in memory
- 🔄 **Memory Recall (MR)** - Retrieve stored values
- ➕ **Memory Add (M+)** - Add to memory
- ➖ **Memory Subtract (M-)** - Subtract from memory
- 🗑️ **Memory Clear (MC)** - Clear memory

### History Features

- 📜 **Calculation History** - Track all calculations with timestamps
- 💾 **Export History** - Save history to JSON file
- 🔍 **View History** - Review past calculations
- 🗑️ **Clear History** - Remove all history

### Error Handling

- ✅ Input validation
- ⚠️ Division by zero protection
- 🛡️ Invalid operation handling
- 🔢 Non-numeric input handling

## 🚀 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/induwara-dissanayake/Calculator-Python-Language.git
   ```

2. **Navigate to the project folder:**

   ```bash
   cd Calculator-Python-Language
   ```

3. **Install optional dependencies (for testing):**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the calculator:**
   ```bash
   python calculator.py
   ```

## 📖 Usage

### Basic Operations Example:

```
➤ Enter operation or 'q' to quit: +
Enter the first number: 15
Enter the second number: 7
✅ Result: 22.0
```

### Scientific Functions Example:

```
➤ Enter operation or 'q' to quit: sqrt
Enter number: 16
✅ Result: 4.0

➤ Enter operation or 'q' to quit: sin
Enter number: 30
✅ Result: 0.5
```

### Memory Operations Example:

```
➤ Enter operation or 'q' to quit: ms
Enter value: 100
✅ Stored 100 in memory

➤ Enter operation or 'q' to quit: m+
Enter value: 50
✅ Added 50 to memory. Current memory: 150

➤ Enter operation or 'q' to quit: mr
✅ Memory value: 150
```

### History Features Example:

```
➤ Enter operation or 'q' to quit: hist

📜 Calculation History:
------------------------------------------------------------
1. [2025-10-31 10:15:23] 15 + 7 = 22.0
2. [2025-10-31 10:16:45] √16 = 4.0
3. [2025-10-31 10:17:30] sin(30°) = 0.5
------------------------------------------------------------
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Using unittest
python -m unittest test_calculator.py

# Using pytest (if installed)
python -m pytest test_calculator.py -v
```

The test suite includes:

- ✅ 40+ unit tests
- 🧪 Tests for all operations
- 🛡️ Edge case testing
- ⚠️ Error condition testing

## 📋 Available Commands

| Command  | Description     | Usage                       |
| -------- | --------------- | --------------------------- |
| `+`      | Addition        | Requires 2 numbers          |
| `-`      | Subtraction     | Requires 2 numbers          |
| `*`      | Multiplication  | Requires 2 numbers          |
| `/`      | Division        | Requires 2 numbers          |
| `^`      | Power           | Requires 2 numbers          |
| `%`      | Modulus         | Requires 2 numbers          |
| `sqrt`   | Square Root     | Requires 1 number           |
| `sin`    | Sine            | Requires 1 number (degrees) |
| `cos`    | Cosine          | Requires 1 number (degrees) |
| `tan`    | Tangent         | Requires 1 number (degrees) |
| `log`    | Logarithm       | Requires number and base    |
| `ln`     | Natural Log     | Requires 1 number           |
| `!`      | Factorial       | Requires 1 integer          |
| `abs`    | Absolute Value  | Requires 1 number           |
| `mc`     | Memory Clear    | No input needed             |
| `mr`     | Memory Recall   | No input needed             |
| `m+`     | Memory Add      | Requires 1 number           |
| `m-`     | Memory Subtract | Requires 1 number           |
| `ms`     | Memory Store    | Requires 1 number           |
| `hist`   | Show History    | No input needed             |
| `clear`  | Clear History   | No input needed             |
| `export` | Export History  | No input needed             |
| `q`      | Quit            | No input needed             |

## 🤝 Contributing

Contributions are welcome! This project is perfect for:

- 🎃 **Hacktoberfest** participants
- 🎓 **Beginners** learning Python
- 👨‍💻 **Developers** wanting to add features

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Quick Start for Contributors:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Run tests (`python -m unittest test_calculator.py`)
5. Commit your changes (`git commit -m 'Add: AmazingFeature'`)
6. Push to the branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

## 🎯 Future Enhancements

- [ ] Graphical User Interface (GUI)
- [ ] Complex number support
- [ ] Matrix operations
- [ ] Equation solver
- [ ] Unit conversions
- [ ] Statistical functions
- [ ] Graphing capabilities
- [ ] Web interface
- [ ] Mobile app version

## 📝 Requirements

- **Python**: 3.7 or higher
- **Dependencies**: None (uses only standard library)
- **Optional**: pytest for testing

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with ❤️ for the Python community
- Perfect for Hacktoberfest contributions
- Special thanks to all contributors

## 📞 Contact & Support

- 🐛 **Report bugs**: Open an issue
- 💡 **Feature requests**: Open an issue
- 🤝 **Discussions**: Start a discussion

---

**⭐ Star this repository if you find it helpful!**

Made with 💻 and ☕ for Hacktoberfest 2025

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is open source and available under the [MIT License](LICENSE).
