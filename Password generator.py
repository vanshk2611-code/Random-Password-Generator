import random
import string

list = (string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@&*?_-^$+" )
password = ("")
 
i = int(input("How long password do you want?:"))

print("\n")

for i in range(i):
    random_character = random.choice(list)
    password = password + random_character
print(password, "\n")