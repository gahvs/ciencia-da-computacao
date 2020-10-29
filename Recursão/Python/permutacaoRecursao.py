#Recebe duas listas como argumento e retorna True se uma for permutação da outra e False caso contrário.

def permut(lista, lista_):

    lista.sort()
    lista_.sort()

    if len(lista) != len(lista_):
        return False
    
    if len(lista) == 0:
        return True

    else :
        if lista.count(lista_[0]) == 1:
            return True and permut(lista[1:], lista_[1:])
        else:
            return False

print(permut( [1,2,3],[1,2,4] ))