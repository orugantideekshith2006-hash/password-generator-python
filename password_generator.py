import string
import random

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password
    try:
    length = int(input("Enter password length: "))
    if length <= 0:
        print("Please enter a positive number.")
    else:
        print("Generated Password:", generate_password(length))
except ValueError:
    print("Invalid input! Please enter a number.")


