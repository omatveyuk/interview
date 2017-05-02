"""Is all chars in string is unique?
    Implement an algorithm to detemine if a string has all unique characters
    without using additional data structures.
"""


def allUniqueChar(string):
    """Check if all chars in string is unique.
        Return: True if all chars is unique, othrwise False.
        >>> allUniqueChar("Oxana")
        False
        >>> allUniqueChar("Misha")
        True

    """
    # Create list with length 128, bc ASCII is 128 chars
    letters = ['' for i in xrange(128)]
    for char in string:
        if letters[ord(char)] != '':
            return False
        letters[ord(char)] = char
    return True

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED.  all_unique_char.py  WORKS SUCCESSFULLY! ***\n"
