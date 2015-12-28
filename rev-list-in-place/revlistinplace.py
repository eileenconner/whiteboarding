"""Reverse list in place.

You cannot do this with reversed(), .reverse(), or list slice
assignment!

    >>> lst = []
    >>> rev_list_in_place(lst)
    []

    >>> lst = ['a']
    >>> rev_list_in_place(lst)
    ['a']

    >>> lst = [1, 2, 3]
    >>> rev_list_in_place(lst)
    [3, 2, 1]

    >>> lst = [1, 2, 3, 4]
    >>> rev_list_in_place(lst)
    [4, 3, 2, 1]
"""


def rev_list_in_place(lst):
    """Reverse list in place.

    You cannot do this with reversed(), .reverse(), or list slice
    assignment!
    """
    if lst == [] or len(lst) == 1:
        return lst

    placeholder = None

    # watch for off by 1 errors
    for i in range((len(lst)/2)):
        placeholder = lst[i]
        lst[i] = lst[-i - 1]
        lst[-i - 1] = placeholder

    return lst


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE THE BEST!\n"
