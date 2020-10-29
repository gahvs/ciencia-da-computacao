#Recebe duas listas e retorna True se elas forem iguais e False caso contrário

def equal(list, _list):

    if len(list) == len(_list) == 0:
        return True

    if list[-1] != _list[-1]:
        return False and equal(list[:-1], _list[:-1])
    
    else:
        return True and equal(list[:-1], _list[:-1])

print(equal( [1, 2, 3],[1, 2, 3] ))

