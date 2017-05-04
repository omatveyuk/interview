""" Reduce string.
    Input consisting of  lowercase English alphabetic letters. 
    In one operation we can delete any pair of adjacent letters with same value.
    Repeat the above operation as many times as it can be performed.

    Return new string or "Empty String"
    >>> superReducedString('aaabccddd')
    'abd'
    >>> superReducedString('baab')
    'Empty String'
    >>> superReducedString('aa')
    'Empty String'
"""


def superReducedString(input_str):
    """Reduce string. Delete pair letters with the same value."""
    new_str = []

    if input_str != []:
        for i in xrange(len(input_str)):
            if new_str == [] or new_str[-1] != input_str[i]:
                new_str.append(input_str[i])

            elif new_str[-1] == input_str[i]:
                new_str.pop()
    if new_str == []:
        return "Empty String"
    else:
        return ''.join(new_str)


if __name__ == "__main__":
    debug = False
    if debug:
        from doctest import testmod
        if testmod().failed == 0:
            print "********** All Tests are passed. *************"

    input_str = raw_input().strip()
    print superReducedString(input_str)
