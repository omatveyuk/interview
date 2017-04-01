"""Given two strings. Find longest common substring.
   For solution is used a matrix.
        0 1 2 3 4 5 6 7 8 6 10
        a b c h e l l o a b c
    0 x 0 0 0 0 0 0 0 0 0 0 0
    1 y 0 0 0 0 0 0 0 0 0 0 0
    2 z 0 0 0 0 0 0 0 0 0 0 0
    3 h 0 0 0 1 0 0 0 0 0 0 0
    4 e 0 0 0 0 2 0 0 0 0 0 0
    5 l 0 0 0 0 0 3 0 0 0 0 0
    6 l 0 0 0 0 0 0 4 0 0 0 0
    7 o 0 0 0 0 0 0 0 5 0 0 0       max lentgh = 5, max index = 7
    8 o 0 0 0 0 0 0 0 0 0 0 0
    9 p 0 0 0 0 0 0 0 0 0 0 0
    10u 0 0 0 0 0 0 0 0 0 0 0

    Add border around matrix:
         0 1 2 3 4 5 6 7 8 6 101112
           a b c h e l l o a b c f
    0    0 0 0 0 0 0 0 0 0 0 0 0 0    
    1  x 0 0 0 0 0 0 0 0 0 0 0 0 0
    2  y 0 0 0 0 0 0 0 0 0 0 0 0 0
    3  z 0 0 0 0 0 0 0 0 0 0 0 0 0
    4  h 0 0 0 0 1 0 0 0 0 0 0 0 0
    5  e 0 0 0 0 0 2 0 0 0 0 0 0 0
    6  l 0 0 0 0 0 0 3 0 0 0 0 0 0
    7  l 0 0 0 0 0 0 0 4 0 0 0 0 0
    8  o 0 0 0 0 0 0 0 0 5 0 0 0 0    max lentgh = 5, max index = 7
    9  o 0 0 0 0 0 0 0 0 0 0 0 0 0
    10 p 0 0 0 0 0 0 0 0 0 0 0 0 0
    11 u 0 0 0 0 0 0 0 0 0 0 0 0 0
    12   0 0 0 0 0 0 0 0 0 0 0 0 0

    >>> lcs("abshelloabc", "xyzhelloopuopuppuh")
    'hello'

    >>> lcs("helloabsfdg", "xyzhelloopu")
    'hello'

    >>> lcs("helloabsfdg", "xyzklshello")
    'hello'

    >>> lcs("asdfnabrfds", "xyzklkhello")

    >>> lcs("kabckk", "abc")
    'abc'

    >>> lcs("ddabc", "kabckkkkkkkkkkkkk")
    'abc'
"""

def lcs(str1, str2):
    """ Longest common substring"""
    # SOLUTION 1
    # # initialize matrix with border by 0
    # # matrix[ixj]: i - length str2(rows); j - length str1(columns)
    # matrix = [[0 for i in xrange(len(str2)+2)] for j in xrange(len(str1)+2)]
    # max_length = 0
    # max_index = None

    # # fill matrix. if char exists in str1 on position j and in str2 on position i
    # # change value matrix[i+1,j+1] (increase index by 1 because we have borders)
    # # matrix[i+1, j+1] = matrix[i,j] + 1 
    # for i in xrange(len(str1)):
    #     for j in xrange(len(str2)):
    #         if str1[i] == str2[j]:
    #             matrix[i+1][j+1] = matrix[i][j] + 1
    #             if matrix[i+1][j+1] > max_length:
    #                 max_length = matrix[i+1][j+1]
    #                 max_index = i           # index in str1

    # if max_index is not None:
    #     return str1[max_index-max_length+1:max_index+1]
    # else:
    #     return None

    # SOLUTION 2
    # don't initialize all matrix
    # use the same rules, but look only on two rows
    max_length = 0
    max_index = None
    prev_row = [0 for i in xrange(len(str1) + 2)]
    curr_row = [0 for i in xrange(len(str1) + 2)]

    for j in xrange(len(str2)):
        for i in xrange(len(str1)):
            if str1[i] == str2[j]:
                curr_row[i+1] = prev_row[i] + 1
                if curr_row[i+1] > max_length:
                    max_length = curr_row[i+1]
                    max_index = i
        prev_row = curr_row
        curr_row = [0 for i in xrange(len(str1) + 2)]

    if max_index is not None:
        return str1[max_index-max_length+1:max_index+1]
    else:
        return None        



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE!\n"