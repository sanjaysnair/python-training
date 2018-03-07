# Assignment with an = on lists does not make a copy. 
# Instead, assignment makes the two variables point to the one list in memory.
gto = ['Bengaluru', 'Paris', 'Bucharest']
global_tools = gto
global_tools.append('test')
print(gto)
print(global_tools)