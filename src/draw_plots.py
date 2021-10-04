"""
This module draws plots using the data from the final_results.json file.

Basically a bunch of hardcoded plots - bad code warning!!!!
"""
import json
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 22})


def read_json(path):
    """
    Read the json file from the path and turn it into dict.
    Return the data
    """

    with open(path, "r") as f:
        data = json.load(f)

    return data


def draw_plot_for_random():
    """
    Draw the proper MatplotLib plots for the random arrays.
    Is a bit hardcoded
    """
    data = read_json("data/final_results.json")

    selection_sort_times = []
    selection_sort_comp = []

    insertion_sort_times = []
    insertion_sort_comp = []

    shell_sort_times = []
    shell_sort_comp = []

    merge_sort_times = []
    merge_sort_comp = []
    # These are the powers of 2
    sizes = [7, 8, 9, 10, 11, 12, 13, 14, 15]

    for i in range(9):
        selection_sort_times.append(round(data["selection_sort"]["random_average"][i][0], 5))
        selection_sort_comp.append(data["selection_sort"]["random_average"][i][1])

        insertion_sort_times.append(round(data["insertion_sort"]["random_average"][i][0], 5))
        insertion_sort_comp.append(data["insertion_sort"]["random_average"][i][1])

        shell_sort_times.append(round(data["shell_sort"]["random_average"][i][0], 5))
        shell_sort_comp.append(data["shell_sort"]["random_average"][i][1])

        merge_sort_times.append(round(data["merge_sort"]["random_average"][i][0], 5))
        merge_sort_comp.append(data["merge_sort"]["random_average"][i][1])

    plt.figure("Random Array Time")
    plt.title("Random Array Average Time")
    plt.plot(sizes, selection_sort_times, "k", linewidth=3.5, label="Selection Sort")
    plt.plot(sizes, insertion_sort_times, "r", linewidth=3.5, label="Insertion Sort")
    plt.plot(sizes, shell_sort_times, "b", linewidth=3.5, label="Shell Sort")
    plt.plot(sizes, merge_sort_times, "g", linewidth=3.5, label="Merge Sort")
    plt.ylabel('Time')
    plt.xlabel('Size - 2^X')
    plt.yscale("log")
    plt.legend(prop={'size': 20}, loc="lower right")

    plt.figure("Random Array Comparisons")
    plt.title("Random Array Average Comparisons")
    plt.plot(sizes, selection_sort_comp, "k", linewidth=3.5, label="Selection Sort")
    plt.plot(sizes, insertion_sort_comp, "r", linewidth=3.5, label="Insertion Sort")
    plt.plot(sizes, shell_sort_comp, "b", linewidth=3.5, label="Shell Sort")
    plt.plot(sizes, merge_sort_comp, "g", linewidth=3.5, label="Merge Sort")
    plt.ylabel('Comparisons')
    plt.xlabel('Size - 2^X')
    plt.yscale("log")
    plt.legend(prop={'size': 20}, loc="lower right")

    plt.show()


def draw_plot_for_sorted():
    """
    Draw the proper MatplotLib plots for the sorted arrays.
    Is a bit hardcoded.
    """
    data = read_json("data/final_results.json")

    selection_sort_times = []
    selection_sort_comp = []

    insertion_sort_times = []
    insertion_sort_comp = []

    shell_sort_times = []
    shell_sort_comp = []

    merge_sort_times = []
    merge_sort_comp = []
    # These are the powers of 2
    sizes = [7, 8, 9, 10, 11, 12, 13, 14, 15]
    for i in range(9):
        selection_sort_times.append(round(data["selection_sort"]["sorted"][i][0], 5))
        selection_sort_comp.append(data["selection_sort"]["sorted"][i][1])

        insertion_sort_times.append(round(data["insertion_sort"]["sorted"][i][0], 5))
        insertion_sort_comp.append(data["insertion_sort"]["sorted"][i][1])

        shell_sort_times.append(round(data["shell_sort"]["sorted"][i][0], 5))
        shell_sort_comp.append(data["shell_sort"]["sorted"][i][1])

        merge_sort_times.append(round(data["merge_sort"]["sorted"][i][0], 5))
        merge_sort_comp.append(data["merge_sort"]["sorted"][i][1])

    plt.figure("Sorted Array Time")
    plt.title("Sorted Array Time")
    plt.plot(sizes, selection_sort_times, "k", linewidth=3.5, label="Selection Sort")
    plt.plot(sizes, insertion_sort_times, "r", linewidth=3.5, label="Insertion Sort")
    plt.plot(sizes, shell_sort_times, "b", linewidth=3.5, label="Shell Sort")
    plt.plot(sizes, merge_sort_times, "g", linewidth=3.5, label="Merge Sort")
    plt.ylabel('Time')
    plt.xlabel('Size - 2^X')
    plt.yscale("log")
    plt.legend(prop={'size': 20}, loc="lower right")

    plt.figure("Sorted Array Comparisons")
    plt.title("Sorted Array Comparisons")
    plt.plot(sizes, selection_sort_comp, "k", linewidth=3.5, label="Selection Sort")
    plt.plot(sizes, insertion_sort_comp, "r", linewidth=3.5, label="Insertion Sort")
    plt.plot(sizes, shell_sort_comp, "b", linewidth=3.5, label="Shell Sort")
    plt.plot(sizes, merge_sort_comp, "g", linewidth=3.5, label="Merge Sort")
    plt.ylabel('Comparisons')
    plt.xlabel('Size - 2^X')
    plt.yscale("log")
    plt.legend(prop={'size': 20}, loc="lower right")

    plt.show()


def draw_plot_for_sorted_inverse():
    """
    Draw the proper MatplotLib plots for the inversely sorted arrays.
    Is a bit hardcoded
    """
    data = read_json("data/final_results.json")

    selection_sort_times = []
    selection_sort_comp = []

    insertion_sort_times = []
    insertion_sort_comp = []

    shell_sort_times = []
    shell_sort_comp = []

    merge_sort_times = []
    merge_sort_comp = []
    # These are the powers of 2
    sizes = [7, 8, 9, 10, 11, 12, 13, 14, 15]
    for i in range(9):
        selection_sort_times.append(round(data["selection_sort"]["sorted_inverse"][i][0], 5))
        selection_sort_comp.append(data["selection_sort"]["sorted_inverse"][i][1])

        insertion_sort_times.append(round(data["insertion_sort"]["sorted_inverse"][i][0], 5))
        insertion_sort_comp.append(data["insertion_sort"]["sorted_inverse"][i][1])

        shell_sort_times.append(round(data["shell_sort"]["sorted_inverse"][i][0], 5))
        shell_sort_comp.append(data["shell_sort"]["sorted_inverse"][i][1])

        merge_sort_times.append(round(data["merge_sort"]["sorted_inverse"][i][0], 5))
        merge_sort_comp.append(data["merge_sort"]["sorted_inverse"][i][1])

    plt.figure("Sorted Inversely Array Time")
    plt.title("Sorted Inversely Array Time")
    plt.plot(sizes, selection_sort_times, "k", linewidth=3.5, label="Selection Sort")
    plt.plot(sizes, insertion_sort_times, "r", linewidth=3.5, label="Insertion Sort")
    plt.plot(sizes, shell_sort_times, "b", linewidth=3.5, label="Shell Sort")
    plt.plot(sizes, merge_sort_times, "g", linewidth=3.5, label="Merge Sort")
    plt.ylabel('Time')
    plt.xlabel('Size - 2^X')
    plt.yscale("log")
    plt.legend(prop={'size': 20}, loc="lower right")

    plt.figure("Sorted Inversely Array Comparisons")
    plt.title("Sorted Inversely Array Comparisons")
    plt.plot(sizes, selection_sort_comp, "k", linewidth=3.5, label="Selection Sort")
    plt.plot(sizes, insertion_sort_comp, "r", linewidth=3.5, label="Insertion Sort")
    plt.plot(sizes, shell_sort_comp, "b", linewidth=3.5, label="Shell Sort")
    plt.plot(sizes, merge_sort_comp, "g", linewidth=3.5, label="Merge Sort")
    plt.ylabel('Comparisons')
    plt.xlabel('Size - 2^X')
    plt.yscale("log")
    plt.legend(prop={'size': 20}, loc="lower right")

    plt.show()


def draw_plot_for_123():
    """
    Draw the proper MatplotLib plots for the shuffled 123 arrays.
    Is a bit hardcoded.
    """
    data = read_json("data/final_results.json")

    selection_sort_times = []
    selection_sort_comp = []

    insertion_sort_times = []
    insertion_sort_comp = []

    shell_sort_times = []
    shell_sort_comp = []

    merge_sort_times = []
    merge_sort_comp = []
    # These are the powers of 2
    sizes = [7, 8, 9, 10, 11, 12, 13, 14, 15]
    for i in range(9):
        selection_sort_times.append(round(data["selection_sort"]["with_repetitions"][i][0], 5))
        selection_sort_comp.append(data["selection_sort"]["with_repetitions"][i][1])

        insertion_sort_times.append(round(data["insertion_sort"]["with_repetitions"][i][0], 5))
        insertion_sort_comp.append(data["insertion_sort"]["with_repetitions"][i][1])

        shell_sort_times.append(round(data["shell_sort"]["with_repetitions"][i][0], 5))
        shell_sort_comp.append(data["shell_sort"]["with_repetitions"][i][1])

        merge_sort_times.append(round(data["merge_sort"]["with_repetitions"][i][0], 5))
        merge_sort_comp.append(data["merge_sort"]["with_repetitions"][i][1])

    plt.figure("{1, 2, 3} Array Time")
    plt.title("{1, 2, 3} Array Time")
    plt.plot(sizes, selection_sort_times, "k", linewidth=3.5, label="Selection Sort")
    plt.plot(sizes, insertion_sort_times, "r", linewidth=3.5, label="Insertion Sort")
    plt.plot(sizes, shell_sort_times, "b", linewidth=3.5, label="Shell Sort")
    plt.plot(sizes, merge_sort_times, "g", linewidth=3.5, label="Merge Sort")
    plt.ylabel('Time')
    plt.xlabel('Size - 2^X')
    plt.yscale("log")
    plt.legend(prop={'size': 20}, loc="lower right")

    plt.figure("{1, 2, 3} Array Comparisons")
    plt.title("{1, 2, 3} Array Comparisons")
    plt.plot(sizes, selection_sort_comp, "k", linewidth=3.5, label="Selection Sort")
    plt.plot(sizes, insertion_sort_comp, "r", linewidth=3.5, label="Insertion Sort")
    plt.plot(sizes, shell_sort_comp, "b", linewidth=3.5, label="Shell Sort")
    plt.plot(sizes, merge_sort_comp, "g", linewidth=3.5, label="Merge Sort")
    plt.ylabel('Comparisons')
    plt.xlabel('Size - 2^X')
    plt.yscale("log")
    plt.legend(prop={'size': 20}, loc="lower right")

    plt.show()


def draw_plots():
    """
    Draw all the plots at once.
    """
    draw_plot_for_random()
    draw_plot_for_sorted()
    draw_plot_for_sorted_inverse()
    draw_plot_for_123()


draw_plots()