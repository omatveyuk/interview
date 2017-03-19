"""Function add_to_zero
   Given list of ints, return True if any two nums in list sum to 0."""

def add_to_zero(numbers):
    """ Add To Zero
        Given list of ints, return True if any two nums in list sum to 0.

    >>> add_to_zero([1, 2, 3])
    False

    >>> add_to_zero([1, 2, 3,-1])
    True

    >>> add_to_zero([1, 2, 3, -5])
    False

    >>> add_to_zero([1, 2, 0, -3, 0])
    True

    >>> add_to_zero([])
    False

    >>> add_to_zero([1])
    False
    """

    for number in numbers:
        if number <= 0:
            if (-number) in numbers:
                return True
    return False


if __name__ == "__main__":
    from doctest import testmod
    if testmod().failed == 0:
        print "All Tests are passed"