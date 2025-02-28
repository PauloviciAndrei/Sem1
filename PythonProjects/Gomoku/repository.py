class Repository:
    def __init__(self, Piece):
        self.board = self.create_board()
        self.piece = Piece

    def create_board(self):
        board = []
        for i in range(0, 15):
            a = []
            for j in range(0, 15):
                a.append(0)
            board.append(a)
        return board

    def get_board(self):
        return self.board

    def add_piece(self, i, j, player):
        if player == 1:
            piece = self.piece(i, j, player, "*")
        else:
            piece = self.piece(i, j, player, "+")

        self.board[i][j] = piece

    def reset_board(self):
        for i in range(0, 15):
            for j in range(0, 15):
                self.board[i][j] = 0
