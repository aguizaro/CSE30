# author: Larissa Munishkina
# date: Mar 27, 2022
# file: test_hangman.py tests a hangman.py
# input: file 'dictionary-short.txt'
# output: possible assertion errors
# edited by Antonio Guizar Orozco on 10-6-2022 for testing/extra credit 

import hangman
import sys
import io
dictionary_file = 'dictionary-short.txt'

if __name__ == '__main__':
    
    # test import_dictionary(filename)
    dict_standard = {2:['ad'],
                     3:['bat'],
                     4:['card'],
                     5:['dress'],
                     6:['engine'],
                     7:['T-shirt'],
                     8:['gasoline'],
                     9:['gathering'],
                     10:['evaluation'],
                     11:['self-esteem'],
                     12:['unemployment']}
    dictionary = hangman.import_dictionary(dictionary_file)
    assert dictionary == dict_standard

    # test get_game_options()
    output_standard = 'The word size is set to 4.\nYou have 4 lives.\n'
    hangman.input = lambda x:'4' # redirect input
    stdout = sys.stdout
    sys.stdout = io.StringIO()   # redirect stdout
    size, lives = hangman.get_game_options()
    output = sys.stdout.getvalue()
    sys.stdout = stdout          # restore stdout
    assert size == 4
    assert lives == 4
    assert output == output_standard

    #Test print_board method for extra credit points
    board= hangman.print_board(['T','E','S','T'],'__ __ __ __', 5, '00000')
    assert board == 'Letters chosen: T, E, S, T\n__ __ __ __    lives: 5   00000'

    print('Everything looks good! No assertion errors!')