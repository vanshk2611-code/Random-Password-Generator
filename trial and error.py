import random
import string

list = (string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@&*?_-^$+" )
password = ("")
 
i = int(input("How long password do you want?:"))

symbols = input("Do you want to include symbols(y/n):")
numbers = input("Do you want to include numbers(y/n):")
letters = input("Do you want to include letters(y/n):")

print("\n")
if (i <100 and i>4 ):
    if(symbols == ("y") and numbers == ("y") and letters == ("y")):
        password = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice("!@&*?_-^$+")
        for i in range(i-4):
            random_character = random.choice(list)
            password = password + random_character 
elif(i<=4):
    print("Password length too small. Please try a bigger number.")
else:
    print("Password length too large. Please try a smaller number.")

print(password, "\n")