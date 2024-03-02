
player = "Player 1"
highestNum = 0

while highestNum < 15:
    selection = input(player + ": Pick the next 1,2 or 3 numbers (comma-separated - eg 1,2,3):\n")
    assert selection != '', "You must enter at least one number!"
    tokens = selection.split(",")
    assert 0 < len(tokens) <= 3, f"I'm sorry Dave! I can't allow you to do that. You may only enter up to three numbers in ascending order! But you've entered: {len(tokens)}"
   # numbers = [int(numeric_string) for numeric_string in tokens]
    numbers = [len(tokens)]
    for i in range(0, len(tokens)):
        numbers[i] = int(tokens[i])

    if len(numbers) == 2:
        assert numbers[0] < numbers[1], f"Numbers must be in ascending order... {numbers}"
    elif len(numbers) == 3:
        assert numbers[0] < numbers[1] < numbers[2], f"Numbers must be in ascending order... {numbers}"

    if numbers[0] > highestNum:
        highestNum = numbers[len(numbers) - 1]
        if player == "Player 1":
            player = "Player 2"
        else:
            player = "Player 1"
    else:
        print(f"Numbers must be in order, and the first number must be greater than the highest number selected in the previous turn: {numbers[0]}")

if highestNum == 15:
    print(player, ": is the winner")

