import random

choices = ["rock", "paper", "scissors"]
usersChoice = input("Choose rock, paper or scissors ").lower()
userChoiceIndex = choices.index(usersChoice)
computerChoiceIndex = random.randint(0,2)
computersChoice = choices[computerChoiceIndex ]
print("I chose:", computersChoice)
if usersChoice == computersChoice:
    print("DRAW! Play Again?")
elif ((userChoiceIndex == 0 and computerChoiceIndex == 2) or (userChoiceIndex == 1 and computerChoiceIndex == 0) or (userChoiceIndex == 2 and computerChoiceIndex == 1)):
    print("You win! :(")
else:
    print ("you lose! :)")

