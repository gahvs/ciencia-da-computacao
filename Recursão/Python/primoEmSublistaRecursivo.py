#Recebe uma lista de listas, e retorna True se houver um número primo em alguma das sublistas e Fal se
#caso contrário

from functools import reduce
import math

exp = lambda item, item_: item or item_

def prime(num):

    for i in range(2, int(math.sqrt(num)+1)):

        if num % i == 0:
            return False
    
    return True 

def sublistPrime(l):

    if len(l[-1]) == 0:
        return False

    else:
        list_ = list( map(prime, l[-1]) )
        return reduce(exp, list_) or sublistPrime(l[:-1])

print( sublistPrime( [[4,4,4,4],[4,4,4],[],[4]] ) )
