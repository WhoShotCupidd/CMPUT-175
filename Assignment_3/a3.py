


def write_py(name, parameters, statements):
    assert name != 'a3'
    
    with open(name + ".py", 'w') as f:
        
        f.write("def " + name + "(" + str(parameters) + "):")
        f.write("\n")
        f.write("   " + statements) 
        
write_py("hello", [1], "print(hello)")