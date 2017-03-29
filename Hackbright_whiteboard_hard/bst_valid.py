"""Is this binary search tree a valid BST?

A valid binary search tree follows a specific rule. In our case,
the rule is "left child must value must be less-than parent-value"
and "right child must be greater-than-parent value".

This rule is recursive, so *everything* left of a parent
must less than that parent (even grandchildren or deeper)
and everything right of a parent must be greater than.

For example, this tree is valid::

        4
     2     6
    1 3   5 7

Let's create this tree and test that::

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.is_valid()
    True

This tree isn't valid, as the left-hand 3 is wrong (it's less
than 2)::

        4
     2     6
    3 3   5 7

Let's make sure that gets caught::

    >>> t = Node(4,
    ...       Node(2, Node(3), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.is_valid()
    False

This tree is invalid, as the bottom-right 1 is wrong --- it is
less than its parent, 6, but it's also less than its grandparent,
4, and therefore should be left of 4::

        4
     2     6
    1 3   1 7

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(1), Node(7))
    ... )

    >>> t.is_valid()
    False

                17
         10           25
      5      13    20    30
    3   6  11    18  22    40
   1 4

    >>> t = Node(17,
    ...       Node(10,
    ...         Node(5,
    ...           Node(3, Node(1), Node(4)),
    ...           Node(6)),
    ...         Node(13, Node(11))
    ...       ),
    ...       Node(25,
    ...         Node(20, Node(18), Node(22)),
    ...         Node(30, Node(None), Node(40))
    ...       )
    ...         )
    >>> t.is_valid()
    True

                    17
         10           25
      5      13    20    30
    3   6  11    18  22    40
   1 4   21

    >>> t = Node(17,
    ...       Node(10,
    ...         Node(5,
    ...           Node(3, Node(1), Node(4)),
    ...           Node(6, Node(None), Node(21))),
    ...         Node(13, Node(11))
    ...       ),
    ...       Node(25,
    ...         Node(20, Node(18), Node(22)),
    ...         Node(30, Node(None), Node(40))
    ...       )
    ...         )
    >>> t.is_valid()
    False

"""


class Node:
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def is_valid(self):
        """Is this tree a valid BST?"""
        def is_valid_subtree(node):

            # base case
            if node is None:
                return True

            # if parent does not have Left child
            if node.left is None:
                left = True

            # if Left child exists check also grand children of Left child and
            # call recursievly is_valid for each granchild
            elif node.left.data < node.data:
                left = ((node.left.left is None) or \
                        (node.left.left.data < node.left.data and node.left.left.data < node.data)) and \
                       ((node.left.right is None) or \
                        (node.left.right.data > node.left.data and node.left.right.data < node.data)) and \
                       is_valid_subtree(node.left.left) and is_valid_subtree(node.left.right)

            # if Left child is greater than parent
            else:
                left = False

            # if parent does not have Right child
            if node.right is None:
                right = True

            # if Right child exists check also grand children of Right child and
            # call recursievly is_valid for each granchild
            elif node.right.data > node.data:
                right = ((node.right.left is None) or \
                         (node.right.left.data < node.right.data and node.right.left.data > node.data)) and \
                        ((node.right.right is None) or \
                         (node.right.right.data > node.right.data and node.right.right.data > node.data)) and \
                        is_valid_subtree(node.right.left) and is_valid_subtree(node.right.right)

            # if Right child is less than parent
            else:
                right = False

            return left and right

        return is_valid_subtree(self)


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; THAT'S VALID!\n"
