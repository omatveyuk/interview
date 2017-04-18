"""Zero one game.
    Alice and Bob are playing the following game:

    The game starts with a sequence of zeroes and ones.
    Alice and Bob take alternating turns, and Alice always moves first.
    During each turn, a player removes one element from the sequence that satisfies the following:
        It is not the first or last element.
        It must be surrounded by zeroes on both sides.
        The first player who can't take their turn loses the game.
        Both players always move optimally.
        START:1 0 1 0 1
        Alice removes 1 in the middle: 1 0 0 1
        Bob doesn't have moves -> Alice won


    >>> [1, 0, 0, 1]
    Bob

    >>> [1, 0, 1, 0, 1]
    Alice

    >>> [0, 0, 0, 0, 0, 0]
    Bob
"""

def oneZeroGame(sequence):
    """Zero one game."""
    continue_game = True
    winner = 'Bob'
    while len(sequence) > 2 and continue_game:
        continue_game = False
        for i in xrange(1, len(sequence)-1):
            if sequence[i-1] == 0 and sequence[i+1] == 0:
                sequence.remove(sequence[i])
                if winner == 'Bob':
                    winner = 'Alice'
                else: 
                    winner = 'Bob'
                continue_game = True
                break
    return winner


if __name__ == '__main__':
    import doctest

    print
    if doctest.testmod().failed == 0:
        print "\t*** ALL TESTS PASSED; GOOD WORK!"
    print