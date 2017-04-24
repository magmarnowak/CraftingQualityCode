def linear_search(L, v):
    """ (list, value) -> int
    Takes a list and a value to be searched for in that list, returns the index
    of the first occurence of the value or -1 if the value is not found.
    >>> linear_search([2, 3, 5, 3], 2)
    0
    >>> linear_search([2, 3, 5, 8], 8)
    3
    >>> linear_search([2, 3, 5, 8], 6)
    -1
    >>> linear_search([2, 3, 5, 3], 3)
    1
    """
    i = 0
    while i != len(L) and v!=[i]:
        if L[i] == v:
            return i
        else:
            i+= 1
    return -1
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
