"""Reverse linked list in place.

    >>> ll = LinkedList(Node(1, Node(2, Node(3))))
    >>> reverse_linked_list_in_place(ll)
    >>> ll.as_string()
    '321'

    >>> ll = LinkedList(Node(1))
    >>> reverse_linked_list_in_place(ll)
    >>> ll.as_string()
    '1'

    >>> ll = LinkedList(None)
    >>> reverse_linked_list_in_place(ll)
    >>> ll.as_string()
    ''

    >>> ll = LinkedList(Node(1, Node(2, Node(3, Node(25, Node(101))))))
    >>> reverse_linked_list_in_place(ll)
    >>> ll.as_string()
    '10125321'


"""

class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList(object):
    """Linked list."""

    def __init__(self, head=None):
        self.head = head

    def as_string(self):
        """Represent data for this list as a string.

        >>> LinkedList(Node(3)).as_string()
        '3'

        >>> LinkedList(Node(3, Node(2, Node(1)))).as_string()
        '321'
        """

        out = []
        n = self.head

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)

def reverse_linked_list_in_place(lst):
    """Given linked list, reverse the nodes in this linked list in place."""
    if lst.head is None or lst.head.next is None:
        return

    cur = lst.head.next
    lst.head.next = None

    while cur is not None:
        next = cur.next
        cur.next = lst.head
        lst.head = cur
        cur = next





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED ***\n"