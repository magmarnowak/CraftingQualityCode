def palindrome(s):
    """
    (str) -> bool
    Return True if and only if s is a palindrome.
    """
    ss = list(s)
    ss.reverse()
    ss = ''.join(ss)
    if s == ss:
        return True
    return False

def tests():
    assert palindrome('kayak')==True
    assert palindrome('redcar')==False

def main():
    tests()

main()
