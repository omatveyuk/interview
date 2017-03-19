"""Binary search
   Return index in list for element which contain number.
   If number does not appear in list or list is empty return -1.

    >>> binary_search([], 3)
    -1

    >>> binary_search([2, 3, 5, 9], 8)
    -1

    >>> binary_search([2, 3, 5, 7, 9], 2)
    0

    >>> binary_search([2, 3, 5, 9], 5)
    2

"""

def binary_search(lst, number):
    """ Return index in list for element which contain number
        Use binary search
    """
    min = 0
    max = len(lst) - 1

    while min != max:
        if lst == []:
            return -1

        mid_point = (min + max) / 2
        if lst[mid_point] == number:
            return mid_point

        if lst[mid_point] > number:
            max = mid_point - 1
        else:
            min = mid_point + 1

    return -1


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"