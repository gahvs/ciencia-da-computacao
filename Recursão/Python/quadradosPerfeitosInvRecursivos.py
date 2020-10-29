#Função que retorna os n primeiros números quadrados perfeitos de forma recursiva

def squares(n):

    return [] if n == 0 else [n*n] + squares(n-1)

print(squares(6))