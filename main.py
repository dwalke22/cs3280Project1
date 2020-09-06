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

def seperate_lengths(values):
    """Seperates different number length values if any"""
    if "," in values:
        values = values.split(",")
    return values

def seperate_prefix(values):
    """Seperates different credit card numbers if any"""
    if "," in values:
        values = values.split(",")
    return values

def seperate_issuers(lines):
    """Seperates each issuer into the different properties"""
    issuers = []
    for line in lines:
        values = line.split(";")
        issuer = {'network': values[0], 'length': seperate_lengths(values[1]),\
                'prefix': seperate_prefix(values[2])}
        issuers.append(issuer)
    return issuers


def load_card_types():
    """Loads a ssv file and returns the seperated lines in a list of dictionaries"""
    types = open('credit_card_types.ssv')
    lines = types.readlines()
    issuers = seperate_issuers(lines)
    types.close()
    return issuers

def main():
    """Main entry point of program."""
    print("Please enter a credit card number:")
    credit_card_number = input()
    print('Credit Card Number:\t' + verify_credit_number(credit_card_number))
    issuers = load_card_types()
    print(issuers)

if __name__ == "__main__":
    main()
