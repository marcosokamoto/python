# Limpa a tela 
import os
os.system('cls') or None

# Tipos de Dados
inteiro = 1 #int
string = "Curso de Python" # string
flutuante = 15.6 # float
boleano = True # bool
n1 = 5; n2 = 2; complexo = complex(n1,n2)
lista = ["Carro", "Avião", "Navio"] # List / Array
tupla = (0,100,1) # Tupla não aceita modificação como a List
dicionario ={ 
    "Canal" : "Youtube",
    "Curso" : "Curso de Python",
    "Nome" : "Marcos"
} # Dictionary
tipo_set = {5,7,4,5,7,4,8} # set não repete valores
tipo_frozenset = {5,7,4,5,7,4,8} # frozenset bloqueia o set, não pode alterar 



# Exibir resultados dos tipos de dados 
print("Int: " + str(inteiro))
print("String: " + string)
print("Float: " + str(flutuante))
print("Bool: " + str(inteiro))
print("Complex real: " + str(complexo.real))
print("Complex imaginaria: " + str(complexo.imag))
print("List na posição 0: " + str(lista[0]))
print("Tupla na posição 1: " + str(tupla[1]))
print("Dictionary: " + str(dicionario["Canal"]))
print("Set: " + str(tipo_set))
print("Frozenset: " + str(tipo_frozenset))