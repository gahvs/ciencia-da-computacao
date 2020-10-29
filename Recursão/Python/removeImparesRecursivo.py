#Recebe uma lista de inteiros e retorna uma lista com os números pares do arg

def removeImpar(list):

    if len(list) == 0:
        return []

    if list[0] % 2 == 0:
        _list = [list[0]]
        return _list + removeImpar(list[1:])
    else:
        return removeImpar(list[1:])

print(removeImpar([1,2,3,4,4,2,6,8,9]))