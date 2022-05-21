#Recebe uma lista e retorna true se ela contém um número Par e False caso contrário

def parImpar(list):

    if len(list) == 0:
        return False

    if list[0] % 2 == 0:
        return True
    
    else:
        return False or parImpar(list[1:])

print(parImpar([1]))