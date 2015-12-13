"""Turn a phrase into Pig Latin.

This takes a space-separated phrase and returns it in Pig Latin.

Rules:

1. If the word begins with a consonant (not a, e, i, o, u),
   move the first letter to the end and add 'ay'

2. If the word begins with a vowel, add 'yay' to the end

For example:

    >>> pig_latin('hello awesome programmer')
    'ellohay awesomeyay rogrammerpay'

"""


def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """
    new_phrase = phrase.split(" ")
    pig_latin = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    for word in new_phrase:
        if word[0] in vowels:
            new_word = word + 'yay'
            pig_latin.append(new_word)
        else:
            new_word = word[1:] + word[0] + 'ay'
            pig_latin.append(new_word)

    return " ".join(pig_latin)

    # runtime O(n^2)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. REATGAY OBJAY!\n"
