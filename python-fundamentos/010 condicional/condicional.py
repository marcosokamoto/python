# Limpa a tela 
import os
os.system('cls') or None

a = True
if a:
    print("Resultado verdadeiro")
print("Fim do programa")


# Verificar se é maior ou menor
num1 = 10
num2 = 5

if num1 > num2:
    print(str(num1) + " é maior que " + str(num2))
print("Fim do programa")

if num2 < num1:
    print(str(num2) + " é menor que " + str(num1))
print("Fim do programa")


# Comparando os elementos
op = "*"
res = 0

if op == "+":
    res = num1 + num2

if op == "-":
    res = num1 - num2

if op == "*":
    res = num1 * num2

if op == "/":
    res = num1 / num2


print(str(num1) + op + str(num2) + " = " + str(res))