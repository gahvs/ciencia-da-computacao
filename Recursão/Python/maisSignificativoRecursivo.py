#Retorna o algarismo mais significativo de um número inteiro de forma recursiva

def prime_alg(n):

    n = str(n)
    if len(n) == 1:
        return n

    if len(n)>1 :
        n = n[:-1]
        return prime_alg(n)
    
print(prime_alg(95465))
