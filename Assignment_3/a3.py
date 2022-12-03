#----------------------------------------------------
# Assignment 3
# Purpose of program: metaprogramming and sorting
#
# Author: Christiaan Venter
# ccid: clventer
# 1707325
#----------------------------------------------------

from importlib import invalidate_caches
from importlib import import_module



# Task 1 #
def write_py(name, parameters, statements):
    """will create a python file with the give name and parameters

    Args:
        name (str): name of file
        parameters (list): all parameters for function in the file
        statements (list): all code inside the function
    """
    assert name != 'a3'
    
    params = str(parameters)
    params = params.replace("[", "").replace("]", "").replace("'", "")
    
    with open(name + ".py", 'w') as f:
        
        f.write("def " + name + "(" + params + "):")
        f.write("\n")
        for i in range(0, len(statements)):
            f.write("   " + statements[i] + "\n") 
       
        
def load_function(name):
    '''
    load_function - imports a module recently created by name
        and returns the function of the same name from inside of it
    name - a string name of the module (not including .py at the end)
    '''
    # invalidate_caches is necessary to import any files created after this file started!
    invalidate_caches()
    print(f"    Attempting to import {name}...")
    module = import_module(name)
    print(f"    Imported!")
    assert hasattr(module, name), f"{name} is missing from {name}.py"
    function = getattr(module, name)
    assert type(function) is type(load_function)
    return function



# Task 2 #
def fixed_bubble(size):
    """will output a file that will bubble sort for a certain size

    Args:
        size (int): size of list to sort

    Returns:
        file: .py file that can be ran with a list the same size to sort
    """
    statements = []
    iterate_length = size - 1
    for i in range(size - 1):
        
        intial = 0
        for i in range(iterate_length):
            statements.append("if alist[" + str(intial) + "] > alist[" + str(intial + 1) + "]:")
            statements.append(f" alist[{intial}], alist[{intial + 1}] = alist[{intial + 1}], alist[{intial}]")
            intial += 1
        
        iterate_length -= 1
        intial = 0
    statements.append("return alist")
        
    write_py("bubble" + str(size), ["alist"], statements)
          
          
                          
# Task 3 #
def flip(symbol):
    """will flip a greater than or less than symbol

    Args:
        symbol (str): symbol to flip

    Returns:
        str: the flipped symbol
    """
    if symbol == "<":
        return ">"
    else:
        return "<"


def greatest_power_of_two_less_than(number):
    """will find the greatest power of two that is less than but not equal to given number

    Args:
        number (int): number to find greatest_power_of_two_less_than

    Returns:
        int: the greatest_power_of_two_less_than
    """
    if number == 1 or number == 2:
        return 1

    start = 1
    
    while start * 2 < number:
        start = start * 2
        
    return start
        

def bitonic(a_list):
    """Will begin the bitonic sort with correct ending and starting values

    Args:
        a_list (list): list to bitonicly sort
    """
    bitonicSort(a_list, 0, len(a_list), ">")


def CompareThenSwap(a_list, a, b, direction):
    """function I implememted to compare two indexes and depending on value and direction do the correct comparison and swap

    Args:
        a_list (list): list holding values to compare
        a (int): first value index
        b (int): second value index
        direction (str): direction to compare and swap as it changes if we swap or not
    """
    if (direction == ">" and a_list[a] > a_list[b]) or (direction == "<" and a_list[a] < a_list[b]):
        a_list[a], a_list[b] =  a_list[b],  a_list[a]


def bitonicSort(a_list, start, end, direction):
    """Will sort a list with bitonic sorting

    Args:
        a_list (list): list to sort
        start (int): where to begin sorting
        end (int): where to end sorting
        direction (str): direction of bitonic sort
    """
    if end - start <= 1:
        return
    
    middle = (end + start) // 2
    
    bitonicSort(a_list, start, middle, direction)
    bitonicSort(a_list, middle, end, flip(direction))
    bitonicMerge(a_list, start, end, direction)
        

def bitonicMerge(a_list, start, end, direction):
    """Will merge two bitonic lists into one

    Args:
        a_list (list): list to merge
        start (int): starting index of the list
        end (int): ending index of the list to merge
        direction (str): direction to merge the list
    """
    if end - start <= 1:
        return

    distance = greatest_power_of_two_less_than(end - start)
    
    middle = end - distance
    
    for i in range(start, middle):
        CompareThenSwap(a_list, i, i + distance, direction)
            
    bitonicMerge(a_list, start, middle, direction)
    bitonicMerge(a_list, middle, end, direction)



# Task 4 #
def fixed_bitonic(size):
    """identical to bitonic above however creates a statement list instead of actually sorting

    Args:
        size (int): size of list to make a sort file for

    Returns:
        file: .py file that will sort that size of list bitoniclly
    """
    statements = []
    fixedBitonicSort(0, size, ">", statements)
    statements.append("return alist")
    write_py("bitonic"+ str(size), "[alist]", statements)
    
    
def fixedBitonicSort(start, end, direction, statements):
    """identical to bitonic sort however calls on fixed versions of sort and merge

    Args:
        start (int): start of list
        end (int): end of list to sort
        direction (str): direction sorting will occur
        statements (list): collection of all statements to occur in output file
    """
    if end - start <= 1:
        return
    
    middle = (end + start) // 2
    
    fixedBitonicSort(start, middle, direction, statements)
    fixedBitonicSort(middle, end, flip(direction), statements)
    fixedBitonicMerge(start, end, direction, statements)


def fixedBitonicMerge(start, end, direction, statements):
    """identical to bitonic merge however calls on fixed versions of merge and compare and swap

    Args:
        start (int): start of list
        end (int): end of list to sort
        direction (str): direction to sort in
        statements (list): collection of statements for output file
    """
    if end - start <= 1:
        return

    distance = greatest_power_of_two_less_than(end - start)
    
    middle = end - distance
    
    for i in range(start, middle):
        fixedCompareThenSwap(i, i + distance, direction, statements)
            
    fixedBitonicMerge(start, middle, direction, statements)
    fixedBitonicMerge(middle, end, direction, statements)


def fixedCompareThenSwap(a, b, direction, statements):
    """where all the magic happens and instead of actually performing a swap it will append to statements what it would have done

    Args:
        a (int): first index of the list
        b (int): second index of the list
        direction (str): direction to sort in
        statements (list): collection of all statements for output file
    """
    if direction == ">":
        statements.append("if alist[" + str(a) + "] > alist[" + str(b) + "]:")
        statements.append(f"    alist[{a}], alist[{b }] = alist[{b}], alist[{a}]")
    
    if direction == "<":
        statements.append("if alist[" + str(a) + "] < alist[" + str(b) + "]:")
        statements.append(f"    alist[{a}], alist[{b}] = alist[{b}], alist[{a}]")
        
# Hope you have a great winter break! 