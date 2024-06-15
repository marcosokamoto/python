# Limpa a tela 
import os
os.system('cls') or None

nome = input("Digite seu nome: ")
print("Nome digitado: " + nome)

print("-" * 50)

num1 = int(input("Digite o primeiro valor...: "))
num2 = int(input("Digite o segundo valor....: "))

res = num1 + num2

print("Soma dos valores: " + str(res))