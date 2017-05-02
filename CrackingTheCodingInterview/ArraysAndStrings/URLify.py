"""Replace all spaces in string with '%20'.
    >>> URLify("Mr John Smith   ", 13)
    'Mr%20John%20Smith'
"""


def URLify(str):
    import re
    return re.sub('\s+', '%20', str.rstrip())


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED.  URLify.py  WORKS SUCCESSFULLY! ***\n"
