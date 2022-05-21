#Receber uma lista e retorna o produto dos elementos de forma recursiva

def prod_list(list):

    return list[0] if len(list) == 1 else (list[-1] * prod_list(list[:-1]))

print(prod_list([1, 2, 3, 4, 5]))