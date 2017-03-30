"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(s):
    """Evaluate expression."""
    # SOLUTION1
    # num1 = None
    # num2 = None

    # for i in xrange(1, len(s)+1):
    #     if s[-i] != ' ':
    #         if s[-i] not in ["+", "*", "-", "/"]:
    #             if num1 is None:
    #                 num1 = int(s[-i])
    #             else:
    #                 num2 = int(s[-i])
    #         else:
    #             if s[-i] == "+":
    #                 num1 = num2 + num1
    #             elif s[-i] == "*":
    #                 num1 = num2 * num1
    #             elif s[-i] == "-":
    #                 num1 = num2 - num1
    #             else:
    #                 num1 = num2 / num1

    # return num1

    #SOLUTION 2

    # base case
    if len(s) == 5:
        if s[0] == "+":
            return int(s[2]) + int(s[4])
        if s[0] == "*":
            return int(s[2]) * int(s[4])
        if s[0] == "-":
            return int(s[2]) - int(s[4])
        return int(s[2]) / int(s[4])

    if s[0] == "+":
        return int(s[2]) + calc(s[4:])
    if s[0] == "*":
        return int(s[2]) * calc(s[4:])
    if s[0] == "-":
        return int(s[2]) - calc(s[4:])
    return int(s[2]) / calc(s[4:])


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n"
