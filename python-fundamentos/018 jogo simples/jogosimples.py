import random
import os
erros = 0
sorteado = random.randrange(0,100)
os.system('cls')
jogador = int(input("Digite o seu numero: "))
while(sorteado != jogador):
    os.system('cls')
    if(sorteado > jogador):
        print("ERRO, o numero e maior")
    elif(sorteado < jogador):
        print("Erro, o numero e menor")
    erros+=1
    jogador = int(input("Digite seu numero: "))

    print("Numero " + str(jogador) + ", voce acertou em " + str(erros+1) + " tentativas")