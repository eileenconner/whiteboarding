# find shortest distance between two nodes A & B in a binary search tree
# write node class
# write methods: find node with given data, identify common ancestor of two nodes,
# find distance between node and that ancestor, find distance between 2 nodes.
# if either A or B does not exist, print "Not found"


class Node(object):
    """Node in a binary search tree."""

    def __init__(self, data, parent=None, left=None, right=None):
        """Initialize node in binary search tree with given data."""
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    def find_node(self, sought):
        """Find node with given data in a binary search tree."""
        node = self

        while node:
            if node.data == sought:
                return node
            elif node.data < sought:
                node = node.left
            elif node.data > sought:
                node = node.right

        return None

    def insert_node(self, data):
        """Insert node at correct place in binary search tree"""
        # check if node already in tree
        # if not, navigate down tree to where it should be
        # insert at correct left/right point related to parent node

        node = self

        if node.data == data:
            return
        else:
            if data < node.data:
                if not node.left:
                    # insert new node at left point w data as data and current node as parent
                    node.left = Node(data, node)
                else:
                    node.left = self.insert_node(data)

            else:
                if not node.right:
                    # as above, insert new node with data & parent values
                    node.right = Node(data, node)
                else:
                    node.right = self.insert_node(data)

    def id_ancestors(self):
        """Return list of ancestors of given node."""
        # navigate upward from node to root of tree
        # for each node visited, add parent to list
        # proceed until parent == None

        node = self
        ancestor_list = []

        while node.parent:
            node = node.parent
            ancestor_list.append(node)

        return ancestor_list


# functions requiring two nodes; not instance methods

def find_distance_node_to_ancestor(node, ancestor):
    """Find distance between a node and ancestor"""
    # set variable to hold distance
    distance = 0

    # while node's parent is not ancestor
    # if data != ancestor value, increment distance variable, go up to parent, and recheck
    # when ancestor found, return distance
    while node.parent != ancestor:
        distance += 1
        node = node.parent

    return distance


def find_common_ancestor(node1, node2):
    """Find first ancestor common to two nodes"""
    # access ancestor lists from node A&B from id_ancestors()
    # navigate through using pointers/max/min like in apple stock problem?
    # think about how to find FIRST common ancestor
    ancestors_a = Node.id_ancestors(node1)
    ancestors_b = Node.id_ancestors(node2)
    first_common_ancestor = None

    # brute force method -- could be optimized
    for i in range(len(ancestors_a)):
        for j in range(len(ancestors_b)):
            if ancestors_a[i] == ancestors_b[j]:
                first_common_ancestor = ancestors_a[i]
                return first_common_ancestor

    return first_common_ancestor


def find_shortest_distance_btw_two_nodes(node1, node2):
    """Find shortest distance between two nodes"""
    # check to be sure both nodes exist
    if not Node.find_node(node1) or Node.find_node(node2):
        return "Not found"

    # run find_common_ancestor
    common_ancestor = find_common_ancestor(node1, node2)
    if not common_ancestor:
        return "These nodes do not have a common ancestor"

    # run find-distance_node_to_ancestor for each node, passing in common ancestor
    # return sum of two values
    distance_1 = find_distance_node_to_ancestor(node1, common_ancestor)
    distance_2 = find_distance_node_to_ancestor(node2, common_ancestor)
    return distance_1 + distance_2
