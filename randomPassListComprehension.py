import random
import string

charChoice = string.ascii_letters + string.digits
pass_len = int(input("Enter the length of password:"))

# list comprehension [function for i in range (n)]
res = [random.choice(charChoice) for i in range(pass_len)]
print(res)
print(" ".join(res))
