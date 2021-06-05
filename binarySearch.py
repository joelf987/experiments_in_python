input_list = [15, 5, 8, 6, 9]

def bubble_Sort():
    for x in range(1, len(input_list)):
        for y in range(0, len(input_list) -1):
            if input_list[y] > input_list[y+1]:
                temp = input_list[y]
                input_list[y] = input_list[y+1]
                input_list[y+1] = temp


def bsearch(number_to_search, start_index=0, end_index=len(input_list) - 1):
    midpoint: int = (start_index + end_index) // 2
    # terminal condition2: have we found the item at midpoint?
    if number_to_search_for == input_list[midpoint]:
        return midpoint
    # terminal condition 1: have we reached the end of the list?
    if start_index == len(input_list) - 1:
        return -1
    elif number_to_search_for < input_list[midpoint]:
        return bsearch(number_to_search, 0, midpoint - 1)
    else:
        return bsearch(number_to_search, midpoint + 1, end_index)


number_to_search_for = int(input("What number are you looking for? "))
bubble_Sort()
index = bsearch(number_to_search_for)
if index == -1:
    print("Number ", number_to_search_for, " not found ")
else:
    print("Number ", number_to_search_for, " found at ", index)
