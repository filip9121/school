def bubble_sort(K): #def creates a function
    n = len(K)  # Get the length of the set or list K
    
    # Outer loop to control the number of passes
    for i in range(n):
        swapped = False  # keeps a track if a swap happens
        
        # Inner loop for comparing adjacent elements
        for j in range(0, n - i - 1):
            if K[j] > K[j + 1]:  # If elements are in the wrong order, swap them
                K[j], K[j + 1] = K[j + 1], K[j]  # Swap the elements
                swapped = True  # Mark that a swap has occurred
        
        # If no swaps were made during the pass, the list is already sorted
        if not swapped:
            break
    
    return K  # Return the sorted list
