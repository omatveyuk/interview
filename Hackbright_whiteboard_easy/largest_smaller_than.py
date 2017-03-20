"""Return index of largest num in sorted list that is smaller than given num.

For example:

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 10)
    2

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 33)
    4

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -1)
    1

Never find xnumber --- it's not smaller than itself!

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 8)
    1

If no such number exists, return None:

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -10) is None
    True

"""


def find_largest_smaller_than(nums, xnumber):
    """Find largest number in sorted list that is smaller than given number."""
    index = None

    for i in xrange(len(nums)):
        if nums[i] < xnumber:
            index = i
        else:
            break
    return index

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU ARE THE MAXIMUM!\n"

