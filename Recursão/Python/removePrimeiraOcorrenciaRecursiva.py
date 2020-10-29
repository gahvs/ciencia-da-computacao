#Recebe uma lista de inteiros e um número natural k, e devolve a lista removendo a primeira ocorrencia
#de k, se houver

def remove(list, n):

    if len(list) == 0:
        return []
    
    if list[0] == n:
        return remove(list[1:], None)
    
    else:
        _list = [list[0]]
        return _list + remove(list[1:], n)

print(remove([1,2,3,4,3,2,1],1))