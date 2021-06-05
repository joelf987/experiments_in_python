input_list = [4, 10, 1, 13, 9, 50, 76, 45, 23, 12]


def lsearch(number_to_search):
    for x in range(0, len(input_list)):
        if input_list[x] == number_to_search:
            return x

    return -1

number_to_search_for = int(input("What number are you looking for? "))

index = lsearch(number_to_search_for)
if index == -1:
    print("Number ", number_to_search_for, " not found ")
else:
    print("Number ", number_to_search_for, " found at ", index)

