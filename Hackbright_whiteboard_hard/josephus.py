"""Given num_item in circle, erase [_every]th person, return survivor.
Imagine a group of 10 in a circle, numbered 1 to 10. 
If we started at the first item (#1) and erased every three item 
This continues, though, looping around again, starting with where we left of at #10.
etc.

1 2 3 4 5 6 7 8 9 10
    x     x     x !

1 2 3 4 5 6 7 8 9 10
  x x     x x ! x  

1 2 3 4 5 6 7 8 9 10
x x x     x x x x ! 

1 2 3 4 5 6 7 8 9 10
x x x   x x x x x !

1 2 3 4 5 6 7 8 9 10
x x x   x x x x x x

    >>> find_survivor(4, 2)
    1

    >>> find_survivor(41, 3)
    31

As a sanity case, if never skip anyone, the last person will be our survivor:

    >>> find_survivor(10, 1)
    10

"""
# class Node(obj):
#     """Class Node"""
#     def __init__

# class circle_ll(obj):
#     """Class Circle Linked Linked"""
#     def __init__(self, node=None):
#         head = node

def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor."""
    lst = [i for i in xrange(1, num_people+1)]
    print lst
    curr = -1
    count = 0
    while count <= num_people-1:
        curr += kill_every
        print "curr: ", curr
        if curr >= num_people:
            curr = curr - num_people + 1
        print "curr: ", curr 
        if lst[curr] != 0:
            lst[curr] = 0
            count += 1
        print "count: ", count
    for i in xrange(num_people):
        if lst[i] != 0:
            return lst[i]


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T! ***\n"
