"""Convert roman number to decimal. 

    >>> convert_roman("XCV")
    95

    >>> convert_roman("IV")
    4

    >>> convert_roman("III")
    3

    >>> convert_roman("VII")
    7

    >>> convert_roman("MDCC")
    1700

    >>> convert_roman("V")
    5
    
    >>> convert_roman("CCCXV")
    315

    >>> convert_roman("DCIX")
    609

    >>> convert_roman("CDIX")
    409

    >>> convert_roman("CDXI")
    411

    >>> convert_roman("CDIII")
    403

    >>> convert_roman("DV")
    505
"""

def convert_roman(roman):
    """Convert roman number to decimal number."""
    d_roman = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}

    number = 0
    roman_lst = list(roman)

    while len(roman_lst) > 1:
        number1 = d_roman[roman_lst.pop()]
        number2 = d_roman[roman_lst[-1]]

        if number2 >= number1:
            number += number1
        else:
            number += number1 - number2
            roman_lst.pop()

    if len(roman_lst) == 1:
        number += d_roman[roman_lst[0]]

    return number



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE!\n"