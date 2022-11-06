
# She Bang above is used to run through my compilier if it causes issues feel free to delete 
#----------------------------------------------------
# Lab 3: Numerical Tic Tac Toe class
# 
# Author: Christiaan Venter
#----------------------------------------------------

class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        
        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        # TO DO: delete pass and print out formatted board
        # e.g. an empty board should look like this:
        #    0   1   2  
        # 0    |   |   
        #   -----------
        # 1    |   |   
        #   -----------
        # 2    |   |           
        
        print("    0   1   2  ")
        print("0   {} | {} | {} ".format(self.board[0][0], self.board[0][1], self.board[0][2]))
        print("   -----------")
        print("1   {} | {} | {} ".format(self.board[1][0], self.board[1][1], self.board[1][2]))
        print("   -----------")
        print("2   {} | {} | {} ".format(self.board[2][0], self.board[2][1], self.board[2][2]))
        
        
    


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        
        if self.board[row][col] == 0:
            return True
        else:
            return False
    
    
    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        
        if self.squareIsEmpty(row, col):
            self.board[row][col] = num
            return True
        else:
            return False
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        check = 0
        
        for i in range(self.size):
            for j in range(self.size):
                if self.squareIsEmpty(i, j):
                    check = 1
                    return False
                
        if check == 0:
            return True
        
        
        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        for i in range(0, self.size):
            if self.board[i][0] + self.board[i][1] + self.board[i][2] == 15:
                return True
        
        for i in range(0, self.size):
            if self.board[0][i] + self.board[1][i] + self.board[2][i] == 15:
                return True
            
        if self.board[0][0] + self.board[1][1] + self.board[2][2] == 15:
            return True
        
        if self.board[0][2] + self.board[1][1] + self.board[2][0] == 15:
            return True

if __name__ == "__main__":
    # TEST EACH METHOD THOROUGHLY HERE
    # suggested tests are provided as comments, but more tests may be required
    
    # start by creating empty board and checking the contents of the board attribute
    myBoard = NumTicTacToe()
    print('Contents of board attribute when object first created:')
    print(myBoard.board)
    
    # does the empty board display properly?
    myBoard.drawBoard()

    # assign a number to an empty square and display
    
    myBoard.update(0, 0, 1)
    myBoard.drawBoard()
    
    # try to assign a number to a non-empty square. What happens?
    
    myBoard.update(0, 0, 2)
    myBoard.drawBoard()
    # Board is not updated
    
    # check if the board has a winner. Should there be a winner after only 1 entry?
    
    print(myBoard.isWinner())
    # There should be no winner as no user should be able to achieve 15 after only 1 entry
    
    # check if the board is full. Should it be full after only 1 entry?
    
    print(myBoard.boardFull())
    # No as no user should be able to fill the board after only 1 entry
    
    # add values to the board so that any line adds up to 15. Display
    
    myBoard.update(0, 1, 5)
    myBoard.update(0, 2, 9)
    myBoard.drawBoard()
    
    # check if the board has a winner
    
    print(myBoard.isWinner())
    
    # check if the board is full
    
    print(myBoard.boardFull())
    
    # test a diagonal win
    
    myBoard.update(1, 1, 9)
    myBoard.update(2, 2, 5)
    print(myBoard.isWinner())
    