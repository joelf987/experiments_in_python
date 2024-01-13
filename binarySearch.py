import time
import random

unordered = [65, 34, 28, 68, 52, 21]
#[random.randint(0,5000) for i in range(1000)]
step = 0

def bubble_Sort(unordered):
    step = 0;
    for x in range(1, len(unordered)):
        for y in range(0, len(unordered) - 1):
            if unordered[y] > unordered[y + 1]:
                step += 1
                print("Pass: ", step)
                temp = unordered[y]
                unordered[y] = unordered[y + 1]
                unordered[y + 1] = temp
                print("At step ",step, " we have: ", unordered)

    return unordered


def merge(left_list, right_list):
    global step
    step += 1
    print("Pass: ", step)
    print ("Stat at step ", step, " is: ", left_list, right_list)
    resultList = []
    left_index = 0
    right_index = 0
    if len(left_list) == len(right_list) == 1:
        if left_list[left_index] < right_list[right_index] :
            resultList.append(left_list[left_index])
            resultList.append(right_list[right_index])
        else:
            resultList.append(right_list[right_index])
            resultList.append(left_list[left_index])

        return resultList

    while left_index < len(left_list) and right_index < len(right_list):
        if(left_list[left_index] < right_list[right_index]):
            resultList.append(left_list[left_index])
            left_index += 1
            continue
        else:
            resultList.append(right_list[right_index])
            right_index += 1
            continue

    if right_index < len(right_list):
        for i in range(right_index, len(right_list)):
            resultList.append(right_list[i])


    if left_index < len(left_list):
        for i in range(left_index, len(left_list)):
            resultList.append(left_list[i])
    return resultList

def merge_sort(list_to_sort):

    if len(list_to_sort) == 1:
        return list_to_sort
    else:
        midpoint: int = len(list_to_sort) // 2
        if len(list_to_sort) == 1:
            left_list  = list_to_sort[0:1]
        else:
            left_list = merge_sort(list_to_sort[:midpoint])

        right_list = merge_sort(list_to_sort[midpoint:])

        return merge(left_list, right_list)




def bsearch(ordered, number_to_search, start_index=0, end_index=len(unordered) - 1):
    midpoint: int = (start_index + end_index) // 2
    # terminal condition2: have we found the item at midpoint?
    if number_to_search_for == ordered[midpoint]:
        return midpoint
    # terminal condition 1: have we reached the end of the list?
    if start_index == len(ordered) - 1:
        return -1
    elif number_to_search_for < ordered[midpoint]:
        return bsearch(ordered, number_to_search, 0, midpoint - 1)
    else:
        return bsearch(ordered, number_to_search, midpoint + 1, end_index)


number_to_search_for = int(input("What number are you looking for? "))
time.perf_counter()
ordered = insertion_sort(unordered)
print ("Time (merge-sort):", time.perf_counter())
print ("sorted", ordered)
time.perf_counter()
# bubble_ordered = bubble_Sort(unordered)
#print ("Time (bubble-sort):", time.perf_counter())
# print ("sorted", bubble_ordered)
# index = bsearch(ordered, number_to_search_for)
# if index == -1:
#     print("Number ", number_to_search_for, " not found ")
# else:
#     print("Number ", number_to_search_for, " found ")

