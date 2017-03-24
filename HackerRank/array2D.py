""" Return max hourglass 
Given 2D array
Hourglass sum is the sum of an hourglass' values.
We define an hourglass in  to be a subset of values with indices falling in this 
pattern in 's graphical representation:

a b c
  d
e f g

Exampe 2D array:
1 2 3 0 0
0 0 1 0 0
1 1 1 1 1
0 3 0 4 5
1 1 0 0 0

Hourglasses:
123  230  300
 0    1    0
111  111  111

001  010  100
 1    1    1
030  304  045

111  111  111
 3    0    4
110  100  000

max_sum = 11

    >>> max_hourglass_2D_array(6, [[1,1,1,0,0,0], [0,1,0,0,0,0], [1,1,1,0,0,0], [0,9,2,-4,-4,0], [0,0,0,-2,0,0], [0,0,-1,-2,-4,0]])
    13

    >>> max_hourglass_2D_array(6, [[-1,-1,0,-9,-2,-2], [-2,-1,-6,-8,-2,-5], [-1,-1,-1,-2,-3,-4], [-1,-9,-2,-4,-4,-5], [-7,-3,-3,-2,-9,-9], [-1,-3,-1,-2,-4,-5]])
    -6

"""

def max_hourglass_2D_array(n, arr):
    # arr = []
    # for arr_i in xrange(n):
    #     arr_temp = map(int,raw_input().strip().split(' '))
    #     arr.append(arr_temp)
    max_hourglass = None
    for i in xrange(n-2):
        for j in xrange(n-2):
            sum_hourglass = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            sum_hourglass += arr[i+1][j+1]
            sum_hourglass += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if sum_hourglass > max_hourglass or sum_hourglass is None:
                max_hourglass = sum_hourglass
    print max_hourglass

if __name__ == "__main__":
    from doctest import testmod
    if testmod().failed == 0:
        print "All Tests are passed"