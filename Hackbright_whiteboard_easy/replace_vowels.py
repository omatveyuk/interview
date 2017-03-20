"""Given list of chars, return a new copy, but with vowels replaced by '*'.

For example::

    >>> replace_vowels(['h', 'i'])
    ['h', '*']

    >>> replace_vowels([])
    []

    >>> replace_vowels(['o', 'o', 'o'])
    ['*', '*', '*']

    >>> replace_vowels(['z', 'z', 'z'])
    ['z', 'z', 'z']

Make sure to handle uppercase::

    >>> replace_vowels(["A", "b"])
    ['*', 'b']

Do not consider `y` a vowel::

    >>> replace_vowels(["y", "a", "y"])
    ['y', '*', 'y']

This should return a new list, not mutate the original::

    >>> a = ['h', 'i']
    >>> out = replace_vowels(a)
    >>> out is not a
    True

"""


def replace_vowels(chars):
    """Given list of chars, return a new copy, but with vowels replaced by '*'."""
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    new_chars = []
    for char in chars:
        if char.lower() in vowels:
            new_chars.append('*')
        else:
            new_chars.append(char)

    # Solution with list comprehension:
    #   return ['*' if char in vowels else char for char in chars]
    
    return new_chars


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
