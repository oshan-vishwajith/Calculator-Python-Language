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
