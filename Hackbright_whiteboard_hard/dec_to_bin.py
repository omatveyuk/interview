"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin(0)
    '0'

    >>> dec2bin(1)
    '1'

    >>> dec2bin(2)
    '10'

    >>> dec2bin(4)
    '100'

    >>> dec2bin(15)
    '1111'
"""

def dec2bin(num):
    """Convert a decimal number to binary representation."""

    # Work backwards, finding the least-significant-bit first,
    # moving up to the most-significant bit.
    #
    # At the end, print the list of bits reversed
    temp = ''
    if num == 0:
        return '0'

    while num != 0:
        temp += str(num%2)
        num = num / 2

    return temp[::-1]


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
