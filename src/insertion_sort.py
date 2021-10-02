"""
Here lies insertion_sort.
"""

def insertion_sort(arr):
    """
    Insertion sort algoritm
    """
    # Comparisons
    comp = 0
    # Move through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move els of [0, i-1] that are greater than key 1 pos ahead
        # Move the key to the pos where it is bigger than the prev num(j+1)
        j = i - 1
        while j >= 0:
            if arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
                comp += 1
            else:
                comp += 1
                break
        arr[j+1] = key
    return comp

if __name__ == "__main__":
    # Driver code to test above
    input_arr = [8, 4, 9, 1, 3, 4, 5, 0]
    print("Input Array", input_arr)
    print(insertion_sort(input_arr))
    print("Sorted Array", input_arr)
