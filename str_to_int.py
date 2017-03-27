"""Converter string to int"""

def positive_int_from_str(str):
    """Return positive integer"""
    if str == "":
        return 0

    return (ord(str[0]) - ord("0")) * (10 ** (len(str)-1)) + positive_int_from_str(str[1:])


def is_valid(str):
    for char in str:
        if char not in ["-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print "Invalid string"
            return False
    return True

def convert_str_to_int(str):
    """Return integer from string
        >>> convert_str_to_int("123")
        123

        >>> convert_str_to_int("0")
        0

        >>> convert_str_to_int("")


        >>> convert_str_to_int("-567")
        -567

        >>> convert_str_to_int("1a34")
        Invalid string

    """
    if is_valid(str):
        if str == "":
            return None

        if str[0] == "-":
            return -1 * positive_int_from_str(str[1:])
        else:
            return positive_int_from_str(str)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"




