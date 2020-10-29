#Recebe uma lista w e retorna duas listas, a primeira com os multiplos de 5 de w e a segunda com os 
#multiplos de 3.

def mult(lista):

    mult5 = []
    mult3 = []

    if len(lista) == 0:
        return []
        
    else:
        if lista[0] % 5 == 0: 
            mult5.append(lista[0])
            return mult5 + mult(lista[1:])

        if lista[0] % 3 == 0: 
            mult3.append(lista[0])
            return mult3 + mult(lista[1:])
        
print(mult( [1,2,3,4,5,9,15] ))         