def binary_search(arr, arr_len, target):
    """
    In Python, this implementation has constant space complexity 
    The input list **needs** to be sorted

    Time complexity: O(log n)
    """
    first = 0 
    last = arr_len

    while first <= last: 
        
        midpoint = (first + last) // 2 

        if arr[midpoint] == target: 
            return midpoint
        elif arr[midpoint] < target: 
            first = midpoint + 1    
        else: 
            last = midpoint - 1
