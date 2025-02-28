class Bot:
    def __init__(self):
        pass

    def valid_line(self, board, location):
        x = location[0]
        y = location[-1]
        i, j = x
        if j != 0:
            if board[i][j - 1] == 0:
                return 1
        i, j = y
        if j != 14:
            if board[i][j + 1] == 0:
                return 1
        return 0

    def valid_column(self, board, location):
        x = location[0]
        y = location[-1]
        i, j = x
        if i != 0:
            if board[i - 1][j] == 0:
                return 1
        i, j = y
        if i != 14:
            if board[i + 1][j] == 0:
                return 1
        return 0

    def valid_diagonal(self, board, location):
        x = location[0]
        y = location[-1]
        i, j = x
        if i != 0 and j != 0:
            if board[i - 1][j - 1] == 0:
                return 1
        i, j = y
        if i != 14 and j != 14:
            if board[i + 1][j + 1] == 0:
                return 1
        return 0

    def get_max_pieces(self, board, player):
        info_diag = self.get_max_pieces_diagonals(board, player)
        info_col = self.get_max_pieces_columns(board, player)
        info_lin = self.get_max_pieces_lines(board, player)
        len_lin, location_lin, type_lin = info_lin
        len_col, location_col, type_col = info_col
        len_diag, location_diag, type_diag = info_diag
        max_info = info_lin
        max_len = 0
        if len_diag != 0 or len_lin != 0 or len_col != 0:
            if len_lin > max_len:
                if self.valid_line(board, location_lin):
                    max_len = len_lin
                    max_info = info_lin
            if len_col > max_len:
                if self.valid_column(board, location_col):
                    max_len = len_col
                    max_info = info_col
            if len_diag > max_len:
                if self.valid_diagonal(board, location_diag):
                    max_len = len_diag
                    max_info = info_diag

        return max_info

    def get_gap_line(self, board, player):
        for i in range(0, 15):
            for j in range(0, 13):
                if board[i][j] != 0:
                    if board[i][j].player == player:
                        if board[i][j + 2] != 0:
                            if board[i][j + 2] != 0 and board[i][j + 1] == 0:
                                return i, j + 1
        return False

    def get_gap_column(self, board, player):
        for j in range(0, 15):
            for i in range(0, 13):
                if board[i][j] != 0:
                    if board[i][j].player == player:
                        if board[i + 2][j] != 0:
                            if board[i + 2][j] != 0 and board[i + 1][j] == 0:
                                return i + 1, j
        return False

    def get_max_pieces_lines(self, board, player):
        max_location = []
        max_pieces = 0
        for i in range(0, 15):
            for j in range(0, 14):
                if board[i][j] != 0:
                    if board[i][j].player == player:
                        current = 0
                        location = []
                        while (
                            board[i][j] != 0 and board[i][j].player == player
                        ):
                            if j < 14:
                                poz = i, j
                                location.append(poz)
                                j = j + 1
                                current = current + 1
                            elif j == 14:
                                if (
                                    board[i][j] != 0
                                    and board[i][j].player == player
                                ):
                                    poz = i, j
                                    location.append(poz)
                                    current = current + 1
                                    break
                        if current > max_pieces:
                            max_pieces = current
                            max_location = location

        return max_pieces, max_location, 1

    def get_max_pieces_columns(self, board, player):
        max_location = []
        max_pieces = 0
        for j in range(0, 15):
            for i in range(0, 14):
                if board[i][j] != 0:
                    if board[i][j].player == player:
                        location = []
                        current = 0
                        while (
                            board[i][j] != 0 and board[i][j].player == player
                        ):
                            if i < 14:
                                poz = i, j
                                location.append(poz)
                                i = i + 1
                                current = current + 1
                            elif i == 14:
                                if (
                                    board[i][j] != 0
                                    and board[i][j].player == player
                                ):
                                    poz = i, j
                                    location.append(poz)
                                    current = current + 1
                                    break
                        if current > max_pieces:
                            max_pieces = current
                            max_location = location

        return max_pieces, max_location, 2

    def get_max_pieces_diagonals(self, board, player):
        max_pieces = 0
        max_location = []
        for k in range(0, 11):
            for i in range(0, 15 - k):
                if board[i][i + k] != 0:
                    if board[i][i + k].player == player:
                        location = []
                        current = 0
                        while (
                            board[i][i + k] != 0
                            and board[i][i + k].player == player
                        ):
                            if i < 14 - k:
                                poz = i, i + k
                                location.append(poz)
                                i = i + 1
                                current = current + 1
                            elif i == 14 - k:
                                if (
                                    board[i][i + k] != 0
                                    and board[i][i + k].player == player
                                ):
                                    poz = i, i + k
                                    location.append(poz)
                                    current = current + 1
                                    break
                        if current > max_pieces:
                            max_pieces = current
                            max_location = location

        for k in range(1, 11):
            for j in range(0, 15 - k):
                if board[j + k][j] != 0:
                    if board[j + k][j].player == player:
                        location = []
                        current = 0
                        while (
                            board[j + k][j] != 0
                            and board[j + k][j].player == player
                        ):
                            if j < 14 - k:
                                poz = j + k, j
                                location.append(poz)
                                j = j + 1
                                current = current + 1
                            elif j == 14 - k:
                                if (
                                    board[j + k][j] != 0
                                    and board[j + k][j].player == player
                                ):
                                    poz = j + k, j
                                    location.append(poz)
                                    current = current + 1
                                    break
                        if current > max_pieces:
                            max_pieces = current
                            max_location = location
        return max_pieces, max_location, 3

    def distance_to_center(self, x):
        i, j = x
        return abs(7 - i) + abs(7 - j)

    def closer_to_center(self, board, x, y, i1, i2, j1, j2):
        if self.distance_to_center(x) < self.distance_to_center(y):
            if board[i1][j1] == 0:
                return x
            else:
                return y
        else:
            if board[i2][j2] == 0:
                return y
            else:
                return x

    def attack_line(self, board, location):
        if len(location) == 4:
            if self.win_possible_line(board, location):
                return self.win_line(board, location)
        else:
            return self.just_attack_line(board, location)

    def win_possible_line(self, board, location):
        x = location[0]
        i, j = x
        if j != 0:
            if board[i][j - 1] == 0:
                return True
        x = location[-1]
        i, j = x
        if j != 14:
            if board[i][j + 1] == 0:
                return True
        return False

    def win_line(self, board, location):
        x = location[0]
        i1, j1 = x
        j1 = j1 - 1
        x = i1, j1
        y = location[3]
        i2, j2 = y
        j2 = j2 + 1
        y = i2, j2
        return self.closer_to_center(board, x, y, i1, i2, j1, j2)

    def just_attack_line(self, board, location):
        x = location[0]
        y = location[-1]
        i1, j1 = x
        i2, j2 = y
        j1 = j1 - 1
        j2 = j2 + 1
        x = i1, j1
        y = i2, j2
        return self.closer_to_center(board, x, y, i1, i2, j1, j2)

    def attack_column(self, board, location):
        if len(location) == 4:
            if self.win_possible_column(board, location):
                return self.win_column(board, location)
        else:
            return self.just_attack_column(board, location)

    def win_possible_column(self, board, location):
        x = location[0]
        i, j = x
        if j != 0:
            if board[i - 1][j] == 0:
                return True
        x = location[-1]
        i, j = x
        if j != 14:
            if board[i + 1][j] == 0:
                return True
        return False

    def win_column(self, board, location):
        x = location[0]
        i1, j1 = x
        i1 = i1 - 1
        x = i1, j1
        y = location[3]
        i2, j2 = y
        i2 = i2 + 1
        y = i2, j2
        return self.closer_to_center(board, x, y, i1, i2, j1, j2)

    def just_attack_column(self, board, location):
        x = location[0]
        y = location[-1]
        i1, j1 = x
        i2, j2 = y
        i1 = i1 - 1
        i2 = i2 + 1
        x = i1, j1
        y = i2, j2
        return self.closer_to_center(board, x, y, i1, i2, j1, j2)

    def attack_diagonal(self, board, location):
        if len(location) == 4:
            if self.win_possible_diagonal(board, location):
                return self.win_diagonal(board, location)
        else:
            return self.just_defend_diagonal(board, location)

    def win_possible_diagonal(self, board, location):
        x = location[0]
        i, j = x
        if i != 0 and j != 0:
            if board[i - 1][j - 1] == 0:
                return True
        x = location[-1]
        i, j = x
        if i != 14 and j != 14:
            if board[i + 1][j + 1] == 0:
                return True
        return False

    def win_diagonal(self, board, location):
        x = location[0]
        i1, j1 = x
        if j1 != 0:
            i1 = i1 - 1
            j1 = j1 - 1
        x = i1, j1
        y = location[3]
        i2, j2 = y
        if i2 != 14:
            i2 = i2 + 1
            j2 = j2 + 1
        y = i2, j2
        return self.closer_to_center(board, x, y, i1, i2, j1, j2)

    def just_attack_diagonal(self, board, location):
        x = location[0]
        y = location[-1]
        i1, j1 = x
        i2, j2 = y
        if j1 != 0:
            i1 = i1 - 1
            j1 = j1 - 1
        i1 = i1 - 1
        j1 = j1 - 1
        if i2 != 14:
            i2 = i2 + 1
            j2 = j2 + 1
        x = i1, j1
        y = i2, j2
        return self.closer_to_center(board, x, y, i1, i2, j1, j2)

    def attack(self, board, location, lcd):
        if lcd == 1:
            move = self.attack_line(board, location)
        elif lcd == 2:
            move = self.attack_column(board, location)
        else:
            move = self.attack_diagonal(board, location)
        return move

    def defend_line(self, board, location):
        if len(location) == 4:
            if self.block_possible_line(board, location):
                return self.block_win_line(board, location)
        else:
            gap = self.get_gap_line(board, 1)
            if gap != False:
                return gap
            else:
                if self.block_possible_line(board, location):
                    return self.just_defend_line(board, location)

    def just_defend_line(self, board, location):
        x = location[0]
        y = location[-1]
        i1, j1 = x
        i2, j2 = y
        j1 = j1 - 1
        j2 = j2 + 1
        x = i1, j1
        y = i2, j2
        return self.closer_to_center(board, x, y, i1, i2, j1, j2)

    def block_possible_line(self, board, location):
        x = location[0]
        i, j = x
        if j != 0:
            if board[i][j - 1] == 0:
                return True
        x = location[-1]
        i, j = x
        if j != 14:
            if board[i][j + 1] == 0:
                return True
        return False

    def block_win_line(self, board, location):
        x = location[0]
        i1, j1 = x
        j1 = j1 - 1
        x = i1, j1
        y = location[3]
        i2, j2 = y
        j2 = j2 + 1
        y = i2, j2
        return self.closer_to_center(board, x, y, i1, i2, j1, j2)

    def defend_column(self, board, location):
        if len(location) == 4:
            if self.block_possible_column(board, location):
                return self.block_win_column(board, location)
        else:
            gap = self.get_gap_column(board, 1)
            if gap != False:
                return gap
            else:
                return self.just_defend_column(board, location)

    def block_possible_column(self, board, location):
        x = location[0]
        i, j = x
        if i != 0:
            if board[i - 1][j] == 0:
                return True
        x = location[-1]
        i, j = x
        if i != 14:
            if board[i + 1][j] == 0:
                return True
        return False

    def block_win_column(self, board, location):
        x = location[0]
        i1, j1 = x
        i1 = i1 - 1
        x = i1, j1
        y = location[3]
        i2, j2 = y
        i2 = i2 + 1
        y = i2, j2
        return self.closer_to_center(board, x, y, i1, i2, j1, j2)

    def just_defend_column(self, board, location):
        x = location[0]
        y = location[-1]
        i1, j1 = x
        i2, j2 = y
        i1 = i1 - 1
        i2 = i2 + 1
        x = i1, j1
        y = i2, j2
        return self.closer_to_center(board, x, y, i1, i2, j1, j2)

    def defend_diagonal(self, board, location):
        if len(location) == 4:
            if self.block_possible_diagonal(board, location):
                return self.block_win_diagonal(board, location)
        else:
            return self.just_defend_diagonal(board, location)

    def block_possible_diagonal(self, board, location):
        x = location[0]
        i, j = x
        if i != 0 and j != 0:
            if board[i - 1][j - 1] == 0:
                return True
        x = location[-1]
        i, j = x
        if i != 14 and j != 14:
            if board[i + 1][j + 1] == 0:
                return True
        return False

    def block_win_diagonal(self, board, location):
        x = location[0]
        i1, j1 = x
        if j1 != 0:
            i1 = i1 - 1
            j1 = j1 - 1
        x = i1, j1
        y = location[3]
        i2, j2 = y
        if i2 != 14:
            i2 = i2 + 1
            j2 = j2 + 1
        y = i2, j2
        return self.closer_to_center(board, x, y, i1, i2, j1, j2)

    def just_defend_diagonal(self, board, location):
        x = location[0]
        y = location[-1]
        i1, j1 = x
        i2, j2 = y
        if j1 != 0:
            i1 = i1 - 1
            j1 = j1 - 1
        if i2 != 14:
            i2 = i2 + 1
            j2 = j2 + 1
        x = i1, j1
        y = i2, j2
        return self.closer_to_center(board, x, y, i1, i2, j1, j2)

    def find_move(self, board, player):
        for i in range(1, 14):
            for j in range(1, 14):
                if board[i][j] != 0:
                    if board[i][j].player != player:
                        if board[i][j - 1] == 0:
                            poz = i, j - 1
                            return poz
                        else:
                            if board[i][j + 1] == 0:
                                poz = i, j + 1
                                return poz
                            else:
                                if board[i - 1][j] == 0:
                                    poz = i - 1, j
                                    return poz
                                else:
                                    poz = i + 1, j
                                    return poz

    def need_defence(self, board, location, lcd):
        if lcd == 1:
            move = self.defend_line(board, location)
        elif lcd == 2:
            move = self.defend_column(board, location)
        else:
            move = self.defend_diagonal(board, location)
        return move
