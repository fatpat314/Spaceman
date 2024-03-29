
import random
import unittest

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

    for letters in secret_word:
        if letters not in letters_guessed:
            return False

        #else:
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''


    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    output = ""
    for letters in secret_word:
        if letters in letters_guessed:
            output += letters + " "
        else:
            output += " _ "
    return output




def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    if guess in secret_word:
        return True
    else:
        return False






def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    letters_guessed = []
    Wrong_guesses = 0




    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    while "_" in get_guessed_word(secret_word, letters_guessed):

        guess = input ("Guess one letter per round: ")
        if len(guess) > 1:
            print("ERROR. Enter ONE letter per round")
        else:
            letters_guessed.append(guess)

        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word):
            print("Letter guessed is in word")
        else:
            Wrong_guesses += 1
            print("Letter not in word")
        #TODO: show the guessed word so far

        print(get_guessed_word(secret_word, letters_guessed))


        #TODO: check if the game has been won or lost
        for letter in letters_guessed:
            print(letter, sep=' ', end=' ')
            if is_word_guessed(secret_word, letters_guessed):
                print("WINNER WINNER CHICKEN DINNER")
            elif Wrong_guesses > 6:
                print("LOSER")


#These function calls that will start the game
def tst():
    #secret_word = load_word()
    print(secret_word)
    print(is_guess_in_word("x", "random"))


#tst()


secret_word = load_word()
print(" ")
print("-------------------------------------------------------------------------")
print("SPACEMAN")
print("-------------------------------------------------------------------------")
print("THE RULES!")
print(" ")
print("Users win if they can guess the mystery word before the spaceman is drawn.")
print("The spaceman is made up of seven parts, and a new part is added for each incorrect guess.")
print("If all seven parts get drawn before the user guesses the word, then they lose")
print("-------------------------------------------------------------------------")
print(" ")

spaceman(load_word())

class Spaceman_tests(unittest.TestCase):
    def test_is_word_guessed(self):
        self.assertEqual(is_word_guessed("secret","secret"), True)

    def test_is_guess_in_word(self):
        self.assertEqual(is_guess_in_word("s","secret"), True)

    def test_spaceman(self):
        self.assertEqual(spaceman("secret"),None)

if __name__ == '__main__':
    unittest.main()
