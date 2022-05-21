#Retorna o n-ésimo número da sequência de Fibonacci de forma recursiva

# 1 1 2 3 5 8 13 21 ...

def fib(n):
    
    return ( fib(n-1) + fib(n-2) ) if n > 1 else n


print(fib(4))