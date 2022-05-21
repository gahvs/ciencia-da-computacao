#Recebe uma lista de números inteiros e retorna uma lista com valor True onde ocorre um valor par e 
#False caso contrário

def func(l):

    if len(l) == 0:
        return []
    
    if l[0] % 2 == 0:
        _list = [True]
        return _list + func(l[1:])
    
    else:
        _list = [False]
        return _list + func(l[1:])

print(func([3, 2, 1, 0]))