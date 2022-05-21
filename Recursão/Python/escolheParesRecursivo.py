#Recebe uma lista de inteiros e retorna uma lista dos números pares

def removeImpares(list):

    if len(list) == 0:
        return []
    
    if list[0] %2 == 0:
        _list = [list[0]]
        return _list + removeImpares(list[1:])
    
    else:
        return removeImpares(list[1:])

print(removeImpares( [1,2,3,4,4,2,6,8,9] ))