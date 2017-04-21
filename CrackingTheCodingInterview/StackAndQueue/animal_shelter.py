""" Ahimal Shelter.
    An animal shelter operates on a strictly FIFO. People must adopt either the 
    oldest (based on arrival time) of all animals as the shelter.
    Implement operators:
    enque()
    dequeueAny()
    dequeueDog()
    dequeueCat()

    >>> animals = AnimalShelter()
    >>> animals.enqueue('cat', '12/02/2016')
    >>> animals.enqueue('cat', '02/02/2017')
    >>> animals.enqueue('cat', '04/01/2017')
    >>> animals.enqueue('dog', '01/02/2017')
    >>> animals.cats.display()
    12/02/2016 02/02/2017 04/01/2017
    >>> animals.dogs.display()
    01/02/2017
    >>> animals.dequeueAny()
    '12/02/2016'
    >>> animals.dequeueCat()
    '02/02/2017'
    >>> animals.dequeueDog()
    '01/02/2017'

    >>> animals.cats.display()
    04/01/2017
    >>> animals.dogs.isEmpty()
    True
"""
from datetime import datetime


# Linked List Implementation
class Node(object):
    """Class Node"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        if self.next is None:
            return "<Node: {0}, next: {1}>".format(self.data.strftime('%m/%d/%Y'), None)    
        else:
            return "<Node: {0}, next: {1}>".format(self.data.strftime('%m/%d/%Y'), \
                                                   self.next.data.strftime('%m/%d/%Y'))


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
            if self.head  is None:
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


class AnimalShelter(object):
    """Class AnimalShelter."""

    def __init__(self):
        self.cats = QueueLL()
        self.dogs = QueueLL()

    def enqueue(self, typeAnimal, data):
        if typeAnimal == 'dog':
            self.dogs.enqueue(data)
        elif typeAnimal == 'cat':
            self.cats.enqueue(data)
        else:
            print "We don't have this animal"

    def dequeueAny(self):
        if self.cats.isEmpty():
            return self.dogs.dequeue()
        if self.dogs.isEmpty():
            return self.cats.dequeue()

        if datetime.strptime(self.cats.peek(), '%m/%d/%Y') > datetime.strptime(self.dogs.peek(), '%m/%d/%Y'):
            return self.dogs.dequeue()

        return self.cats.dequeue()

    def dequeueCat(self):
        if not self.cats.isEmpty():
            return self.cats.dequeue()

    def dequeueDog(self):
        if not self.dogs.isEmpty():
            return self.dogs.dequeue()


if __name__ == "__main__":
    import doctest
    
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED.  ANIMAL SHELTER WORKS SUCCESSFULLY! ***\n"