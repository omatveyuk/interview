"""Quick sort in place.
   Using Lomuto partition scheme.

    >>> arr = [2,8,3,6,1,4,7]
    >>> quick_sort(arr, 0, len(arr)-1)
    >>> arr
    [1, 2, 3, 4, 6, 7, 8]

    >>> arr = [2,8,3,6,1,9,4,7]
    >>> quick_sort(arr, 0, len(arr)-1)
    >>> arr
    [1, 2, 3, 4, 6, 7, 8, 9]

    >>> arr = []
    >>> quick_sort(arr, 0, len(arr)-1)
    >>> arr
    []

    >>> arr = [1]
    >>> quick_sort(arr, 0, len(arr)-1)
    >>> arr
    [1]
"""

def quick_sort(arr, lo_index, hi_index):
    if lo_index < hi_index:
        pivot_index = partition(arr, lo_index, hi_index)
        quick_sort(arr, lo_index, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, hi_index)


def partition(arr, lo_index, hi_index):
    """Return pivot index"""
    pivot = arr[hi_index]  
    i = lo_index - 1    
    for j in xrange(lo_index, hi_index):
        if arr[j] <= pivot:
            i += + 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[hi_index] = arr[hi_index], arr[i+1]
    # for item in arr:
    #     print item,
    # print
    return i + 1


if __name__ == "__main__":
    debug = True
    if debug:
        from doctest import testmod
        if testmod().failed == 0:
            print "********** All Tests are passed. *************" 