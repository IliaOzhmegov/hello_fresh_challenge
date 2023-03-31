import unittest
from src.spell import generate_pattern


class TestGeneratePattern(unittest.TestCase):

    def test_pattern_for_chilie(self):
        expected = r'\s?chil[ei|ie|i|e]\s?'
        result = generate_pattern('chilie')
        self.assertEqual(result, expected)

    def test_pattern_for_chicken(self):
        expected = r'\s?chi[ck|c|k]en\s?'
        result = generate_pattern('chicken')
        self.assertEqual(result, expected)
