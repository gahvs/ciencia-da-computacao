#Recebe uma lista e retorna a lista invertida de forma recursiva

def reverse(list):

    if len(list) == 0:
        return []
    
    else:
        _list = [list[-1]]
        return _list + reverse(list[:-1])
    
print(reverse([1, 2, 3, 4, 5]))