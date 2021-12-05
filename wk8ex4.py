# i already thought it looked familiar: https://adventofcode.com/2015/day/10

def next(curr: int) -> int:
    """ Next returns the next value of the Look-and-say
        sequence.
    """
    inString = str(curr)
    out = ''

    while len(inString) > 0:
        num = inString[0]
        counter = 1

        for i in range(1, len(inString)):
            if inString[i] == num:
                counter += 1
            else:
                break
        out += f'{counter}{num}'
        inString = inString[counter:]

    return int(out)


assert next(21) == 1211
assert next(2222) == 42
assert next(312211) == 13112221
assert next(13211321322113) == 1113122113121113222113
assert next(1113122113) == 311311222113


def read_it(n: int) -> None:
    """ Print out the first n amount of items of the
        Look-and-say sequence.
    """

    prev = 1
    for _ in range(n):
        print(prev)
        prev = next(prev)
