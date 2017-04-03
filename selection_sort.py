
"""Selection sort.

6 5 3 8 7 2
2 5 3 8 7 6
2 3 5 8 7 6
2 3 5 8 7 6
2 3 5 6 7 8
2 3 5 6 7 8

Find min in list
Swap min with the first unsorted position
Save sorted elements, and repeat for unsorted elements. 

>>> selection_sort([6, 5, 3, 8, 7, 2])
[2, 3, 5, 6, 7, 8]

>>> selection_sort([2, 3, 4, 7])
[2, 3, 4, 7]

"""


def selection_sort(alist):
    """ Selection sort. """

    for i in xrange(len(alist) - 1):
        min = i
        for j in xrange(i+1, len(alist)):
            if alist[j] < alist[min]:
                min = j
        alist[i], alist[min] = alist[min], alist[i]
    
    return alist


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T! ***\n"
