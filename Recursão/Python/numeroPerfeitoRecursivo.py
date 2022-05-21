#Verifica se um número n é perfeito usando recursão.

def calc(n, temp):

    if temp == 1:
        return temp

    if n % temp == 0:
        return temp + calc(n, temp-1)
    else:
        return 0 + calc(n, temp-1)

def alg_perfct(n):

    return True if n == calc(n, n-1) else False

print(alg_perfct(6))

