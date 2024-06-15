# Limpa a tela 
import os
os.system('cls') or None

import random # importa random

num_i = 10
num_f = 5.2
num_c = 1j

num_r = random.randrange(0,59)

x = num_r

print("Valor: " + str(x) + " - Tipo: " + str(type(x)))

num_array = [ # List / Array
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59)
] 

print("Valor 1: " + str(num_array[0]))
print("Valor 2: " + str(num_array[1]))
print("Valor 3: " + str(num_array[2]))
print("Valor 4: " + str(num_array[3]))
print("Valor 5: " + str(num_array[4]))