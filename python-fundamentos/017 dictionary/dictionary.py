import os
os.system('cls')

carro={"Fabricante":"Honda",
        "Modelo":"HRV",
        "Ano":"2016",
        "Cor":"Prata"
        }

# Exibe Honda através da chave Fabricante
print(carro["Fabricante"])
print(carro.get("Fabricante"))
print("-" * 50)

# Alterar um elemento
carro["Cor"] = "Preto"

print(carro)
print(carro["Cor"]) # Exibe somente a cor
print("-" * 50)

# Percorrer todos os elementos 
print("Percorrer todos os elementos\n")
for x in carro:
   # print(x) Chave
   print(carro[x]) # Valor

print("-" * 50)

# Exibir os itens
print("Exibir os itens\n")
for c,v in carro.items():
    print(c + ": " + v) 

print("-" * 50)

# Verificar se há um elemento no dicionário
if "Modelo" in carro:
    print("Sim modelo e uma chave\n")

print("-" * 50)

# Verificar o tamanho do dicionário
print("Tamanho do Dictionary: " + str(len(carro)))

print("-" * 50)

# Adicionar elemento ao dicionário
carro["Cambio"] = "Automatico"
print(carro)

print("-" * 50)

# Remover um elemento do dicionário
carro.pop("Cambio") # del carro["Cambio"]
print(carro)
print("Cambio removido")

print("-" * 50)

# Limpar todos os elementos
carro.clear()

# Novo dicionario
carros = {
    "Carro1":{
        "Fabricante":"Honda",
        "Modelo":"HRV"
    },
    "Carro2":{
        "Fabricante":"Volkswagem",
        "Modelo":"Golf"
    },
    "Carro3":{
        "Fabricante":"Ford",
        "Modelo":"Focus"
    }
}

# Exibir novo dicionário
print(carros["Carro1"]["Fabricante"])

print("-" * 50)

# Criar para cada carro sendo um dicionario e depois criar um dicionario com todos os carros

Carro1={
    "Fabricante":"Honda",
    "Modelo":"HRV"
}
Carro2={
   "Fabricante":"Volkswagem",
   "Modelo":"Golf"
}
Carro3={
    "Fabricante":"Ford",
    "Modelo":"Focus"
}

Carros={
    "C1": Carro1,
    "C2": Carro2,
    "C3": Carro3
}

print(Carros["C1"]["Modelo"])