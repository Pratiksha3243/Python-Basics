import string
import random

n = int(input("Enter the length of password you want to generate : "))
if(n==0):
    raise ValueError("Password cannot be 0")

allCharacters = string.ascii_letters + string.digits

randomPass = ""

for i in range(n):
    randomPass += random.choice(allCharacters)
    
print(randomPass)


