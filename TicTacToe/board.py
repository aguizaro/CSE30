'''
PA2 by Antonio Guizar Orozco
Board class used for tictac.py
Simulates a classic tic tac toe board
'''
class Board:
    def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.board = list(self.sign * 9)
            # the winner's sign O or X
            self.winner = ""
            self.moves= ['A1','B1','C1','A2','B2','C2','A3','B3','C3']
    #accessor function
    def get_winner(self):
        return self.winner
    #Mutator function
    def set(self, cell, sign):
        # mark the cell on the board with the sign X or O
        for i in range(len(self.moves)):
            if self.moves[i] == cell.upper():
                self.board[i] = sign        

    #checks if that cell on the board is empty
    def isempty(self, cell):
        for i in range(len(self.moves)):
            if self.moves[i] == cell.upper():
                # return True if the cell is empty (not marked with X or O)
                if self.board[i] == ' ':
                    return True
        return False

    # check all game terminating conditions, if one of them is present, assign the var done to True
    # depending on conditions assign the instance var winner to O or X
    def isdone(self):
        done = False
        self.winner = ''
         #check all horizontal conditions
        if (self.board[0] == self.board[1] == self.board[2]) and self.board[0] != ' ':
            self.winner= self.board[0] 
            done= True
        elif (self.board[3] == self.board[4] == self.board[5]) and self.board[3] != ' ':
            self.winner= self.board[3] 
            done= True
        elif (self.board[6] == self.board[7] == self.board[8]) and self.board[6] != ' ':
            self.winner= self.board[6] 
            done= True
        #check all diagonals
        elif (self.board[0] == self.board[4] == self.board[8]) and self.board[0] != ' ':
            self.winner= self.board[0] 
            done= True
        elif (self.board[6] == self.board[4] == self.board[2]) and self.board[6] != ' ':
            self.winner= self.board[6] 
            done= True
        #check all vertical conditions
        elif (self.board[0] == self.board[3] == self.board[6]) and self.board[0] != ' ':
            self.winner= self.board[0] 
            done= True
        elif (self.board[1] == self.board[4] == self.board[7]) and self.board[1] != ' ':
            self.winner= self.board[1] 
            done= True
        elif (self.board[2] == self.board[5] == self.board[8]) and self.board[2] != ' ':
            self.winner= self.board[2] 
            done= True
        #condition where there is a draw
        if ' ' not in self.board:
            return True
        else:
            return done

    #displays the board in its current condition
    def show(self):
        # draw the board
        print(f'\n   A   B   C\n +---+---+---+\n1| {self.board[0]} | {self.board[1]} | {self.board[2]} |\n +---+---+---+\n2| {self.board[3]} | {self.board[4]} | {self.board[5]} |\n +---+---+---+\n3| {self.board[6]} | {self.board[7]} | {self.board[8]} |\n +---+---+---+')

    