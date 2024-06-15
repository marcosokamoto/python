# Limpa a tela 
import os
os.system('cls') or None

curso = "Curso de Python"

# retorna True porque Python está em curso
res = "Python" in curso
print(curso)
print("-" * len(curso)) # separador
print("\nA palavra Python está contida na string: " + str(res))

# retorna False porque Python está em curso
res = "Python" not in curso
print("\nA palavra Python não está contida na string " + str(res))


# Converte o text em maiuscula e verifica a palavra python se está contida na string retornando True
texto = "Curso de Python"
palavra = "python"

res = palavra.upper() in texto.upper()
print("\nA palavra python está contida na string: " + str(res))


# Concatenação de Strings
materia = "Programação Python"
canal = "Youtube"

resultado = materia + " no " + canal
print(resultado)

# Concatenação de data
cidade = "São Paulo"
dia = 15 
mes = "Dezembro"
ano = 2022

print(cidade + ", " + str(dia) + " de " + mes + " de " + str(ano))

# Outra forma de exibir data
data = "{}, {} de {} de {}\n {}"
print(data.format(cidade, dia, mes, ano, canal))

# \' \"  \n \r \t \b