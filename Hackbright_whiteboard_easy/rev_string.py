"""Reverse a string.

For example::

    >>> rev_string("")
    ''

    >>> rev_string("a")
    'a'

    >>> rev_string("porcupine")
    'enipucrop'

"""


def rev_string(astring):
    """Return reverse of string.

    You may NOT use the reversed() function!
    """
    output = ''
    for i in xrange(1, len(astring)+1):
        output += astring[-i]
    return output



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !KROW DOOG\n"
