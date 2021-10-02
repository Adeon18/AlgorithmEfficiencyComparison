"""
This module draws plots using the data from the final_results.json file.
"""
import json
import matplotlib.pyplot as plt


def read_json(path):
    """
    Read the json file from the path and turn it into dict.
    Return the data
    """

    with open(path, "r") as f:
        data = json.load(f)

    return data


def draw_plot():

    data = read_json("final_results.json")

    algos = ["selection_sort", "insertion_sort", "shell_sort", "merge_sort"]
    selection_sort_times = []
    selection_sort_comp = []

    insertion_sort_times = []
    insertion_sort_comp = []

    shell_sort_times = []
    shell_sort_comp = []

    merge_sort_times = []
    merge_sort_comp = []
    sizes = [2**7, 2**8, 2**9, 2**10, 2**11, 2**12, 2**13, 2**14, 2**15]

    for i in range(9):
        selection_sort_times.append(round(data["selection_sort"]["random_average"][i][0], 5))
        selection_sort_comp.append(data["selection_sort"]["random_average"][i][1])

        insertion_sort_times.append(round(data["insertion_sort"]["random_average"][i][0], 5))
        insertion_sort_comp.append(data["insertion_sort"]["random_average"][i][1])

        shell_sort_times.append(round(data["shell_sort"]["random_average"][i][0], 5))
        shell_sort_comp.append(data["shell_sort"]["random_average"][i][1])

        merge_sort_times.append(round(data["merge_sort"]["random_average"][i][0], 5))
        merge_sort_comp.append(data["merge_sort"]["random_average"][i][1])

    plt.figure("Random Array Comparisons")
    plt.title("Random Array Average Comparisons")
    plt.plot(sizes, selection_sort_times, "k", linewidth=3.5, label="Selection Sort")
    plt.plot(sizes, insertion_sort_times, "r", linewidth=3.5, label="Insertion Sort")
    plt.plot(sizes, shell_sort_times, "b", linewidth=3.5, label="Shell Sort")
    plt.plot(sizes, merge_sort_times, "g", linewidth=3.5, label="Merge Sort")
    plt.ylabel('Comparisons')
    plt.xlabel('Size')
    plt.yscale("log")
    plt.legend(prop={'size': 20}, loc="lower right")

    plt.figure("Random Array Time")
    plt.title("Random Array Average Time")
    plt.plot(sizes, selection_sort_comp, "k", linewidth=3.5, label="Selection Sort")
    plt.plot(sizes, insertion_sort_comp, "r", linewidth=3.5, label="Insertion Sort")
    plt.plot(sizes, shell_sort_comp, "b", linewidth=3.5, label="Shell Sort")
    plt.plot(sizes, merge_sort_comp, "g", linewidth=3.5, label="Merge Sort")
    plt.ylabel('Time')
    plt.xlabel('Size')
    plt.yscale("log")
    plt.legend(prop={'size': 20}, loc="lower right")

    plt.show()


    
    


draw_plot()