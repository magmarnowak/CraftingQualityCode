def insert(L, i):
    """(list, int) -> NoneType

    Precondition: L[:i] is sorted from smallest to largest.

    Move L[i] to where it belongs in L [:i +1].
    >>> L = [7, 3, 5, 2]
    >>> insert(L, 1)
    >>> L
    [3, 7, 5, 2]
    """

    value = L[i]

    j = i
    while j != 0 and L[j-1] > value:
        L[j] = L[j-1]
        j -= 1

    L[j] = value


def insertion_sort(L):
    """ (list) -> list
    Precondition: all items in the list must be of the same type.
    Takes an unsorted list and returns it as a new list in ascending order.
    >>> insertion_sort([4, 2, 8, -1, 2])
    [-1, 2, 2, 4, 8]
    >>> insertion_sort([])
    []
    >>> insertion_sort([1])
    [1]
    """

    for i in range(len(L)):
        insert(L, i)
    return L


if __name__ == '__main__':
    import doctest
    doctest.testmod()
