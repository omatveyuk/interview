""" Find index of element in array

>>> find_index(4, [6, 5, 3, 8, 7, 2])
None

>>> find_index(3, [6, 5, 3, 8, 7, 2])
2

>>> find_index(6, [6, 5, 3, 8, 7, 2])
0

>>> find_index(2, [6, 5, 3, 8, 7, 2])
5

>>> find_index(2, [2])
0

>>> find_index(2, [])
None

"""

def find_index(elm, alist):
    """Given an array and an element, find an index in the list."""

    if alist == []:
        print None
        return None

    if elm == alist[0]:
        return 0

    index = find_index(elm, alist[1:])

    return None if index is None else index+1

    
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T! ***\n"