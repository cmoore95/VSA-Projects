# Name:
# Date:


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!


def correct(word, letter_prompt, answer_list, wrong_list, guesses):

    if letter_prompt in word:
        answer_list.append(letter_prompt)
        return answer_list
    else:
         wrong_list.append(letter_prompt)
         return wrong_list

#def partial_word():


def hangman():
    word=choose_word(wordlist)
    letter_count=0
    guesses=9
    blank_word=[]
    answer_list = []
    wrong_list = []
    print 'Welcome to hangman'
    print word
    for letter in word:
        letter_count=letter_count+1
    print 'Your word has',letter_count,'letters in it.'

    while guesses>0:
        letter_prompt = raw_input('Guess a letter ')
        correct(word, letter_prompt, answer_list, wrong_list, guesses)
        if answer_list:
            guesses=guesses
        else:
            guesses=guesses-1
        print 'You have', guesses, 'guesses left.'





hangman()