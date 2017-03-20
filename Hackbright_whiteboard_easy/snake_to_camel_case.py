"""Given a variable name in snake_case, return camelCase of name.

For example::

    >>> snake_to_camel("hi_balloonicorn")
    'hiBalloonicorn'

"""


def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name."""
    lst_variable_name = variable_name.split('_')
    camel_case_name = lst_variable_name[0]
    for i in xrange(1, len(lst_variable_name)):
        camel_case_name += lst_variable_name[i].capitalize()
    return camel_case_name


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"
