""" Check if a string has had one or zero edits.
    There are three types of edits: insert char, remove char, edit char.
    Given two strings, return True if there are one edit away. Otherwise False.

    >>> isOneAway('pale', 'ple')
    True
    >>> isOneAway('pales', 'pale')
    True
    >>> isOneAway('pale', 'bale')
    True
    >>> isOneAway('pale', 'bake')
    False
    >>> isOneAway('a', 'o')
    True
    >>> isOneAway('','o')
    True
    >>> isOneAway('pale', 'poles')
    False
    >>> isOneAway('pale', 'plle')
    True
    >>> isOneAway('pale', 'plles')
    False
    >>> isOneAway('pale', 'ples')
    False
    >>> isOneAway('pall', 'pll')
    True
    >>> isOneAway('pll', 'pd')
    False
    >>> isOneAway('pall', 'lpl')
    False
"""


def isOneAway(str_before, str_after):
    """Given two strings, return True if there are one edit away. Otherwise False."""

    edited = False
    len_before = len(str_before)
    len_after = len(str_after)

    # Case when was deleted or inserted more than 1 char
    if abs(len_before - len_after) > 1:
        return False

    # Case when string before and string after has the same lenght
    # No more than one char has to be edited
    if len_before - len_after == 0:
        for i in xrange(len_before):
            if str_before[i] != str_after[i]:
                if edited:
                    return False
                edited = True
        return edited

    # Case when was deleted/inserted 1 char (check that any other char was not edited)
    i = j = 0
    while i < len_before and j < len_after:
        if str_before[i] != str_after[j]:

            if edited:
                return False

            if len_before > len_after:
                i += i
            else:
                j += 1
            edited = True

        else:
            i += 1
            j += 1

    return True


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED.  one_away.py  WORKS SUCCESSFULLY! ***\n"
