class Services:
    def __init__(self, repository, bot):
        self.repository = repository
        self.bot = bot

    def get_board(self):
        board = self.repository.get_board()
        return board

    def reset_board(self):
        self.repository.reset_board()

    def add_piece(self, position, player):
        x = str.split(position)
        i = int(x[0]) - 1
        j = int(x[1]) - 1
        self.repository.add_piece(i, j, player)

    def add_piece_bot(self, position, player):
        i, j = position
        self.repository.add_piece(i, j, player)

    def check_lines(self, board, player):
        for i in range(0, 15):
            for j in range(0, 11):
                if board[i][j] != 0:
                    if board[i][j].player == player:
                        nr = 1
                        for k in range(j + 1, j + 5):
                            if board[i][k] != 0:
                                if board[i][k].player == player:
                                    nr = nr + 1
                        if nr == 5:
                            return 1
        return 0

    def check_columns(self, board, player):
        for j in range(0, 15):
            for i in range(0, 11):
                if board[i][j] != 0:
                    if board[i][j].player == player:
                        nr = 1
                        for k in range(i + 1, i + 5):
                            if board[k][j] != 0:
                                if board[k][j].player == player:
                                    nr = nr + 1
                        if nr == 5:
                            return 1
        return 0

    def check_diagonals(self, board, player):
        for k in range(0, 11):
            for i in range(0, 15 - k - 4):
                if board[i][i + k] != 0:
                    if board[i][i + k].player == player:
                        nr = 1
                        for j in range(i + 1, i + 5):
                            if board[j][j + k] != 0:
                                if board[j][j + k].player == player:
                                    nr = nr + 1
                        if nr == 5:
                            return 1

        for k in range(1, 11):
            for j in range(0, 15 - k - 4):
                if board[j + k][j] != 0:
                    if board[j + k][j].player == player:
                        nr = 1
                        for i in range(j + 1, j + 5):
                            if board[i + k][i] != 0:
                                if board[i + k][i].player == player:
                                    nr = nr + 1
                        if nr == 5:
                            return 1

    def check_win(self, board, player):
        if self.check_lines(board, player) == 1:
            return 1
        if self.check_columns(board, player) == 1:
            return 1
        if self.check_diagonals(board, player) == 1:
            return 1

    def bot_move(self, board):
        move = None
        len_player, location_player, type_player = self.bot.get_max_pieces(
            board, 1
        )
        len_bot, location_bot, type_bot = self.bot.get_max_pieces(board, 2)
        if len_player > len_bot:
            move = self.bot.need_defence(board, location_player, type_player)
        else:
            move = self.bot.attack(board, location_bot, type_bot)
        if move == None:
            move = self.bot.find_move(board, 2)
            print(move)
        self.add_piece_bot(move, 2)
        if self.check_win(board, 2) == 1:
            return True
        return False
