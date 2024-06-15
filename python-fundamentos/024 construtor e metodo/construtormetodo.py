import os
os.system('cls')

class Carro:
    velMax = 0
    ligado = False
    cor = ""

    # Definindo método construtor
    def __init__(self,v,l,c):
        self.velMax = v
        self.ligado = l
        self.cor = c

    # Criar novo método Mostrar
    def mostrar(self):
        print("Velocidade Maxima: " + str(self.velMax))
        print("Cor: " + self.cor)
        estado = "sim" if self.ligado else "N"
        print("Ligado: " + estado)
        print("----------------------------------------")
    
    # Definir o método ligar
    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False
    
    def andar(self):
        if(self.ligado):
            print("Andando")
        else:
            print("Carro desligado")


# Definindo valor no construtor        
c1 = Carro(200, False, "Preto")
c2 = Carro(120, False, "Branco")
c3 = Carro(350, False, "Vermelho")

c1.ligar()

# Chamar o método Mostrar
c1.mostrar()
c2.mostrar()
c3.mostrar()

c2.ligar()
c2.andar()


