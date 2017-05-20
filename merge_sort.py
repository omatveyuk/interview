"""Merge sort.
    1. Make Everything a List of One. Devide list on two parts evry recursion call.
    2. Merge Strategy
        Start with two sorted lists
        Initialize new, empty list for results
        Compare first element of each sorted list
        Remove whichever element is lower and add it to the results list
        Continue comparing 1st elements of each list until a list is empty
        Append the remaining items from the other list to results lis

    >>> merge_sort([2,8,3,6,1,4,7])
    [1, 2, 3, 4, 6, 7, 8]

    >>> merge_sort([2,8,3,6,1,9,4,7])
    [1, 2, 3, 4, 6, 7, 8, 9]

    >>> merge_sort([])
    []

    >>> merge_sort([1])
    [1]
"""

def merge(lst1, lst2):
    """Merge two ordered lists"""
    lst = []
    while lst1 != [] or lst2 != []:
        if lst1 == []:
            lst.append(lst2.pop(0))
        elif lst2 == []:
            lst.append(lst1.pop(0))
        elif lst1[0] < lst2[0]:
            lst.append(lst1.pop(0))
        else:
            lst.append(lst2.pop(0))
    return lst

def merge_sort(lst):
    """Merge sort"""

    if len(lst) <= 1:
        return lst

    # divide lst in two parts
    midpoint = len(lst)/2
    left = merge_sort(lst[:midpoint])
    right = merge_sort(lst[midpoint:])

    return merge(left, right)


debug = True
if debug:
    from doctest import testmod
    if testmod().failed == 0:
        print "********** All Tests are passed. *************" 


