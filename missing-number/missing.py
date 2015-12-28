"""Given a list of numbers 1...max_num, find which one is missing in a list.

    >>> missing_number([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
    8
    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8

"""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list
    """

    for item in range(1, max_num):
        if item not in nums:
            return item


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. NICELY DONE!\n"
