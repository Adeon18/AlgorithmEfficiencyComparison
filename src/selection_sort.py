"""
Here lies the selection sort algorithm
"""


def selection_sort(arr):
    """
    Find the min element and put it to front.
    """
    comp = 0
    for i in range(len(arr)):
        min_idx = i
        # 
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
            comp += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return comp


if __name__ == "__main__":
    test = [1, 2, 3, 4, 5]

    print(selection_sort(test))

    print(test)
    

