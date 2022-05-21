#Recebe uma lista e uma função, e retorna as imagens dos elementos da lista aplicado a função

suc = lambda x : x + 1

def map(suc, list):

    if len(list) == 0:
        return []
    
    else:
        _list = [suc(list[0])]
        return _list + map(suc, list[1:])

print(map(suc, [0, 1, 2, 3, 4, 5]))