def split(arr):
    """ 
    Divide the unsorted list at midpoint into sublists 
    Returns two sublists - left and right 

    Takes overall O(log n) time
    """ 

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    return left, right 

def merge(left, right):
    """ 
    Merges two lists sorting them in the process
    Returns a new, merged list

    Runs in overall O(n) time
    """

    l = []
    i = 0   # Indexes on left
    j = 0   # Indexes on right

    # Assumes equal size lists as arguments
    while i < len(left) and j < len(right):
        if left[i] < right[j]: 
            l.append(left[i])
            i += 1 
        else:
            l.append(right[j]) 
            j += 1 
    
    # Assumes len(right) < len(left)
    # Add elements on left to the new list
    # Assumes within the list the elements are already sorted
    while i < len(left):
        l.append(left[i])
        i += 1
    # Opposite scenario 
    while j < len(right):
        l.append(right[j])
        j += 1

    return l 


def merge_sort(arr):
    """
    Sorts a list in ascending order
    Returns a new, sorted list
    
    Divide: find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists in previous step
    Combine: Merge the sorted sublists created in previous step

    This principle decreases the amount of comparisons made

    By multiplying the time complexity of sub 
    steps -  "split" and "merge" - respectively linear and 
    logarithmic time, the overall time complexity 
    the of Merge Sort algorithm is O(n log n)* 

    * See bottom of document
    """

    if len(arr) <= 1:
        return arr 
    
    # Divides argument list into two sublists 
    left_half, right_half = split(arr)

    # Calls recursively the function to divide it again
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # Merge the sublists
    return merge(left, right)

def verify_sorted(arr): 

    n = len(arr)

    # Discard naively sorted 
    # Stopping condition
    if n == 0 or n == 1: 
        return True
    
    # Compares first two indexes to see if they are sorted
    # Then, recursively compare all sublists using the same logic
    # At each call, the list decreases 
    return arr[0] < arr[1] and verify_sorted(arr[1:])


# This implementation actually takes
# O (kn log n) because Python's documentation
# says that slicing (lines 10 and 11) is not
# a O(1) operation. In fact, it is O(k) where
# k is the slice size

# TO-DO 
# Implement an algorithm that uses 
# an iterative mechanism instead of 
# a recursive one. This is less 
# resource expensive in Python

