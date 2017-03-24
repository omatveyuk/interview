"""Does a string have balanced parentheses?

For example::

   >>> has_balanced_parens("()")
   True

   >>> has_balanced_parens("(Oh Noes!)(")
   False

   >>> has_balanced_parens("((There's a bonus open paren here.)")
   False

   >>> has_balanced_parens(")")
   False

   >>> has_balanced_parens("(")
   False

   >>> has_balanced_parens("(This has (too many closes.) ) )")
   False

If you receive a string with no parentheses, consider it balanced::

   >>> has_balanced_parens("Hey...there are no parens here!")
   True
"""


def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""
    parentheses = []
    for char in phrase:
      if char == ')' and parentheses == []:
        return False
      if char == '(':
        parentheses.append('(')
      if char == ')':
        parentheses.pop()

    if parentheses != []:
      return False
    return True

    # SOlUTION2
    # parens = 0
    # for char in phrase:
    #     if char == "(":
    #         parens = parens + 1
    #     elif char == ")":
    #         parens = parens - 1
    #         if parens < 0:
    #             # We can never close more than we have open
    #             return False
    # # Make sure we have none left
    # if parens > 0:
    #     return False
    # else:
    #     return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n"
