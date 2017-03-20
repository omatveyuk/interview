"""Does word contains unique set of characters?

For example::

    >>> has_unique_chars("Monday")
    True

    >>> has_unique_chars("Moonday")
    False

    >>> has_unique_chars("")
    True

Uppercase and lowercase letters should be considered separately::

    >>> has_unique_chars("Bob")
    True
"""


def has_unique_chars(word):
    """Does word contains unique set of characters?"""
    unique = set()
    for char in word:
        if char in unique:
            return False
        unique.add(char)
    return True

# def has_unique_chars(word):
#     """Does word contains unique set of characters?"""
#     unique_word = set(word)
#     return len(unique_word) == len(word)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME!\n"
