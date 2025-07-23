import random

randomNum = random.randint(1,100)

attempts = 0
difflevel = input("Enter the mode of difficulty (Easy, Medium, Hard) =")

if(difflevel == "Easy" or difflevel == "e" or difflevel == "E" or difflevel == "easy"):
    attempts =10
    
if(difflevel == "Medium" or difflevel == "m" or difflevel == "M" or difflevel == "medium"):
    attempts =5
    
if(difflevel == "Hard" or difflevel == "h" or difflevel == "H" or difflevel == "hard"):
    attempts =3

else:
    print("Invalid input")

while(True):
    userInput = int(input(f"Guess a random number between 1 and {100}="))
    
    
    if(not userInput.isdigit):
        if
        
    if(userInput == randomNum):
        print(f"You Win ")
        break
    
    elif(userInput<randomNum):
        print(f"Guess a higher number.")
        
    else:
        print(f"Guess a lower number.")