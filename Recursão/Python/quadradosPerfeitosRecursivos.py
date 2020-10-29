#Função que retorna os n primeiros números quadrados perfeitos de forma recursiva

def squares(n):

    return [] if n == 0 else squares(n-1) + [n*n] 

print(squares(6))