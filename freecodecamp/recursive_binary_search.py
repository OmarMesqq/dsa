def recursive_binary_search(arr, arr_len, target):
    """ 
    This Python implementation has logarithmic **space** complexity. 
    Therefore, an iterative version may be a better fit.
    """ 
    if arr_len == 0:    # 1st base/stopping case
        return False 
    else:
        midpoint = arr_len // 2 
        
        if arr[midpoint] == target: # 2nd base/stopping case
            return True
        else:
            if arr[midpoint] < target: 
                return recursive_binary_search(arr[midpoint+1:], target)

