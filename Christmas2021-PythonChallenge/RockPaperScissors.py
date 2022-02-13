import random
import sys
from enum import Enum

class Result(Enum):
    LOSE = -1
    DRAW = 0
    WIN = 1

choices = ["rock", "paper", "scissors"]


def playGame():
    usersChoice = input("Choose rock, paper or scissors ").lower()
    userChoiceIndex = choices.index(usersChoice)
    computerChoiceIndex = random.randint(0, 2)
    computersChoice = choices[computerChoiceIndex]
    print("I chose:", computersChoice)
    if usersChoice == computersChoice:
        result = Result.DRAW
    elif ((userChoiceIndex == 0 and computerChoiceIndex == 2) or \
          (userChoiceIndex == 1 and computerChoiceIndex == 0) or \
          (userChoiceIndex == 2 and computerChoiceIndex == 1)):
        result = Result.WIN
    else:
        result = Result.LOSE

    return result


def main(argv):
    result = playGame()
    if result == Result['WIN']:
        print("You win! :(")
    elif result == Result.DRAW:
        print("DRAW! Play Again?")
    else:
        print ("you lose! :)")


if __name__ == "__main__":
    main(sys.argv)
