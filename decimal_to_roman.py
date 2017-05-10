""" Convert ecimal notation to roman notaion.

    >>> convert_decimal(95)
    'XCV'

    >>> convert_decimal(4)
    'IV'

    >>> convert_decimal(3)
    'III'

    >>> convert_decimal(7)
    'VII'

    >>> convert_decimal(8)
    'VIII'

    >>> convert_decimal(1700)
    'MDCC'

    >>> convert_decimal(5)
    'V'
    
    >>> convert_decimal(315)
    'CCCXV'

    >>> convert_decimal(609)
    'DCIX'

    >>> convert_decimal(409)
    'CDIX'

    >>> convert_decimal(411)
    'CDXI'

    >>> convert_decimal(403)
    'CDIII'

    >>> convert_decimal(505)
    'DV'

    >>> convert_decimal(1984)
    'MCMLXXXIV'

    >>> convert_decimal(1084)
    'MLXXXIV'
"""

d_roman = { 0: '',
            1:'I',
            5:'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M' }

def convert_decimal(number, n = 1000):
    if number == 0:
        return ''

    counter = number / n
    if counter <= 3:
        roman = d_roman[n] * counter
    elif counter == 4:
        roman = d_roman[n] + d_roman[n * 5]
    elif counter == 5:
        roman = d_roman[n * 5]
    elif counter < 9:
        roman = d_roman[n * 5] + d_roman[n] * (counter - 5)
    elif counter == 9:
        roman = d_roman[n] + d_roman.get(n*10, '')

    return roman + convert_decimal(number % n, n / 10)


if __name__ == "__main__":
    debug = True
    if debug:
        from doctest import testmod
        if testmod().failed == 0:
            print "********** All Tests are passed. *************" 



