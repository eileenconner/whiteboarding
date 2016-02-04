"""Given two linked lists, treat them like numbers and add them together.

This should take two linked lists in "reverse-digit" format, sum them up,
and return the head of a new linked list in "reverse-digit" format.

A list is in reverse-digit format if it is each digit as a node, in
least-significant-place-first order. For example, "123", would become
the list 3->2->1.

Let's add 1 + 2::

    >>> l1 = Node(1)
    >>> l2 = Node(2)
    >>> add_linked_lists(l1, l2).as_rev_string()
    '3'

Let's add 123 + 456::

    >>> l1 = Node(3, Node(2, Node(1)))
    >>> l2 = Node(6, Node(5, Node(4)))
    >>> add_linked_lists(l1, l2).as_rev_string()
    '579'

Let's make sure we carry: 144 + 456:

    >>> l1 = Node(4, Node(4, Node(1)))
    >>> l2 = Node(6, Node(5, Node(4)))
    >>> add_linked_lists(l1, l2).as_rev_string()
    '600'

Let's make sure it works with mismatched lengths: 123 + 89::

    >>> l1 = Node(3, Node(2, Node(1)))
    >>> l2 = Node(9, Node(8))
    >>> add_linked_lists(l1, l2).as_rev_string()
    '212'

"""

class Node(object):
    """Linked list node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_rev_string(self):
        """Represent data for this node and it's successors as a string.

        >>> l1 = Node(3)
        >>> l1.as_rev_string()
        '3'

        >>> l1 = Node(3, Node(2, Node(1)))
        >>> l1.as_rev_string()
        '123'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(reversed(out))


def add_linked_lists(l1, l2):
    """Given two linked lists, treat them like numbers and add them together.

    l1: the head node of a linked list in "reverse-digit" format
    l2: the head node of another "reverse-digit" format

    Returns: head node of linked list of sum in "reverse-digit" format.
    """

    # initialize pointers and variables
    p1 = l1
    p2 = l2
    prev = None
    ll = None
    carry = 0

    while p1 or p2:
        # add values at pointers plus carried value to make value for new node
        new_val = p1.data + p2.data + carry
        # if number is over 9, carry the 1 and only store ones digit
        if new_val > 9:
            carry = 1
            new_val = new_val - 10
        else:
            carry = 0

        # establish new linked list with nodes with new_val values
        if prev:
            prev.next = Node(new_val)
            prev = prev.next
        # if no prev, this node is the head of the linked list
        else:
            prev = Node(new_val)
            ll = prev

    # check if either list has any nodes remaining
    last_list = None
    if p1:
        last_list = p1
    elif p2:
        last_list = p2

    # add values remaining in existing list to new linked list
    while last_list:
        new_val = last_list.data + carry
        prev.next = Node(new_val)
        prev = prev.next
        carry = 0
        last_list = last_list.next

    return ll


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WOWZA!\n"
