"""Given two strings. Find longest common substring.
   For solution is used a matrix.
        0 1 2 3 4 5 6 7 8 6 1011
        a b c h e l l o a b c f
    0 x 0 0 0 0 0 0 0 0 0 0 0 0
    1 y 0 0 0 0 0 0 0 0 0 0 0 0
    2 z 0 0 0 0 0 0 0 0 0 0 0 0
    3 h 0 0 0 1 0 0 0 0 0 0 0 0
    4 e 0 0 0 0 2 0 0 0 0 0 0 0
    5 l 0 0 0 0 0 3 0 0 0 0 0 0
    6 l 0 0 0 0 0 0 4 0 0 0 0 0
    7 o 0 0 0 0 0 0 0 5 0 0 0 0      max lentgh = 5, max index = 
    8 o 0 0 0 0 0 0 0 0 0 0 0 0
    9 p 0 0 0 0 0 0 0 0 0 0 0 0
    10u 0 0 0 0 0 0 0 0 0 0 0 0


    >>> lcs("abshelloabcf", "xyzhellolopu")
    'hello'
"""

def lcs(str1, str2):
    """ Longest common substring"""
    # initialize
    matrix = [[0 for i in xrange(len(str1))] for j in xrange(len(str2))]
    max_length = 0 
    max_index = 0

    for i in xrange(len(str1)):
        matrix.append([])
        for j in xrange(len(str2)):
            if str1[i] != str2[j]:
                matrix[i][j] = 0
            else:
                matrix[i][j] = matrix[i-1][j-1] + 1
                if matrix[i][j] > max_length:
                    max_length = matrix[i][j]
                    max_index = i 

    return str1[max_index-max_length+1:max_index+1]


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE SORTING!\n"