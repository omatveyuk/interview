"""Quick sort.
    The first element in a sub-array should be used as a pivot.
    Divide array into two subarrays (left: are numbers smaller than pivot, right: 
    numbers are greater than pivot), along with the pivot, are merged together.
    Partition the left side before partitioning the right side.
    The pivot should be placed between sub-arrays while merging them.
    Array of length 1 or less will be considered sorted, and there is no need 
    to sort or to print them.
    >>> quick_sort([5, 8, 1, 3, 7, 9, 2])
    [1, 2, 3, 5, 7, 8, 9]

"""

def quick_sort(ar):    
    if len(ar) <= 1:
        return ar

    left = []
    right = []
    for i in xrange(1, len(ar)):
        if ar[i] > ar[0]:
            right.append(ar[i])
        if ar[i] < ar[0]:
            left.append(ar[i])

    # for printing intermediate result:
    # change docstring:
    #    >>> quick_sort([5, 8, 1, 3, 7, 9, 2])
    #    2 3
    #    1 2 3
    #    7 8 9
    #    1 2 3 5 7 8 9
    #
    # uncomment following code:
    # sort_ar = quick_sort(left) + [ar[0]] + quick_sort(right)
    # for elm in sort_ar:
    #     print elm,
    # print 
    # return sort_ar

    return quick_sort(left) + [ar[0]] + quick_sort(right)
        
if __name__ == "__main__":
    debug = True
    if debug:
        from doctest import testmod
        if testmod().failed == 0:
            print "********** All Tests are passed. *************"   

