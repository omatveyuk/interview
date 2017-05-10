""" Find sum of matrix elements.
    Input a rectangular matrix, each cell containing an integer. Some cells are 0. 
    That is why any cell that is 0 or is located anywhere below 0 in the same column
    is not considered to sum.

    Calculate the total price of all the cells that are suitable for condition.
    Example: 0 1 1 2      Suitable for condition: x 1 1 2
             0 5 0 0                              x 5 x x
             2 0 3 3                              x x x x

    >>> matrixElementsSum([[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]])
    9

    >>> matrixElementsSum([[1,1,1,0], [0,5,0,1], [2,1,3,10]])
    9

"""
def matrixElementsSum(matrix):
    total_sum = sum(matrix[0][j] for j in xrange(len(matrix[0])))
    unsuitable_columns = set([j for j in xrange(len(matrix[0])) if matrix[0][j] == 0])

    for row in xrange(1, len(matrix)):
        for column in xrange(len(matrix[0])):
            if column not in unsuitable_columns:
                if matrix[row-1][column] != 0:
                    total_sum += matrix[row][column]
                else:
                    unsuitable_columns.add(column)
    return total_sum



if __name__ == "__main__":
    debug = True
    if debug:
        from doctest import testmod
        if testmod().failed == 0:
            print "********** All Tests are passed. *************"
