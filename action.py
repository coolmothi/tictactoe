from player import auto_player
from player import manual_player
from player import random_player
from game import game
import copy

nog=1000
p1wins =0
p2wins = 0
draws = 0
board_no =1
p1weights=[.5,.5,.5,.5,.5,.5,.5]
p2weights=[.5,.5,.5,.5,.5,.5,.5]

def getweightsfromfile():
    fp=open("weights.txt","r")
    ws = fp.readline()
    global p1weights
    global p2weights
    weight_strings=ws.rsplit(" ")
    for i in range(7):
        p1weights[i]=float(weight_strings[i])


    ws = fp.readline()
    weight_strings = ws.rsplit(" ")
    for i in range(7):
        p2weights[i] = float(weight_strings[i])

    fp.close()


def write_weights():
    fp = open("weights.txt", "w")
    global p1weights
    global  p2weights

    for i in range(7):
        fp.write(str(p1weights[i])+" ")
    fp.write("\n")


    for i in range(7):
        fp.write(str(p2weights[i]) + " ")

    fp.close()




def train_vs_random():
    for i in range(nog):
        p1= auto_player(1,0.0005)
        p2= random_player(2)
        global p1weights
        global board_no
        g = game(p1,p2)

        p1.set_game(g)
        p2.set_game(g)

        getweightsfromfile()
        p1.set_weights(p1weights)

        while True:
            p1.choose_move()
            if(g.isdone()):
                g.final_board=copy.deepcopy(g.board)
                print board_no
                board_no += 1
                g.print_board(g.final_board)
                break
            p2.choose_move()
            if (g.isdone()):
                g.final_board = copy.deepcopy(g.board)
                print board_no
                board_no += 1
                g.print_board(g.final_board)
                break

        p1.adjust_weights()

        p1weights = copy.deepcopy(p1.weights)

        if g.winner == p1:
            global p1wins
            p1wins += 1
        elif g.winner == p2:
            global p2wins
            p2wins +=1
        else:
            global draws
            draws +=1

        print "\n\n\n"
    write_weights()
    print " Run summary"
    print " Player 1 wins = "+str(p1wins)
    print " Player 2 wins = "+str(p2wins)
    print " Draws = "+str(draws)

    print " Weights"
    print " p1 weights: "
    print p1weights
    print " p2 weights: "
    print p2weights

    print " P1 win percentage\n"
    print str(p1wins/nog)+"%"


def train_vs_player():
    for i in range(nog):
        p1= auto_player(1,0.005)
        p2= auto_player(2,0.1)
        global p1weights
        global p2weights
        global board_no
        g = game(p1,p2)

        p1.set_game(g)
        p2.set_game(g)
        getweightsfromfile()
        p1.set_weights(p1weights)
        p2.set_weights(p2weights)

        while True:
            p1.choose_move()
            if(g.isdone()):
                g.final_board=copy.deepcopy(g.board)
                print board_no
                board_no += 1
                g.print_board(g.final_board)
                break
            p2.choose_move()
            if (g.isdone()):
                g.final_board = copy.deepcopy(g.board)
                print board_no
                board_no += 1
                g.print_board(g.final_board)
                break

        p1.adjust_weights()
        p2.adjust_weights()

        p1weights = copy.deepcopy(p1.weights)
        p2weights = copy.deepcopy(p2.weights)

        if g.winner == p1:
            global p1wins
            p1wins += 1
        elif g.winner == p2:
            global p2wins
            p2wins +=1
        else:
            global draws
            draws +=1

        print "\n\n\n"
    write_weights()
    print " Run summary"
    print " Player 1 wins = "+str(p1wins)
    print " Player 2 wins = "+str(p2wins)
    print " Draws = "+str(draws)

    print " Weights"
    print " p1 weights: "
    print p1weights
    print " p2 weights: "
    print p2weights

def play_manual():
    p1=auto_player(1,0.005)
    p2=manual_player(2)
    global p1weights
    g=game(p1,p2)

    p1.set_game(g)
    p2.set_game(g)
    getweightsfromfile()
    p1.set_weights(p1weights)

    while True:
        p1.choose_move()
        g.print_board(g.cur_board())
        if(g.isdone()):
            g.final_board=copy.deepcopy(g.board)
            g.print_board(g.final_board)
            break
        p2.choose_move()
        if (g.isdone()):
            g.final_board = copy.deepcopy(g.board)
            g.print_board(g.final_board)
            break


    p1.adjust_weights()
    write_weights()
    print p1.weights


#train_vs_random()
#play_manual()

train_vs_player()