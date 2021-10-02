"""
Here lies the shell sort algorithm.
"""


def shell_sort(arr):
    """
    Here lies the shell sort algorithm
    """
    comp = 0
    arr_len = len(arr)
    gap = 1
    # Get the gap number
    while gap < arr_len/3:
        gap = 3*gap + 1
    
    while gap >= 1:
        for i in range(gap, arr_len):
            j = i
            while (j >= gap):
                if (arr[j] < arr[j-gap]):
                    arr[j], arr[j-gap] = arr[j-gap], arr[j]
                    j -= gap
                    comp += 1
                else:
                    comp += 1
                    break
        gap = gap // 3

    return comp



if __name__ == "__main__":
    test = [7, 4, 5, 3, 1, 2, 80, 4, 3, 1, 0]

    print(shell_sort(test))

    print(test)
    