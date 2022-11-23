


def write_py(name, parameters, statements):
    assert name != 'a3'
    
    params = str([param for param in parameters])
    params = params.replace("[", "").replace("]", "").replace("'", "")
    
    
    
    with open(name + ".py", 'w') as f:
        
        f.write("def " + name + "(" + params + "):")
        f.write("\n")
        for i in range(0, len(statements)):
            f.write("   " + statements[i] + "\n") 
        
write_py("add", ["a", "b"], ["r = a + b", "return r"])