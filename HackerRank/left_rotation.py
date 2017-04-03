"""Left Rotation.
Given an array of n integers and a number d perform  left rotations on the array.
d <= n
Then print the updated array as a single line of space-separated integers.

>>> left_rotation([1, 2, 3, 4, 5], 4)
5 1 2 3 4

>>> left_rotation([1, 2, 3, 4, 5, 6], 1)
2 3 4 5 6 1

>>> left_rotation([1, 2, 3], 0)
1 2 3

>>> left_rotation([1, 2, 3], 3)
1 2 3

"""

def left_rotation(arr, d):
    """Left rotation"""
    for i in xrange(d/2):
        arr[i], arr[d-1-i] = arr[d-1-i], arr[i]
    
    for i in xrange((len(arr)-d)/2):
        arr[d+i], arr[-i-1] = arr[-i-1], arr[d+i]
    
    arr.reverse()
    for item in arr:
        print item, 


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T! ***\n"