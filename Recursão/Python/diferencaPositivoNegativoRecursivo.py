#Recebe uma lista de inteiros e retorna a diferença entre o número de números positivos e 
#o número de números positivos

def negpos(list):

    if len(list) == 0:
        return 0

    if list[0] < 0:
        return -1 + + negpos(list[1:])
    
    else:
        return 1 + negpos(list[1:])

print(negpos( [-1, 1] ))


