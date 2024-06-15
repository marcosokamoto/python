import os
os.system('cls')

# Na lista aceita modificação
#l_carros = ["HRV","Golf","Argo"]

# Na tupla não aceita modificação
#t_carros = ("HRV","Golf","Argo")


# Converter uma tupla para uma lista
t_carros = ("HRV","Golf","Argo")
l_carros = list(t_carros)
l_carros[2] = "Focus"

# Converter uma lista em tupla
t_carros = tuple(l_carros)

for x in t_carros:
    print(x)
