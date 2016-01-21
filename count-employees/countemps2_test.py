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


if __name__ == '__main__':
    unittest.main()
