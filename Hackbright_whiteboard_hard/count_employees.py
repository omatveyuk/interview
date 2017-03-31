"""Count employees in an org chart.

Our organization has the following org chart::

                    Jane
          Jessica          Janet
       Al  Bob  Jen     Nick  Nora
                                Henri

Let's make this chart::

    >>> henri = Node("Henri")
    >>> nora = Node("Nora", [henri])
    >>> nick = Node("Nick")
    >>> janet = Node("Janet", [nick, nora])
    >>> al = Node("Al")
    >>> bob = Node("Bob")
    >>> jen = Node("Jen")
    >>> jessica = Node("Jessica", [al, bob, jen])
    >>> jane = Node("Jane", [jessica, janet])

And test our counting function::

    >>> henri.count_employees()
    0

    >>> nora.count_employees()
    1

    >>> jane.count_employees()
    8

    >>> jessica.count_employees()
    3

    >>> janet.count_employees()
    3

We provide a non-recursive version, let's make sure that gives the same
answer::

    >>> henri.count_employees_nonrecursive()
    0

    >>> nora.count_employees_nonrecursive()
    1

    >>> jane.count_employees_nonrecursive()
    8

    >>> jessica.count_employees_nonrecursive()
    3

    >>> janet.count_employees_nonrecursive()
    3
"""


class Node(object):
    """Node in a tree."""

    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

    def count_employees(self):
        """Return a count of how many employees this person manages.

        Return a count of how many people that manager manages. This should
        include *everyone* under them, not just people who directly report to
        them.
        """
        if self.children == [] or self.children is None:
            return 0

        return len(self.children) + sum([child.count_employees() for child in self.children])

    def count_employees_nonrecursive(self):
        """Return a count of how many employees this person manages.

        Return a count of how many people that manager manages. This should
        include *everyone* under them, not just people who directly report to
        them.
        Non-recirsive method.
        """
        count = []
        sum = 0
        count.extend(self.children)
        while count != []:
            node = count.pop()
            sum +=1
            count.extend(node.children)
        return sum
        


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU ARE A TREE GENIUS!\n"

