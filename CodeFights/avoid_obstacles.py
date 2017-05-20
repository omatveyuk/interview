""" Avoid obstacles.
    Given an array of integers representing coordinates of obstacles situated on
    a straight line.
    Assume that you are jumping from the point with coordinate 0 to the right. 
    You are allowed only to make jumps of the same length represented by some integer.

    Find the minimal length of the jump enough to avoid all the obstacles.



    
    >>> avoidObstacles([5, 3, 6, 7, 9])
    4

    >>> avoidObstacles([2, 3])
    4

    >>> avoidObstacles([1, 4, 10, 6, 2])
    7

"""

def avoidObstacles(inputArray):
    max_elm = max(inputArray)
    
    for i in xrange(2, max_elm + 1):
        check = True
        for item in inputArray:
            if item % i == 0:
                check = False
                break
        if check:
            return i

    return max_elm + 1
            



if __name__ == "__main__":
    debug = True
    if debug:
        from doctest import testmod
        if testmod().failed == 0:
            print "********** All Tests are passed. *************"