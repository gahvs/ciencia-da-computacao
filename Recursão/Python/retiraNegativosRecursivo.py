#Recebe uma lista de inteiros e retorna uma lista sem os números inteiros

def remove(list):

    if len(list) == 0:
        return []
    
    if list[0] >= 0:
        _list = [list[0]]
        return _list + remove(list[1:])
    
    else:
        return remove(list[1:])

print(remove([1, -2, -3, 7, 0]))