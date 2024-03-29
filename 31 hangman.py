# Dependency on words.py to import words
import random
import string

from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words).upper()
    # print ('Computer selected words.....{}'.format(word))
    word_letters = set(word)
    # print('Computer selected words{}'.format(word_letters))
    alphabet = set(string.ascii_uppercase)
    #print ('alphabet.......',''.join(alphabet))
    used_letters=set()
    while len(word_letters) > 0:
        print('You have used this letter', ' '.join(used_letters))

        word_list= [letter if letter in used_letters else '-' for letter in word]
        print('Current word list ....',' '.join(word_list))

        user_letter = input('Guess a letter...').upper()
        #print (user_letter)
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            #print (used_letters)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You have already used that letter. Try again')

        else:
            print('Invalid character. Please try again')
    print (word)

hangman()