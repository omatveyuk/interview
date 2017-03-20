"""Given a string, return True if it is a pangram, False otherwise.
   A pangram is a sentence that contains all the letters of the English alphabet
   at least once

For example::

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True
    
    >>> is_pangram("I love cats, but not mice")
    False
"""


def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""
    import string
    alphabet = set(list(string.ascii_lowercase))
    chars_sentence = set(list(sentence.lower()))
    if (alphabet & chars_sentence) == alphabet:
        return True
    return False

    # solution 2
    # used = {char.lower() for char in sentence if char.isalpha()}
    # return len(used) == 26


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
