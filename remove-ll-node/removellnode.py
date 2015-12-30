class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_string(self):
        """Represent data for this node and its successors as a string.
            >>> Node(3).as_string()
            '3'
            >>> Node(3, Node(2, Node(1))).as_string()
            '321'
        """

        out = []
        n = self
        while n:
            out.append(str(n.data))
            n = n.next
        return "".join(out)


def remove_node(node):
    """Given a node in a linked list, remove it.
    Remove this node from a linked list. Note that we do not have access to
    any other nodes of the linked list, like the head or the tail.
    Does not return anything; changes list in place."""

    node.data == node.next.data
    node.next == node.next.next


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. BEST!\n"
