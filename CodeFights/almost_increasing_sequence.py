""" Almost Increasing Sequence.
    Given a sequence of integers as an array, determine whether it is possible 
    to obtain a strictly increasing sequence by removing no more than one element
    from the array.

    >>> almostIncreasingSequence([1, 3, 2, 1]) == True
    False

    >>> almostIncreasingSequence([1, 3, 2]) == True
    True

    >>> almostIncreasingSequence([10, 1, 2, 3, 4, 5]) == True
    True

    >>> almostIncreasingSequence([1, 1]) == True
    True

    >>> almostIncreasingSequence([1, 2, 1, 2]) == True
    False

    >>> almostIncreasingSequence([1, 2, 3, 4, 99, 5, 6]) == True
    True

    >>> almostIncreasingSequence([1, 2, 3, 4, 3, 6]) == True
    True

    >>> almostIncreasingSequence([1, 2, 3, 4, 3]) == True
    True

    >>> almostIncreasingSequence([1, 2, 3, 4, 5, 3, 5, 6]) == True
    False

    >>> almostIncreasingSequence([40, 50, 60, 10, 20, 30]) == True
    False
"""

def almostIncreasingSequence(sequence):
    i = 0
    j = 1
    counter = 0
    while i < len(sequence)-1 and j < len(sequence): 
        # print "counter:", counter
        # print "s[{0}]: {1} s[{2}]: {3}".format(i, sequence[i], j, sequence[j])
        if sequence[i] >= sequence[j]:
            if counter == 1:
                return False    
            counter += 1    
            if i != 0:
                # if sequence[i-1] < sequence[j]:
                #     i -= 1
                #     continue
                # else:
                if sequence[i-1] >= sequence[j]:
                    j += 1
                    continue
        i = j
        j += 1

    return True


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"