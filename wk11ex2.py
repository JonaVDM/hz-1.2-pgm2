import random


class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.

           Why isn't this in __str__?
        """
        s = ''
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-' + "\n"

        for i in range(self.width):
            s += " " + str(i % 10)

        return s

    def add_move(self, col: int, player: str) -> None:
        """ Drop down a tile using x
        """
        for i in range(self.height - 1, -1, -1):
            if self.data[i][col] != ' ':
                continue
            self.data[i][col] = player
            break

    def clear(self) -> None:
        """ Clears out all the data currently in the board
        """
        self.data = [[' ']*self.width for row in range(self.height)]

    def set_board(self, move_string):
        """Accepts a string of columns and places
        alternating checkers in those columns,
        starting with 'X'.

        For example, call b.set_board('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.set_board('000000') to
        see them alternate in the left column.

        move_string must be a string of one-digit integers.
        """
        next_checker = 'X'   # we starten door een 'X' te spelen
        for col_char in move_string:
            col = int(col_char)
            if 0 <= col <= self.width:
                self.add_move(col, next_checker)
            if next_checker == 'X':
                next_checker = 'O'
            else:
                next_checker = 'X'

    def allows_move(self, col: int) -> bool:
        """ Returns a boolean based on weather a move is
            allowed or not
        """
        if col < 0 or col > self.width - 1:
            return False
        if self.data[0][col] == ' ':
            return True
        return False

    def is_full(self):
        """ Checks if the board is currently full
        """
        full_cols = 0
        for i in range(0, self.width):
            if not self.allows_move(i):
                full_cols += 1
        return full_cols == self.width

    def del_move(self, col: int) -> None:
        """ Deletes the top most tile dropped down in column col

            Cool that you say this is useful, but that doesn't mean anything
            unless you actual tell why this is useful.. This just screams bad
            teaching
        """
        for i in range(self.height):
            if self.data[i][col] == ' ':
                continue
            self.data[i][col] = ' '
            break

    def wins_for(self, player: str) -> bool:
        """ Checks if a player has won ANYWHERE on the board
        """
        for y in range(self.height):
            for x in range(self.width):
                if in_a_row_n_east(player, y, x, self.data, 4) or \
                        in_a_row_n_northeast(player, y, x, self.data, 4) or \
                        in_a_row_n_south(player, y, x, self.data, 4) or \
                        in_a_row_n_southeast(player, y, x, self.data, 4):
                    return True
        return False

    def cols_to_win(self, player):
        """ Checks if player can win in the next move
            returns all the positions where player can win
        """
        wins = []
        for col in range(self.width):
            if not self.allows_move(col):
                continue
            self.add_move(col, player)
            if self.wins_for(player):
                wins.append(col)
            self.del_move(col)
        return wins

    def ai_move(self, player):
        """ Decide where the ai should be putting down its
            stone. Returns the number of the decided column
        """
        opponent = "X"
        if player == "X":
            opponent = "O"

        opponentWins = self.cols_to_win(opponent)
        selfWins = self.cols_to_win(player)

        if len(selfWins) > 0:
            return selfWins[0]

        if len(opponentWins) > 0:
            return opponentWins[0]

        col = -1
        while not self.allows_move(col):
            col = random.randint(0, self.width)

        return col

    def host_game(self) -> None:
        """ Runs the game.
            Why is this in the class, that doesn't make much sense...
        """
        player = 'X'
        computer = 'O'
        while True:
            print(self)

            col = -1
            while not self.allows_move(col):
                col = int(input(f'Kies een kolom ({player}): '))

            self.add_move(col, player)

            if self.wins_for(player):
                print(f'{player} heeft gewonnen -- Gefeliciteerd!')
                break

            if self.is_full():
                print('Niemand wint, het bord is vol')
                break

            comp_move = self.ai_move(computer)
            self.add_move(comp_move, computer)
            print(
                f'De computer ({computer}) heeft gekozen voor col {comp_move}')

            if self.wins_for(computer):
                print(f'{computer} wint -- loser, word verslagen door een matige AI')
                break

            if self.is_full():
                print('Niemand wint, het bord is vol')
                break

        print(self)


def in_a_row_n_east(ch, r_start, c_start, a, n):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists a (array),
       returns True if there are n ch's in a row
       heading east and returns False otherwise.
    """
    h = len(a)
    w = len(a[0])
    if r_start < 0 or r_start > h - 1:
        return False
    if c_start < 0 or c_start + (n-1) > w - 1:
        return False
    for i in range(n):
        if a[r_start][c_start+i] != ch:
            return False
    return True


def in_a_row_n_south(ch, r_start, c_start, a, n):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists a (array),
       returns True if there are n ch's in a row
       heading south and returns False otherwise.
    """
    h = len(a)
    w = len(a[0])
    if r_start < 0 or r_start + (n-1) > h - 1:
        return False
    if c_start < 0 or c_start > w - 1:
        return False
    for i in range(n):
        if a[r_start+i][c_start] != ch:
            return False
    return True


def in_a_row_n_northeast(ch, r_start, c_start, a, n):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists a (array),
       returns True if there are n ch's in a row
       heading northeast and returns False otherwise.
    """
    h = len(a)
    w = len(a[0])
    if r_start - (n-1) < 0 or r_start > h - 1:
        return False
    if c_start < 0 or c_start + (n-1) > w - 1:
        return False
    for i in range(n):
        if a[r_start-i][c_start+i] != ch:
            return False
    return True


def in_a_row_n_southeast(ch, r_start, c_start, a, n):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists a (array),
       returns True if there are n ch's in a row
       heading southeast and returns False otherwise.
    """
    h = len(a)
    w = len(a[0])
    if r_start < 0 or r_start + (n-1) > h - 1:
        return False
    if c_start < 0 or c_start + (n-1) > w - 1:
        return False
    for i in range(n):
        if a[r_start+i][c_start+i] != ch:
            return False
    return True
