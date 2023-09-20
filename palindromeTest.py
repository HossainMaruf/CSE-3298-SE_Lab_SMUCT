import unittest
from palindrome import is_palindrome

class PalindromeTest(unittest.TestCase):
    def test_455(self):
        coming_value = is_palindrome("455")
        assert coming_value == False
    def test_121(self):
        coming_value = is_palindrome(121) 
        assert coming_value == True
    def test_amma(self):
        coming_value = is_palindrome("amma") 
        assert coming_value == True
    def test_abba(self):
        coming_value = is_palindrome("abba") 
        assert coming_value == True
    def test_PPP(self):
        coming_value = is_palindrome("PPP") 
        assert coming_value == True
