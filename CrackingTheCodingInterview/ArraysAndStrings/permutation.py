"""Check if one string is permutation of another string.
   Return: True if one string is permutation of another string, otherwise False.
"""


def permutation(str1, str2):
    """Check if one string is permutation of another string.
    >>> permutation("oxana", "xanao")
    True
    >>> permutation("oxana", "oxanaM")
    False
    >>> permutation("oxana", "mariia")
    False

    """
    # SOLUTION 1
    if len(str1) != len(str2):
        return False
    str1.sort()               # O(n) = nlog(n)
    str2.sort()
    return str1 == str2

    #SOLUTION 2
    from collections import Counter     # O(n) = nlog(n)
    return Counter(str1) == Counter(str2)


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED.  permutation.py  WORKS SUCCESSFULLY! ***\n"
