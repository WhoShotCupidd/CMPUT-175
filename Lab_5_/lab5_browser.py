#----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program:
#
# Author: Christiaan Venter
#----------------------------------------------------

from stack import Stack

def getAction():
    """Grabs input from user and checks if valid input

    Raises:
        Exception: will be raised if input is invalid

    Returns:
        action: string of valid action user inputted
    """
    
    action = input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ")
    if action == "<" or action == ">" or action == "q" or action == "=":
        return action
    else:
        raise Exception("Invalid action")
        

def goToNewSite(current, bck, fwd):
    """Goes to new site user inputs

    Args:
        current (str): string description of current website
        bck (stack): stack containing all previous websites
        fwd (stack): stack containing all websites previously visited

    Returns:
        str: new current website
    """
    
    fwd = fwd.clear()
    bck.push(current)
    current = input("URL: ")
    return current
     
    
def goBack(current, bck, fwd):
    """Goes back one website

    Args:
        current (str): string description of current website
        bck (stack): stack containing all previous websites
        fwd (stack): stack containing all websites previously visited

    Returns:
        str: new current website
    """
    
    try:
        new = bck.pop()
        fwd.push(current)
        return new
    except Exception:
        print("Cannot go back.")
        return current
    
    
      
      

def goForward(current, bck, fwd):
    """Goes forward one website

    Args:
        current (str): string description of current website
        bck (stack): stack containing all previous websites
        fwd (stack): stack containing all websites previously visited

    Returns:
        str: new current website
    """
    
    try:
        new = fwd.pop()
        bck.push(current)
        return new
    except Exception:
        print("Cannot go forward.")
        return current
        

def main():
    
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()
            
        except Exception as actionException:
            print(actionException.args[0])
            
        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
                print(current)
            elif action == '<':
                current = goBack(current, back, forward)
            elif action == '>':
                current = goForward(current, back, forward)
            elif action == 'q':
                quit = True
           
            
            
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    