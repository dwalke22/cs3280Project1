#!/usr/bin/env python3
"""
Provides utility methods for verifying credit card numbers
"""
import re


def luhn_verified(credit_card_number):
    """Performs the Luhn algorithm on the credit card number to confirm it is real"""
    result = "Fake"
    if "-" in credit_card_number:
        credit_card_number = credit_card_number.replace("-", "")
    elif " " in credit_card_number:
        credit_card_number = credit_card_number.replace(" ", "")
    sum_of_numbers = 0
    numbers = []
    for digit in credit_card_number:
        digit = int(digit)
        numbers.append(digit)
    offset = (len(numbers) + 1) % 2
    for i, number in enumerate(numbers):
        if (i + offset) % 2:
            number = number * 2
            sum_of_numbers += number -9 if number > 9 else number
        else:
            sum_of_numbers += number
    if sum_of_numbers % 10 == 0:
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
