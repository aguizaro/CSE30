''' 
PA5 by Antonio Guizar Orozco 12-02-2022
This program will play a fifteen puzzle game in a GUI window using tkinter
'''

from tkinter import *
from fifteen import Fifteen
          
#if the shuffle button is clicked, the game will shuffle the tiles and make a new board
def click_shuffle(game, master):
    game.shuffle()
    make_buttons(game,master)
    gui.update()

#if the quit button is clicked, the gui window is destroyed and program ends
def click_quit(master):
    global over
    master.destroy()
    over= True

#if a tile button has been clicked, it will move the tile if its a valid move
def clickButton(game, btn, tile):
    global empty_button
    if game.is_valid_move(tile):
        #save current positions of buttons to be swapped
        btn_position= btn.grid_info()
        e_btn_position= empty_button.grid_info()
        game.update(tile) #update the game
        #swap the positions of the buttons
        btn.grid(row=e_btn_position['row'], column= e_btn_position['column'])
        empty_button.grid(row=btn_position['row'], column=btn_position['column'])

#makes the buttons and positions them on the board 
def make_buttons(game, master):
    global empty_button
    #delete previous tile buttons if there are any
    if master.grid_slaves():
        list= master.grid_slaves()
        for tile in list:
            tile.destroy()
    #make new tile buttons after shuffle
    rowindex,colindex= 0, 0

    #make a grid of tiles as buttons 
    for tile in game.tiles:
        
        if colindex % 4 == 0:  #update row and column placement of buttons
            rowindex+=1
            colindex= 0
        if tile == 0: tile= '' #make the empty tile apear empty
        b= Button(gui, text= tile, height=5, width= 7)
        b.config(command= lambda g= game, x=b, y=tile,: clickButton(g,x,y))
        b.grid(row= rowindex, column= colindex)
        colindex+=1

        if tile == '': empty_button= b #save empty button outside for loop

    #make shuffle and quit buttons
    shuffle= Button(gui, text= 'Shuffle', height=3, width= 5, foreground='blue')
    shuffle.config(command= lambda g= game, x=gui,: click_shuffle(g,x))
    shuffle.grid(row= 5, column= 1)

    quit= Button(gui, text= 'Quit', height=3, width= 5, foreground= 'red')
    quit.config(command= lambda x=gui : click_quit(x))
    quit.grid(row= 5, column= 2)

if __name__ == '__main__':
    # make a GUI window
    gui = Tk()
    gui.title('Fifteen Puzzle')
    gui.geometry('400x440')
    game= Fifteen() #make game object
    game.shuffle()
    empty_button='' #global var used to store button of empty tile
    make_buttons(game,gui) #make and arrange all the buttons

    over= False
    while not over: #keep updating the window as long as the game is not over
        gui.update()
        if game.is_solved(): #if the puzzle is solved, print winner and disable tile buttons
            label= Label(gui, text= "YOU WIN!", font=("Helvetica", 20), foreground='white')
            label.grid(row=5, column=0)
            #do not disable the shuffle or quit buttons or the winner label
            list= gui.grid_slaves()
            list.remove(list[-17])
            list.remove(list[-17])
            list.remove(list[0])
            #disable all tile buttons when the game is won
            for tile in list:
                tile['state'] = 'disabled'
            gui.update()
    

