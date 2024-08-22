import random

target = random.randint(1, 100)

while True:
    userChoice = input("Enter the Number or press (Q) to Quit: ")
    if (userChoice == "Q" or userChoice == "q"):
        print("You Quited Successfully..")
        break
    
    userChoice = int(userChoice)
    if (userChoice == target):
        print("Success : You have chosen a correct number.")
        break
    elif (userChoice > target):
        print("Your choice greater than the target... Take smaller number.")
    else:
        print("Your choice smaller than the target... Take greater number.")
    
print("----GAME OVER----")
    