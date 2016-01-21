"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin(0)
    '0'
    >>> dec2bin(1)
    '1'
    >>> dec2bin(2)
    '10'
    >>> dec2bin(4)
    '100'
    >>> dec2bin(15)
    '1111'


"""


def dec2bin(num):
    """Convert a decimal number to binary representation."""

    binary_num = []

    if num == 0:
        return '0'

    while num is not 0:
        binary_num.append(str(num % 2))
        num = num / 2

    return "".join(reversed(binary_num))


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
