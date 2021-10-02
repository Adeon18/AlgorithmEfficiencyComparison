"""
This is a huge module that tests the algorithms of selection sort, insertion sort,
merge sort and shell sort.
"""
import time
import random
import json

from copy import deepcopy

# from src import *
from merge_sort import merge_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from shell_sort import shell_sort


def test_random_array():
    """
    Test the algos for arrays of size 2^7 - 2^15.
    Testing 5 times and getting the averge time.
    """

    data = {
        "selection_sort": {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
        },
        "insertion_sort": {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
        },
        "merge_sort": {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
        },
        "shell_sort": {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
        },
    }

    for j in range(5):
        for arr_len in [2**7, 2**8, 2**9, 2**10, 2**11, 2**12, 2**13, 2**14, 2**15]:
            # print("Started with new length")
            # Initialize the array
            test_array = [random.randint(0, 1000) for _ in range(arr_len)]
            # Make 4 copies of it
            copy1 = deepcopy(test_array)
            copy2 = deepcopy(test_array)
            copy3 = deepcopy(test_array)
            copy4 = deepcopy(test_array)
            # Print iteration data
            print("Test:", j, "Array length:", arr_len, flush=True)

            #
            # Start the timer for selection sort
            print("Started Selection Sort...")
            start = time.time()

            selection_sort(deepcopy(copy1))

            end = time.time() - start
            data["selection_sort"][j+1].append(end)
            to_json_file(data)

            #
            # Start the timer for Insertion sort
            print("Started Insertion Sort...")
            start = time.time()

            insertion_sort(deepcopy(copy2))

            end = time.time() - start
            data["insertion_sort"][j+1].append(end)
            to_json_file(data)

            #
            # Start the timer for Shell sort
            print("Started Shell Sort...")
            start = time.time()

            shell_sort(deepcopy(copy3))

            end = time.time() - start
            data["shell_sort"][j+1].append(end)
            to_json_file(data)

            #
            # Start the timer for Merge sort
            print("Started Merge Sort...")
            start = time.time()

            merge_sort(deepcopy(copy4))

            end = time.time() - start
            data["merge_sort"][j+1].append(end)
            to_json_file(data)



def to_json_file(data):
    with open('results1.json', 'w') as data_file:
        json.dump(data, data_file)



test_random_array()




