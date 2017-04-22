def count_lowercase_vowels(s):
    """ (str) -> int

    Return the number of lowercase vowels (a, e, i, o and u) in a string

    >>> count_lowercase_vowels('Happy Anniversary!')
    4
    >>> count_lowercase_vowels('xyz')
    0
    """

    num_vowels = 0

    for char in s:
        if char in 'aeiou':
            num_vowels += 1

    return num_vowels  
