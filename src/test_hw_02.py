from unittest import TestCase


class Test(TestCase):
    def test_is_anagram(self):
        from hw_02 import is_anagram
        self.assertTrue(is_anagram('abc', 'cba'))
        self.assertTrue(is_anagram('abc', 'cAb'))
        self.assertFalse(is_anagram('abc', 'cbaa'))
        self.assertTrue(is_anagram('Лунь', 'нуль'))
        self.assertFalse(is_anagram('Лунь', 'нульЛ'))


