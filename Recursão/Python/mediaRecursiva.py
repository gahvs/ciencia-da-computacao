#Calcula a média de uma sequência de números de forma recursiva

def media_digitos(num):
    num = str(num)

    if len(num) == 1:
        return int(num)

    else:
        n = len(num)
        return (int(num[0]) + (n-1) * media_digitos(num[1:])) / n

print(media_digitos(1234))