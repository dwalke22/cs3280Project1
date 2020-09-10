#!/usr/bin/env python3
"""
Unit test for utils.py
"""

import unittest
import utils

__author__ = "David Walker"
__version__ = "Fall 2020"

class TestUtils(unittest.TestCase):
    def test_non_valid_number(self):
        result = utils.is_valid("abcd")
        self.assertEqual(result, False)

    def test_valid_number_no_spec_chars(self):
        result = utils.is_valid("1234123412341234")
        self.assertEqual(result, True)

    def test_vaild_number_with_space(self):
        result = utils.is_valid("1234 1234 1234 1234")
        self.assertEqual(result, True)

    def test_vaild_number_with_dash(self):
        result = utils.is_valid("1234-1234-1234-1234")
        self.assertEqual(result, True)

    def test_fake_card(self):
        result = utils.luhn_verified("4573055613536303099")
        self.assertEqual(result, "Fake")

if __name__ == "__main__":
    unittest.main()
