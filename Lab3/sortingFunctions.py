"""
Name: 
sortingFunctions.py
Description: Implementation of sorting algorithms.
"""

import time, random

# Implementation of insertionSort algorithm
def insertionSort(list_to_sort:list) -> list:
    
    for i in range(len(list_to_sort)):          #uses the length of the list as total amount of iterations for loop

        j = i   #initialize an index for second loop

        while j > 0 and list_to_sort[j - 1] > list_to_sort[j]:      #loops until j is equal to 0 and the value of the last element of the list is greater than the value before it

            list_to_sort[j], list_to_sort[j - 1] = list_to_sort[j - 1], list_to_sort[j]     #swaps the values in corresponding index

            j -= 1      #decrements the j by 1

    return list_to_sort

# Implementation of bubbleSort algorithm
def bubbleSort(list_to_sort:list) -> list:
    
    print(list_to_sort)

    for i in range(len(list_to_sort) - 1):      #uses one less than the length of the list for index range of loop

        print (list_to_sort)

        for j in range(len(list_to_sort) - 1 - i):      #uses one less than the length of the previous loop for index range

            if list_to_sort[j] > list_to_sort[j + 1]:       #checks if the current index in the list has a greater value than the index after

                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]         #swaps the two values from the respective index positions
                

        print (list_to_sort)      

    return list_to_sort

# Returns a random list of the given length
def createRandomList(length:int) -> list:
    return random.sample(range(max(100, length)), length)
    
# Returns the length of time (in seconds) that it took
# for the function_to_run to sort a list of length list_length
def getRuntime(function_to_run, list_length) -> float:
    # Create a new list to sort
    list_to_sort = createRandomList(list_length)
    # Get the time before running
    start_time = time.time()
    # Sort the given list
    function_to_run(list_to_sort)
    # Get the time after running
    end_time = time.time()
    # Return the difference
    return end_time - start_time


if __name__ == '__main__':
    print (getRuntime(bubbleSort, 10000))