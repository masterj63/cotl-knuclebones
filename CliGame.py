from Board import Game


class CliGame:
    def __init__(self):
        self.__game = Game()

    def print_boards(self):
        print("Player 1's board:")
        for i in range(3):
            for j in range(3):
                print(self.__game.board1.board[i][j], end=' ')
            print()
        print("Player 2's board:")
        for i in range(3):
            for j in range(3):
                print(self.__game.board2.board[i][j], end=' ')
            print()
        print()

    def run(self):
        import random
        while not self.__game.is_over():
            self.print_boards()
            current_player = self.__game.get_current_player()
            die = random.randint(1, 6)
            print(f"Player {current_player}'s turn. Rolled die: {die}")
            while True:
                try:
                    i = int(input("Enter row (0-2): "))
                    j = int(input("Enter column (0-2): "))
                    if self.__game.play(i, j, die):
                        break
                    else:
                        print("Illegal move. Try again.")
                except ValueError:
                    print("Invalid input. Please enter integers for row and column.")
        self.print_boards()
        score1 = self.__game.board1.count_score()
        score2 = self.__game.board2.count_score()
        print(f"Game over! Player 1's score: {score1}, Player 2's score: {score2}")
        if score1 > score2:
            print("Player 1 wins!")
        elif score2 > score1:
            print("Player 2 wins!")
        else:
            print("It's a tie!")
