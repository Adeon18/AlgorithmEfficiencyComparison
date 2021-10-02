"""
This module is responsible for analising results and turning the data into it's
final form before visualization.
"""
import json


def read_json(path):
    """
    Read the json file from the path and turn it into dict.
    Return the data
    """

    with open(path, "r") as f:
        data = json.load(f)

    return data

def to_json_file(data):
    """
    Write the data to a json file
    """
    with open('final_results.json', 'w') as data_file:
        json.dump(data, data_file, indent=4)


def count_average_time_and_comp(old_data, new_data):
    """
    Count the average time and comparisons of the random generated lists
    for all the algos and rewrite the data.
    """

    algos = ["selection_sort", "insertion_sort", "shell_sort", "merge_sort"]

    for a in algos:
        # For each of 2^7 ... 2^15
        for i in range(9):
            av_time = 0
            av_comp = 0
            # For each of 5 experiments
            for j in range(5):
                av_time += old_data[a]["random_{}".format(j+1)][i][0]
                av_comp += old_data[a]["random_{}".format(j+1)][i][1]
            av_time = av_time / 5
            av_comp = av_comp / 5
            # Write new data entry
            new_data[a]["random_average"].append((av_time, av_comp))
    
    to_json_file(new_data)
    
    return new_data


def trim_rest(old_data, new_data):
    """
    Trim the rest of the data(sorted, unsorted and the 3rd one)
    """

    algos = ["selection_sort", "insertion_sort", "shell_sort", "merge_sort"]

    for a in algos:

        for i in range(9):
            # Sorted and unsorted
            new_data[a]["sorted"].append(old_data[a]["sorted"][i])
            new_data[a]["sorted_inverse"].append(old_data[a]["sorted_inverse"][i])
    
            # 3 Experiments of {1, 2, 3}
            av_time = 0
            av_comp = 0
            # For each of 5 experiments
            for j in range(3):
                av_time += old_data[a]["with_repetitions_{}".format(j+1)][i][0]
                av_comp += old_data[a]["with_repetitions_{}".format(j+1)][i][1]
            av_time = av_time / 3
            av_comp = av_comp / 3
            # Write new data entry
            new_data[a]["with_repetitions"].append((av_time, av_comp))
    
    to_json_file(new_data)


def trim_data():
    """
    Read and trim all the experiment data
    """
    print("Started Trimming..")
    new_data = {
        "selection_sort": {
            "random_average": [],
            "sorted": [],
            "sorted_inverse": [],
            "with_repetitions": []

        },
        "insertion_sort": {
            "random_average": [],
            "sorted": [],
            "sorted_inverse": [],
            "with_repetitions": []
        },
        "merge_sort": {
            "random_average": [],
            "sorted": [],
            "sorted_inverse": [],
            "with_repetitions": []
        },
        "shell_sort": {
            "random_average": [],
            "sorted": [],
            "sorted_inverse": [],
            "with_repetitions": []
        },
    }

    old_data = read_json("raw_test_results.json")

    count_average_time_and_comp(old_data, new_data)
    trim_rest(old_data, new_data)

    print("Trimming Done.")


trim_data()


