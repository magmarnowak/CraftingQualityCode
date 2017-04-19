def palindrome(s):
    """
    (str) -> bool
    Return True if and only if s is a palindrome.
    """
    i = 0
    j = -1
    for i in range(len(s)//2):
        if s[i] != s[j]:
            return False
        j += -1
    return True

print(palindrome('kayak'))
print(palindrome('racecar'))
print(palindrome('redcar'))

#O(n)
