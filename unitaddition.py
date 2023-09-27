import unittest
from Adder import sumNumbers

class addtest(unittest.TestCase):
  def test_100(self):
    coming_value = sumNumbers(100)
    assert coming_value == 5050
  def test_10(self):
    coming_value = sumNumbers(10)
    assert coming_value == 55
  def test_15(self):
    coming_value = sumNumbers(15)
    assert coming_value == 121
  