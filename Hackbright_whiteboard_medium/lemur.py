"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
"""


def  lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"
    # one tree
    if len(branches) <= 1:
        return 0
    # only two tree
    if len(branches) == 2:
        if branches[1] == 1:
            return 0
        else:
            return 1
    index = 0
    count = 0
    # we have more than 2 trees
    while index <= (len(branches)-2):
        if branches[index+2] == 0:
            index += 2
        else:
            index += 1
        count += 1
    return count

    #SOLUTION 2
    # at = 0
    # n_jumps = 0

    # while at < len(branches) - 1:
    #     at += 2
    #     if at >= len(branches) or branches[at] == 1:
    #         # We can jump this far, so only jump 1
    #         at -= 1
    #     n_jumps += 1

    # return n_jumps

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE JUMPING!\n"