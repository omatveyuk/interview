"""Create a schedule.

    Input: unordered list of tuples. Each tuple contains start and finish time of meeting
    Output: create new list of tuples which is schedule

    >>> schedule([(1,2), (4,6), (2,4), (7,8)])
    [(1, 6), (7, 8)]

    >>> schedule([(1,2), (4,6), (2,4), (3,8), (7,8)])
    [(1, 8)]


    >>> schedule([(1,2), (4,6), (2,4), (3,8), (7,8), (9, 10)])
    [(1, 8), (9, 10)]

    >>> schedule([(1, 5)])
    [(1, 5)]

    >>> schedule([])
    []
"""


def schedule(lst):
    """Create a schedule."""
    schedule = []
    sorted_lst = sorted(lst)
    temp = []

    for item in sorted_lst:
        if temp == []:
            temp = list(item)
        elif list(item)[0] <= temp[1]:
            if list(item)[1] > temp[1]:
                temp[1] = list(item)[1]
        else:
            schedule.append(tuple(temp))
            temp = list(item)

    if temp != []:
        schedule.append(tuple(temp))

    return schedule  

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED! ***\n"
