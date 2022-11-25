#----------------------------------------------------
# Assignment 2
# Purpose of program: create a wordle game
#
# Author: Christiaan Venter
# ccid: clventer
# 1707325
#----------------------------------------------------


# IMPORTANT NOTE
# my auto_wordle runs for a long time then gives an error however I have contacted my TA and they have reported this as ok


# Imports used
from random import choice
from collections.abc import MutableSet

# Class containing all possible words for the game or wordle
class WordleWords(MutableSet):

    def __init__(self, letters):
        self._words = set()
        self.letters = letters
    
    def __contains__(self, word):
        """sees if _words contains given word 

        Args:
            word (str): word to check if in list 

        Returns:
            bool: false or true wether in list or not
        """
        return word in self._words
    
    def __iter__(self): 
        return iter(self._words)
    
    def __len__(self):
        """returns the amount of words 

        Returns:
            int: integer description of amount of words 
        """
        return len(self._words)
    
    def add(self, word):
        """adds word to list 

        Args:
            word (str): word to add
        """
        self._words.add(word)
        
    def discard(self, word):
        """removes word from list

        Args:
            word (str): word to remove 
        """
        self._words.remove(word)
        
    def load_file(self, filename):
        """find load given file and make a list with all possible words 

        Args:
            filename (str): name of file to make word list with
        """
        file = open(filename,"r")
        for lines in file.readlines():
            line = lines.rstrip("\n")
            if len(line) == self.letters:
                self._words.add(line.upper())
            
    
    def check_word(self, word):
        """checks word and sees if it is all caps and if it is too long or short 

        Args:
            word (str): word we wish to check 

        Raises:
            NotLettersError: if word contains any string not contained within ALPHABET constant
            TooLongError: raised if word is longer than letters
            TooShortError: raised if word is shorter than letters 
        """
        ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        for letter in word:
            if letter not in ALPHABET:
                raise NotLettersError()
        
        if len(word) > (self.letters):
            raise TooLongError
        
        if len(word) < (self.letters):
            raise TooShortError
    
    def letters(self):
        """getter for amount of letters

        Returns:
            int: amount of letter
        """
        return self.letters
    
    def copy(self):
        """creates an identical copy to current wordlewords class

        Returns:
            WordleWords: class containing identical values
        """
        copy = WordleWords(self.letters)
        copy._words = set(self._words)
        return copy
        
# Class used to check guesses
class Guess:
    def __init__(self, _guess, answer):
        self._guess = _guess
        self.answer = answer

    def guess(self):
        """getter for the guess made

        Returns:
            str: the guess made
        """
        return self._guess
    
    def correct(self):
        """returns all correctly guessed letters in the right position

        Returns:
            str: all the correct letters formated correctly 
        """
        stri = ""
        for i in range(len(self._guess)):
            if self._guess[i] == self.answer[i]:
                stri += self._guess[i]
            else:
                stri += "_"
        return stri
    
    def misplaced(self):     
        """returns all letters that were guessed but not in the right position

        Returns:
            str: all mislaced letters
        """
        wrongPos = ""
        
        for i in range(len(self._guess)):
            if self.answer[i] in self._guess and self.answer[i] != self._guess[i]:
                wrongPos += self.answer[i]
                
        return ''.join(sorted(wrongPos))

    def wrong(self):
        """returns a string with all the wrong letters

        Returns:
            str: all incorrect answers
        """
        wrongLetters = ""
        i = 0
        correct = self.correct()
        
        for guessLetter in self._guess:
            if (guessLetter not in self.answer) or (self._guess.count(guessLetter) != self.answer.count(guessLetter) and correct[i] == "_"):
                wrongLetters += guessLetter
            i += 1    
            
        return "".join(sorted(wrongLetters))
    
    def is_win(self):
        """returns wether or not answer is the same as guess

        Returns:
            bool: wether similar or incorrect 
        """
        if self._guess == self.answer:
            return True
        else:
            return False
    
# used to play the game of wordle
class Wordle:
    def __init__(self,words):
        self.random_word = choice(list(words._words))
        #words.discard(self.random_word)
        self._guessesmade = 0
        
    def guesses(self):
        """getter function for the amount of guesses made

        Returns:
            int: amount of guesses
        """
        return self._guessesmade
    
    def guess(self, guessed):
        """returns a guess object and adds one to the guesses made

        Args:
            guessed (str): guess the user made

        Returns:
            Guess: guess object with guess made
        """
        self._guessesmade += 1
        return Guess(guessed, self.random_word)
        
# all error classes used 
class TooShortError(ValueError):
    pass


class TooLongError(ValueError):
    pass


class NotLettersError(ValueError):
    pass