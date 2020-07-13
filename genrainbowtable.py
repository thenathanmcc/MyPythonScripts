#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:35:38 2020

@author: nathan
"""
import sys
from hashlib import sha256

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', 
            '$', '%', '^', '&', '*', '(', '-', ' ']

def printHelpInfo():
    print("========= Rainbow Table Generator =========\n")
    print("This tool generates a table of precomputed SHA256 hashes\nfor brute force password cracking.")
    print("Usage: ./genrainbowtable.py max_password_length")

def permutations(string, current_string_length, target_length, alphabet):
        if (current_string_length == target_length):
            string = string.replace(' ', '')
            print(string.strip(' ') + " : " + sha256(string.encode('utf-8')).hexdigest())
            return
        else:
            for i in alphabet:
                permutations(string + i, current_string_length + 1, target_length, alphabet)

try:
    target_string_length = int(sys.argv[1])
    if (target_string_length < 1):
        print("Error: max_password_length must be greater than 1")
        exit(0)
except ValueError:
    printHelpInfo()
    print("Error: Please enter an integer for the string length. ")
    exit(0)
except IndexError:
    printHelpInfo()
    exit(0)

permutations('', 0, target_string_length, alphabet)         
                