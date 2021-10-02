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



def test_selection_sort(arr_copy, data, data_param):
    """
    Test selection sort and write the results to the data and to json.
    """
    print("Started Selection Sort...")
    start = time.time()

    comp = selection_sort(arr_copy)

    end = time.time() - start
    data["selection_sort"][data_param].append((end, comp))
    to_json_file(data)


def test_insertion_sort(arr_copy, data, data_param):
    """
    Test insertion sort and write the results to the data and to json.
    """
    print("Started Insertion Sort...")
    start = time.time()

    comp = insertion_sort(arr_copy)

    end = time.time() - start
    data["insertion_sort"][data_param].append((end, comp))
    to_json_file(data)


def test_shell_sort(arr_copy, data, data_param):
    """
    Test shell sort and write the results to the data and to json.
    """
    print("Started Shell Sort...")
    start = time.time()

    comp = shell_sort(arr_copy)

    end = time.time() - start
    data["shell_sort"][data_param].append((end, comp))
    to_json_file(data)


def test_merge_sort(arr_copy, data, data_param):
    """
    Test merge sort and write the results to the data and to json.
    """
    print("Started Merge Sort...")
    start = time.time()

    comp = merge_sort(arr_copy)

    end = time.time() - start
    data["merge_sort"][data_param].append((end, comp))
    to_json_file(data)


def test_random_array(data):
    """
    Test the algos for arrays of size 2^7 - 2^15.
    Testing 5 times and getting the averge time.
    """

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

            # START THE TESTING ALGOS
            ###############################
            # Test and time selection sort
            test_selection_sort(copy1, data, "random_{}".format(j+1))

            # Test and time Insertion sort
            test_insertion_sort(copy2, data, "random_{}".format(j+1))

            # Test and time Shell sort
            test_shell_sort(copy3, data, "random_{}".format(j+1))

            # Test and time Merge sort
            test_merge_sort(copy4, data, "random_{}".format(j+1))



def test_sorted_array(data):
    """
    Test the algos for a sorted array of elements
    """
    print("Testing for sorted Array")
    for arr_len in [2**7, 2**8, 2**9, 2**10, 2**11, 2**12, 2**13, 2**14, 2**15]:
        test_arr = [i for i in range(arr_len)]
        print("Array length:", arr_len, flush=True)
        # Test and time selection sort
        test_selection_sort(deepcopy(test_arr), data, "sorted")

        # Test and time Insertion sort
        test_insertion_sort(deepcopy(test_arr), data, "sorted")

        # Test and time Shell sort
        test_shell_sort(deepcopy(test_arr), data, "sorted")

        # Test and time Merge sort
        test_merge_sort(deepcopy(test_arr), data, "sorted")


def test_sorted_inverse_array(data):
    """
    Test the algos for a sorted inverse array elements
    """
    print("Testing for sorted inverse Array")
    for arr_len in [2**7, 2**8, 2**9, 2**10, 2**11, 2**12, 2**13, 2**14, 2**15]:
        test_arr = [i for i in range(arr_len, 0, -1)]
        print("Array length:", arr_len, flush=True)
        # Test and time selection sort
        test_selection_sort(deepcopy(test_arr), data, "sorted_inverse")

        # Test and time Insertion sort
        test_insertion_sort(deepcopy(test_arr), data, "sorted_inverse")

        # Test and time Shell sort
        test_shell_sort(deepcopy(test_arr), data, "sorted_inverse")

        # Test and time Merge sort
        test_merge_sort(deepcopy(test_arr), data, "sorted_inverse")


def test_array_w_repetitions(data):
    """
    Test the algos for an array of {1, 2, 3} elems.
    Run 3 experiments
    """
    for i in range(3):
        for arr_len in [2**7, 2**8, 2**9, 2**10, 2**11, 2**12, 2**13, 2**14, 2**15]:
            test_arr = [random.randint(1, 3) for _ in range(arr_len)]
            print("Test:", i, "Array length:", arr_len, flush=True)
            # Test and time selection sort
            test_selection_sort(deepcopy(test_arr), data, "with_repetitions_{}".format(i+1))

            # Test and time Insertion sort
            test_insertion_sort(deepcopy(test_arr), data, "with_repetitions_{}".format(i+1))

            # Test and time Shell sort
            test_shell_sort(deepcopy(test_arr), data, "with_repetitions_{}".format(i+1))

            # Test and time Merge sort
            test_merge_sort(deepcopy(test_arr), data, "with_repetitions_{}".format(i+1))


def to_json_file(data):
    """
    Write the data to a json file
    """
    with open('raw_test_results.json', 'w') as data_file:
        json.dump(data, data_file, indent=4)


def test_all():
    """
    Run the experiment for all the 4 sorting algos and 8 types of inputs.
    """

    data = {
        "selection_sort": {
            "random_1": [],
            "random_2": [],
            "random_3": [],
            "random_4": [],
            "random_5": [],
            "sorted": [],
            "sorted_inverse": [],
            "with_repetitions_1": [],
            "with_repetitions_2": [],
            "with_repetitions_3": []

        },
        "insertion_sort": {
            "random_1": [],
            "random_2": [],
            "random_3": [],
            "random_4": [],
            "random_5": [],
            "sorted": [],
            "sorted_inverse": [],
            "with_repetitions_1": [],
            "with_repetitions_2": [],
            "with_repetitions_3": []
        },
        "merge_sort": {
            "random_1": [],
            "random_2": [],
            "random_3": [],
            "random_4": [],
            "random_5": [],
            "sorted": [],
            "sorted_inverse": [],
            "with_repetitions_1": [],
            "with_repetitions_2": [],
            "with_repetitions_3": []
        },
        "shell_sort": {
            "random_1": [],
            "random_2": [],
            "random_3": [],
            "random_4": [],
            "random_5": [],
            "sorted": [],
            "sorted_inverse": [],
            "with_repetitions_1": [],
            "with_repetitions_2": [],
            "with_repetitions_3": []
        },
    }
    test_random_array(data)
    test_sorted_array(data)
    test_sorted_inverse_array(data)
    test_array_w_repetitions(data)


test_all()




