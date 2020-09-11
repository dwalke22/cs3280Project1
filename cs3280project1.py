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
import utils

__author__ = "David Walker"
__verison__ = "Fall 2020"

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
    for i in lengths_list:
        if len(number) == int(i):
            matches = True
    return matches

def prefix_matches(prefixes, number):
    """Determines if credit card prefix matches a prefix"""
    prefix_list = seperate_prefixes(prefixes)
    matches = False
    for i in prefix_list:
        regex = re.compile(i)
        if regex.match(number):
            matches = True
    return matches

def determine_card_type(credit_card_number, issuers):
    """Determines a card type for a given card number"""
    card_type = ""
    length = False
    prefix = False
    for issuer in issuers:
        length = length_matches(issuer['length'], credit_card_number)
        prefix = prefix_matches(issuer['prefix'], credit_card_number)
        if length and prefix:
            card_type = issuer['network']
    return card_type

def main():
    """Main entry point of program."""
    print("Please enter a credit card number:")
    credit_card_number = input()
    if utils.is_valid(credit_card_number):
        print('Credit Card Number:\t' + credit_card_number)
        issuers = load_card_types()
        card_type = determine_card_type(credit_card_number, issuers)
        print('Credit Card Type:\t' + card_type)
        if "-" in credit_card_number:
            credit_card_number = credit_card_number.replace("-", "")
        elif " " in credit_card_number:
            credit_card_number = credit_card_number.replace(" ", "")
        print('Luhn Verification:\t' + utils.luhn_verified(credit_card_number))
    else:
        print('Credit Card Number:\tInvalid')
        print('Credit Card Type:\tInvalid')
        print('Luhn verification:\tN/A')

if __name__ == "__main__":
    main()
