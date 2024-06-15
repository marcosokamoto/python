# Limpa a tela 
import os
os.system('cls') or None


carros = ["HRV", "Golf", "Argo", "Focus","Fit", "Fusion", "Polo"]

for x in carros:
    print(x)
    if(x == "Golf"):
        print("  VW")

print("-" * 50)

for x in carros:
    print(x)
    if (x=="Fit"):
        break
    
print("Fim do programa")