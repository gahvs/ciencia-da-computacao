#Recebe uma lista de inteiros e retorna uma lista com elementos que ocupam os indices ímpares

def indices_impar(l):

    last = len(l) - 1 

    if len(l) == 0:
        return []
    
    if last % 2 != 0:
        _list = [l[last]]
        return indices_impar(l[:-1]) + _list
    
    else:
        return indices_impar(l[:-1])

print(indices_impar([0,1,2,3,4,5,6]))