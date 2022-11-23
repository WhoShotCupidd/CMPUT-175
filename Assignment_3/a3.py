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
        


def main():
    write_py("add", ["a", "b"], ["r = a + b", "return r"])
    add = load_function("add")
    assert add(1, 2) == 3
    
    
    
    
# Task 2

def fixed_bubble(size):
    pass



# Task 3
