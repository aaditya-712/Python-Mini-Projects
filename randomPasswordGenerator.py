import random
import string

pass_len = int(input("Enter the length of password:"))
charChoice = string.ascii_letters + string.digits + string.punctuation
print(charChoice)

password = ""
for i in range(pass_len):
    password += (random.choice(charChoice))

print("your random password is: ",password)