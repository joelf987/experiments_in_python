import random

'''
Shuffles the input string, leaving the first character in place.
'''
def shuffle(answer):
    l = list(answer[1:])
    random.shuffle(l)
    return answer[:1] + "".join(l)

def yes_or_no(question):
    reply = list(str(input(question+' (y/n): ')).lower().strip()).pop(0)
    if reply == 'y':
        return True
    if reply == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")


def main():
    length = int(input("How long do you want the password? "))
    reply = yes_or_no("Do you want to include numbers?")
    print("Including numbers: ", reply)
    include_numbers = reply
    reply = yes_or_no("Do you want to include special characters?")
    print("Including special characters: ", reply)
    include_special_characters = reply
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    specials = "@'#~[]{}-_,./<>?!£$%^*:;"

    if include_numbers & include_special_characters:
        component_length = length // 3
        remainder = length % 3
        character_length = component_length * 3
        letter_length = component_length
        if character_length < length:
            letter_length = letter_length + remainder
        result = ''.join(random.choice(letters) for i in range(letter_length)) +\
                    ''.join(random.choice(numbers) for i in range(component_length)) +\
                    ''.join(random.choice(specials) for i in range(component_length))
        print(len(result))
        print(shuffle(result))
    elif include_numbers:
        component_length = length // 2
        character_length = component_length * 2
        letter_length = component_length
        if character_length < length:
            letter_length = letter_length + 1
        result = ''.join(random.choice(letters) for i in range(letter_length)) + ''.join(
            random.choice(numbers) for i in range(component_length))
        print(len(result))
        print(shuffle(result))
    elif include_special_characters:
        component_length = length // 2
        character_length = component_length * 2
        letter_length = component_length
        if character_length < length:
            letter_length = letter_length + 1
        result = ''.join(random.choice(letters) for i in range(letter_length)) + ''.join(
            random.choice(specials) for i in range(component_length))
        print(len(result))
        print(shuffle(result))
    else:
        print(''.join(random.choice(letters) for i in range(length)))


if __name__ == "__main__":
    main()