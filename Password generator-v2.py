import random
import string

list = (string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@&*?_-^$+" )
password = ("")

i = int(input("How long password do you want?:"))

symbols = input("Do you want to include symbols(y/n):")
numbers = input("Do you want to include numbers(y/n):")
letters = input("Do you want to include letters(y/n):")
allowed = ""


if(symbols == "y"):
    x = (random.choice(string.ascii_letters))
    allowed = allowed + string.ascii_letters
    i = i - 1
elif(symbols == "n"):
    x = ("")
if(numbers == "y"):
    y = (random.choice(string.digits))
    allowed = allowed + string.digits
    i = i - 1
elif(numbers == "n"):
    y = ("")
if(letters == "y"):
    z = (random.choice("!@&*?_-^$+"))
    allowed = allowed + "!@&*?_-^$+"
    i = i - 1
elif(letters == "n"):
    z = ("")

password = x+y+z
for i in range(i<100 and i>0):
    random_characters = random.choice(allowed)
    password = password + random_characters
if(i<0):
    print("Password length too small. Try a bigger number.")
if(i>=100):
    print("Password length too big. Try a bigger number")

print(password)

