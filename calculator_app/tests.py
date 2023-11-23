from django.test import TestCase
from calculator_app.calculator import Calculator

class CalculatorTestCase(TestCase):
  def setUp(self):
    self.calc = Calculator()

  def test_addition(self):
    result = self.calc.add(3, 5)
    assert result == 8
  
  def test_subtraction(self):
    result = self.calc.subtract(5, 3)
    assert result == 2
  
  def test_multiply(self):
    result = self.calc.multiply(3, 5)
    assert result == 15
  
  def test_divide(self):
    result = self.calc.divide(10, 2) 
    assert result == 5
  
  def test_raise_to_power_of(self):
    result = self.calc.raise_to_power_of(2, 4)
    assert result == 16
  
  def test_remainder(self):
    result = self.calc.remainder(2, 5)
    assert result == 2
  
  def test_square_root(self):
    result = self.calc.square_root(25)
    assert result == 5
  
  def test_square_root_of_negative_number(self):
    try:
      self.calc.square_root(-4)
    except ValueError as e:
      assert str(e) == "Square root of a negative number is not allowed."
  
  def test_memory_operations(self):
    self.calc.add(10, 5)
    self.calc.store_to_memory()
    self.calc.subtract(8, 3)
    self.calc.recall_from_memory()
    assert self.calc.result == 15
  
  def test_trigonometric_functions(self):
    self.calc.sin(30)
    assert self.calc.result == 0.5
    self.calc.cos(60)
    assert self.calc.result == 0.5
    self.calc.tan(45)
    assert self.calc.result == 1
  
  def test_calculate_expression(self):
    result = self.calc.calculate_expression("(5 + 3) * 2 - 4 / 2")
    assert result == 14
  
  def test_memory_clear(self):
    self.calc.add(10, 5)
    self.calc.store_to_memory()
    self.calc.clear_memory()
    self.calc.recall_from_memory()
    assert self.calc.result == 0
  
  def test_factorial(self):
    self.calc.factorial(5)
    assert self.calc.result == 120
  
  def test_ln(self):
    self.calc.ln(2.71828)
    assert round(self.calc.result, 5) == 1
  
  def test_log(self):
    self.calc.log(100, 10)
    assert round(self.calc.result, 5) == 2
  
  def test_pi(self):
    self.calc.pi()
    assert round(self.calc.result, 5) == 3.14159
  
  def test_e(self):
    self.calc.e()
    assert round(self.calc.result, 5) == 2.71828

# Create your tests here.
