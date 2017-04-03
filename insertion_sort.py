"""Insertion sort.
6 5 3 8 7 2
5 6 3 8 7 2
3 5 6 8 7 2
3 5 6 8 7 2
3 5 6 7 8 2
2 3 5 6 7 8
For each item in the list, starting at the second, find out how far to the left
it goes--as soon as we find a number smaller than it, we insert item after this number

>>> insertion_sort([6, 5, 3, 8, 7, 2])
[2, 3, 5, 6, 7, 8]

>>> insertion_sort([2, 3, 4, 7])
[2, 3, 4, 7]

"""

def insertion_sort(alist):
    """Given a list, sort it using insertion sort."""

    for i in xrange(len(alist)):
        j = i
        while j > 0 and alist[j-1] > alist[j]:
            alist[j-1], alist[j] = alist[j], alist[j-1]
            j -= 1
    return alist


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T! ***\n"