""" Binary Search Tree.

                15
           10         27
         7   13    25    38


    >>> t = BinarySearchTree(Node(15,
    ...       Node(10, Node(7), Node(13)),
    ...       Node(27, Node(25), Node(38))
    ... ))

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
    >>> t.root.left.left.left.data == 0
    True

    Adding 4, 10:

                  15
            10           27
         7     13     25    38
       0     10  14 23  26    40
         4


    >>> t.insert(4)
    >>> t.insert(10)

    >>> t.root.left.left.left.data == 0
    True
    >>> t.root.left.left.left.right.data == 4
    True
    >>> t.root.left.right.left.data == 10
    True
    >>> t.root.left.left.right is None
    True
    >>> t.root.left.right.right.data == 14
    True
    >>> t.root.right.left.left.data == 23
    True
    >>> t.root.right.left.right.data == 26
    True

    >>> t.root.data == 15
    True
    >>> t.root.right.data == 27
    True
    >>> t.root.right.right.data == 38
    True
    >>> t.root.right.right.right.data == 40
    True
    >>> t.root.right.right.left is None
    True

    >>> t.find(89)
    False
    >>> t.find(4)
    True

    >>> t.getHeight()
    5

    >>> t.inOrder()
    0 4 7 10 10 13 14 15 23 25 26 27 38 40

    >>> t.postOrder()
    4 0 7 10 14 13 10 23 26 25 40 38 27 15

    >>> t.preOrder()
    15 10 7 0 4 13 10 14 27 25 23 26 38 40

    >>> t.levelOrder()
    15 10 27 7 13 25 38 0 10 14 23 26 40 4

    >>> t.delete(40)
    >>> t.find(40)
    False
    >>> t.root.right.right.right
    >>> t.root.right.right.right is None
    True

"""
# Linked List Implementation
class NodeLL(object):
    """Class Node"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class QueueLL(object):
    """ Implementation Queue with using linked list list. """

    def __init__(self):
        self.head = self.tail = None

    def dequeue(self):
        """Remove the top element from the queue."""
        if self.head is not None:
            top = self.head
            self.head = self.head.next
            # if it was dequeueped last item from the queue
            if self.head is None:
                self.tail = None
            return top.data

    def enqueue(self, item):
        """Add a new item to the top of the queue."""
        # Add first item to the queue
        if self.head is None:
            self.head = self.tail = NodeLL(item)
        else:
            self.tail.next = NodeLL(item)
            self.tail = self.tail.next

    def peek(self):
        """Return the top of the queue."""
        if self.head is not None:
            return self.head.data

    def isEmpty(self):
        """Return true if the queue is empty."""
        return self.head is None and self.tail is None

# Binary Search Tree Implementation
class Node(object):
    def __init__(self, data, left=None, right=None):
        """Binary Search tree Node with data and left/right optional"""
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
        """Insert data to Node as a Left or Right child"""
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

    def find(self, data):
        """Return True is Node is found or False"""
        # Found node
        if data == self.data:
            print "FIND NODE", self
            print id(self)
            return True

        # Go to the right subtree
        if data > self.data:
            print "{0} > {1} Go to the right subtree".format(data, self.data)
            if self.right:
                return self.right.find(data)
            # The data doesn't exist in BST
            print "DON'T FIND NODE"
            return False

        # Go to the left subtree
        else:
            if self.left:
                print "{0} < {1} Go to the left subtree".format(data, self.data)
                return self.left.find(data)
            # The data doesn't exist in BST
            print "DON'T FIND NODE"

            return False

    def getHeight(self):
        """Return height of the Binary Search Tree"""
        return 1 + max(self.left.getHeight() if self.left is not None else 0,\
                       self.right.getHeight() if self.right is not None else 0)

    # Traversal Tree
    def inOrder(self):
        """InOrder Traversel Tree.
        (from smallest value to the biggest)
        An inorder traversal of tree  is a recursive algorithm that follows
        the left subtree; once there are no more left subtrees to process,
        we process the right subtree. The elements are processed in left-root-right order.
        """
        if self:
            if self.left:
                self.left.inOrder()
            print self.data,
            if self.right:
                self.right.inOrder()

    def postOrder(self):
        """PostOrder Traversal Tree.
        A postorder traversal of tree  is a recursive algorithm that follows
        the left and right subtrees before processing the root element.
        The elements are processed in left-right-root order.
        """
        if self:
            if self.left:
                self.left.postOrder()
            if self.right:
                self.right.postOrder()
            print self.data,

    def preOrder(self):
        """ProOrder Traversal Tree. (Deep First Search DFS)
        A preorder traversal goes as deeply to the left as possible
        A preorder traversal of tree  is a recursive algorithm that processes
        the root and then performs preorder traversals of the left and right subtrees.
        The elements are processed root-left-right order.

        """
        if self:
            print self.data,
            if self.left:
                self.left.preOrder()
            if self.right:
                self.right.preOrder()

    def levelOrder(self):
        """Level-Order Traversal. Breadth-First-Search (BFS).
        A level-order traversal of tree  is a recursive algorithm that processes
        the root, followed by the children of the root (from left to right),
        followed by the grandchildren of the root (from left to right), etc.
        Uses a queue of references to binary trees to keep track of the subtrees at each level.
        """
        if self:
            queue = QueueLL()
            queue.enqueue(self)

            while not queue.isEmpty():
                queueNode = queue.dequeue()
                print queueNode.data,

                if queueNode.left:
                    queue.enqueue(queueNode.left)
                if queueNode.right:
                    queue.enqueue(queueNode.right)

    def delete(self, data):
        """Delete Node with data from the Binary Search Tree."""
        if self:
            if data < self.data:
                print "{0} < {1} Go to the left subtree".format(data, self.data)
                self.left.delete(data)
            elif data > self.data:
                print "{0} > {1} Go to the right subtree".format(data, self.data)
                self.right.delete(data)
            else:
                print "{0} == {1} FIND Node".format(data, self.data)
                print "ID NODE", id(self)
                # Node to be deleted is leaf. Simply remove Node
                if self.left is None and self.right is None:
                    print "Node is leaf.", self
                    print id(self), self
                    del(self)
                    # self = None
                    # print id(self), self

                # Node to be deleted has one child. Copy child to the Node and delete child
                elif self.left is None:
                    print "Node has only right child {0}".format(self.right) 
                    self = self.right
                elif self.right is None:
                    print "Node has only left child {0}".format(self.left) 
                    self = self.left

                # Node to be deleted has two children.
                # Find inorder successor of the node (smallest in the right subtree).
                # (for another solution you can use preorder succesor (biggest in the left subtree))
                else:
                    print "Node has two children {0}, {1}".format(self.left, self.right)
                    print "Find the leftmost leaf in the right subtree" 
                    current = self.right
                    # loop down to find the leftmost leaf (smallest in the right subtree)
                    while(current.left is not None):
                        current = current.left 
                    print current.data
                    # Copy the inorder successor's content to node which will be deleted
                    print "deleted node: ", self
                    self.data = current.data
                    print "After delete", self
                    # Delete the inorder successor
                    current = None
 


class BinarySearchTree(object):
    """Class Binary Search Tree"""
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        """Insert new data in Binary Search Tree."""
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.insert(data)

    def find(self, data):
        """Find Node in Binary Search Tree"""
        if self.root:
            return self.root.find(data)
        return False

    def getHeight(self):
        """Height of Binary Search Tree"""
        if self.root:
            return self.root.getHeight()
        return 0

    def inOrder(self):
        """ InOrder Traversal Tree.
            An inorder traversal of a binary search tree will process the tree's
            elements in ascending order. Left-Root-Right order.
        """
        if self.root:
            return self.root.inOrder()

    def postOrder(self):
        """ PostOrder Traversal Tree. Left-Right-Root order"""
        if self.root:
            return self.root.postOrder()

    def preOrder(self):
        """ PreOrder Traversal Tree. Root-Left_Right order.
            Deep First Search (DFS)"""
        if self.root:
            return self.root.preOrder()

    def levelOrder(self):
        """ LevelOrder Traversal Tree. Level-by-Level.
            Breadth-First-Search (BFS)."""
        if self.root:
            return self.root.levelOrder()

    def delete(self, data):
        """Delete data from Binary Search Tree"""
        if self.root:
            return self.root.delete(data)
        else:
            return "Data does not exist in Binary Tree"



if __name__ == "__main__":
    import doctest
    
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED.  BST WORKS SUCCESSFULLY! ***\n"