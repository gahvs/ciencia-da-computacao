#Recebe duas listas e retorna True se a primeira for sufixo da segunda e False caso contrário

def sfx(list, list_):

    if len(list) == 0:
        return True

    if list[-1] == list_[-1]:
        return True and sfx(list[:-1], list_[:-1])

    else:
        return False

print(sfx( [1,2,3],[1,2,3] ))

