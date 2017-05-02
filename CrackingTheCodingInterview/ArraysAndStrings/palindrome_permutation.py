""" Given a string, check if it is a permutation of a palindrome.
    Return True if a string ia a permuation of a palindrome, otherwise False.
    >>> isPalindromePermutation("Tact Cao")
    True

    >>> isPalindromePermutation("car")
    False

    >>> isPalindromePermutation("rar")
    True
"""


def isPalindromePermutation(input_str):
    """Return True if a string ia a permuation of a palindrome, otherwise False."""
    # Count how often each char appears in the string.
    # Count odd results. If this sum > 1 return False

    # SOLUTION 1
    # input_str = input_str.lower().replace(' ', '')
    # unique_char = set(input_str)
    # return False if sum(input_str.count(i) % 2 for i in unique_char) > 1 else True

    # SOLUTION 2
    # use Counter which is collectins of tuples where 0-element of item is char,
    # 1st-element - how many times this char appears in the string
    from collections import Counter
    input_str = input_str.lower().replace(' ', '')
    return False if sum(item[1] % 2 for item in Counter(input_str).items()) > 1 else True


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED.  palindrome_permutation.py  WORKS SUCCESSFULLY! ***\n"
