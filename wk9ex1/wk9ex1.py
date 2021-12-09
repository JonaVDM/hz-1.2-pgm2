#
# wk9ex1.py - Practicum Game of Life
#
# Naam:
#

import random
from turtle import window_height


def create_one_row(width):
    """ returns one row of zeros of width "width"...
         You might use this in your create_board(width, height) function """
    row = []
    for _ in range(width):  # Avoid unused variables! Dude..
        row += [0]
    return row


def create_board(width, height):
    """Returns a 2D array with "height" rows and "width" columns."""
    a = []
    for _ in range(height):
        a.append(create_one_row(width))
    return a


def print_board(a):
    """This function prints the 2D list-of-lists a."""
    for row in a:               # row is de hele rij
        for col in row:         # col is het individuele element
            print(col, end='')  # druk dat element af
        print()


def diagonalize(width, height):
    """Creates an empty board and then modifies it
       so that it has a diagonal strip of "on" cells.
       But do that only in the *interior* of the 2D array.
    """
    a = create_board(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if row == col:
                a[row][col] = 1
            else:
                a[row][col] = 0

    return a


def inner_cells(width, height):
    """ Creates an empty board and fills the inside cells
        with 1.
    """
    board = create_board(width, height)

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            board[i][j] = 1

    return board


def random_cells(width, height):
    """ Creates an empty board and fills the inside cells
        randomly with 1.
    """
    board = create_board(width, height)

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            board[i][j] = random.choice([0, 1])

    return board


def copy(board):
    """ Craetes a deep copy of the given board.
    """
    newBoard = create_board(len(board[0]), len(board))

    for i in range(1, len(board) - 1):
        for j in range(1, len(board[0]) - 1):
            newBoard[i][j] = board[i][j]

    return newBoard


def inner_reverse(board):
    """ Reverse the inside cells of the board.
        1 becomes 0 and 0 becomes 1
    """
    newBoard = copy(board)

    for i in range(1, len(board) - 1):
        for j in range(1, len(board[0]) - 1):
            if board[i][j] == 1:
                newBoard[i][j] = 0
            else:
                newBoard[i][j] = 1

    return newBoard


def count_neighbours(row, col, board):
    """ Counts the direct neighbours of the given cell
    """
    counter = 0
    for y in range(row - 1, row + 2):
        for x in range(col - 1, col + 2):
            if x == col and y == row:
                continue
            if y > 0 and y < len(board) - 1 and x > 0 and x < len(board[y]) - 1:
                counter += board[y][x]
    return counter


def next_life_generation(board):
    """Makes a copy of a and then advances one
       generation of Conway's Game of Life within
       the *inner cells* of that copy.
       The outer edge always stays at 0.
    """
    newBoard = copy(board)
    for y in range(1, len(board) - 1):
        for x in range(1, len(board[y]) - 1):
            c = count_neighbours(y, x, board)
            if c < 2 or c > 3:
                newBoard[y][x] = 0
            elif c == 3:
                newBoard[y][x] = 1

    return newBoard
