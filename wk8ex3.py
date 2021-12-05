import random
import math


def throw_dart() -> bool:
    """ Throw a dart onto a random position on the board
        when the dart hits inside the circle we will return
        True, otherwise it's gonna be a False
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    return abs(x)**2 + abs(y)**2 < 1


def for_pi(n: int) -> float:
    """ Throw many many darts, in fact as many as you want
        indicated by the parameter n. After we carefully
        have thrown all the dart whilst being basically
        blindfolded, we will return the outcome which is
        hopefully a number pretty close to PI.
    """
    hits = 0
    for i in range(1, n + 1):
        if throw_dart():
            hits += 1
        print(f"{hits} raak van {i} worpen dus pi is {4 * (hits / i)}")
    return 4 * (hits / n)


def while_pi(error: float) -> float:
    """ Throw many many darts, although this time you will
        not be able to chose how many dart we will throw.
        When PI - our estimation are under the beautiful
        parameter error, we will return the amount of throws
        it took to get there.
    """
    hits = 0
    counter = 0
    while counter == 0 or abs(math.pi - 4 * (hits / counter)) > error:
        counter += 1
        if throw_dart():
            hits += 1
        print(f"{hits} raak van {counter} worpen dus pi is {4 * (hits / counter)}")
    return counter
