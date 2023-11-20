'''
PA4 EC by Antonio Guizar Orozco 12-04-2022
Calculator program using my own calculate method insstead of python built in eval method
'''
# create a GUI calculator using tkinter
from tkinter import *


from stack import Stack
from tree import ExpTree

#converts expression in infix notation to postfix notation
def infix_to_postfix(infix):
    precedence= {'^': 3,'*': 2, '/': 2, '+': 1, '-': 1 , '(': 0}
    operators= ['+', '-', '*', '/', '^', '(', ')']
    s= Stack()
    postfix=[]
    number= ''
    for input in infix:
        if input not in operators: #push operands to postfix output
            number+= input
            #if last element is a digit append it to postfix
            if infix.find(input) == len(infix) -1:
                postfix.append(number) if number else None
                number=''
            
        else: #if input is an operator
            postfix.append(number) if number else None
            number= ''
            if s.isEmpty():
                s.push(input)

            elif input == '(': #push if openening parenthesis
                s.push(input)
            elif input == ')': #if closing parenthesis, pop everything to postfix until you find opening parenthesis
                while not s.peek() == '(':
                    postfix.append(s.pop())
                s.pop() #pop oppening parenthesis without adding to postfix
            #push input operator to the stack if it has higher precedence than top of stack
            elif precedence[input] > precedence[s.peek()]:
                s.push(input)
            #if input operator has lower precedence than top of stack, pop the top of stack and add to output
            elif precedence[input] < precedence[s.peek()]:
                postfix.append(s.pop())
                #continue this until precedence of input is higher or equal to precedence of top of stack
                p= check_precedence(s,input)
                postfix.append(p) if p else None
            elif precedence[input] == precedence[s.peek()]:
                #if not L to R then push to stack
                if s.peek() == '^': #This is the only R to L operator
                    s.push(input)
                else:
                    postfix.append(s.pop())
                    p= check_precedence(s,input)
                    postfix.append(p) if p else None
            
    #pop remaining operators in stack to postfix
    postfix.append(number) if number else None
    while not s.isEmpty():
        postfix.append(s.pop())
    
    return ' '.join(postfix)

#checks which operator has higher precidence 
def check_precedence(s, input):
    precedence= {'^': 3,'*': 2, '/': 2, '+': 1, '-': 1 , '(': 0}
    postfix=''
    #continue this until precedence of input is higher or equal to precedence of top of stack
    while not s.isEmpty():
        if input == '(': #push if openening parenthesis
            s.push(input)
        elif precedence[input] < precedence[s.peek()]:
            postfix+= ' ' + s.pop()
        elif precedence[input] > precedence[s.peek()]:
            s.push(input)
            return postfix
        elif precedence[input] == precedence[s.peek()]:
            #if not L to R then push to stack
            if s.peek() == '^': #This is the only R to L operator
                s.push(input)
            else:
                postfix+= ' ' + s.pop()
                posttfix+= ' ' + check_precedence(s, input)
    if s.isEmpty():
        s.push(input)
    return postfix
#takes infix expression and returns the result of the calculation
def calculate(infix):
    postfix= infix_to_postfix(infix)
    tree= ExpTree.make_tree(postfix)
    return ExpTree.evaluate(tree)


def calculator(gui):   
    # name the gui window
    gui.title("Calculator")
    # make a entry text box
    entrybox = Entry(gui, width=36, borderwidth=5)
    # position the entry text box in the gui window using the grid manager
    entrybox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    
    # create buttons: 1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,= 
    b0 = addButton(gui,entrybox,'0')
    b1 = addButton(gui,entrybox,'1')
    b2 = addButton(gui,entrybox,'2')
    b3 = addButton(gui,entrybox,'3')
    b4 = addButton(gui,entrybox,'4')
    b5 = addButton(gui,entrybox,'5')
    b6 = addButton(gui,entrybox,'6')
    b7 = addButton(gui,entrybox,'7')
    b8 = addButton(gui,entrybox,'8')
    b9 = addButton(gui,entrybox,'9')
    b_add = addButton(gui,entrybox,'+')
    b_sub = addButton(gui,entrybox,'-')
    b_mult = addButton(gui,entrybox,'*')
    b_div = addButton(gui,entrybox,'/')
    b_clr = addButton(gui,entrybox,'c')
    b_eq = addButton(gui,entrybox,'=')

    # add buttons to the grid
    buttons =[ b7,    b8, b9,    b_clr, 
               b4,    b5, b6,    b_sub, 
               b1,    b2, b3,    b_add, 
               b_mult,b0, b_div, b_eq ]
    k = 4           
    for i in range(k):
        for j in range(k):
            buttons[i*k+j].grid(row=i+1, column=j, columnspan=1)

def addButton(gui, entrybox, value):
    return Button(gui, text=value, height=4, width=9, command = lambda: clickButton(entrybox, value))

def clickButton(entrybox, value):
    if value == 'c':
        entrybox.delete(0, len(entrybox.get()))
    elif value == '=':
        current= entrybox.get()
        entrybox.delete(0, len(entrybox.get()))
        try:
            entrybox.insert(0,calculate(current))
        except (ValueError, TypeError, ZeroDivisionError):
            pass
    else:
        entrybox.insert(len(entrybox.get()), value)
    
# main program
# create the main window
gui = Tk()
# create the calculator layout
calculator(gui)
# update the window
gui.mainloop()