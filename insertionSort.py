import datetime
import random

step = 0

def unorderedlist(size):
    returnList = []
    for i in range(0, size):
       returnList.append(random.randint(0, 100))
    return returnList

def insertion_sort(list_to_sort):
    for i in range (0, len(list_to_sort) - 1):
            checkAndSwapIfNecessary(list_to_sort, i)
            backtrackAndInsertAtCorrectPosition(i, list_to_sort)
    return list_to_sort


def backtrackAndInsertAtCorrectPosition(i, list_to_sort):
    for j in range(i, 0, -1):
        checkAndSwapIfNecessary(list_to_sort, j - 1)


def checkAndSwapIfNecessary(unordered, i):
    if (unordered[i] > unordered[i + 1]):
        temp = unordered[i]
        unordered[i] = unordered[i + 1]
        unordered[i + 1] = temp



print("start: ", datetime.datetime.now())
unordered = unorderedlist(10000)
print ("unordered", unordered)
ordered = insertion_sort(unordered)
print ("end:", datetime.datetime.now())
print ("sorted", ordered)