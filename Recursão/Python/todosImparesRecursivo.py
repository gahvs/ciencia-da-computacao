#Recebe uma lista de inteiros e retorna true se ela contém apenas números impares e False caso contrário

def todosImpares(list):

    if len(list) == 0:
        return True
    
    if list[0] % 2 == 0:
        return False
    
    else:
        return True and todosImpares(list[1:])

print(todosImpares([1, 2, 3, 4, 5]))
