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

def main():
    """Main entry point of program."""
    credit_card_regex = re.compile(r'\d{13,19}|(\d{4}-){3}\d{4}|(\d{4} ){3}\d{4}')
    print("Please enter a credit card number:")
    credit_card_number = input()
    match = credit_card_regex.search(credit_card_number)
    print(match)

if __name__ == "__main__":
    main()
