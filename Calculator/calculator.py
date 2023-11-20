'''
PA4 Antonio Guizar Orozco 11-20-2022
This program will take a mathematical expression by the user and print the resilt of the calculation
This program makes use of class Stack for our conversions and class ExpTree to make a tree and traverse it for calculations
'''
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

# a driver to test calculate module
if __name__ == '__main__':
    print('Welcome to Calculator Program!')
    while(True):
        try:
            user_input= str(input("Please enter your expression here. To quit enter 'quit' or 'q':\n"))
            if user_input == 'q' or user_input == 'quit':
                break
            #print result of calculation as a decimal wrapped in a string
            print(float(calculate(user_input)))
        except (ValueError, TypeError):
            pass
    print('Goodbye!')

    '''
    # test infix_to_postfix function
    print(infix_to_postfix('(5+2)*3'))
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    print(infix_to_postfix('5+2*3'))
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'
    #test floating point
    print(infix_to_postfix('15.1+2.9*3.3'))
    assert infix_to_postfix('15.1+2.9*3.3') == '15.1 2.9 3.3 * +'

    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0
    print(calculate('((5*3)+5)*2.5'))
    print('No assert errors :)')
    '''
    
