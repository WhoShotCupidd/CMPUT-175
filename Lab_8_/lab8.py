#----------------------------------------------------
# Lab 8: recursion
# Purpose of program: have some fun with recursion
#
# Author: Christiaan Venter
# ccid: clventer
# 1707325
#----------------------------------------------------


def mylen(some_list):
    """will return integer length of list

    Args:
        some_list (list): list we wish to find the length of

    Returns:
        int: length of list
    """
    
    # base case and recursive call
    if some_list != []:
        return 1 + mylen(some_list[1:])
    return 0


def intDivision(dividend, divisor):
    """will return the natural number of the division between two numbers

    Args:
        dividend (int): what we are dividing
        divisor (int): what we are dividing it by

    Raises:
        ValueError: checks to make sure the divisor is non zero
        ValueError: checks to make sure both numbers are non negative

    Returns:
        int: quotient of division
    """
    
    # value checks 
    if divisor == 0:
        raise ValueError("Divisor must be non zero")
    if divisor < 0 or dividend < 0:
        raise ValueError("Divisor and Divident must be non zero")
    
    # base case and recursive call
    if dividend >= divisor:
        return 1 + intDivision(dividend - divisor, divisor)
    return 0


def sumdigits(number):
    """wil compute sum of all individual digits in a given number

    Args:
        number (int): number to compute sum of all individual digits

    Returns:
        int: sum of all individual digits in a given number
    """
    
    # base case and recursive call
    if number == 0:
        return 0
    return (number % 10) + sumdigits(int(number//10))


def reverseDisplay(number):
    """reverses the order of the digits in a given number

    Args:
        number (int): number to reverse the order of the digits

    Raises:
        ValueError: if number negative or zero cannot reverse

    Returns:
        int: reversed order of digits
    """
    
    # intialize variables
    number = str(number)
    

    # base case and recursive call
    if number == "":
        return ""
    else:
        return int(str(number[-1]) + str(reverseDisplay(number[:-1])))
    

def recursive_binary_search(key,alist,low,high):
    """finds element in the list using binary search algorithm

    Args:
        key (int): the number to find in the list
        alist (list): the list to seach elements
        low (int): lowest index of the list
        high (int): highest index of the list

    Returns:
        int: index of the element in the list
    """
        
    # intialize variables
    middle = (low + high) // 2
    
    # binary search algorithm using recursive calls
    if alist[middle] == key:
        return middle
    elif high - low <= 1:
        return "Item is not in the list"
    elif alist[middle] > key:
        return recursive_binary_search(key, alist, low, middle)
    else:
        return recursive_binary_search(key, alist, middle + 1, high)


def main():
    #length
    #alist=[43,76,97,"string"]
    #print(mylen(alist))
    
    #dividing
    n = int(input('Enter an integer dividend: '))
    m = int(input('Enter an integer divisor: '))
    print('Integer division', n, '//', m, '=', intDivision(n,m)) 
    
    #sum of digits
    number = int(input('Enter a number:'))
    print("Sum:",sumdigits(number)) 
    
    #reverse order
    #removed the "int" since it just checked for u
    number = (input('Enter a number:'))
    print("Reversed:",reverseDisplay(number))
    
    #recursive binary search
    print("")
    print("Binary search:")
    print("")
    some_list = [-8,-2,1,3,5,7,9]
    print("looking for 9")
    print(recursive_binary_search(9,some_list,0,len(some_list)-1))
    print("looking for -8")
    print(recursive_binary_search(-8,some_list,0,len(some_list)-1))
    print("looking for 4")
    print(recursive_binary_search(4,some_list,0,len(some_list)-1)) 
    

    
    
main() 