
"""Count the number of items in a list, using recursion. For example:

    >>> count_recursively([])
    0
    >>> count_recursively([1, 2, 3])
    3

"""


def count_recursively(lst):
    """Return number of items in a list, using recursion."""
    count = 0

    for i in range(len(lst)):
        count += 1
        count_recursively(lst[i+1:])

    return count


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU ARE WINNAR!\n"
