
### Easy ###


def is_palindrome(word):
    """Return True/False if this word is a palindrome.

        >>> is_palindrome("a")
        True
        >>> is_palindrome("noon")
        True
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("porcupine")
        False

    Treat spaces and uppercase letters normally:

        >>> is_palindrome("Racecar")
        False

    """
    reversed_word = ''.join(reversed(word))

    i = 0

    while i < len(word):
        if word[i] != reversed_word[i]:
            return False
        i += 1

    return True


def is_prime(num):
    """Write a function that returns True or False, depending on whether the integer passed into it is a prime number.

    Only numbers >1 can be prime numbers:

        >>> is_prime(0)
        False
        >>> is_prime(1)
        False

    Any number >1 that has no divisors other than 1 and itself is a prime number:

        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(4)
        False
        >>> is_prime(11)
        True
        >>> is_prime(999)
        False

    """
    if num <= 1:
        return False

    for i in range(2, num-1):
        if num % i == 0:
            return False

    return True


def lucky_numbers(num):
    """Return n unique random numbers from 1-10 (inclusive).

    Given the numbers 1-10, return n random numbers, making sure to never return
    the same number twice. You can trust that this function will never be called
    with n < 0 or n > 10.

    It's legal to ask for no numbers:
        >>> lucky_numbers(0)
        []

    And if we ask for all numbers, we shouldn't get any repeats:

        >>> sorted(lucky_numbers(10))
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    """

    number_pool = range(1, 11)
    results = []

    from random import shuffle

    for i in range(num):
        shuffle(number_pool)
        results.append(number_pool.pop())

    return results


def sort_ab(a, b):
    """Given already-sorted lists, 'a' and 'b', return sorted list of both.

    You may not use sorted() or .sort().

    Check edge cases of empty lists:

        >>> sort_ab([], [])
        []
        >>> sort_ab([1, 2,3], [])
        [1, 2, 3]
        >>> sort_ab([], [1, 2, 3])
        [1, 2, 3]

    Check:

        >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
        [1, 2, 3, 5, 6, 7, 8, 10]
    """

    if a == [] and b == []:
        return []
    elif a == []:
        return b
    elif b == []:
        return a
    else:
        a.reverse()
        b.reverse()
        sorted_list = []
        while len(a) > 0 and len(b) > 0:
            if a[-1] < b[-1]:
                sorted_list.append(a.pop())
            elif b[-1] < a[-1]:
                sorted_list.append(b.pop())
        if len(a) >= 1:
            for i in range(len(a)):
                sorted_list.append(a.pop())
        elif len(b) >= 1:
            for i in range(len(b)):
                sorted_list.append(b.pop())

    return sorted_list


### Medium ###

def reverse_linked_list():
    """Write a function that takes the head node of a linked list and returns
    the head of a new, reversed linked list."""
    pass


### Hard ###

### run tests

if __name__ == "__main__":
    from doctest import testmod
    if testmod().failed == 0:
        print "yay everything passed"
