"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> find_mode([1]) == {1}
    True

    >>> find_mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> find_mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def find_mode(nums):
    """Find the most frequent num(s) in nums."""
    set_nums = set(nums)
    max_fr = 0
    for number in set_nums:
        frequency = nums.count(number)
        if frequency > max_fr:
            max_frequency = set([number])
            max_fr = frequency
        elif frequency == max_fr:
            max_frequency.add(number)

    return max_frequency


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"
