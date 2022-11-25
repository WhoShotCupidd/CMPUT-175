#----------------------------------------------------
# Lab 8: recursion
# Purpose of program: have some fun with recursion
#
# Author: Christiaan Venter
# ccid: clventer
# 1707325
#----------------------------------------------------

#
from random import choice
from collections.abc import MutableSet

#
class WordleWords(MutableSet):

    def __init__(self, letters):
        self._words = set()
        self.letters = letters
    
    def __contains__(self, word):
        return word in self._words
    
    def __iter__(self): 
        return iter(self._words)
    
    def __len__(self):
        return len(self._words)
    
    def add(self, word):
        self._words.add(word)
        
    def discard(self, word):
        self._words.remove(word)
        
    def load_file(self, filename):
        file = open(filename,"r")
        for lines in file.readlines():
            line = lines.rstrip("\n")
            if len(line) == self.letters:
                self._words.add(line.upper())
            
    
    def check_word(self, word):
        ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        for letter in word:
            if letter not in ALPHABET:
                raise NotLettersError()
        
        if len(word) > (self.letters):
            raise TooLongError
        
        if len(word) < (self.letters):
            raise TooShortError
    
    def letters(self):
        pass
    
    def copy(self):
        copy = WordleWords(self.letters)
        copy._words = set(self._words)
        return copy
        

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
    

class Wordle:
    def __init__(self,words):
        self.random_word = choice(list(words._words))
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
        
    
class TooShortError(ValueError):
    pass


class TooLongError(ValueError):
    pass


class NotLettersError(ValueError):
    pass