import random
import string
import sys

# Still gotta add the add the comments on how everything works and what part of code does what I saw it in a professional code.

list = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@&*?_-^$+"
password = ""

length = int(input("How long password do you want?:"))
extra = 0


symbols = input("Do you want to include symbols(y/n):")
numbers = input("Do you want to include numbers(y/n):")
letters = input("Do you want to include letters(y/n):")
allowed = ""
x = ""
y = ""
z = ""

if letters == "y" or letters == "Y":
    x = x + (random.choice(string.ascii_letters))
    allowed = allowed + string.ascii_letters
    extra += 1
if numbers == "y" or numbers == "Y":
    y = y +  (random.choice(string.digits))
    allowed = allowed + string.digits
    extra += 1
if symbols == "y" or symbols == "Y":
    z = z + (random.choice("!@&*?_-^$+"))
    allowed = allowed + "!@&*?_-^$+"
    extra += 1
elif allowed == "":
    print("You need to select at least one option.")
    sys.exit()

if length - extra < 0:
    print("Password length too small. Try a bigger number.")
    sys.exit()
if length  > 99:
    print("Password length too big. Try a smaller number")
    sys.exit()
    
password = x+y+z
for i in range(length - extra):
    random_characters = random.choice(allowed)
    password = password + random_characters
print("Password Is:", password)



'''
The stuff below is just to test the cases and debug that is the password being generated correctly or not 
and is it the correct length or not. This might not be the best way to do it but as a beginner it works for me and I am still learning.
'''
# print(len(password))
# print("x:", x)
# print("y:", y)
# print("z:", z)