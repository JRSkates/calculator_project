import math
import re

class Calculator:
  def __init__(self):
    self.result = 0
    self.memory = 0

  def add(self, x, y):
    self.result = x + y
    return self.result
  
  def subtract(self, x, y):
    self.result = x - y
    return self.result
  
  def multiply(self, x, y):
    self.result = x * y
    return self.result
  
  def divide(self, x, y):
    if y == 0:
      raise ValueError("Division by zero is not allowed")
    self.result = x / y
    return self.result
  
  def square_root(self, x):
    if x < 0:
      raise ValueError("Square root of a negative number is not allowed.")
    self.result = math.sqrt(x)
    return self.result
  
  def sin(self, x):
    self.result = round(math.sin(math.radians(x)), 1)
    return self.result
  
  def cos(self, x):
    self.result = round(math.cos(math.radians(x)), 1)
    return self.result
  
  def tan(self, x):
    self.result = round(math.tan(math.radians(x)), 1)
    return self.result
  
  def calculate_expression(self, expression):
    allowed_chars = "0123456789+-*/(). "
    if any(char not in allowed_chars for char in expression):
      raise ValueError("Invalid characters in the expression.")
    
    if expression.count("(") != expression.count(")"):
      raise ValueError("Unbalanced parentheses in the expression.")
    
    expression = expression.replace("^", "**")

    self.result = eval(expression)
    return self.result

  def raise_to_power_of(self, x, y):
    self.result = x**y
    return self.result
  
  def remainder(self, x, y):
    self.result = x % y
    return self.result
  
  def factorial(self, x):
    if x < 0:
      raise ValueError("Factorial is not defined for negative numbers.")
    self.result = math.factorial(x)
    return self.result
  
  def ln(self, x):
    if x <= 0:
      raise ValueError("Natural logarithm is not defined for non-positive numbers.")
    self.result = math.log(x)
    return self.result
  
  def log(self, x, base):
    if x <= 0 or base <= 0 or base == 1:
      raise ValueError("Logarithm is not defined for non-positive numbers or base 1.")
    self.result = math.log(x, base)
    return self.result
  
  def pi(self):
    self.result = math.pi
    return self.result
  
  def e(self):
    self.result = math.e
    return self.result

  def clear_memory(self):
    self.memory = 0
  
  def store_to_memory(self):
    self.memory = self.result

  def recall_from_memory(self):
    self.result = self.memory
    return self.result
