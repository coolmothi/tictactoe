import copy

class game:
    def __init__(self, X_player, O_player):
        self.board=[[0, 0, 0], [0,0,0], [0, 0, 0]]
        self.xp = X_player
        self.op = O_player
        self.winner = 0
        self.final_board=[[0, 0, 0], [0,0,0], [0, 0, 0]]
        self.gh=[]
        self.gh.append(self.board)

    def set_square(self, value, x , y):
        self.board[x][y]=value
        self.gh.append(copy.deepcopy(self.board))

    def cur_board(self):
        return self.board


    def check_forwin(self, value):
        won = False
        for i in range(3):
            if self.board[i][0] == value and self.board[i][1] == value and self.board[i][2] == value:
                won = True
                break
            if self.board[0][i] == value and self.board[1][i] == value and self.board[2][i] == value:
                won = True
                break
            if self.board[0][0] == value and self.board[1][1] == value and self.board[2][2] == value:
                won = True
                break
            if self.board[0][2] == value and self.board[1][1] == value and self.board[2][0] == value:
                won = True
                break

        if won:
            if value == 1:
                self.winner = self.xp
                return True
            else:
                self.winner = self.op
                return True
        else:
            return False




    def isdone(self):

        if self.check_forwin(1):
            return True

        if self.check_forwin(2):
            return True

        done = True

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    done = False
                    break

            if not done:
                break
        if done:
            self.winner = 0
            return True

        else:
            return False

    def get_row_pointer_count(self, board, value, num):
        c = 0
        rc = 0
        zc = 0
        for i in range(3):
            c = 0
            zc = 0
            for j in range(3):
                if board[i][j] == value:
                    c = c + 1
                if board[i][j] == 0:
                    zc = zc + 1
            if c == num and zc == 3 - num:
                rc = rc + 1

        return rc

    def get_col_pointer_count(self, board, value, num):
        c = 0
        rc = 0
        for i in range(3):
            c = 0
            zc = 0
            for j in range(3):
                if board[j][i] == value:
                    c = c + 1
                if board[j][i] == 0:
                    zc = zc + 1
            if c == num and zc == 3 - num:
                rc = rc + 1

        return rc

    def get_diagonal_pointer_count(self, board, value, num):
        c = 0
        rc = 0
        zc = 0
        if board[0][0] == value:
            c = c + 1
        elif board[0][0] == 0:
            zc = zc + 1

        if board[1][1] == value:
            c = c + 1
        elif board[1][1] == 0:
            zc = zc + 1

        if board[2][2] == value:
            c = c + 1
        elif board[2][2] == 0:
            zc = zc + 1

        if c == num and zc == 3 - num:
            rc = rc + 1

        c = 0
        zc = 0
        if board[0][2] == value:
            c = c + 1
        elif board[0][2] == 0:
            zc = zc + 1

        if board[1][1] == value:
            c = c + 1
        elif board[1][1] == 0:
            zc = zc + 1

        if board[2][0] == value:
            c = c + 1
        elif board[2][0] == 0:
            zc = zc + 1

        if c == num and zc == 3 - num:
            rc = rc + 1

        return rc

    def poniter_count(self, board, value, num):
        return self.get_row_pointer_count(board, value, num) + self.get_col_pointer_count(board, value, num)+self.get_diagonal_pointer_count(board, value, num)






    def get_board_features(self, board):
        x1 = self.poniter_count(board, 1, 2)
        x2 = self.poniter_count(board, 2, 2)
        x3 = self.poniter_count(board, 1, 3)
        x4 = self.poniter_count(board, 2, 3)
        x5 = self.poniter_count(board, 1, 1)
        x6 = self.poniter_count(board, 2, 1)

        return x1, x2, x3, x4, x5, x6


    def print_board(self, board):
        rowres=''
        for i in range(3):
            rowres=''
            for j in range(3):
                if board[i][j] == 1:
                    rowres= rowres+" x |"
                elif board[i][j] == 2:
                    rowres= rowres+" 0 |"
                else:
                    rowres= rowres+"   |"

            print rowres
            print 12*"-"