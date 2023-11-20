'''
PA2 by Antonio Guizar Orozco
Player classes used for tictac.py
Includes Player Class, AI class(subclass of Player) and MiniMax class(subclass of AI)
Simulates a tic tac toe player
'''
from random import choice

class Player:
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X
    #accessor functions
    def get_sign(self):
        return self.sign
    def get_name(self):
        return self.name

    #prompts the player to choose a move and writes it to the board
    def choose(self, board):
        again= True
        while(again):
            try:
                # prompt the user to choose a cell
                cell= str(input(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n')).upper()
                if not len(cell) == 2: #if len too short or too long
                    raise ValueError
                elif not cell[0].isalpha(): #Check first character is a letter
                    raise ValueError
                elif not cell[1].isdigit(): #check second char is a number
                    raise ValueError
                elif ord(cell[0]) < 65 or ord(cell[0]) > 67: #Check colums between A-C
                    raise ValueError
                elif int(cell[1]) < 1 or int(cell[1]) > 3: #Check row between 1-3
                    raise ValueError
                elif not board.isempty(cell): #check if cell is empty
                    raise ValueError
                else: # if the user enters a valid string and the cell on the board is empty, update the board
                    board.set(cell,self.sign)
                    again= False
            except (ValueError):
                print('You did not choose correctly.')

#This AI will choose random spots on the board to fill
class AI(Player):
    def __init__(self, name, sign):
        super().__init__(name, sign)
        self.moves= ['A1','B1','C1','A2','B2','C2','A3','B3','C3']
    #overriden choose class for AI objects
    def choose(self, board):
        again= True
        print(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n')
        #chooses a random empty spot on the board and marks it
        while(again):
            cell= choice(self.moves)
            if board.isempty(cell):
                board.set(cell, self.sign)
                self.moves.remove(cell)
                again= False

#This AI will choose the best move calculated using recursion
class MiniMax(AI):
    def __init__(self, name, sign, opponent_sign):
        super().__init__(name, sign,)
        self.opponent_sign= opponent_sign
        self.moves= ['A1','B1','C1','A2','B2','C2','A3','B3','C3']

    #returns a cell on the board that corresponds to the best move for the current state of the game
    def minimax(self, board, self_player, start):
        move=''
        min_score, max_score= 10, -10
        if board.isdone(): #base case
            if board.get_winner() == self.sign: return 1 #return 1 if self won
            elif board.get_winner() ==' ': return 0 #return 0 if its a tie
            else: return -1 #return -1 if self lost
        else:
            if self_player: #minimax for P1
                for m in self.moves:
                    if board.isempty(m):
                        board.set(m, self.sign)
                        score= self.minimax(board, False, False)
                        board.set(m, ' ')
                        if score > max_score:
                            max_score= score
                            move= m
            else: #minimax for P2
                for m in self.moves:
                    if board.isempty(m):
                        board.set(m, self.opponent_sign)
                        score= self.minimax(board, True, False)
                        board.set(m, ' ')
                        if score < min_score:
                            min_score= score
                            move=m
            #return correct values based on whose turn it is      
            if start: return move
            elif self_player: return max_score
            else: return min_score

#overriden choose method for MiniMax objects
    def choose(self, board):
        print(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')
        board.set(self.minimax(board,True,True), self.sign)
    
