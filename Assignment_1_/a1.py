#----------------------------------------------------
# Assignment 1: Encryption and Decryption 
# Purpose of program: Using frequencies of english langauge to guess simple 3 digit keys and decrypt messages
#
# Author: Christiaan Venter
# ccid: clventer
# 1707325
#----------------------------------------------------

# imports
from math import log2


def decrypt(text, key):
    """decrypt text using a key given

    Args:
        text (str): text we wish to decrypt
        key (str): key to decrypt with

    Returns:
        decrypted: string containg decrypted text
    """
    
    # intial variable intialization
    ALPHABET = "\n !\"'(),-.0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted = ""
    
    # travserse through every letter and decrypt letter
    for postion in range(len(text)):
        text_character = ALPHABET.index(text[postion])
        key_character = ALPHABET.index(key[postion % len(key)])
        decrypted_char = (text_character - key_character) % len(ALPHABET)
        decrypted += ALPHABET[decrypted_char]
    
    return decrypted


def get_frequencies(text):
    """function that returns a dictionary of frequencies of each letter in the given text

    Args:
        text (str): the given text frequencie will be calculated for

    Returns:
        freq: dictionary of frequencies of each letter in the given text
    """
    
    # intial variable intialization
    ALPHABET = "\n !\"'(),-.0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    freq = {}
    text = text.upper()
    
    # traverse through given text and get total number of each letter    
    for postion in range(len(text)):
        if text[postion] in freq:
            freq[text[postion]] = freq[text[postion]] + 1
        else:
            freq[text[postion]] = 1
    
    # convert the total numbers of each number into frequencies
    for key in freq:
        length = len(text)
        freq[key] = freq[key] / length
    
    return freq

        
def cross_entropy(freqs1, freqs2):
    """calculate the cross entropy of two given frequencies

    Args:
        freqs1 (dict): first frequency
        freqs2 (dict): seconf frequency

    Returns:
        cross_entropy: cross entropy of two given frequencies
    """
    
    # intial variable intialization
    compareList = []
    cross_entropy = 0
    
    # finding shared elements 
    for keys1 in freqs1.keys():
        compareList.append(keys1)
    
    for keys2 in freqs2.keys():
        if keys2 not in compareList:
            compareList.append(keys2)
    
    # minimum variables for calculations
    min1 = min(freqs1.values())
    min2 = min(freqs2.values())

    # doing the calculations based on each case
    for letters in compareList:
        if letters in freqs1 and letters in freqs2:
            cross_entropy -= freqs1.get(letters) * log2(freqs2.get(letters))
        if letters in freqs1 and letters not in freqs2:
            cross_entropy -= freqs1.get(letters) * log2(min2)
        if letters not in freqs1 and letters in freqs2:
            cross_entropy -= min1 * log2(freqs2.get(letters))
    
    return cross_entropy
    
    
def GetNthLetters(text, n):
    """i created this function so guess_key would be more readable

    Args:
        text (str): text we can to find each nth letter
        n (int): the n value we wish to skip

    Returns:
        text[::n]: string with nth letter only
    """
    
    return text[::n]


def guess_key(encrypted):
    """will use english frequency to guess the 3 digit key

    Args:
        encrypted (str): the text we wish to guess the 3 digit key

    Returns:
        key: the 3 digit key
    """
    
    # intial variable intialization
    file = open("frank.txt", 'r')
    lines = file.read().upper()
    # base variables, trying to make it so less lines of code and look better
    ENGLISHFREQUENCIES, encrypted, ALPHABET = get_frequencies(lines), encrypted.upper(), "\n !\"'(),-.0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # strings containing only the 3rd letter starting at 1,2,3
    firstLetterKeyEncrypted = GetNthLetters(encrypted, 3)
    secondLetterKeyEncrypted = GetNthLetters(encrypted[1:], 3)
    thirdLetterKeyEncrypted = GetNthLetters(encrypted[2:], 3)
    
    # dictionarys that will later be used to compare frequencies
    minimum1, minimum2, minimum3 = {}, {}, {}
    
    # traverse through the ALPHABET and find cross entropy comparing english frequencies and frequencies contained in each key value
    for i in range(len(ALPHABET)):
        minimum1[ALPHABET[i]] = cross_entropy(ENGLISHFREQUENCIES, get_frequencies(decrypt(firstLetterKeyEncrypted,ALPHABET[i])))
        minimum2[ALPHABET[i]] = cross_entropy(ENGLISHFREQUENCIES, get_frequencies(decrypt(secondLetterKeyEncrypted,ALPHABET[i])))
        minimum3[ALPHABET[i]] = cross_entropy(ENGLISHFREQUENCIES, get_frequencies(decrypt(thirdLetterKeyEncrypted,ALPHABET[i])))
        
    # using lambda functions as they are anonymous functions that make sorting and finding minimums easier
    # finds the letter of each key by finding the lowest entropy
    lettermin1 = (min(minimum1.items(), key=lambda x: x[1]))[0]
    lettermin2 = (min(minimum2.items(), key=lambda x: x[1]))[0]
    lettermin3 = (min(minimum3.items(), key=lambda x: x[1]))[0]

    # add minimum letter for 3 dictionarys to key
    key = str(lettermin1) + str(lettermin2) + str(lettermin3)

    return key
    
    
def crack(encrypted_text):
    """combines all functions to produce a decypted message

    Args:
        encrypted_text (str): text we wish to guess key and decrypt

    Returns:
        decryptedMessage: string containing decrypted text
    """
    
    # finds key first then uses key to decrypt
    decryptedKey = guess_key(encrypted_text)
    decryptedMessage = decrypt(encrypted_text, decryptedKey)
    return decryptedMessage