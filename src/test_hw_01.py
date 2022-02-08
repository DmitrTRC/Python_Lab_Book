from unittest import TestCase


class Test(TestCase):
    def test_is_palindrome(self):
        from hw_01 import is_palindrome
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('a'))
        self.assertTrue(is_palindrome('aa'))
        self.assertFalse(is_palindrome('ab'))
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('abba'))
        self.assertTrue(is_palindrome('abcdcba'))
        self.assertTrue(is_palindrome('abcdcba'))
        self.assertTrue(is_palindrome('abcdcba'))
        self.assertFalse(is_palindrome('abcdcbb'))
        self.assertFalse(is_palindrome('abcdcbc'))
        self.assertFalse(is_palindrome('abcdcbd'))
        self.assertFalse(is_palindrome('abcdcbe'))
        self.assertFalse(is_palindrome('abcdcbf'))
        self.assertFalse(is_palindrome('abcdcbg'))
