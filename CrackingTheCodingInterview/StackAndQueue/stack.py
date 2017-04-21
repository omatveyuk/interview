"""Implementation Stack.
    A stack uses LIFO (last in first out) ordering
    Operations:
        pop():              Remove the top item from the stack O(1)
        push(item):         Add a new item to the top of the stack O(1)
        peek():             Return the top of the stack
        isEmpty():          Return true if the stack is empty

    >>> my_stack = Stack()
    >>> my_stack.isEmpty()
    True
    >>> my_stack.push(2)
    >>> my_stack.display()
    2
    >>> my_stack.push(1)
    >>> my_stack.push(5)
    >>> my_stack.push(3)
    >>> my_stack.display()
    2 1 5 3
    >>> my_stack.peek()
    3
    >>> my_stack.display()
    2 1 5 3
    >>> my_stack.pop()
    3
    >>> my_stack.display()
    2 1 5
    >>> my_stack.isEmpty()
    False

"""

class Stack(object):
    """ Implementation Stack with using simple list. """

    def __init__(self):
        self.stack = []

    def display(self):
        """Display stack,"""
        for item in self.stack:
            print item,

    def pop(self):
        """Remove the top element from the sctack."""
        if self.stack != []:
            return self.stack.pop()

    def push(self, item):
        """Add a new item to the top of the stack."""
        self.stack.append(item)

    def peek(self):
        """Return the top of the stack."""
        if self.stack != []:
            return self.stack[-1]

    def isEmpty(self):
        """Return true if the stack is empty."""
        return self.stack == []

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED.  IT WORKS SUCCESSFULLY! ***\n"