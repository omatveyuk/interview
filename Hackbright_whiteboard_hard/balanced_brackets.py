"""Does a given string have balanced pairs of brackets?

Given a string, return True or False depending on whether the string
contains balanced (), {}, [], and/or <>.

Many of the same test cases from Balance Parens apply to the expanded
problem, with the caveat that they must check all types of brackets.

These are fine::

   >>> has_balanced_brackets("<ok>")
   True

   >>> has_balanced_brackets("<{ok}>")
   True

   >>> has_balanced_brackets("<[{(yay)}]>")
   True

These are invalid, since they have too many open brackets::

   >>> has_balanced_brackets("(Oops!){")
   False

   >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
   False

These are invalid, as they close brackets that weren't open::

   >>> has_balanced_brackets(">")
   False

   >>> has_balanced_brackets("(This has {too many} ) closers. )")
   False

Here's a case where the number of brackets opened matches
the number closed, but in the wrong order::

    >>> has_balanced_brackets("<{Not Ok>}")
    False

If you receive a string with no brackets, consider it balanced::

   >>> has_balanced_brackets("No brackets here!")
   True

"""


def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """
    brackets = {')': '(',
                '}': '{',
                ']': '[',
                '>': '<'}
    seen_brackets = []
    for char in phrase:
      if char in ['(', '{', '[', '<']:
        seen_brackets.append(char)
      elif char in brackets.keys():
        if  seen_brackets == [] or brackets[char] != seen_brackets.pop():
          return False
    if seen_brackets != []:
      return False
    return True

    #SOLUTION2

    # closers_to_openers = {")": "(", "]": "[", "}": "{", ">": "<"}
    # # Set of all opener characters; used to match openers quickly.
    # openers = set(closers_to_openers.values())
    # # Create an empty list to use as a stack.
    # openers_seen = []

    # for char in phrase:

    #     # Push open brackets onto the stack.
    #     if char in openers:
    #         openers_seen.append(char)
    #     # For closers:
    #     #
    #     # - if nothing is open; fail fast
    #     # - if we are the twin of the most recent opener, pop & continue
    #     # - else we're the twin to a different opener; fail fast
    #     elif char in closers_to_openers:
    #         if openers_seen == []:
    #             return False

    #         if openers_seen[-1] == closers_to_openers.get(char):
    #             openers_seen.pop()

    #         else:
    #             return False

    # # An empty stack means the brackets are balanced.
    # return openers_seen == []

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY BRACKETS!\n"
