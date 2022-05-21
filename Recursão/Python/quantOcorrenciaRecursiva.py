#Recebe uma lista de inteiros e um inteiro n, e retorna o número de vezes que n ocorre na lista

def qnt(list, n):

    if len(list) == 0:
        return 0

    if list[0] == n:
        return 1 + qnt(list[1:], n)
    
    else:
        return 0 + qnt(list[1:], n)

print(qnt([1,2,3,2,1,2], 2))

