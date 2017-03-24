"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8
    
    """
    #SOLUTION 1
    # # create list the same length as max_nums with all False value
    # check_lst = [False] * max_num
    # # change element with index of number-1 to True if number exists in nums
    # for number in nums:
    #     check_lst[number-1] = True
    # return check_lst.index(False) + 1

    #SOLUTION 2
    # fisn difference between expectation sum of numbers and real sum
    # difference will be missing number
    expectation_sum = sum([num+1 for num in xrange(max_num)])
    real_sum = sum([num for num in nums])
    return expectation_sum - real_sum




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. NICELY DONE!\n"
