def palindrome(s):
    """
    (str) -> bool
    Return True if and only if s is a palindrome.
    """
    if s == reverse(s):
        return True
    return False

def reverse(s):
    """
    (str) -> str
    Returns a reversed version of a string
    """
    rev = ''
    for char in s:
        rev = char + rev
    return rev

print(palindrome('kayak'))
print(palindrome('racecar'))
print(palindrome('redcar'))

# O(n)
