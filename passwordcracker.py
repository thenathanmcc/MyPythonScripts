#!/bin/env python3
#Written by Nathan McCulloch
import bcrypt
import hashlib
import sys
from enum import Enum

class HashingFunction(Enum):
	SHA256 = 1
	SHA512 = 2
	MD5 = 3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
			'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
			'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '&', '*', '(', ')', '.', '_', '-']

reduced_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
					'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
					'0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def setHashingFunction(string):
	if (string == "md5"):
		return HashingFunction.MD5
	elif (string == "sha256"):
		return HashingFunction.SHA256
	elif (string == "sha512"):
		return HashingFunction.SHA512

def printHelp():
	print("=======================================")
	print("This tool is used for brute force password cracking of hashed passwords.")
	print("Usage: ./passwordcracker.py hashed_password target_length")
	print("Flags:\n-s salt\n-h hashingFunction(md5, sha256, sha512)\n-e starting_string\n-R (Use only alphanumeric characters)\n-O (display output)")

def matchFound(string, hashing_function):
	print()
	print("====== Match Found ======")
	if (hashing_function == HashingFunction.MD5):
		print(string, " -- ", hashlib.md5((salt + string).encode("utf-8")).hexdigest())
	elif (hashing_function == HashingFunction.SHA256):
		print(string, " -- ", hashlib.sha256((salt + string).encode("utf-8")).hexdigest())
	elif (hashing_function == HashingFunction.SHA512):
		print(string, " -- ", hashlib.sha256((salt + string).encode("utf-8")).hexdigest())
	print("Original Password: ", string)
	print("=========================")

def permutations(target_hash, string, target_length, current_length, alphabet, salt, hashing_function, display_ouput):
	if (hashing_function == HashingFunction.MD5):
		if (target_hash == hashlib.md5((salt + string).encode("utf-8")).hexdigest()):
			matchFound(string, hashing_function)
			return
	elif (hashing_function == HashingFunction.SHA256):
		if (target_hash == hashlib.sha256((salt + string).encode("utf-8")).hexdigest()):
			matchFound(string, hashing_function)
			return
	elif (hashing_function == HashingFunction.SHA512):
		if (target_hash == hashlib.sha512((salt + string).encode("utf-8")).hexdigest()):
			matchFound(string, hashing_function)
			return
	if (current_length == target_length):
		if (display_ouput):
			print("Current password: ", string, end='\r')
		return
	else:
		for letter in alphabet:
			permutations(target_hash, string + letter, target_length, current_length + 1, alphabet, salt, hashing_function, display_ouput)

## Set default configuration
hashed_password = ""
starting_string = ""
target_length = 8
salt = ""
hashing_function = HashingFunction.MD5
alphanumeric = False
display_ouput = False


try:
	hashed_password = sys.argv[1]
	target_length = int(sys.argv[2])
except ValueError:
	printHelp()
	sys.exit(0)
except IndexError:
	printHelp()
	sys.exit(0)
 
for index in range(len(sys.argv)):
	if sys.argv[index] == "-s":
		salt = sys.argv[index+1]
	if sys.argv[index] == "-h":
		hash_function = setHashingFunction(sys.argv[index+1])
	if sys.argv[index] == "-e":
		starting_string = sys.argv[index+1]
	if sys.argv[index] == "-R":
		alphanumeric = True
	if sys.argv[index] == "-O":
		display_ouput = True

if alphanumeric:
	permutations(hashed_password, starting_string , 5, len(starting_string), reduced_alphabet, salt, hashing_function, display_ouput)
else:
	permutations(hashed_password, starting_string , 5, len(starting_string), alphabet, salt, hashing_function, display_ouput)

print()
print("DONE")