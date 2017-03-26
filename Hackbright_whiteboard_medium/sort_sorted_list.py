"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """
    new_lst = []
    index_a = 0
    index_b = 0

    while index_a < len(a) and index_b < len(b):
        if a[index_a] <= b[index_b]:
            new_lst.append(a[index_a])
            index_a += 1
        else:
            new_lst.append(b[index_b])
            index_b += 1

    if index_a < len(a):
        new_lst.extend(a[index_a:])

    if index_b < len(b):
        new_lst.extend(b[index_b:])
        
    return new_lst


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n"
