"""
Unit tests for the Advanced Python Calculator
Run with: python -m pytest test_calculator.py
Or: python -m unittest test_calculator.py
"""

import unittest
import math
from calculator import (
    add, subtract, multiply, divide, power, modulus,
    square_root, sine, cosine, tangent, logarithm, natural_log,
    factorial, absolute_value,
    memory_clear, memory_recall, memory_add, memory_subtract, memory_store
)


class TestBasicOperations(unittest.TestCase):
    """Test basic arithmetic operations"""
    
    def test_addition(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(0, 0), 0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)
    
    def test_subtraction(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(0, 0), 0)
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2, places=7)
    
    def test_multiplication(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(0, 100), 0)
        self.assertAlmostEqual(multiply(0.2, 0.3), 0.06, places=7)
    
    def test_division(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertAlmostEqual(divide(1, 3), 0.333333, places=5)
        # Test division by zero
        self.assertIn("Error", divide(10, 0))
    
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)
        self.assertEqual(power(10, 0), 1)
        self.assertAlmostEqual(power(2, 0.5), 1.414213, places=5)
    
    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(15, 4), 3)
        self.assertEqual(modulus(20, 5), 0)
        # Test modulus by zero
        self.assertIn("Error", modulus(10, 0))


class TestScientificFunctions(unittest.TestCase):
    """Test scientific calculator functions"""
    
    def test_square_root(self):
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), 1.414213, places=5)
        self.assertEqual(square_root(0), 0)
        # Test negative number
        self.assertIn("Error", square_root(-4))
    
    def test_sine(self):
        self.assertAlmostEqual(sine(0), 0, places=7)
        self.assertAlmostEqual(sine(30), 0.5, places=7)
        self.assertAlmostEqual(sine(90), 1, places=7)
        self.assertAlmostEqual(sine(180), 0, places=7)
    
    def test_cosine(self):
        self.assertAlmostEqual(cosine(0), 1, places=7)
        self.assertAlmostEqual(cosine(60), 0.5, places=7)
        self.assertAlmostEqual(cosine(90), 0, places=7)
    
    def test_tangent(self):
        self.assertAlmostEqual(tangent(0), 0, places=7)
        self.assertAlmostEqual(tangent(45), 1, places=7)
    
    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(100, 10), 2, places=7)
        self.assertAlmostEqual(logarithm(8, 2), 3, places=7)
        self.assertAlmostEqual(logarithm(1, 10), 0, places=7)
        # Test invalid inputs
        self.assertIn("Error", logarithm(-5, 10))
        self.assertIn("Error", logarithm(10, 0))
        self.assertIn("Error", logarithm(10, 1))
    
    def test_natural_log(self):
        self.assertAlmostEqual(natural_log(math.e), 1, places=7)
        self.assertAlmostEqual(natural_log(1), 0, places=7)
        self.assertAlmostEqual(natural_log(math.e**2), 2, places=7)
        # Test invalid input
        self.assertIn("Error", natural_log(-5))
        self.assertIn("Error", natural_log(0))
    
    def test_factorial(self):
        self.assertEqual(factorial(0.0), 1)
        self.assertEqual(factorial(1.0), 1)
        self.assertEqual(factorial(5.0), 120)
        self.assertEqual(factorial(10.0), 3628800)
        # Test invalid inputs
        self.assertIn("Error", factorial(-5.0))
        self.assertIn("Error", factorial(5.5))
    
    def test_absolute_value(self):
        self.assertEqual(absolute_value(5), 5)
        self.assertEqual(absolute_value(-5), 5)
        self.assertEqual(absolute_value(0), 0)
        self.assertAlmostEqual(absolute_value(-3.14), 3.14, places=7)


class TestMemoryFunctions(unittest.TestCase):
    """Test memory operations"""
    
    def setUp(self):
        """Clear memory before each test"""
        memory_clear()
    
    def test_memory_clear(self):
        memory_store(100)
        result = memory_clear()
        self.assertIn("cleared", result.lower())
        self.assertEqual(memory_recall(), 0)
    
    def test_memory_store_and_recall(self):
        memory_store(42)
        self.assertEqual(memory_recall(), 42)
        memory_store(-10)
        self.assertEqual(memory_recall(), -10)
    
    def test_memory_add(self):
        memory_store(10)
        memory_add(5)
        self.assertEqual(memory_recall(), 15)
        memory_add(-3)
        self.assertEqual(memory_recall(), 12)
    
    def test_memory_subtract(self):
        memory_store(20)
        memory_subtract(5)
        self.assertEqual(memory_recall(), 15)
        memory_subtract(-5)
        self.assertEqual(memory_recall(), 20)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions"""
    
    def test_large_numbers(self):
        self.assertEqual(add(1e10, 1e10), 2e10)
        self.assertEqual(multiply(1e6, 1e6), 1e12)
    
    def test_very_small_numbers(self):
        self.assertAlmostEqual(add(1e-10, 1e-10), 2e-10, places=20)
    
    def test_negative_operations(self):
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(multiply(-4, -5), 20)
        self.assertEqual(divide(-10, 2), -5)
    
    def test_zero_operations(self):
        self.assertEqual(multiply(0, 1000), 0)
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(add(0, 0), 0)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
