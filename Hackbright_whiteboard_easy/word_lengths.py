"""Get dictionary of word-length: {words}.

Given a phrase, return dictionary keyed by word-length, with the value for
each length being the set of words of that length.

For example::

    >>> answer = word_lengths("cute cats chase fuzzy rats")

This should return {4: {'cute', 'cats'}, 5: {'chase', 'fuzzy', 'rats'}},
but since both dictionaries and sets are unordered, we can't just check if
it matches that exact string, so we'll test more carefully::

    >>> sorted(answer.keys())
    [4, 5]

    >>> answer[4] == {'cute', 'cats', 'rats'}
    True

    >>> answer[5] == {'chase', 'fuzzy'}
    True

Punctuation should be considered part of a word, so you only need to
split the string on whitespace::

    >>> answer = word_lengths("Hi, I'm Balloonicorn")

    >>> sorted(answer.keys())
    [3, 12]

    >>> answer[3] == {'Hi,', "I'm"}
    True

    >>> answer[12] == {"Balloonicorn"}
    True
"""


def word_lengths(sentence):
    """Get dictionary of word-length: {words}."""
    words = {}
    for word in sentence.split(' '):
        words[len(word)] = words.get(len(word), set())
        words[len(word)].add(word)
    return words

    # Solution Hackbright:
    # lengths = {}
    # words = sentence.split()
    # for word in words:
    #     if len(word) not in lengths:
    #         lengths[len(word)] = set()
    #     lengths[len(word)].add(word)
    # return lengths

    #Solution with setdefault:
    # lengths = {}
    # words = sentence.split()
    # for word in words:
    #     lengths.setdefault(len(word), set()).add(word)
    # return lengths


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NOTHING ESCAPES YOU!\n"
