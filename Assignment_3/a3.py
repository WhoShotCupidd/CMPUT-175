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
    
    params = str([param for param in parameters])
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
            statements.append("if alist[" + str(intial) + "] > alist[" + str(intial + 1) + "]:") # now need to add swap
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
    
    print(number)
    if number == 1 or number == 2:
        return -1

    
    start = 1
    
    while start * 2 < number:
        start = start * 2
        
    return start
        
        
        
        

# Correct
def bitonic(a_list):
    
    bitonicSort(a_list, 0, len(a_list) - 1, ">")



# Check
def CompareThenSwap(a_list, a, b, direction):
    if (direction == "<" and a_list[a] > a_list[b]) or (direction == ">" and a_list[a] < a_list[b]):
        a_list[a], a_list[b] =  a_list[b],  a_list[a]


# Check
def bitonicSort(a_list, start, end, direction):
    
    
    # problem here
    if end - start == 1 or start - end == 1:
        return
    
    middle = (end - start) // 2
    
    bitonicSort(a_list, start, middle, direction)
    bitonicSort(a_list, middle, end, flip(direction))
    bitonicMerge(a_list, start, end, direction)
        

# Check
def bitonicMerge(a_list, start, end, direction):
    
    if end - start == 1:
        return

    distance = greatest_power_of_two_less_than(start - end)
    
    middle = end - distance
    
    for i in range(start, start + middle):
        CompareThenSwap(a_list, i, i + distance, direction)
            
    bitonicMerge(a_list, start, middle, direction)
    bitonicMerge(a_list, middle, end, direction)











# Task 4 #
def fixed_bitonic(size):
    
    statements = []
    #iterate_length = size - 1
    
    
    

    """
    statements = []
    iterate_length = size - 1
    for i in range(size - 1):
        
        intial = 0
        for i in range(iterate_length):
            statements.append("if alist[" + str(intial) + "] > alist[" + str(intial + 1) + "]:") # now need to add swap
            statements.append(f" alist[{intial}], alist[{intial + 1}] = alist[{intial + 1}], alist[{intial}]")
            intial += 1
        
        iterate_length -= 1
        intial = 0
    statements.append("return alist")
        
        
    write_py("bubble" + str(size), ["alist"], statements)
    """




# Main
def main():
    write_py("divide", ["a", "b"], ["r = a // b", "return r"])
    divide = load_function("divide")
    assert divide(3, 1) == 3
    fixed_bubble(4)
    a_list = [1,4,2,8,3]
    bitonic(a_list)

# call on main function
if __name__ == "__main__":
    main()