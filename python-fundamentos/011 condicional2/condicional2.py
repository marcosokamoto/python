# Limpa a tela 
import os
os.system('cls') or None


# Declarar variaveis
num1 = 10
num2 = 5
clima = "sol"
lugar = ""
dinheiro = 500


if clima == "sol" or (dinheiro >= 300 and dinheiro <= 500):
    lugar = "clube"
else:
    lugar = "cinema"

print("Vou ao " + lugar)


# Efetuando tomada de decisão
op = "*"
res = 0

if op == "+":
    res = num1 + num2

elif op == "-":
    res = num1 - num2

elif op == "*":
    res = num1 * num2

elif op == "/":
    res = num1 / num2

else:
    print("Operador inválido")

print(str(num1) + op + str(num2) + " = " + str(res))