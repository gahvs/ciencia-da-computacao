#Recebe uma lista de inteiros e um natural k, e devolve uma lista sem as ocorrencias de k

def remove(list, k):

    if len(list) ==0:
        return []
    
    if list[0] == k:
        return remove(list[1:], k)
    
    else:
        _list = [list[0]]
        return _list + remove(list[1:], k)
    
print(remove([1,2,3,4,3,2,1],3))