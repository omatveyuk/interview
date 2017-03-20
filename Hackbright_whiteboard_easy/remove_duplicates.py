"""Function that is given a list of items and returns a new list of those items, 
   in the same order, but with duplicate removed
    
    >>> deduped([1, 1, 1])
    [1]

Keep items in the order where they first appeared:

    >>> deduped([1, 2, 1, 1, 3])
    [1, 2, 3]

    >>> deduped([5, 1, 5, 2, 5, 5, 3, 2])
    [5, 1, 2, 3]

A list with no duplicates would return the same:

    >>> deduped([1, 2, 3])
    [1, 2, 3]

    >>> deduped([])
    []

This should return a new list, not mutate the existing list:

    >>> a = [1, 2, 3]
    >>> b = deduped(a)
    >>> a == b
    True

    >>> a is b
    False

"""

def deduped(lst):
    """Return new list from items with duplicates removed."""

    # not right solution:
    # Except that sets do not maintain order, so we cant extract the original
    # order where items appeared; our answer could be [2, 1, 3], when we want [1, 2, 3]
    # return list(set(lst))

    # runtime solution O(n), because "in" for set O(1)
    seen = set()
    new_lst = []
    for item in lst:
        if item not in seen:
            new_lst.append(item)
            seen.add(item)
    return new_lst



if __name__ == "__main__":
    from doctest import testmod
    if testmod().failed == 0:
        print "All Tests are passed"