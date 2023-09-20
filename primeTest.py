import unittest
from prime import is_prime

class PrimTest(unittest.TestCase):
    def test_10(self):
        coming_value = is_prime(10)
        assert coming_value == False
    def test_21(self):
        coming_value = is_prime(21) 
        assert coming_value == False
    def test_1(self):
        coming_value = is_prime(1) 
        assert coming_value == False
    def test_0(self):
        coming_value = is_prime(0) 
        assert coming_value == False
    def test_negative_value(self):
        coming_value = is_prime(-10) 
        assert coming_value == False
