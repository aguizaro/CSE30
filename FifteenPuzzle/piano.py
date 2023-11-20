from tkinter import *
import pygame

def play_C(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound('../Music_Notes/Piano/C.wav') # file path depends on where you place the file 
    sound.play()

def play_D(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound('../Music_Notes/Piano/D.wav')
    sound.play()
    
def play_C_sharp(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound('../Music_Notes/Piano/C_s.wav')
    sound.play()

# main program
gui = Tk()           # make a GUI window
topframe = Frame(gui, width=20, height=5)
topframe.grid(column=0, row=0)
bottomframe = Frame(gui, width=20, height=15)
bottomframe.grid(column=0, row=1)


# white keys
button1 = Button(bottomframe, width=3, height=10, bg='ivory', )
button1.bind('<Button-1>', play_C)
button1.grid(column=0, row=0, columnspan=2, rowspan=3)

button3 = Button(bottomframe, width=3, height=10, bg='ivory')
button3.bind('<Button-1>', play_D)
button3.grid(column=2, row=0, columnspan=2, rowspan=3)

# black keys
button2 = Button(bottomframe, width=2, height=7, foreground='black')
button2.bind('<Button-1>', play_C_sharp)
button2.grid(column=1, row=0, columnspan=2, rowspan=2)

# white keys
button1 = Button(bottomframe, width=3, height=10, bg='ivory', )
button1.bind('<Button-1>', play_C)
button1.grid(column=3, row=0, columnspan=2, rowspan=3)

button3 = Button(bottomframe, width=3, height=10, bg='ivory')
button3.bind('<Button-1>', play_D)
button3.grid(column=5, row=0, columnspan=2, rowspan=3)

# black keys
button2 = Button(bottomframe, width=2, height=7, foreground='black')
button2.bind('<Button-1>', play_C_sharp)
button2.grid(column=4, row=0, columnspan=2, rowspan=2)

# white keys
button1 = Button(bottomframe, width=3, height=10, bg='ivory', )
button1.bind('<Button-1>', play_C)
button1.grid(column=6, row=0, columnspan=2, rowspan=3)

button3 = Button(bottomframe, width=3, height=10, bg='ivory')
button3.bind('<Button-1>', play_D)
button3.grid(column=8, row=0, columnspan=2, rowspan=3)

# black keys
button2 = Button(bottomframe, width=2, height=7, foreground='black')
button2.bind('<Button-1>', play_C_sharp)
button2.grid(column=7, row=0, columnspan=2, rowspan=2)


mainloop()