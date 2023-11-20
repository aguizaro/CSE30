''' 
PA4 by Antonio Guizar Orozco  12-02-2022
This program simulates a 15 puzzle game. Fifteen used in game.py to play the game in a GUI window
'''
from random import choice

class Fifteen:
        # tiles are numbered 1-15, the last tile is 0 (an empty space)
    def __init__(self, size = 4):
        self.tiles = [i for i in range(1,size**2)]
        self.tiles.append(0)
    
    # update the list of tiles
    def update(self, move):
        if self.is_valid_move(move):
            self.transpose(0, move)

    # exchange i-tile with j-tile  
    # tiles are numbered 1-15, the last tile is 0 (empty space) 
    def transpose(self, i, j):
        index_i= self.tiles.index(i)
        index_j= self.tiles.index(j)

        self.tiles[index_i], self.tiles[index_j] = self.tiles[index_j], self.tiles[index_i]
    
    # shuffle tiles
    def shuffle(self, steps=100):
        valid_moves= []
        for tile in self.tiles:
            if self.is_valid_move(tile):
                valid_moves.append(tile)

        index = self.tiles.index(0)
        for i in range(steps):
            while True:
                move_index = choice(range(1,15 + 1))
                if self.is_valid_move(move_index):
                    break
            self.tiles[index],self.tiles[move_index] = self.tiles[move_index],self.tiles[index]
            index = move_index
        
    # checks if the move is valid: one of the tiles is 0 and another tile is its neighbor    
    def is_valid_move(self, move):
        #check if move is above,below, or to the side of blank tile
        index_0= self.tiles.index(0) #index of blank tile
        try: #if move is not on board
            index_move= self.tiles.index(move)
        except ValueError:
            return False
        #check if move is on right side
        if index_move == index_0 + 1:
            return True 
        #check if move is on left side
        if index_move == index_0 - 1:
            return True
        #check if move is above
        if index_move == index_0 - 4:
            return True
        #check if move is below
        if index_move == index_0 + 4:
            return True
        return False

    # verify if the puzzle is solved
    def is_solved(self):
        if self.tiles[-1] != 0:
            return False
        for i in range(len(self.tiles)-2):
            if self.tiles[i] > self.tiles[i+1]:
                return False
        return True

    # draw the layout with tiles:
    # +---+---+---+---+
    # | 1 | 2 | 3 | 4 |
    # +---+---+---+---+
    # | 5 | 6 | 7 | 8 |
    # +---+---+---+---+
    # | 9 |10 |11 |12 |
    # +---+---+---+---+
    # |13 |14 |15 |   |
    # +---+---+---+---+
    def draw(self):
        index= 0
        string='# +---+---+---+---+\n# |'
        for tile in self.tiles:
            if tile > 9:
                if tile == 0: tile= ' '
                string+= str(tile) + ' |'
            else:
                if tile == 0: tile= ' '
                string+= ' ' + str(tile) + ' |'
            index+=1
            if index % 4 == 0:
                string+= '\n# +---+---+---+---+\n# |'
        print(string[:-4])

    # return a string representation of the vector of tiles as a 2d array  
    # 1  2  3  4
    # 5  6  7  8
    # 9 10 11 12
    #13 14 15    
    def __str__(self):
        index= 0
        string= ''
        for i in range(4):
            for j in range(4):
                if self.tiles[index] == 0:
                    string+= '   '
                elif self.tiles[index] > 9:
                    string+= str(self.tiles[index]) + ' '

                else:
                    string+= ' ' + str(self.tiles[index]) + ' '
                index+=1
            string+= '\n'
        return string

#driver code to run the puzzle game
if __name__ == '__main__':
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')

    
    
        
