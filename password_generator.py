import string
import random

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password
length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))

