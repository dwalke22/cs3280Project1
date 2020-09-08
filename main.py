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
import sys

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
    """Seperates different number length values"""
    return values.split(",")

def seperate_prefixes(values):
    """Seperates different credit card numbers"""
    return values.split(",")

def seperate_issuers(lines):
    """Seperates each issuer into the different properties"""
    issuers = []
    for line in lines:
        line = line.strip('\n')
        values = line.split(";")
        issuer = {'network': values[0], 'length': values[1],\
                'prefix': values[2]}
        issuers.append(issuer)
    return issuers


def load_card_types():
    """Loads a ssv file and returns the seperated lines in a list of dictionaries"""
    types = open(sys.argv[1])
    lines = types.readlines()
    issuers = seperate_issuers(lines)
    types.close()
    return issuers

def length_matches(lengths, number):
    """Determines if credit card lenth matches a length"""
    lengths_list = seperate_lengths(lengths)
    matches = False
    for i in range(len(lengths_list)):
        if len(number) == int(lengths_list[i]):
            matches = True
        i += 1
    return matches

def prefix_matches(prefixes, number):
    """Determines if credit card prefix matches a prefix"""
    prefix_list = seperate_prefixes(prefixes)
    matches = False
    for i in range(len(prefix_list)):
        if prefix_list[i] in number:
            matches = True
        i += 1
    return matches

def determine_card_type(credit_card_number, issuers):
    """Determines a card type for a given card number"""
    card_type = "Invalid"
    length = False
    prefix = False
    for issuer in issuers:
        length = length_matches(issuer['length'], credit_card_number)
        prefix = prefix_matches(issuer['prefix'], credit_card_number)
        if length and prefix:
            card_type = issuer
    return card_type['network']

def main():
    """Main entry point of program."""
    print("Please enter a credit card number:")
    credit_card_number = input()
    print('Credit Card Number:\t' + verify_credit_number(credit_card_number))
    issuers = load_card_types()
    card_type = determine_card_type(credit_card_number, issuers)
    print('Credit Card Type:\t' + card_type)

if __name__ == "__main__":
    main()
