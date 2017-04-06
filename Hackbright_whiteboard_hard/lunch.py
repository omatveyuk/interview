"""Leveret lunch count.
garden
A list of the garden cells with carrot counts. This will be a list of rows, 
with each row being a list of columns.
Start in the middle of the garden. If there are more than one cell in the middle, 
start in the middle cell with the most number of carrots. 
(There will never be a tie for the middle cell with the most number of carrots).

Eat all the carrots in that cell and then moves to the neighboring cell with 
the most number of carrots. Look first to west, then north, then east, then south. 
If there is a tie for the most number of carrots, take the first cell in the list
that has the high number of carrots in it.

Once there are no neighboring cells with carrots, return the number of carrots eaten.

Check that garden is valid::

    >>> garden = [
    ...     [1, 1],
    ...     [1],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden not a matrix!

    >>> garden = [
    ...     [1, 1],
    ...     [1, 'a'],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden values must be ints!

Consider simple cases::

    >>> garden = [
    ...     [0, 0, 0],
    ...     [0, 0, 0],
    ...     [0, 0, 0]
    ... ]

    >>> lunch_count(garden)
    0

    >>> garden = [
    ...     [1, 1, 1],
    ...     [0, 1, 1],
    ...     [9, 1, 9]
    ... ]

    >>> lunch_count(garden)
    3

    >>> garden = [
    ...     [1, 1, 1],
    ...     [1, 1, 1],
    ...     [1, 1, 1]
    ... ]

    >>> lunch_count(garden)
    9

Make sure it works with even-sides
(this will start with the 4 and head east)::

    >>> garden = [
    ...     [9, 9, 9, 9],
    ...     [9, 3, 1, 0],
    ...     [9, 1, 4, 2],
    ...     [9, 9, 1, 0],
    ... ]

    >>> lunch_count(garden)
    6

Consider our most complex case::

    >>> garden = [
    ...     [2, 3, 1, 4, 2, 2, 3],
    ...     [2, 3, 0, 4, 0, 3, 0],
    ...     [1, 7, 0, 2, 1, 2, 3],
    ...     [9, 3, 0, 4, 2, 0, 3],
    ... ]

    >>> lunch_count(garden)
    15

"""


def lunch_count(garden):
    """Given a garden of nrows of ncols, return carrots eaten."""

    # Sanity check that garden is valid

    row_lens = [len(row) for row in garden]
    assert min(row_lens) == max(row_lens), "Garden not a matrix!"
    assert all(type(c) is int for c in row for row in garden), \
        "Garden values must be ints!"

    # Get number of rows and columns

    nrows = len(garden)
    ncols = len(garden[0])

    # Get value of garden cell
    def _get_value(j, i, nrows, ncols, seen):
        if (j, i) not in seen and j >= 0  and j < nrows and \
            i >= 0 and i < ncols:
            return garden[j][i]
        return 0

    start_i = ncols / 2
    start_j = nrows / 2

    if nrows % 2 != 0 and ncols % 2 == 0:
        if garden[start_i][start_j] < garden[start_i - 1][start_j]:
            start_i = ncols / 2 - 1

    elif nrows % 2 == 0 and ncols % 2 != 0:
        if garden[start_i][start_j] < garden[start_i][start_j - 1]:
            start_j = nrows / 2 - 1

    else:
        if garden[start_i - 1][start_j] > garden[start_i][start_j] and \
           garden[start_i - 1][start_j] > garden[start_i - 1][start_j - 1] and \
           garden[start_i - 1][start_j] > garden[start_i][start_j - 1]:
           start_i -= 1

        elif garden[start_i][start_j - 1] > garden[start_i][start_j] and \
            garden[start_i][start_j - 1] > garden[start_i - 1][start_j - 1] and \
            garden[start_i][start_j - 1] > garden[start_i - 1][start_j]:
            start_j -= 1

        elif garden[start_i - 1][start_j - 1] > garden[start_i][start_j] and \
            garden[start_i - 1][start_j - 1] > garden[start_i][start_j - 1] and \
            garden[start_i - 1][start_j - 1] > garden[start_i - 1][start_j]:
            start_i -= 1
            start_j -= 1

    total = garden[start_j] [start_i]
    seen = set([(start_j, start_i)])

    curr_j = start_j
    curr_i = start_i
    while True:
        west_j = curr_j
        west_i = curr_i - 1
        west = _get_value(west_j, west_i, nrows, ncols, seen)

        north_j = curr_j - 1
        north_i = curr_i
        north = _get_value(north_j, north_i, nrows, ncols, seen)

        east_j = curr_j
        east_i = curr_i + 1
        east = _get_value(east_j, east_i, nrows, ncols, seen)

        south_j = curr_j + 1
        south_i = curr_i
        south = _get_value(south_j, south_i, nrows, ncols, seen)

        if west == 0 and north == 0 and east == 0 and south == 0:
            return total

        if west >= north and west >= east and west >= south:
            total += west
            curr_j = west_j
            curr_i = west_i
            seen.add((west_j, west_i))
            continue

        if north >= east and north >= south and north >= west:
            total += north
            curr_j = north_j
            curr_i = north_i
            seen.add((north_j, north_i))
            continue            

        if east >= south and east >= west and east >= north:
            total += east
            curr_j = east_j
            curr_i = east_i
            seen.add((east_j, east_i))
            continue 

        if south >= west and south >= north and south >= east:
            total += south
            curr_j = south_j
            curr_i = south_i
            seen.add((south_j, south_i))
            continue


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS! HOP ALONG NOW! ***\n"
