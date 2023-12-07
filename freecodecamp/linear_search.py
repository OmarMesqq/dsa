def linear_search(arr, target, arr_len):
    """  
    Traverses a sorted/unsorted list and returns the index position
    if target is in the list. Otherwise, returns False.

    Time complexity: O(n)
    """  
    for it in range(arr_len):

        if arr[it] == target:
            return it
        else:
            continue

    return False
