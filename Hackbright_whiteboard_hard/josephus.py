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
class Node(object):
    """Class Node"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return "<Node data={0}>".format(self.data)

class Circle_ll(object):
    """Class Circle Linked Linked"""
    def __init__(self):
        self.head = None

    def insert(self, node):
        if self.head == None:
            self.head = node
            node.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr=curr.next
            node.next = curr.next
            curr.next = node

    def remove(self, data):
        # data is in head and circle linked list has only 1 node.
        # Remove head. Empty circle linked list"
        if self.head.data == data and self.head.next == self.head:
            self.head = None
            return

        curr = self.head
        # data is in head. Remove node which is head, move head to the next node
        if self.head.data == data:
            new_head = self.head.next
            while curr.next != self.head:
                curr = curr.next
            self.head = new_head
            curr.next = self.head
        else:
        # data is in inner node. Remove this node
            while curr.data != data:
                prev = curr
                curr = curr.next
            prev.next = curr.next

    def display(self):
        if self.head == None:
            print "Empty circle linked llst"
        else:
            curr = self.head
            while curr.next != self.head:
                print curr.data,
                curr = curr.next
            print curr.data
            print curr.next.data, '...'

def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor."""

    # Create circle linked list with size = num.people
    my_circle_ll = Circle_ll()
    for i in xrange(num_people):
        my_circle_ll.insert(Node(i+1))

    # Remove each kill_every node until circle linked list will have 1 node
    curr = my_circle_ll.head
    while curr != curr.next:
        for i in xrange(kill_every - 1):
            # If we will every 3rd person, we'll skip over two
            curr = curr.next
        my_circle_ll.remove(curr.data)
        curr = curr.next

    return my_circle_ll.head.data

# Solution Hackbright
# class Node(object):
#     """Doubly-linked node."""

#     def __init__(self, data, prev=None, next=None):
#         self.data = data
#         self.prev = prev
#         self.next = next

#     def __repr__(self):
#         return "<Node prev=%s data=%s next=%s>" % (
#             self.prev.data, self.data, self.next.data)

#     @classmethod
#     def make_list(cls, n):
#         """Construct a circular doubly-linked list of n items. Returns head node.

#             >>> node = Node.make_list(3)

#             >>> node.data
#             1

#             >>> node.next.data
#             2

#             >>> node.next.next.next.data
#             1

#             >>> node.prev.data
#             3

#             >>> node.prev.prev.prev.data
#             1
#         """

#         # Make the first node (and remember that it's the first)
#         first = node = prev = cls(1)

#         # Make every other node
#         for i in range(2, n + 1):
#             node = Node(i, prev=prev)
#             prev.next = node
#             prev = node

#         # Fix the last and first node's prev/next
#         node.next = first
#         first.prev = node

#         return first

# def find_survivor(num_people, kill_every):
#     """Given num_people in circle, kill [kill_every]th person, return survivor."""
#     node = Node.make_list(num_people)

#     # Loop until we're the only item in the list (last survivor)
#     while node.next != node:

#         for i in range(kill_every - 1):
#             # If we will every 3rd person, we'll skip over two
#             node = node.next

#         # We're on the node to kill. Remove it from our doubly-linked list
#         node.prev.next = node.next
#         node.next.prev = node.prev

#         node = node.next

#     return node.data
       


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T! ***\n"
