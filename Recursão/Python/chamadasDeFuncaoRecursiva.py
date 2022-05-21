#F(x) = { x / 2  => se x for um número par
#       { 3x + 1 => caso contrário
#Retorna o número de chamadas para que F(n) chamada recursivamente retorne 1

def num_it(n):

    if n == 1:
        return 0

    if n%2 == 0:
        return 1 + num_it(n/2)
    
    else:
        return 1 + num_it((3*n) + 1)

print(num_it(11))