"""Using binary search, find val in range 1-100. Return # of guesses.

    >>> binary_search(50)
    1
    >>> binary_search(25)
    2
    >>> binary_search(75)
    2
    >>> binary_search(31) <= 7
    True
    >>> max([binary_search(i) for i in range(1, 101)])
    7
"""


def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""
    assert 0 < val < 101, "Val must be between 1-100"
    num_guesses = 1

    highest = 100
    lowest = 1
    guess = (highest + lowest) / 2

    while val != guess:
        if val > guess:
            lowest = guess
        else:
            highest = guess
        guess = (highest + lowest) / 2
        num_guesses += 1

    return num_guesses

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE THE BEST!\n"
