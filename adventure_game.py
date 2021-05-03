# adventures in pycharm

import random
import time

# Define variables

hp = 30

print ("you are standing on a path at the edge of the jungle. There is a cave to your left and a beach to your right ")
time.sleep(1)

#loop until we get a recognised responsed
while True:
    direction1 = input("do you want to go left or right? ")
    direction1 = direction1.lower() # needed to accept LEFT or RiGhT etc.
    if direction1 == "left":
        print("you walk into the cave and notice there is an opening.")
        print("A small snake bites you, and you lose 20 health points")
        hp = hp - 20
        break # leave the loop
    elif direction1 == "right":
        print("you walk to the beach but remember you haven't got any swimwear.")
        print("the cool water revitalises you. You have never felt more alive, gain 70 health points")
        hp += 70
        break # leave the loop
else:
    print("you think for a while")
    time.sleep(1)

# Check health points after player has made a move
print(" you now have", hp, "health points")
if hp <= 0:
    print("you are dead I'm sorry.")

print("You're adventure has ended, thank you for playing. Goodbye")

