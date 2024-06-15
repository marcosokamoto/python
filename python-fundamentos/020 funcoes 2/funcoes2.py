import os
os.system("cls")

# soma passando parametro para a funcao
def soma(*num):
    r = 0
    for n in num:
        r += n

    print("Soma = " + str(r))

soma(5,7)
soma(12,8)

# Argumentos arbitrarios
def textos(*txt):
    for t in txt:
        print(t)

textos("Canal", "Youtube","Curso", "de", "Python")

# Passar um valor padrao para o argumento arbitrario

def carros(c="Golf"):
    print("Modelo: " + c)

carros()

# Passar uma lista de valores
valores = [1,5,3,2]
def somar(num):
    r = 0
    for n in num:
        r += n

    print("Soma = " + str(r))

somar(valores)