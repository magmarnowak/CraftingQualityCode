def binary_search(L, v):
    """ (list, value) -> int

    Precondition: L is sorted in increasing order, and all items in L can be
    compared to v.

    Takes a list and a value to be searched for in that list, returns the index
    of the first occurence of the value or -1 if the value is not found.

    >>> binary_search([2, 3, 5, 7], 2)
    0
    >>> binary_search([2, 3, 5, 5], 5)
    2
    >>> binary_search([2, 3, 5, 8], 6)
    -1
    >>> binary_search([], 2)
    -1
    """
    # if len(L) > 0:
    #     mid_index = len(L)//2
    #     if v != L[mid_index]:
    #         if v < L[mid_index]:
    #             return(binary_search(L[:mid_index], v))
    #         else:
    #             return(binary_search(L[mid_index:], v))
    #     return mid_index
    # return -1

    b = 0
    e = len(L) - 1

    while b <= e:
        m = (b+e) // 2
        if L[m] < v:
            b = m + 1
        else:
            e = m - 1
    if b == len(L) or L[b] != v:
        return -1
    return b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
