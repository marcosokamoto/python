import os
os.system('cls')

# Array / List
#carros = ["HRV", "Golf", "Focus", "Argo"]

#for x in carros:
#    print(x)

# Criando uma matriz
carros = [
    ["Modelo", "HRV"],
    ["Fabricante", "Honda"],
    ["Ano", "2016"]
]


# Adicionar um elemento na matriz
carros.append(["Cor","Prata"])

# Alterar um elemento na matriz
carros[2][1] = "2019"

# Exibir o conteúdo das matrizes
for l,c in carros:
    print("Linha: " + l + " | Coluna: " + c)