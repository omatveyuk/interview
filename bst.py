""" Binary Search Tree.

                15
           10         27
         7   13    25    38


    >>> t = Node(15,
    ...       Node(10, Node(7), Node(13)),
    ...       Node(27, Node(25), Node(38))
    ... )

    Adding 0, 14, 40, 26, 23  :

                15
           10          27
         7   13     25    38
       0       14 23  26    40

    >>> t.insert(0)
    >>> t.insert(14)
    >>> t.insert(40)
    >>> t.insert(26)
    >>> t.insert(23)
    >>> t.left.left.left.data == 0
    True

    Adding 4, 10:

                15
           10          27
         7   13     25    38
       0   10  14 23  26    40
         4


    >>> t.insert(4)
    >>> t.insert(10)

    >>> t.left.left.left.data == 0
    True
    >>> t.left.left.left.right.data == 4
    True
    >>> t.left.right.left.data == 10
    True
    >>> t.left.left.right is None
    True
    >>> t.left.right.right.data == 14
    True
    >>> t.right.left.left.data == 23
    True
    >>> t.right.left.right.data == 26
    True
    
    >>> t.data == 15
    True
    >>> t.right.data == 27
    True
    >>> t.right.right.data == 38
    True
    >>> t.right.right.right.data == 40
    True
    >>> t.right.right.left is None
    True

    >>> t.find_node(89) is None
    True
    >>> t.find_node(4)
    <Node 4; left: None; right: None>

    >>> t.delete(4)
    >>> t.find_node(4) is None
    True
    >>> t.left.left.left.right is None
    True



    


"""
class Node(object):
    def __init__(self, data, left=None, right=None):
        """Create Binary Search Tree as Node with data and left/right optional"""
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        if self is None:
            return self
        elif self.left is None and self.right is None:
            return "<Node {0}; left: {1}; right: {2}>".format(self.data, self.left, self.right)
        elif self.left is None:
            return "<Node {0}; left: {1}; right: {2}>".format(self.data, self.left, self.right.data)
        elif self.right is None:
            return "<Node {0}; left: {1}; right: {2}>".format(self.data, self.left.data, self.right)
        else:
            return "<Node {0}; left: {1}; right: {2}>".format(self.data, self.left.data, self.right.data)

    def insert(self, data):
        """Insert new data in Binary Search Tree."""

        if data >= self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)


    def find_node(self, data):
        """Return Node or None"""
        # Found node
        if data == self.data:
            return self

        # Go to the right subtree
        if data > self.data:
            if self.right is None:
                # The data doesn't exist in BST
                return None
            else:
                return self.right.find_node(data)

        # Go to the left subtree    
        else:
            if self.left is None:
                # The data doesn't exist in BST
                return None
            else:
                return self.left.find_node(data)




    def delete(self, data):
        """ Delete Node from BST.
        Three casses:
        node is a leaf
        node has one child
        node has two children

        """
        # Find node
        node = self.find_node(data)
        print id(node)
        print id(self.find_node(data))
        print node

        #Case 1: node is a leaf
        if node.left == node.right == None:
            node = None
            print node
            self.find_node(data) = None
            print self.find_node(data)






if __name__ == "__main__":
    import doctest
    
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED.  BST WORKS SUCCESSFULLY! ***\n"