# Limpa a tela 
import os
os.system('cls') or None

def linha():
    print("-" * 100)


# Cria uma lista de carros
carros = ["HRV", "Golf", "Argo", "Focus"]

# Copia toda a lista para uma nova lista
carros2=list(carros)
print(str(len(carros2)) + " carros na lista carros2: " + str(carros2) + "\n")
linha()

# Fundir duas lista
carros3 = carros + carros2 
print(str(len(carros3)) + " carros na lista carros3: " + str(carros3) + "\n")
linha()

# Altera na terceira posicção no lugar de Focus agora é Fusion
carros[3]="Fusion" 

# Metodo Append - adiciona item ao final da lista
carros.append("Fit")
carros.append("Fusion")
carros.append("Polo")

# Verifica o tamanho da lista 
print(str(len(carros)) + " carros na lista: " + str(carros) + "\n")
linha()

# Remove item da lista 
carros.remove("Fusion")
print("\nCarro Fusion removido da lista")
print(str(len(carros)) + " carros na lista: " + str(carros) + "\n")
linha()

# Metodo Pop remove o último item da lista
carros.pop()
print(str(len(carros)) + " carros na lista: " + str(carros) + "\n")
linha()

# Metodo Del remove o item selecionado
del carros[2]
print(str(len(carros)) + " carros na lista: " + str(carros) + "\n")
linha()

# Metodo Clear limpa todos os elementos da lista
carros.clear()
print(str(len(carros)) + " carros na lista: " + str(carros) + "\n")


