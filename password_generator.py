import random
import string
def check_strength(password):
    strength = 0
    
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:',.<>?/`~" for c in password):
        strength += 1

    if strength == 4:
        return "Very Strong"
    elif strength == 3:
        return "Strong"
    elif strength == 2:
        return "Medium"
    else:
        return "Weak"
length = int(input("Enter password length: "))

if length < 4:
    print("Password length should be at least 4")
else:
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    characters = string.ascii_letters + string.digits + string.punctuation

    password += [random.choice(characters) for _ in range(length - 4)]

    random.shuffle(password)

    print("Generated Strong Password:", ''.join(password))
    print("Strength:", check_strength(''.join(password)))
save = input("Do you want to save password to file? (y/n): ")

if save.lower() == 'y':
    with open("saved_passwords.txt", "a") as file:
        file.write(''.join(password) + "\n")
    print("Password saved successfully.")
