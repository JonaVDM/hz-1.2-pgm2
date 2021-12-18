#
# wk9ex2.py
#
# Naam:
#


# dit is een functie om tweedimensionale arrays
#  (lijsten van lijsten) af te drukken
def print_2d(a):
    """print_2d prints a 2D array, a
       as rows and columns
       Argument: a, a 2D list of lists
       Result: None (no return value)
    """
    rows = len(a)
    cols = len(a[0])

    for r in range(rows):      # rows == aantal rijen
        for c in range(cols):  # cols == aantal kolommen
            print(a[r][c], end=' ')
        print()

    return None  # dit is impliciet aanwezig
    # als er geen return-statement aanwezig is


# een paar tests voor print_2d
a = [['X', ' ', 'O'], ['O', 'X', 'O']]
print("2-row, 3-col a is")
print_2d(a)

a = [['X', 'O'], [' ', 'X'], ['O', 'O'], ['O', 'X']]
print("4-row, 2-col a is")
print_2d(a)


# maak een tweedimensionale array van een ééndimensionale string
def create_a(rows, cols, s):
    """Returns a 2D array with
       rows rows and
       cols cols
       using the data from s: across the
       first row, then the second, etc.
       We'll only test it with enough data!
    """
    a = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row += [s[0]]  # voeg dat karakter toe
            s = s[1:]          # verwijder het eerste karakter
        a += [new_row]
    return a


# een paar tests voor create_a:
a = [['X', ' ', 'O'], ['O', 'X', 'O']]
new_a = create_a(2, 3, 'X OOXO')
assert new_a == a

a = [['X', 'O'], [' ', 'X'], ['O', 'O'], ['O', 'X']]
new_a = create_a(4, 2, 'XO XOOOX')
assert new_a == a


def in_a_row_3_east(ch, r_start, c_start, a):
    """ Check if three on a row towards east are the same
    """
    for i in range(c_start, c_start+3):
        if i >= len(a[c_start]):
            return False
        if a[r_start][i] != ch:
            return False
    return True


def in_a_row_3_south(ch, r_start, c_start, a):
    """ Check if three on a row towards south are the same
    """
    for i in range(r_start, r_start+3):
        if i >= len(a):
            return False
        if a[i][c_start] != ch:
            return False
    return True


def in_a_row_3_southeast(ch, r_start, c_start, a):
    """ Check if three on a row towards south east are the same
    """
    for i in range(3):
        if r_start+i >= len(a[0]) or c_start+i >= len(a):
            return False
        if a[r_start+i][c_start+i] != ch:
            return False
    return True


def in_a_row_3_northeast(ch, r_start, c_start, a):
    """ Check if three on a row towards north east are the same
    """
    for i in range(3):
        if r_start-i < 0 or c_start+i >= len(a):
            return False
        if a[r_start-i][c_start+i] != ch:
            return False
    return True


# tests voor in_a_row_3_east
a = create_a(3, 4, 'XXOXXXOOOOOO')
assert not in_a_row_3_east('X', 0, 0, a)
assert in_a_row_3_east('O', 2, 1, a)
assert not in_a_row_3_east('X', 2, 1, a)
assert not in_a_row_3_east('O', 2, 2, a)

# tests voor in_a_row_3_south
a = create_a(4, 4, 'XXOXXXOXXOO OOOX')
assert in_a_row_3_south('X', 0, 0, a)
assert not in_a_row_3_south('O', 2, 2, a)
assert not in_a_row_3_south('X', 1, 3, a)
assert not in_a_row_3_south('O', 42, 42, a)

# # tests voor in_a_row_3_southeast
a = create_a(4, 4, 'XOOXXXOXX XOOOOX')
assert in_a_row_3_southeast('X', 1, 1, a)
assert not in_a_row_3_southeast('X', 1, 0, a)
assert in_a_row_3_southeast('O', 0, 1, a)
assert not in_a_row_3_southeast('X', 2, 2, a)

# # tests voor in_a_row_3_northeast
a = create_a(4, 4, 'XOXXXXOXXOXOOOOX')
assert in_a_row_3_northeast('X', 2, 0, a)
assert in_a_row_3_northeast('O', 3, 0, a)
assert not in_a_row_3_northeast('O', 3, 1, a)
assert not in_a_row_3_northeast('X', 3, 3, a)
