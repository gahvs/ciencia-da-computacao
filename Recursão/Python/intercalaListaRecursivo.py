#Recebe duas listas e retorna uma lista resultante da intercalação das listas argumento.

def itcl(list, list_):

    if len(list) == len(list_) == 0:
        return []

    if len(list_) == 0 and len(list) != 0:
        return [list[0]] + itcl(list[1:], [])

    elif len(list) == 0 and len(list_) != 0:
        return [list_[0]] + itcl([], list_[1:])
    
    else:
        return [list[0], list_[0]] + itcl(list[1:], list_[1:])

print(itcl( [2,4], [1,3,5,7,9] ))
