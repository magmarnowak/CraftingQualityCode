def get_index_of_smallest(L, i):
    """(list, int) -> int
    Teturn the index of the smallest intem in L[i:].
    >>> get_index_of_smallest([4, 2, 8, -1], 0)
    3
    """
    index_of_smallest = i
    for j in range(i+1, len(L)):
        if L[j] < L[index_of_smallest]:
            index_of_smallest = j
    return index_of_smallest

def selection_sort(L):
    """ (list) -> list
    Precondition: all items in the list must be of the same type.
    Takes an unsorted list and returns it as a new list in ascending order.
    >>> selection_sort([4, 2, 8, -1])
    [-1, 2, 4, 8]
    >>> selection_sort([])
    []
    >>> selection_sort([1])
    [1]
    """
    for i in range(len(L)):
        index_of_smallest = get_index_of_smallest(L, i)
        L[index_of_smallest], L[i] = L[i], L[index_of_smallest]
    return L

if __name__ == '__main__':
    import doctest
    doctest.testmod()
