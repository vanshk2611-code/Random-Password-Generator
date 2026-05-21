import random
import string

# 1. Setup the ingredients
all_characters = ""
password = ""

# 2. Get the Boss's order
try:
    length = int(input("How long should the password be?: "))
except ValueError:
    print("❌ Error: Please enter a number (like 12), not words!")
    exit() # Stops the program if they type "abc" for length

use_symbols = input("Include symbols (!@#$)? (y/n): ").lower()
use_numbers = input("Include numbers (123)? (y/n): ").lower()
use_letters = input("Include letters (abc)? (y/n): ").lower()

# 3. Fill the bucket based on the 'y' answers
if use_letters == "y":
    all_characters += string.ascii_letters
if use_numbers == "y":
    all_characters += string.digits
if use_symbols == "y":
    all_characters += "!@&*?_-^$+"

# 4. The MVP Logic: Check if we can actually build it
if all_characters == "":
    print("❌ Error: You didn't pick any ingredients! Run it again.")
elif length <= 0:
    print("❌ Error: The password needs to be at least 1 character long.")
else:
    # The Loop: Pick a random piece 'length' times
    for _ in range(length):
        password += random.choice(all_characters)
    
    print("\n----------------------------")
    print(f"YOUR SECURE PASSWORD: {password}")
    print("----------------------------")
