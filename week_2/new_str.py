class new_str(str):
    """ A string with added functionality """
    def compare(self):
        """
        (new_str) -> bool
        Checks if the first and the last letter of the string are the same.
        >>> s = new_str('hanah')
        >>> s.compare()
        True
        >>> s = new_str('mike')
        >>> s.compare()
        False
        """
        return self[0] == self[-1]

    def compare_2(self, string):
        """
        (new_str) -> bool
        Checks if the first and the last letter of the string are the same.
        >>> s = new_str()
        >>> s.compare_2('hanah')
        True
        >>> s = new_str()
        >>> s.compare_2('mike')
        False
        """
        return string[0] == string[-1]

# "mike".compare() # does not work

if __name__ == '__main__':
    import doctest
    doctest.testmod()
