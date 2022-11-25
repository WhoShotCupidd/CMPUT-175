from importlib import invalidate_caches
from importlib import import_module


def write_py(name, parameters, statements):
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


def main():
    write_py("divide", ["a", "b"], ["r = a // b", "return r"])
    divide = load_function("divide")
    assert divide(3, 1) == 3

    
    
    
    
    
# Task 2

def fixed_bubble(size):
    pass



# Task 3



if __name__ == "__main__":
    main()