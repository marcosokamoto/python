import os
os.system("cls")

valores = [1,5,3,2]
def somar(num):
    r = 0
    for n in num:
        r += n
    return r

def valLista(num):
    for v in num:
        print(v)

#valLista(valores)

print(str(valores) + ": Soma = " + str(somar(valores)))