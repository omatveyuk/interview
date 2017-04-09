"""Paint board
    >>> board = Board(7, 5)
    >>> board.display()
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .

    >>> board.paint_cell(3,2,'*')
    >>> board.display()
    . . . . .
    . . . . .
    . . . . .
    . . * . .
    . . . . .
    . . . . .
    . . . . .

    >>> board.paint_cell(2,9,'*')
    The cell is out of range

    >>> board.paint_cell(9,2,'*')
    The cell is out of range

    >>> board.paint_all_board('*')
    >>> board.display()
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *

    >>> board.paint_all_board('.')
    >>> board.paint_cell(0,1,'*')
    >>> board.paint_cell(1,1,'*')
    >>> board.paint_cell(2,2,'*')
    >>> board.paint_cell(3,3,'*')
    >>> board.paint_cell(4,4,'*')
    >>> board.paint_cell(5,3,'*')
    >>> board.paint_cell(6,4,'*')
    >>> board.display()
    . * . . .
    . * . . .
    . . * . .
    . . . * .
    . . . . *
    . . . * .
    . . . . *

    >>> board.paint_from_border_to_border(6,1,'-')
    >>> board.display()
    - * . . .
    - * . . .
    - - * . .
    - - - * .
    - - - - *
    - - - * .
    - - - - *

    >>> board.paint_from_border_to_border(5,4,'K')
    >>> board.display()
    - * . . .
    - * . . .
    - - * . .
    - - - * .
    - - - - *
    - - - * K
    - - - - *

    >>> board.paint_from_border_to_border(25,44,'K')
    >>> board.display()
    - * . . .
    - * . . .
    - - * . .
    - - - * .
    - - - - *
    - - - * K
    - - - - *

    >>> board.paint_all_board('.')
    >>> board.paint_cell(0,1,'*')
    >>> board.paint_cell(1,1,'*')
    >>> board.paint_cell(2,2,'*')
    >>> board.paint_cell(3,3,'*')
    >>> board.display()
    . * . . .
    . * . . .
    . . * . .
    . . . * .
    . . . . .
    . . . . .
    . . . . .

    >>> board.paint_from_border_to_border(6,1,'-')
    >>> board.display()
    - * - - -
    - * - - -
    - - * - -
    - - - * -
    - - - - -
    - - - - -
    - - - - -

    >>> board.paint_all_board('.')
    >>> board.paint_cell(0,1,'*')
    >>> board.paint_cell(1,1,'*')
    >>> board.paint_cell(2,2,'*')
    >>> board.paint_cell(3,1,'*')
    >>> board.paint_cell(3,3,'*')
    >>> board.paint_cell(4,4,'*')
    >>> board.paint_cell(5,3,'*')
    >>> board.paint_cell(6,4,'*')
    >>> board.display()
    . * . . .
    . * . . .
    . . * . .
    . * . * .
    . . . . *
    . . . * .
    . . . . *

    >>> board.paint_from_border_to_border(6,1,'-')
    >>> board.display()
    - * . . .
    - * . . .
    - - * . .
    - * - * .
    - - - - *
    - - - * .
    - - - - *

    >>> board.paint_all_board('.')
    >>> board.paint_cell(0,1,'*')
    >>> board.paint_cell(1,1,'*')
    >>> board.paint_cell(2,2,'*')
    >>> board.paint_cell(3,3,'*')
    >>> board.paint_cell(4,4,'*')
    >>> board.paint_cell(5,3,'*')
    >>> board.paint_cell(6,4,'*')
    >>> board.paint_cell(3,1,'*')
    >>> board.paint_cell(4,0,'*')
    >>> board.paint_cell(5,1,'*')
    >>> board.paint_cell(6,2,'*')
    >>> board.display()
    . * . . .
    . * . . .
    . . * . .
    . * . * .
    * . . . *
    . * . * .
    . . * . *

    >>> board.paint_from_border_to_border(3,2,'-')
    >>> board.display()
    . * . . .
    . * . . .
    . . * . .
    . * - * .
    * - - - *
    . * - * .
    . . * . *

"""

class Cell(object):
    def __init__(self, h, w, color='.'):
        self.w = w
        self.h = h
        self.color = color

    def __repr__(self):
        return "Cell({0},{1}: {2})".format(self.h, self.w, self.color)

    def is_valid(self):
        return self.color == '.'



class Board(object):
    #stack = []
    stack = set([])
    def __init__(self, height, width):
        """Create and initialize board with dot"""
        self.width = width
        self.height = height
        self.board = [[Cell(h, w) for w in xrange(width)] for h in xrange(height)]

    def display(self):
        """Print board"""
        for h in xrange(self.height):
            for w in xrange(self.width):
                print self.board[h][w].color,
            print

    def get_cell(self, h, w):
        """Check if cell location inside board"""
        if (w >= 0 and w < self.width) and (h >= 0  and h < self.height):
            return self.board[h][w]
        else:
            return None    

    def paint_cell(self, h, w, color):
        """Color one cell.
            w has range from 0 to width-1    columns
            h has range from 0 to height-1   rows
        """
        cell = self.get_cell(h, w)
        if cell is None:
            print "The cell is out of range"
        else:
            cell.color = color

    def paint_all_board(self, color):
        """Color board"""
        for h in xrange(self.height):
            for w in xrange(self.width):
                self.board[h][w].color = color

    def get_west_north_east_south(self, cell):
        """Get cells aroud cell (west, north, ast, south)"""
        return [self.get_cell(cell.h, cell.w - 1), self.get_cell(cell.h + 1, cell.w), \
                self.get_cell(cell.h, cell.w + 1), self.get_cell(cell.h - 1, cell.w)]

    def paint_from_border_to_border(self, h, w, color):
        """Paint board from border to border"""
        # SOLUTION 1   inefficient
        # cell = self.get_cell(h, w)

        # if cell is not None and cell.is_valid():
        #     self.stack.append(cell)

        # while self.stack != []:
        #     cell = self.stack.pop()
        #     cell.color = color
        #     west_norh_east_south = self.get_west_north_east_south(cell) 
        #     self.stack.extend([cell for cell in west_norh_east_south if cell is not None and cell.is_valid()])
        
        # SOLUTION 2
        cell = self.get_cell(h, w)

        if cell is not None and cell.is_valid():
            self.stack.add(cell)

        while len(self.stack) > 0:
            cell = self.stack.pop()
            cell.color = color
            west_norh_east_south = self.get_west_north_east_south(cell) 
            for cell in west_norh_east_south:
                if cell is not None and cell.is_valid():
                    self.stack.add(cell)

    
        



if __name__ == '__main__':
    import doctest
#    stack = []
    print
    if doctest.testmod().failed == 0:
        print "\t*** ALL TESTS PASSED; GOOD WORK! ***"
    print

