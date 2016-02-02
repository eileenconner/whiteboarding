import unittest

import countemps2


class CountEmployeesTest(unittest.TestCase):

    def test_node_with_no_employees_returns_zero(self):
        node = countemps2.Node('nochildren')

        self.assertEqual(0, node.count_employees())

    def test_node_with_one_child_with_no_children_returns_one(self):
        no_children = countemps2.Node('no_children')
        parent = countemps2.Node('parent', children=[no_children])

        self.assertEqual(1, parent.count_employees())

    def test_node_with_child_and_grandchild_returns_two(self):
        grandchild = countemps2.Node('no_children')
        child = countemps2.Node('child', children=[grandchild])
        parent = countemps2.Node('parent', children=[child])

        self.assertEqual(2, parent.count_employees())

    def test_node_with_two_children_with_no_children_returns_two(self):
        child1 = countemps2.Node('child1')
        child2 = countemps2.Node('child2')
        parent = countemps2.Node('parent', children=[child1, child2])

        self.assertEqual(2, parent.count_employees())

    def test_node_with_child_and_two_grandchildren_returns_three(self):
        grandchild1 = countemps2.Node('gc1')
        grandchild2 = countemps2.Node('gc2')
        child = countemps2.Node('child', children=[grandchild1, grandchild2])
        parent = countemps2.Node('parent', children=[child])

        self.assertEqual(3, parent.count_employees())

    def test_node_w_two_children_w_two_children_apiece_returns_six(self):
        grandchild1 = countemps2.Node('gc1')
        grandchild2 = countemps2.Node('gc2')
        grandchild3 = countemps2.Node('gc3')
        grandchild4 = countemps2.Node('gc4')
        child1 = countemps2.Node('child1', children=[grandchild1, grandchild2])
        child2 = countemps2.Node('child2', children=[grandchild3, grandchild4])
        parent = countemps2.Node('parent', children=[child1, child2])

        self.assertEqual(6, parent.count_employees())

    def test_node_is_instance_of_node_class(self):
        node = countemps2.Node('node')

        self.assertIsInstance(node, countemps2.Node)

    def test_node_contains_assigned_name(self):
        child = countemps2.Node('child')
        node = countemps2.Node('node', children=[child])

        self.assertIn('node', node.name)
        self.assertIn('child', child.name)

    def test_child_in_node_children(self):
        child = countemps2.Node('child')
        node = countemps2.Node('node', children=[child])

        self.assertIn(child, node.children)

if __name__ == '__main__':
    unittest.main()
