#Recebe uma lista de listas, e retorna uma lista de listas com os indices em que 
#ocorrem números primos nas sublistas

import math

def func(primes):
    index = []
    for i in range(len(primes)):
        if primes[i] == True:
            index.append(primes.index(True)) 
            primes[i] = False
    return index 

def prime(num):

    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    
    return True 

def indexPrimeSub(lista):

    if len(lista) == 0:
        return []
    
    else:
        index = func( list(map(prime, lista[0])) )
        return [index] + indexPrimeSub(lista[1:])

print(indexPrimeSub([ [1,2,3,4,5],[11,12,13,14,15],[],[22,33,44]]))