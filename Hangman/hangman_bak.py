

# assignment: programming assignment 1
# author: Antonio Guizar Orozco
# date: 10-6-2022
# file: hangman.py is a program that will play a hangman game where the user may decide word length, number of
# lives and may decide to play again after the game is finished
# input: takes input from STDIN
# output: prints to STDOUT
from random import choice, random

dictionary_file = "dictionary-short.txt"   # make a dictionary.txt in the same folder where hangman.py is located

def import_dictionary (filename) :
    dictionary = {2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}
    word_len=0
    max_size = 12
    min_size = 3
    with open(filename) as read_file:
        for line in read_file:
            word= line.strip()
            word_len= len(word)
            if word_len <= max_size and word_len >= min_size - 1:
                dictionary[word_len].append(line.strip())
    return dictionary

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options () :
    max_size= 12
    min_size= 3
    max_lives= 10
    min_lives= 1
    try :
        word_size= int(input('Please choose a size of a word to be guessed [3 - 12, default any size]:\n'))
        if word_size not in range(min_size, max_size + 1):
            raise ValueError
        else:
            print(f'The word size is set to {word_size}.')        
    except (ValueError, TypeError) :
        print('A dictionary word of any size will be chosen.')
        word_size= choice(list(dictionary))
        print('Please choose a number of lives [1 - 10, default 5]:\n')
        print('You have 5 lives.')
        num_lives= 5;
        return (word_size, num_lives)
    try:
        num_lives= int(input('Please choose a number of lives [1 - 10, default 5]:\n'))
        if (num_lives not in range(min_lives,max_lives + 1)):
            raise ValueError
        else:
            print(f'You have {num_lives} lives.')
    except (ValueError, TypeError):
        print('You have 5 lives.')
        num_lives= 5

    return (word_size, num_lives)

def print_board(chosen_letters_, hidden_word_, num_lives_, health_bar_):
    # format and print the game interface:
        # Letters chosen: E, S, P                list of chosen letters
        # __ P P __ E    lives: 4   XOOOO        hidden word and lives
        print('Letters chosen: ', end='')
        print(', '.join(chosen_letters_)) if chosen_letters_ else print('')
        print(hidden_word_, end='    ') 
        print(f'lives: {num_lives_}', end='   ')
        print(health_bar_)

# MAIN
if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)
    # print a game introduction
    print('Welcome to the Hangman Game!')

    # START MAIN LOOP (OUTER PROGRAM LOOP)
    playagain= True;
    while (playagain):
        # set up game options (the word size and number of lives)
        options= get_game_options()
        # select a word from a dictionary (according to the game options)
        # use choice() function that selects an item from a list randomly, for example:
        # mylist = ['apple', 'banana', 'orange', 'strawberry']
        # word = choice(mylist)
        word= choice(dictionary[options[0]]).lower()
        #print(word) #Testing only
        #set up options for game
        game_won= False;
        chosen_letters= []
        hidden_word= '__ ' * len(word)
        num_lives= options[1]
        #print(f'num_lives= {num_lives}') #testing only
        health_bar= 'O' * num_lives
        spent_lives= 0;
        correct_guesses= 0

         #add the '-' on the board for words that have a dash
        if '-' in word:
            dash_index= word.find('-')
            temp_list= hidden_word.split()
            temp_list[dash_index]= '-'
            hidden_word= ' '.join(temp_list)
            correct_guesses += 1

        # START GAME LOOP   (INNER PROGRAM LOOP)   
        board= True
        while (not game_won):

            if board: #only print the board if chose a valid letter
                print_board(chosen_letters, hidden_word, num_lives, health_bar)
            board= True
            
            # ask the user to guess a letter until they input something
            while(True):
                try:
                    letter= str(input('Please choose a new letter > \n')).upper()
                    if (not letter) or (len(letter) > 1) or (not letter.isalpha()):
                        raise ValueError
                    break
                except (ValueError, TypeError):
                    None
            if letter in chosen_letters:
                print('You have already chosen this letter. ')
                board= False
            elif letter.lower() in word:
                # if the letter is correct update the hidden word
                print('You guessed right! ')
                chosen_letters.append(letter) # update the list of chosen letters
                
                index= 0
                found=[]
                while index < len(word):
                    index= word.find(letter.lower(),index)
                    if index == -1:
                        break
                    found.append(index)
                    index += 1
                
                #update hidden_list with correctly guessed letters
                hidden_list= hidden_word.split()
                for i in found:
                    correct_guesses += 1
                    hidden_list[i]= letter
                hidden_word= ' '.join(hidden_list)
            else:
                print('You guessed wrong, you lost one life. ')
                # update the list of chosen letters
                chosen_letters.append(letter)
                num_lives= num_lives - 1
                spent_lives= spent_lives + 1
                health_bar= 'X' * spent_lives + 'O' * num_lives     
            # check if the user guesses the word correctly or lost all lives,
            # if yes finish the game
            if correct_guesses == len(word):
                game_won= True
                #print board after game is over
                print_board(chosen_letters, hidden_word, num_lives, health_bar)
                print(f'Congratulations!!! You won! The word is {word.upper()}!')

            elif num_lives <= 0:
                #print board after game is over
                print_board(chosen_letters, hidden_word, num_lives, health_bar)
                print(f'You lost! The word is {word.upper()}!')
                break
        
        # END GAME LOOP INNER PROGRAM LOOP)
        ask_again= True;
        while(ask_again):   # ask if the user wants to continue playing, 
        # if yes start a new game, otherwise terminate the program
            try:
                play= str(input('Would you like to play again [Y/N]?\n'))
                if play.lower() == 'n':
                    print('Goodbye!')
                    playagain= False
                    ask_again= False
                elif play.lower() == 'y':
                    ask_again= False
                elif (not(play.lower() == 'n')) or (not(play.lower() == 'y')):
                    raise ValueError           
            except (ValueError, TypeError):
                None
    # END MAIN LOOP (OUTER PROGRAM LOOP)

    