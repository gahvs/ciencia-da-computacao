#Calcula o fatorial de um número natural de forma recursiva

def fat(n):
    
    return 1 if n <= 1 else (n * fat(n-1))

print(fat(3))