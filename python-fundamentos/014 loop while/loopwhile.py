# Limpa a tela 
import os
os.system('cls') or None

i = 0
while i < 9:
    print(i)
    i+=1
    if(i >= 5):
        break
print("\nFim do loop")

print("-" * 50)


# Percorrendo um lista através do while
x = 0
carros = ["HRV", "Golf","Argo", "Onix", "Focus"]
tam = len(carros)

while x < tam:
    print(carros[x])
    x+=1
    if(x >= 5):
        break
print("\nFim do loop")

print("-" * 50)

# Utilizando o INPUT para criar uma lista 

cores = []
cor = input("Digite o nome da nova cor: ")
while cor != "-1":
    cores.append(cor)
    cor = input("Digite o nome da nova cor: ")

os.system('cls')
for n in cores:
    print(n)

print("\nFim do loop")

