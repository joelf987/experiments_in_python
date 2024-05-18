import datetime
import random

step = 0

def unorderedlist(size):
    returnList = []
    for i in range(0, size):
       returnList.append(random.randint(0, 100))
    return returnList

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


print("start: ", datetime.datetime.now())
unordered = unorderedlist(10000)
print ("unordered", unordered)
bubble_ordered = bubble_Sort(unordered)
print("end: ", datetime.datetime.now())
print ("sorted", bubble_ordered)
