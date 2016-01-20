"""Practice writing tree/node instance methods"""


class Node(object):
    """Node in a tree."""

    def __init__(self, data, children=None):
        """Initialize node with given data."""
        children = children or []
        assert isinstance(children, list)
        self.data = data
        self.children = children

    def __repr__(self):
        """Debugging-friendly representation."""

        return "<Node %s>" % self.data

    def traverse_tree(self):
        """Traverse tree depth-first from given root node."""
        to_visit = [self]
        visited = []

        while to_visit:
            node = to_visit.pop()
            to_visit.extend(node.children)
            visited.append(node)

        return visited

    def depth_first_search(self, data):
        """Perform depth-first search for data."""
        # uses stack
        to_visit = [self]

        while to_visit:
            node = to_visit.pop()

            if node.data == data:
                return node

            to_visit.extend(node.children)

        return None

    def breadth_first_search(self, data):
        """Perform breadth-first search for data."""
        # uses queue
        to_visit = [self]

        while to_visit:
            node = to_visit.pop(0)

            if node.data == data:
                return node

            to_visit.extend(node.children)

        return None

    def recursive_search(self, data):
        """Recursively search a tree for data, depth-first."""
        if self.data == data:
            return self

        for child in self.children:
            child.recursive_search(data)

        return None
