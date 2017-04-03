"""Bubble sort.

6 5 3 8 7 2
5 3 6 7 2 8
3 5 2 6 7 8
3 2 5 6 7 8
2 3 5 6 7 8

The big numbers bubble to the top. After the first pass through the list, 
the biggest number will be all the way to the right. After the second pass, 
the second highest number will be second from the right, and so on.

>>> bubble_sort([6, 5, 3, 8, 7, 2])
[2, 3, 5, 6, 7, 8]

>>> bubble_sort([2, 3, 4, 7])
[2, 3, 4, 7]

"""

def bubble_sort(alist):
    """Given a list, sort it using bubble sort."""

    for i in range(len(alist) - 1):

        for j in range(len(alist) - 1):

            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]

    return alist


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T! ***\n"