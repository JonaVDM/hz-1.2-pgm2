#
# wk7ex5.py - Aan de slag met lussen!
#
# Naam:
#

import random


def power(b: int, p: int) -> int:
    """ Calculate b to the power of p, and return this
    """
    if p == 0:
        return 1

    result = b
    for _ in range(p - 1):
        result *= b
    return result


assert power(2, 5) == 32
assert power(5, 2) == 25
assert power(42, 0) == 1
assert power(0, 42) == 0
assert power(0, 0) == 1


def summed_odds(l: list) -> int:
    """ Get a sum of all the odd numbers in a list.
    """
    result = 0
    for x in l:
        if x % 2 != 0:
            result += x
    return result


assert summed_odds([4, 5, 6]) == 5
assert summed_odds(range(3, 10)) == 24


def until_a_repeat(high: int) -> int:
    """ Well, I would say the name is clear enough... Generate random
        numbers until you find one that was already there. Weird shit,
        I know.
        The amount of steps given to make this exercise is a bit much,
        maybe turn it down just a tiny bit...

        Returns the amount of times it took before it found a repeat.
    """
    l = []

    while (unique(l)):
        l.append(random.choice(range(0, high)))

    return len(l)


def unique(l: list) -> bool:
    """Returns whether all elements in L are unique.
       Argument: L, a list of any elements.
       Return value: True, if all elements in L are unique,
                  or False, if there is any repeated element
    """
    if len(l) == 0:
        return True
    elif l[0] in l[1:]:
        return False
    else:
        return unique(l[1:])
