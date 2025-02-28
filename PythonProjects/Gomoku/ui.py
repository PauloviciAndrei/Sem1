class UI:
    def __init__(self, services, Invalid_command, Invalid_move):
        self.services = services
        self.Invalid_command = Invalid_command
        self.Invalid_move = Invalid_move

    def print_board(self, board):
        print("    ", end="")
        for i in range(0, 15):
            if i < 9:
                print("0" + str(i + 1), end=" ")
            else:
                print(i + 1, end=" ")
        print()
        print("    ", end="")
        for i in range(0, 15):
            print("__", end=" ")
        print()
        for i in range(0, 15):
            if i < 9:
                print("0" + str(i + 1), end=" | ")
            else:
                print(i + 1, end=" | ")
            for j in range(0, 15):
                if board[i][j] == 0:
                    print(board[i][j], end="  ")
                else:
                    print(str(board[i][j].symbol), end="  ")

            print()
        print()

    def play_again(self, result):
        print("Play again?")
        print("1.Yes")
        print("2.No")
        cmd = int(input("Give command: "))
        print()
        if cmd == 1:
            result = False
            self.services.reset_board()
            self.print_board(self.services.get_board())
        return result

    def run(self):
        win = False
        draw = False
        lose = False
        self.print_board(self.services.get_board())
        print()
        board = self.services.get_board()
        while win == False and draw == False and lose == False:
            move = input("Your move: ")
            print()
            board = self.services.get_board()
            if self.Invalid_command.invalid_move_command(self, move) == 1:
                if (
                    self.Invalid_move.piece_alredy_exists(
                        self, self.services.get_board(), move
                    )
                    == 1
                ):
                    self.services.add_piece(move, 1)
                    if self.services.check_win(board, 1):
                        print("You won!")
                        print()
                        win = True
                        self.print_board(board)
                        win = self.play_again(win)
                    else:
                        self.services.bot_move(board)
                        if self.services.check_win(board, 2):
                            print("You lost!")
                            print()
                            lose = True
                            lose = self.play_again(lose)
                        if lose == False and win == False:
                            self.print_board(board)
