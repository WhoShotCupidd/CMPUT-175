#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program: To simulate a web browser
#
# Author: Christiaan Venter
#----------------------------------------------------

def getAction():
    """function that gets the action from the user

    Returns:
        usrInput: string that will contain either =, <, >, or q 
    """
    
    valid = False
    
    while not valid:
        usrInput = input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ")
        
        if usrInput == '=' or usrInput == '<' or usrInput == '>' or usrInput == 'q':
            valid = True
        else:
            print('Invalid action. Try again.')
    
    return usrInput
    


def goToNewSite(current, pages): 
    """function that recieves a new site from the user and adds it to the lists of sites and moves to that sight

    Args:
        current (int): index of the current site
        pages (list): list with all pages accessed

    Returns:
        current: updates current index of the site the user is on
    """
    
    
    url = input("URL: ")
    
    
    del pages[current+1:]
    print(pages)
    pages.append(url)
    
    
    current = len(pages) - 1
    return current
    
    
    
    

def goBack(current, pages):
    """function that goes back to the previous page

    Args:
        current (int): index of the current site
        pages (list): list with all the pages accessed

    Returns:
        current: updates current index of the site the user is on
    """
    
    # Bound check
    if current == 0:
        print('Cannot go back')
    else:
        current -= 1
    return current



def goForward(current, pages):
    """function that goes forward to the next page

    Returns:
        current: updates current index of the site the user is on
    """
    
    # Bound check
    if current == len(pages) - 1:
        print('Cannot go forward')
    else:
        current += 1
    return current


def main():
    """
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    """   
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    currentIndex = 0
    quit = False
    
    while not quit:
        print('\nCurrently viewing', websites[currentIndex])
        action = getAction()
        
        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites)
            print(currentIndex)
        elif action == '<':
            currentIndex = goBack(currentIndex, websites)
        elif action == '>':
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            quit = True
        
    
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()    