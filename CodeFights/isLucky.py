""" Given a ticket number n, determine if it's lucky or not.
    Ticket numbers usually consist of an even number of digits. 
    A ticket number is considered lucky if the sum of the first half of the digits
    is equal to the sum of the second half.
    Return True if the ticket is lucky, otherwise False

    >>> isLucky(12390)
    False

    >>> isLucky(1230)
    True
"""
def isLucky(n):
    if len(str(n)) % 2 != 0:
        return False

    half_n = len(str(n)) / 2
    # print "first half:", str(n)[:half_n]
    # print "second half:", str(n)[half_n:]
    if sum(int(i) for i in str(n)[:half_n]) == sum(int(i) for i in str(n)[half_n:]):
        return True
    return False

if __name__ == "__main__":
    debug = True
    if debug:
        from doctest import testmod
        if testmod().failed == 0:
            print "********** All Tests are passed. *************"
