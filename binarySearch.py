inputList = [5, 6, 8, 9, 15]


def bsearch(input_list, number_to_search, start_index=0, end_index=len(inputList) - 1):
    midpoint: int = (start_index + end_index) // 2
    # terminal condition 1: have we reached the end of the list?
    if start_index == len(input_list) - 1:
        return -1
    # terminal condition2: have we found the item at midpoint?
    if number_to_search_for == input_list[midpoint]:
        return midpoint
    elif number_to_search_for < input_list[midpoint]:
        return bsearch(input_list, number_to_search, 0, midpoint - 1)
    else:
        return bsearch(input_list, number_to_search, midpoint + 1, end_index)


number_to_search_for = int(input("What number are you looking for? "))

index = bsearch(inputList, number_to_search_for)
if index == -1:
    print("Number ", number_to_search_for, " not found ")
else:
    print("Number ", number_to_search_for, " found at ", index)
