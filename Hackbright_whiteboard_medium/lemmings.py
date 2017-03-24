"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""
    max_distance = cafes[0]
    for i in xrange(len(cafes)-1):
        if ((cafes[i+1] - cafes[i])/2 ) > max_distance:
            max_distance = (cafes[i+1] - cafes[i])/2
    if cafes[-1] != (num_holes - 1) and \
       (num_holes - 1 - cafes[-1]) > max_distance:
       max_distance = num_holes - 1 - cafes[-1]
    return max_distance
                


           

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; GREAT JOB!\n"
