"""An array of integers tight if every pair of adjacent integers
   in the array has <=1 an absolute difference . 

   Given a, b, and c, complete the function below by returning the length of the 
   shortest tight array such that the first element is a, the last element is c,
   and the array contains b.

   >>> tight_arrays(5, 7, 11)
   7

   >>> tight_arrays(3, 1, 2)
   4

   >>> tight_arrays(5, 5, 6)
   2

   >>> tight_arrays(1, 100, 1)
   199
"""

def tight_arrays(start, middle, finish):
    result_length = abs(middle - start)          

    result_length += abs(middle - finish) + 1
    return result_length
    
if __name__ == "__main__":
    debug = True
    if debug:
        from doctest import testmod
        if testmod().failed == 0:
            print "********** All Tests are passed. *************"


