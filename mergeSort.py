import datetime
import random

step = 0

def unorderedlist(size):
    returnList = []
    for i in range(0, size):
       returnList.append(random.randint(0, 100))
    return returnList


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

print("start: ", datetime.datetime.now())
unordered = unorderedlist(10000)
print ("unordered", unordered)
ordered = merge_sort(unordered)
print("end: ", datetime.datetime.now())
print ("sorted", ordered)