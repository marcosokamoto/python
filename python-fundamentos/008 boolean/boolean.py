aula = True 
aula01 = False
valor = 10 > 15
curso = "Python" # retorna True
curso01 = "" # retorna False
num = 0 # retorna False, diferente de 0 retorna True

print(aula)
print(aula01)
print(valor)
print(bool(curso))
print(bool(curso01))

if aula:
    print("Possui texto")
else:
    print("Vazio")
