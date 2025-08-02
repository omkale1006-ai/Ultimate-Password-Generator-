# Welcome to the Secure Password Generator Project! 🔐

import random
import string

# Function to generate a strong password
def generate_password(length):
    # Combine all lowercase, uppercase, digits, and punctuation characters
    all_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    # Password must be at least 4 characters long
    if length < 4:
        return "Password length should be at least 4 characters."

    # Ensure the password includes at least one letter, one uppercase, one digit, and one symbol
    password = [
        random.choice(string.ascii_letters),     # Random letter (a-z or A-Z)
        random.choice(string.ascii_uppercase),   # Random uppercase letter (A-Z)
        random.choice(string.digits),            # Random digit (0-9)
        random.choice(string.punctuation),       # Random symbol (!, @, #, etc.)
    ]

    # Add remaining characters randomly
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to make it more secure and unpredictable
    random.shuffle(password)

    # Join list into a string and return the final password
    return "".join(password)

# 🌟 Program starts here
print("🔐 Welcome to the Secure Password Generator!\n")

try:
    user_length = int(input("Enter desired password length (minimum 4): "))
    final_password = generate_password(user_length)
    print("\n✅ Your generated password is:", final_password)
except ValueError:
    print("❌ Please enter a valid number.")
