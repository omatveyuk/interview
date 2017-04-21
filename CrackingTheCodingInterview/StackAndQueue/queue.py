"""Implementation Queue.
    A queue uses FIFO (first in first out) ordering
    Operations:
        dequeue():          Remove the first item from the Queue  (for list: O(n), for linked list: O(1) )
        enqueue(item):      Add a new item to the end of the Queue  O(1)
        peek():             Return the top of the Queue (first item)
        isEmpty():          Return true if the Queue is empty

Test Queue implemetation with list
    >>> my_queue = Queue()
    >>> my_queue.isEmpty()
    True
    >>> my_queue.enqueue(2)
    >>> my_queue.display()
    2
    >>> my_queue.enqueue(1)
    >>> my_queue.enqueue(5)
    >>> my_queue.enqueue(3)
    >>> my_queue.display()
    2 1 5 3
    >>> my_queue.peek()
    2
    >>> my_queue.display()
    2 1 5 3
    >>> my_queue.dequeue()
    2
    >>> my_queue.display()
    1 5 3
    >>> my_queue.isEmpty()
    False

Test Queue implemetation with linked list
    >>> my_queue = QueueLL()
    >>> my_queue.isEmpty()
    True
    >>> my_queue.enqueue(2)
    >>> my_queue.display()
    2
    >>> my_queue.enqueue(1)
    >>> my_queue.enqueue(5)
    >>> my_queue.enqueue(3)
    >>> my_queue.display()
    2 1 5 3
    >>> my_queue.peek()
    2
    >>> my_queue.display()
    2 1 5 3
    >>> my_queue.dequeue()
    2
    >>> my_queue.display()
    1 5 3
    >>> my_queue.isEmpty()
    False
    >>> my_queue.dequeue()
    1
    >>> my_queue.dequeue()
    5
    >>> my_queue.dequeue()
    3
    >>> my_queue.isEmpty()
    True
"""
# List Implementation
class Queue(object):
    """ Implementation Queue with using simple list. """

    def __init__(self):
        self.queue = []

    def display(self):
        """Display queue,"""
        for item in self.queue:
            print item,

    def dequeue(self):
        """Remove the top element from the queue."""
        if self.queue != []:
            return self.queue.pop(0)

    def enqueue(self, item):
        """Add a new item to the top of the queue."""
        self.queue.append(item)

    def peek(self):
        """Return the top of the queue."""
        if self.queue != []:
            return self.queue[0]

    def isEmpty(self):
        """Return true if the queue is empty."""
        return self.queue == []


# Linked List Implementation
class Node(object):
    """Class Node"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        if self.next is not None:
            return "<Node: {0}, next: {1}>".format(self.data, self.next.data)
        else:
            return "<Node: {0}, next: {1}>".format(self.data, self.next)

class QueueLL(object):
    """ Implementation Queue with using linked list list. """

    def __init__(self):
        self.head = self.tail = None

    def display(self):
        """Display queue"""
        cur = self.head
        while cur.next is not None:
            print cur.data,
            cur = cur.next
        print cur.data

    def dequeue(self):
        """Remove the top element from the queue."""
        if self.head is not None:
            top = self.head
            self.head = self.head.next
            # if it was dequeueped last item from the queue
            if self.head == None:
                self.tail = None
            return top.data

    def enqueue(self, item):
        """Add a new item to the top of the queue."""
        # Add first item to the queue
        if self.head is None:
            self.head = self.tail = Node(item)
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def peek(self):
        """Return the top of the queue."""
        if self.head is not None:
            return self.head.data

    def isEmpty(self):
        """Return true if the queue is empty."""
        return self.head is None and self.tail is None

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED.  IT WORKS SUCCESSFULLY! ***\n"