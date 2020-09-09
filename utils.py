#!/usr/bin/env python3
"""
Provides utility methods for verifying credit card numbers
"""
import re


def luhn_verified(credit_card_number):
    """Performs the Luhn algorithm on the credit card number to confirm it is real"""
    result = "Fake"
    if is_valid(credit_card_number):
        result = "Authentic"
    return result


def is_valid(sequence):
    """Verifies that the entered sequence is a vaild credit card number"""
    credit_card_regex = re.compile(r'\d{13,19}|(\d{4}-){3}\d{4}|(\d{4} ){3}\d{4}')
    match = credit_card_regex.match(sequence)
    valid = False
    if match:
        valid = True
    return valid
