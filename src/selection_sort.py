"""
Here lies the selection sort algorithm
"""


def selection_sort(arr):
    """
    Find the min element and put it to front.
    """

    for i in range(len(arr)):
        min_idx = i
        # 
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == "__main__":
    test = [3, 0, 7, 10, 5, 4, 6, 7, 2, 1]

    selection_sort(test)

    print(test)
    

