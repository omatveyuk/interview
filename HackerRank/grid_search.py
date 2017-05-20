"""The Grid Search.
   Given a 2D array of digits, try to find the occurrence of a given 2D pattern of digits. 

   Example:
   Array:           Pattern:        Result:
   1234567890       876543          True  
   0987654321       111111
   1111111111       111111
   1111111111  
   2222222222

   >>> arr = [[1,2,3,4,5,6,7,8,9,0], [0,9,8,7,6,5,4,3,2,1], [1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1], [2,2,2,2,2,2,2,2,2,2]]
   >>> pattern = [[8,7,6,5,4,3], [1,1,1,1,1,1], [1,1,1,1,1,1]]
   >>> grid_search(arr, pattern)
   True

   >>> pattern = []
   >>> grid_search(arr, pattern)
   False

   >>> pattern = [[8,7,6,5,4,3,2,2,2,2,2], [1,1,1,1,1,1,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1,1]]
   >>> grid_search(arr, pattern)
   False

   >>> pattern = [[8,7,6], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1]]
   >>> grid_search(arr, pattern)
   False

   >>> arr = []
   >>> grid_search(arr, pattern)
   False

   >>> arr = [[1,2,3,4,5,6], [5,6,7,8,9,0], [2,3,4,5,6,7], [1,9,4,7,2,9]]
   >>> pattern = [[2,3,4,5], [6,7,8,9], [3,4,5,6], [9,4,7,2]]
   >>> grid_search(arr, pattern)
   True


   >>> arr = [[1,2,3,4,5,6], [5,6,7,8,9,0], [2,3,4,5,6,7], [1,9,4,7,2,9]]
   >>> pattern = [[1,2,3,4], [5,6,7,8], [2,3,4,5], [1,9,4,7]]
   >>> grid_search(arr, pattern)
   True

   >>> arr = [[1,2,3,4,5,6], [5,6,7,8,9,0], [2,3,4,5,6,7], [1,9,4,7,2,9]]
   >>> pattern = [[3,4,5,6], [7,8,9,0], [4,5,6,7], [4,7,2,9]]
   >>> grid_search(arr, pattern)
   True

   >>> arr = [[2,3,4,5], [6,7,8,9], [3,4,5,6], [9,4,7,2]]
   >>> pattern = [[2,3,4,5], [6,7,8,9], [3,4,5,6], [9,4,7,2]]
   >>> grid_search(arr, pattern)
   True

   >>> arr = [[1,2,3,4,5,6], [5,6,7,8,9,0], [2,3,4,5,6,7], [1,9,4,7,2,9]]
   >>> pattern = [[1,2,3,4,5,6], [5,6,7,8,9,0]]
   >>> grid_search(arr, pattern)
   True

   >>> arr = [[1,2,3,4,5,6], [5,6,7,8,9,0], [2,3,4,5,6,7], [1,9,4,7,2,9]]
   >>> pattern = [[5,6,7,8,9,0], [2,3,4,5,6,7]]
   >>> grid_search(arr, pattern)
   True

   >>> arr = [[1,2,3,4,5,6], [5,6,7,8,9,0], [2,3,4,5,6,7], [1,9,4,7,2,9]]
   >>> pattern = [[2,3,4,5,6,7], [1,9,4,7,2,9]]
   >>> grid_search(arr, pattern)
   True
"""

def check_pattern(arr, pattern, row, col, height, width):
    for r in xrange(height):
        # print "CHECK row", r, "in array"
        # print "part of arr", arr[r][col:col+width]
        # print "pattern    ", pattern[r]
        if arr[row + r][col:col+width] != pattern[r]:
            # print "FALSE"
            return False
    return True



def grid_search(arr, pattern):
    if arr == [] or pattern == [] or len(arr[0]) < len(pattern[0]) or len(arr) < len(pattern):
        return False

    shift_right = len(pattern[0])
    shift_down = len(pattern)
    row = 0

    for row in xrange(len(arr)+1 - shift_down):
        col = 0
        # print "CURRENT row", row, "col", col
        for col in xrange(len(arr[0])+1 - shift_right):
            if check_pattern(arr, pattern, row, col, shift_down, shift_right):
                return True
            col +=1
        row +=1

    return False


if __name__ == "__main__":
    debug = True
    if debug:
        from doctest import testmod
        if testmod().failed == 0:
            print "********** All Tests are passed. *************"