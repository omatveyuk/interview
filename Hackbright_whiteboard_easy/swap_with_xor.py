#x = 10   1010
#y = 3   11

def swap_with_xor(x, y):
    """Swap two variables
        >>> swap_with_xor(10, 3)
        (3, 10)
        >>> swap_with_xor(2, 2)
        (2, 2)

    """
    x = x ^ y       # 1010
                    # 0011
                    # ---
                    # 1001
                    # x = 9

    y = y ^ x       # 0011
                    # 1001
                    # ---
                    # 1010
                    # y = 10

    x = x ^ y       # 1001
                    # 1010
                    # ---
                    # 0011
                    # x = 3
    return (x, y)


if __name__ == "__main__":
    from doctest import testmod
    if testmod().failed == 0:
        print "All Tests are passed"

