import datetime
import random

step = 0

def unorderedlist(size):
    returnList = []
    for i in range(0, size):
       returnList.append(random.randint(0, 100))
    return returnList

#The main qsort call passes the list to sort and defaults
#the low and high to the start and end of the list.
def qsort(list_to_sort, lo=0, hi=None):
    '''Defaults the high to the end of the list if none passed (initial state)'''
    if hi == None:
        hi = len(list_to_sort) - 1

    '''Check bounds to make sure they're valid'''
    if lo < 0 or lo >= hi:
        return

    '''Get the pivot index'''
    pivot = partition(list_to_sort, lo, hi)
    '''sort the left side of the pivot'''
    qsort(list_to_sort, lo, pivot - 1)
    '''...and the right side of the pivot'''
    qsort(list_to_sort, pivot+1, hi)
    '''finally return the sorted list - since we're sorting in-place, we simply return the same list'''
    return list_to_sort

#This method partitions and returns the pivot index.
# It sorts items as it moves through the lo/hi, around the pivot
# to the correct position for the item
def partition(list_to_sort, lo, hi):
    pivot = list_to_sort[hi]

    i = lo
    for j in range (lo, hi):
        if (list_to_sort[j] < pivot):
            swap(list_to_sort, i, j)
            i += 1

    swap(list_to_sort, i, hi)
    return i

#swaps the specified indices in the list
def swap(list_to_sort, i, j):
    if i == j:
        return
    temp = list_to_sort[i]
    list_to_sort[i] = list_to_sort[j]
    list_to_sort[j] = temp


print("start: ", datetime.datetime.now())
unordered = unorderedlist(10000)
print ("unordered", unordered)
ordered = qsort(unordered)
print("end: ", datetime.datetime.now())
print ("sorted", ordered)