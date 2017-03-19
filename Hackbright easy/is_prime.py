"""Is a number a prime number?

Only numbers >1 can be prime numbers:

    >>> is_prime(0)
    False

    >>> is_prime(1)
    False

Any number >1 that has no divisors other than 1 and itself
is a prime number:

    >>> is_prime(2)
    True

    >>> is_prime(3)
    True

    >>> is_prime(4)
    False

    >>> is_prime(11)
    True

    >>> is_prime(999)
    False
"""

import math

def is_prime(num):
    """Is a number a prime number?"""
    if num <= 1:
        return False
    for i in xrange(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU MET YOUR PRIME DIRECTIVE!\n"




