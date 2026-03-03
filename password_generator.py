import random
import string

length = int(input("Enter password length: "))

use_upper = input("Include Uppercase? (y/n): ").lower() == 'y'
use_lower = input("Include Lowercase? (y/n): ").lower() == 'y'
use_digits = input("Include Digits? (y/n): ").lower() == 'y'
use_symbols = input("Include Symbols? (y/n): ").lower() == 'y'

characters = ""

if use_upper:
    characters += string.ascii_uppercase
if use_lower:
    characters += string.ascii_lowercase
if use_digits:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

if characters == "":
    print("You must select at least one character type!")
else:
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)
