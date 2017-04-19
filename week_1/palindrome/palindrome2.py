def palindrome(s):
    """
    (str) -> bool
    Return True if and only if s is a palindrome.
    """
    if len(s)%2==0:
        left = s[:len(s)//2]
        right = s[len(s)//2:]
    else:
        left = s[:len(s)//2]
        right = s[(len(s)//2)+1:]
    if left == reverse(right):
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

# O(n/2)
