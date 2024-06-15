# Limpa a tela 
import os
os.system('cls') or None

curso = "Curso de Python"
print(curso)
print("Posição 0 letra: " + str(curso[0]))
print("Faixa da posição 0 até 5: " + str(curso[0:5]))
print("Tamanho da string: " + str(len(curso)))

print("-" * 40)
# Remove espaços na string
materia = "Curso de Python"
print(materia.strip())

# converte para minusculo
print(materia.lower
().strip())

# converte para maiuscula
print(materia.upper
().strip())

# troca a string 
print(materia.replace("Python", "C#"))

# faz uma subdivisão numa string
a = materia.split(" ")
print(a[2])