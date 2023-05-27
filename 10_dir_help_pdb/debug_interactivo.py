import pdb

def add(a, b):
    pdb.set_trace()
    return a + b

print(add(2, 3))

'''
En este ejemplo, la funcion pdb.set_trace() es usada para colocar un breakpoint 
en la funcion add(). Cuando se ejecuta el programa, se detendra en esta linea  
y entrara en la consola PDB. 

From here, you can use various commands to inspect the 
state of the program and step through the code. For example, you can use
the n command to step to the next line, the s command to step into a function call, 
and the c command to continue execution until the next breakpoint2.

'''
