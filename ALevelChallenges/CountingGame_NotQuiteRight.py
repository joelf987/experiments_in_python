player = "Player 1"
highestNum = 0

while highestNum < 15:
    selection = int(input(player + ": How many numbers? Pick 1,2 or 3:\n"))
    if selection < 1 or selection > 3:
        print("You can choose a number between 1 and 3")
    else:
        for i in range(0, selection):
            highestNum = highestNum + 1
            if highestNum == 15:
                print(f"{player}'s number[{i + 1}]: {highestNum}")
                break # player has reached 15!!!!

            print(f"{player}'s number[{i + 1}]: {highestNum}")

        if player == "Player 1":
            player = "Player 2"
        else:
            player = "Player 1"

if highestNum == 15:
    print(player, ": is the winner")
