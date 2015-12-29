"""Print items from a list using recursion.

    >>> print_recursively([1, 2, 3])
    1
    2
    3

"""


def print_recursively(lst):
    """Print items from a list using recursion."""

    if lst:
        print lst[0]
        print_recursively(lst[1:])


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WIN FOR YOU!\n"
