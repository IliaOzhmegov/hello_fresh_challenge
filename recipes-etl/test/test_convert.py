import unittest
import polars as pl
from src.convert import convert_to_minutes


class TestConvertToMinutes(unittest.TestCase):

    def test_both_hours_and_minutes(self):
        df = pl.DataFrame({'T': 'PT1H10M'})
        expected = {'T': 70}
        result = convert_to_minutes(df, 'T').to_dicts()[0]
        self.assertDictEqual(result, expected)

    def test_only_minutes(self):
        df = pl.DataFrame({'T': 'PT10M'})
        expected = {'T': 10}
        result = convert_to_minutes(df, 'T').to_dicts()[0]
        self.assertDictEqual(result, expected)

    def test_only_hours(self):
        df = pl.DataFrame({'T': 'PT2H'})
        expected = {'T': 120}
        result = convert_to_minutes(df, 'T').to_dicts()[0]
        self.assertDictEqual(result, expected)

    def test_empty(self):
        df = pl.DataFrame({'T': 'PT'})
        expected = {'T': None}
        result = convert_to_minutes(df, 'T').to_dicts()[0]
        self.assertDictEqual(result, expected)

    def test_empty_and_alias(self):
        df = pl.DataFrame({'T': 'PT'})
        expected = {'T': 'PT', 'T2': None}
        result = convert_to_minutes(df, 'T', 'T2').to_dicts()[0]
        self.assertDictEqual(result, expected)
