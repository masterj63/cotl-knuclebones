# The goal of this file/project is to create a bot to play the following board game.
# Two players play against each other. Both of them have a 3x3 board (i.e. nine cells).
# One by one, the players throw a die, get a random number between 1 and 6 and choose a cell on their board to place the die onto.
# 1. Initially, the boards are empty, i.e. every cell's value is nil.
# 2. If the player that's about to roll has a full board, the game if over and the score is counted.
# 3. The player places the die onto a free cell on their board.
# 4. After placing the die, all dice with the same value as the rolled die are removed from the opponent's board.
# 5. The players alternate turns until one of them has a full board.
# 6. The score is the sum of scores for each row.
# The score of a row is:
# 1. 9*N, if it contains the dice that are all N; else
# 2. 4*N + M, if it contains N twice and M once; else
# 3. N + M + K, if all the dice are different values N, M and K.
# The player with the highest score wins.
# We number rows and cols from 0 to 2.

class Board:
    def __init__(self):
        # A 3x3 array representing the boards of the players.
        # 0 means empty cell, otherwise the cell is occupied by a die, and the permitted values are 1, 2, 3, 4, 5, 6.
        # Visually, the board coordinates are:
        # (0,0) (0,1) (0,2)
        # (1,0) (1,1) (1,2)
        # (2,0) (2,1) (2,2)
        self.board: list[list[int]] = [[0, 0, 0] for _ in range(3)]

    def is_full(self) -> bool:
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return False
        return True

    # The score is the sum of scores for each row.
    # The score of a row is:
    # 1. 9*N, if it contains the dice are all N; else
    # 2. 4*N + M, if it contains N twice and M once; else
    # 3. N + M + K, if all the dice are different values N, M and K.
    def count_score(self) -> int:
        score = 0
        for j in range(3):
            if self.board[0][j] == self.board[1][j] \
                    and self.board[0][j] == self.board[2][j]:
                N = self.board[0][j]
                score += N * 9
            elif self.board[0][j] == self.board[1][j]:
                N = self.board[0][j]
                score += N * 4
                score += self.board[2][j]
            elif self.board[0][j] == self.board[2][j]:
                N = self.board[0][j]
                score += N * 4
                score += self.board[1][j]
            elif self.board[1][j] == self.board[2][j]:
                score += self.board[0][j]
                N = self.board[1][j]
                score += N * 4
            else:
                score += self.board[0][j]
                score += self.board[1][j]
                score += self.board[2][j]
        return score

    # Returns `False` if the move is illegal:
    # -  a coordinate (`i` or `j`) is outside 0..2
    # - `die` is outside 1..6
    # - the cell is occupied.
    def place_a_die(self, i: int, j: int, die: int) -> bool:
        i, j, die = round(i), round(j), round(die)

        if die < 1 or 6 < die:
            return False
        if i < 0 or 2 < i:
            return False
        if j < 0 or 2 < j:
            return False
        if self.board[i][j] != 0:
            return False

        self.board[i][j] = die
        return True

    # Removes all dice with value `die` from the column `j`.
    def remove_dice(self, j: int, die: int) -> None:
        for i in range(3):
            if self.board[i][j] == die:
                self.board[i][j] = 0

    # the score and the board in a nice format
    def __str__(self):
        s = str(self.count_score()) + " ;"
        for i in range(3):
            for j in range(3):
                s += " "
                s += str(self.board[i][j])
            s += ","
        return s

class Game:
    def __init__(self):
        self.board1: Board = Board()
        self.board2: Board = Board()
        # Either 1 or 2.
        self.current_player: int = 1

    def get_current_player(self) -> int:
        return self.current_player

    def is_over(self) -> bool:
        return self.board1.is_full() if self.current_player == 1 else self.board2.is_full()

    def get_current_board(self) -> Board:
        return self.board1 if self.current_player == 1 else self.board2

    def get_opponent_board(self) -> Board:
        return self.board2 if self.current_player == 1 else self.board1

    def play(self, i: int, j: int, die: int) -> bool:
        if self.current_player == 1:
            current_player_board = self.board1
            opponent_player_board = self.board2
            next_player = 2
        else:
            current_player_board = self.board2
            opponent_player_board = self.board1
            next_player = 1
        if current_player_board.place_a_die(i, j, die):
            self.current_player = next_player
            opponent_player_board.remove_dice(j, die)
            return True
        else:
            return True
