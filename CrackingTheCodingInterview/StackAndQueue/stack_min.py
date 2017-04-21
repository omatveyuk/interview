"""Implementation Stack with Min.
    A stack uses LIFO (last in first out) ordering
    Operations:
        pop():              Remove the top item from the stack O(1)
        push(item):         Add a new value to the top of the stack O(1)
        peek():             Return the top of the stack
        isEmpty():          Return true if the stack is empty
        min_stack():        Returm min value in stack O(1)

    >>> my_stack = StackMin()
    >>> my_stack.isEmpty()
    True
    >>> my_stack.push(2)
    >>> my_stack.display()
    2
    >>> my_stack.push(5)
    >>> my_stack.push(1)
    >>> my_stack.push(3)
    >>> my_stack.display()
    2 5 1 3
    >>> my_stack.min_stack()
    1
    >>> my_stack.peek()
    3
    >>> my_stack.display()
    2 5 1 3
    >>> my_stack.pop()
    3
    >>> my_stack.pop()
    1
    >>> my_stack.display()
    2 5
    >>> my_stack.isEmpty()
    False
    >>> my_stack.min_stack()
    2


"""
class Node(object):
    """Class Node"""
    def __init__(self, data, min_value=None):
        self.data = data
        self.min_value = min_value

    def __repr__(self):
        return "<Node: {0}, min: {1}>".format(self.data, self.min_value)

class StackMin(object):
    """ Implementation Stack with using simple list and saving min. """

    def __init__(self):
        self.stack = []

    def display(self):
        """Display stack,"""
        for item in self.stack:
            print item.data,

    def pop(self):
        """Remove the top element from the stack."""
        if self.stack != []:
            return self.stack.pop().data
        return None

    def push(self, data):
        """Add a new item to the top of the stack."""
        cur_min = data
        if self.stack != [] and self.stack[-1].min_value < cur_min:
            cur_min = self.stack[-1].min_value
        self.stack.append(Node(data, cur_min))

    def peek(self):
        """Return the top of the stack."""
        if self.stack != []:
            return self.stack[-1].data
        return None

    def isEmpty(self):
        """Return true if the stack is empty."""
        return self.stack == []

    def min_stack(self):
        """Return min value in stack"""
        if self.stack != []:
            return self.stack[-1].min_value
        return None

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED.  IT WORKS SUCCESSFULLY! ***\n"