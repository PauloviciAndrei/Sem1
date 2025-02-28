class Invalid_command(Exception):

    def invalid_move_command(self, move):
        try:
            x = str.split(move)
            if len(x) != 2:
                raise Invalid_command
            x[0] = int(x[0])
            x[1] = int(x[1])
            if x[0] > 15 or x[0] < 1:
                raise Invalid_command
            if x[1] > 15 or x[1] < 1:
                raise Invalid_command

        except:
            print("Invalid move command!")
            print()

        else:
            return 1


class Invalid_Move(Exception):

    def piece_alredy_exists(self, board, move):
        try:
            x = str.split(move)
            x[0] = int(x[0]) - 1
            x[1] = int(x[1]) - 1
            if board[x[0]][x[1]] != 0:
                raise Invalid_Move

        except:
            print("The square is occupied!")
            print()
        else:
            return 1
