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
    def __init__(self, guess, answer):
        self.guess = guess
        self.answer = answer

    def guess(self):
        return self.guess
    
    def correct(self):
        stri = ""
        for i in range(len(self.guess)):
            if self.guess[i] == self.answer[i]:
                stri += self.guess[i]
            else:
                stri += "_"
        return stri
    
    def misplaced(self):
        # duplicates
        correctGuesses = self.correct()
        wrongPos = ""
        for i in range(len(self.guess)):
            if self.guess[i] in correctGuesses and (self.guess[i] != correctGuesses[i]):
                wrongPos += self.guess[i]
        return wrongPos
            
    def wrong(self):
        wrongLetters = ""
        for guessLetter in self.guess:
            if guessLetter not in self.answer:
                wrongLetters += guessLetter
        return wrongLetters
    
    def is_win(self):
        if self.guess == self.answer:
            return True
    


class TooShortError(ValueError):
    pass

class TooLongError(ValueError):
    pass

class NotLettersError(ValueError):
    pass



class Wordle:
    def __init__(self,words):
        pass
    
