"""Return n unique random numbers from 1-10 (inclusive).

Given the numbers 1-10, return `n` random numbers, making sure
to never return the same number twice. You can trust that this
function will never be called with n < 0 or n > 10.

It's tricky to test random functions! However, we can make sure
asking for zero numbers gives us an empty list::

    >>> lucky_numbers(0)
    []

And if we ask for all numbers, we shouldn't get any repeats::

    >>> sorted(lucky_numbers(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""

import random


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""
    lucky_numbers = []
    count = 1
    while count <= n:
        number =  random.randint(1,10)
        if number not in lucky_numbers:
            lucky_numbers.append(number)
            count += 1

    return lucky_numbers

    # nums = range(1, 11)
    # lucky_nums = []

    # for i in range(n):
    #     num = random.choice(nums)
    #     nums.remove(num)
    #     lucky_nums.append(num)

    # return lucky_nums


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
