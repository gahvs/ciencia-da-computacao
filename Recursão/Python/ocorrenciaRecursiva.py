#Recebe uma lista de inteiros e um numero n, e retorna True se n ocorre na lista e False caso contrário

def ocorre(list, n):

    if len(list) == 0:
        return False
    
    if list[0] == n:
        return True
    
    else:
        return False or ocorre(list[1:], n)

print(ocorre([1, 2, 3], 4))

