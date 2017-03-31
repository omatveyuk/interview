"""Convert a hexadecimal string, like '1A', into it's decimal equivalent.

    >>> hex_convert('6')
    6

    >>> hex_convert('10')
    16

    >>> hex_convert('FF')
    255

    >>> hex_convert('FFFF')
    65535
"""


def hex_convert(hex_in):
    """Convert a hexadecimal string, like '1A', into it's decimal equivalent."""

    number = 0
    dict_16 = {'0': 0,
               '1': 1,
               '2': 2,
               '3': 3,
               '4': 4,
               '5': 5,
               '6': 6,
               '7': 7,
               '8': 8,
               '9': 9,
               'A': 10,
               'B': 11,
               'C': 12,
               'D': 13,
               'E': 14,
               'F': 15}
    for i in xrange(len(hex_in)):
        number += dict_16[hex_in[-i-1]] * (16 ** i)
    return number


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. YOU'RE TERRIFIC!\n"
