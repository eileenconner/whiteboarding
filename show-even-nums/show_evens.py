"""
You will be given a list of integers, some even and some odd:

    >>> lst = [1, 2, 3, 4, 6, 8]

Write a function that returns the indices (0-based, as usual in Python) of all
the numbers which are even.

So, for our list above, that would be:

    >>> show_evens(lst)
    [1, 3, 4, 5]

"""


def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list."""

    indices = []

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            indices.append(i)

    return indices


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** YOU DID A GOOD!\n"
