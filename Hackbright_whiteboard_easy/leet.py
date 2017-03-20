"""Translate phrase to "leet-speak".

For example::

    >>> translate_leet("Hi Balloonicorn")
    'Hi B@1100nic0rn'

    >>> translate_leet("Hackbright is the Shizzle")
    'H@ckbrigh7 i5 7h3 5hizz13'

"""


def translate_leet(phrase):
    """Translates input into "leet-speak"."""
    leet_dict = {'a': '@', 
                 'o': '0',
                 'e': '3',
                 'l': '1',
                 's': '5',
                 't': '7'}

    new_str = ''
    for char in phrase:
        new_str += leet_dict.get(char.lower(), char)
    return new_str
if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AE3S0M3!\n"
