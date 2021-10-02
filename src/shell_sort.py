"""
Here lies the shell sort algorithm.
"""


def shell_sort(arr):
    """
    Here lies the shell sort algorithm
    """
    
    arr_len = len(arr)
    gap = 1
    # Get the gap number
    while gap < arr_len/3:
        gap = 3*gap + 1
    
    while gap >= 1:
        for i in range(gap, arr_len):
            j = i
            while (j >= gap) and (arr[j] < arr[j-gap]):
                arr[j], arr[j-gap] = arr[j-gap], arr[j]
                j -= gap
        gap = gap // 3




if __name__ == "__main__":
    test = [3, 0, 7, 10, 5, 4, 6, 7, 2, 1]

    shell_sort(test)

    print(test)
    