"""Given a list, sort it using insertion sort.

For example::

    >>> from random import shuffle
    >>> alist = range(1, 11)

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""


def insertion_sort(alist):
    """Given a list, sort it using insertion sort."""
    # SOLUTION 1
    for i in xrange(len(alist)):
        j = i
        # For each item in the list, starting at the second, find out
        # how far to the left it goes--swap elements if previous number is 
        # greater than number
        while j > 0 and alist[j-1] > alist[j]:
            alist[j-1], alist[j] = alist[j], alist[j-1]
            j -= 1
    return alist


    # SOLUTION 2
    # for i in range(1, len(alist)):
    #     # For each item in the list, starting at the second, find out
    #     # how far to the left it goes--as soon as we find a number
    #     # smaller than it, we've gone far enough back
    #     j = i - 1
    #     while j >= 0 and alist[j] > alist[i]:
    #         j -= 1
    #     j += 1

    #     # now j in the position where we should move i to, and we should
    #     # put everything over to the right after that
    #     if j != i:
    #         alist[j:i + 1] = alist[i:i + 1] + alist[j:i]

    # return alist


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE SORTING!\n"
