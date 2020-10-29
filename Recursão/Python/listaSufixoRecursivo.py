#Recebe uma lista s e uma lista w e retorna True se s for sufixo de w e False caso contrário

def sufixo(list, _list):

    if len(list) == 0:
        return True
    
    if list[-1] != _list[-1]:
        return False and sufixo(list[:-1], _list[:-1])
    
    else:
        return True and sufixo(list[:-1], _list[:-1])

print(sufixo([2,3],[1,2,3]))
