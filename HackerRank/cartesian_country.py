""" Cartesian Country.
    Cartesian Country is a rectangular region of the xy-plane with corners at x1, y1
    and x2, y2. Each lattice point (i.e., point with integer  and  coordinates)
    in Cartesian Country denotes an island city surrounded by water.

    The country's Rulers live in the capital at coordinate xC, yC. Traveling between
    cities and the capital is a treacherous sea journey, so they decide to commission
    bridges satisfying all the following conditions:

    A bridge is a straight line with endpoints at two non-capital cities.
    The capital must be at the exact center (or midpoint) of the line.
    Two overlapping bridges are considered to be different if they connect different cities.

    Example:
    Coners at points (1,1) and (5,4). Capital - (2,3).
    Result:
    Max number of bridges: 4
    between (1,4) and (3,2)
    between (1,3) and (3,3)
    between (1,2) and (3,4)
    between (2,2) and (2,4)

    >>> getMaxBridges(1, 1, 5, 4, 2, 3)
    4

    >>> getMaxBridges(1, 1, 5, 4, 3, 2)
    7

    >>> getMaxBridges(1, 1, 5, 4, 3, 1)
    2

    >>> getMaxBridges(1, 1, 5, 4, 1, 3)
    1

    >>> getMaxBridges(1, 1, 5, 4, 1, 1)
    0

    >>> getMaxBridges(1, 1, 5, 4, 0, 1)
    0
"""

def getMaxBridges(x1, y1, x2, y2, xC, yC):

    # 1st solution
    # def checkCoordinates(x1, y1, x2, y2, xP, yP):
    #     if xP <= x2 and xP >= x1 and yP >= y1 and yP <= y2:
    #         return True
    #     return False

    # steps_rows = min(abs(xC-x1), abs(x2-xC))
    # steps_cols = min(abs(yC-y1), abs(y2-yC))
    # bridges = 0
    # for i in xrange(0,steps_rows+1):
    #     for j in xrange(0, steps_cols+1):
    #         if i == 0 and j == 0:
    #             continue
    #         if checkCoordinates(x1, y1, x2, y2, xC+i, yC+j) and checkCoordinates(x1, y1, x2, y2, xC-i, yC-j):    
    #             bridges += 1
    #         if i != 0 and j != 0:
    #             if checkCoordinates(x1, y1, x2, y2, xC+i, yC-j) and checkCoordinates(x1, y1, x2, y2, xC-i, yC+j):
    #                 bridges += 1
    
    # 2nd solution (improved)
    if xC <= x2 and xC >= x1 and yC >= y1 and yC <= y2:
        steps_rows = min(abs(xC-x1), abs(x2-xC))
        steps_cols = min(abs(yC-y1), abs(y2-yC))
        bridges = steps_rows + steps_cols + (steps_rows * steps_cols) * 2
    else:
        bridges = 0

    return bridges

if __name__ == "__main__":
    from doctest import testmod
    if testmod().failed == 0:
        print "********** All Tests are passed. *************"