import os
os.system('cls')

x = 10
try:
    print(x)
except:
    print("Erro no programa")
else:
    print("Tudo certo")
finally:
    print("Fim do tratamento")


num =- 10

if num < 1:
    raise Exception("Valor não permitido")

if not type(num) is int:
    raise Exception("Valor não permitido")
else: 
    print(str(num))