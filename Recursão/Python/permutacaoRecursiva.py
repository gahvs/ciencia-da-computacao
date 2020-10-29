#Recebe como argumento duas listas s e w, e retorna True se s for uma permutação de w

def permut(list, _list):

    if len(list) == len(_list) == 0:
        return True

    