def bubble_sort(L):
    """ (list) -> list
    Precondition: all items in the list must be of the same type.
    Takes an unsorted list and sorts it in place in ascending order.
    >>> bubble_sort([4, 2, 8, -1, 2])
    [-1, 2, 2, 4, 8]
    >>> bubble_sort([])
    []
    >>> bubble_sort([1])
    [1]
    """
    end = len(L) - 1
    while end > 0:
        for i in range(end):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
        end -= 1
    return L

if __name__ == '__main__':
    import doctest
    doctest.testmod()
