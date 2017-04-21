"""Sort stack.
    Sort the stack such that the smallest items are on the top.
    Use additional temporary stack (not the other data structures)
    Stack Methods:
    pop()
    push()
    peek()
    is_Empty()

    >>> my_stack = Stack()
    >>> my_stack.isEmpty()
    True
    >>> my_stack.push(2)
    >>> my_stack.push(1)
    >>> my_stack.push(5)
    >>> my_stack.push(3)
    >>> my_stack.display()
    2 1 5 3
    >>> sort_stack(my_stack).display()
    5 3 2 1

    >>> my_stack = Stack()
    >>> my_stack.isEmpty()
    True
    >>> my_stack.push(1)
    >>> my_stack.push(23)
    >>> my_stack.push(5)
    >>> my_stack.push(3)
    >>> my_stack.display()
    1 23 5 3
    >>> sort_stack(my_stack).display()
    23 5 3 1

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

def sort_stack(stack):
    """Sort the stack such that the smallest items are on the top.
        Use additional temporary stack (not the other data structures).
    """
    temp_stack = Stack()
    # get top value from the stack and add it in temporary stack
    temp_stack.push(stack.pop())

    # loop through stack
    while not stack.isEmpty():
        # if value in stack greater than top value in temporary stack
        # remove value from stack to the temporary stack
        if stack.peek() > temp_stack.peek():
            temp_stack.push(stack.pop())

        else:
            # if value in stack less than top value in temporary stack
            # remove value from stack 
            temp_value = stack.pop()
            # loop through temporary stack until found value less or empty temporary stack 
            # and remove all value in temporary stack which greater than temp_value to stack 
            while temp_value < temp_stack.peek() and not temp_stack.isEmpty():
                stack.push(temp_stack.pop())
            # add temp_value to temporary stack
            temp_stack.push(temp_value)

    # for Sorting the stack such that the smallest items are on the top
    # remove all elements from temp_stack to stack
    while not temp_stack.isEmpty():
        stack.push(temp_stack.pop())

    return stack



if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED.  IT WORKS SUCCESSFULLY! ***\n"