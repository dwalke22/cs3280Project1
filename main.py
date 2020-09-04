#!/usr/bin/env python3
"""
Script to verify a valid credit card.

Credit Card Verification
Loads standard credit card types from a .ssv file
(semi-colon seperated values) to be used to identify
the type of credit card. The type of card will be used
and Luhn's algorithm will be used to verify that the credit
card is genuine.
"""

import re

__author__ = "David Walker"
__verison__ = "Fall 2020"

def verify_credit_number(credit_card_number):
    """Verifies that the credit card number follows is a normal number"""
    credit_card_regex = re.compile(r'\d{13,19}|(\d{4}-){3}\d{4}|(\d{4} ){3}\d{4}')
    match = credit_card_regex.match(credit_card_number)
    valid = ''
    if match:
        valid = match.group()
    else:
        valid = 'Invalid'
    return valid

def main():
    """Main entry point of program."""
    print("Please enter a credit card number:")
    credit_card_number = input()
    print('Credit Card Number:\t' + verify_credit_number(credit_card_number))

if __name__ == "__main__":
    main()
