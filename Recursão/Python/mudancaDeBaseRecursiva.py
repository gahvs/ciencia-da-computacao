# Mudando a base de um número de forma recursvia


def conv(n):
    base = 2
    strConv = '0123456789ABCDEF'

    if n < base:
        return strConv[n]
    else:
        return conv(n//base) + strConv[n % base]


# base suportadas: 2~16
print(conv(4))
