# IMPORTA O MÓDULO OU BIBLIOTECA os (INTEGRA OS PROGRAMAS E RECURSOS DO S.O) 
import os   

# IMPRIME #60 VEZES
print("#" * 60) 

# CRIAMOS UMA VARIAVEL QUE VAI RECEBER DO USUÁRIO UM IP
ip_ou_host = input("Digite o IP ou host a ser verificado: ")

# CHAMANDO SYSTEM DA BIBLIOTECA os - COMANDO PING -n -num DE PACOTES QUE SERÃO 3 {}
print("-" * 60) # IMPRIME -60 VEZES
os.system('ping -n 3 {} ' .format(ip_ou_host))

 # IMPRIME -60 VEZES
print("-" * 60)
