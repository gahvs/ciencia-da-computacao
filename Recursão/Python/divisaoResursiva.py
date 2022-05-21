#Divide dois inteiros de forma recursiva

def div(a, b):
    #print(a)

    if a < b:
        return 0

    if a:
        return 1 + div(a-b, b)

    else:
        return 0

print(div(3, 4))  