import random
from game import game
import copy

class auto_player:
    def __init__(self, value, lc):
        self.moves=[]
        self.history=[]
        self.training_egs=[]
        self.mark = value
        self.weights=[]
        self.tiemoves=[]
        self.lc= lc

    def set_weights(self, weights):
        self.weights=copy.deepcopy(weights)

    def set_game(self, game):
        self.cgame=game


    def get_moves(self):
        cur_board = copy.deepcopy(self.cgame.cur_board())

        self.moves=[]
        for i in range(3):
            for j in range(3):
                if cur_board[i][j] == 0 :
                    move=[i,j]
                    self.moves.append(move)

    def evaluate_board(self, board):
        x1, x2, x3, x4, x5, x6 = self.cgame.get_board_features(board)
        w0, w1, w2, w3, w4, w5, w6 = self.weights
        return w0 + x1*w1 + x2*w2 + x3*w3 + x4*w4 + x5*w5 + x6*w6

    def choose_move(self):
        cur_board = self.cgame.cur_board()
        temp_board = copy.deepcopy(cur_board)
        max_value = float("-inf")
        cur_value=0.0
        self.tiemoves = []
        self.get_moves()

        for move in self.moves:
            temp_board = copy.deepcopy(cur_board)
            cur_value = 0
            temp_board[move[0]][move[1]] = self.mark
            cur_value=self.evaluate_board(temp_board)
            if(cur_value > max_value):
                max_value=cur_value
                self.tiemoves = []
                self.tiemoves.append(move)

            elif cur_value == max_value:
                self.tiemoves.append(move)


        if len(self.tiemoves) == 1:
            self.cgame.set_square(self.mark,self.tiemoves[0][0],self.tiemoves[0][1])
        else:

            try:
                r = random.randint(0,len(self.tiemoves)-1)
            except ValueError,ve:
                r=0
            try:
                self.cgame.set_square(self.mark, self.tiemoves[r][0], self.tiemoves[r][1])
            except IndexError, ie:
                print "do nothing"

        cur_board = self.cgame.cur_board()

        #self.history.append(cur_board)



    def gen_training_egs(self):
        self.training_egs=[]
        self.history=copy.deepcopy(self.cgame.gh)

        for i in range(0,len(self.history)):
            hboard=copy.deepcopy(self.history[i])
            self.cgame.board = copy.deepcopy(hboard)
            if self.cgame.isdone():
                if self.cgame.winner == self:
                    self.training_egs.append([hboard,100])
                elif self.cgame.winner == 0:
                    self.training_egs.append(([hboard,0]))
                else:
                    self.training_egs.append([hboard,-100])

            else:
                nextboard=copy.deepcopy(self.history[i+1])
                self.training_egs.append([hboard,self.evaluate_board(nextboard)])


    def adjust_weights(self):
        self.gen_training_egs()
        for example in self.training_egs:
            cur_board= copy.deepcopy(example[0])
            vtrain = example[1]
            features= self.cgame.get_board_features(cur_board)
            vesti = self.evaluate_board(cur_board)
            for i in range(1,7):
                self.weights[i]=self.weights[i]+self.lc*(vtrain - vesti)*features[i-1]
                if self.weights[i] == float("nan"):
                    print "just waiting"



class manual_player:
    def __init__(self, value):
        self.mark = value

    def set_game(self, game):
        self.cgame=game

    def get_input(self):
        self.x=int(raw_input("Enter X: "))
        self.y = int(raw_input("Enter Y: "))

    def choose_move(self):
        self.get_input()
        self.cgame.set_square(self.mark,self.x,self.y)

class random_player:
    def __init__(self, value):
        self.mark = value
        self.moves=[]

    def set_game(self, game):
        self.cgame=game


    def get_moves(self):
        cur_board = copy.deepcopy(self.cgame.cur_board())

        self.moves=[]
        for i in range(3):
            for j in range(3):
                if cur_board[i][j] == 0 :
                    move=[i,j]
                    self.moves.append(move)

    def choose_move(self):
        self.get_moves()
        self.x = self.moves[random.randint(0,len(self.moves)-1)][0]
        self.y = self.moves[random.randint(0, len(self.moves) - 1)][1]
        self.cgame.set_square(self.mark, self.x, self.y)
