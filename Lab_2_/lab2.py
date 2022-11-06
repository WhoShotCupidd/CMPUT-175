#!/usr/bin/env python3
# She Bang above is used to run through my compilier if it causes issues feel free to delete 

# This program will take a txt file and decrypt the message using a key it will make use of two functions
# ccid: clventer, name: Christiaan Lemmer Venter

def getInputFile():
    """
    Will request the user to enter a filename and if the extension is not .txt will ask again
    Returns:
        filename: string of the filename
    """
    
    filename = input("Enter the name of the file to input file: ")
    incorrect = True
    if filename[-4:] == ".txt":  # checks if the file is a txt file
        incorrect = False
    while incorrect == True:
        filename = input("Invalid filename extension. Please re-enter the input filename: ")
        if filename[-4:] == ".txt":
            incorrect = False
    return filename

def decrypt(filename):
    """
    Will read the text file given and using the key decrypt the text
    Args:
        filename (str): string descriptor of filename
    Returns:
        decrepted: string that has the decrypted message
    """
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        decrepted = ""
        lines[1] = lines[1].strip()
        lines[1] = lines[1].split()
        temp = " ".join(lines[1])
        lines[1] = temp

        for i in range(0,len(lines[1])):
            
            if lines[1][i] == " " or lines[1][i] == "   ":  # This if will check if the character is a space and if it is it will add a space to the decrepted string
                decrepted += " "
                space = True 
            else:
                space = False
            
            if space != True:  # This if will check if the character is not a space and if it is not it will add the character to the decrepted string
                ordLetter = ord(lines[1][i])

                for j in range(0,int(lines[0])):
                    
                    ordLetter -= 1  # subtracts 1 from the ascii value
                    
                    if ordLetter < 65:  # alphabet wrapping for lowercase letters
                        ordLetter = 122
                    elif ordLetter < 97 and ordLetter > 90:  # alphabet wrapping for uppercase letters
                        ordLetter = 122
            
                decrepted += chr(ordLetter).lower()  # adds the decrepted character to the decrepted string
                
    file.close()            
    return decrepted

def main():          
    filename = getInputFile()
    decrepted = decrypt(filename)
    print(decrepted)
    
main()