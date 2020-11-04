pica = "\u2660"
corazon = "\u2665"
diamante = "\u2666"
trebol = "\u2663"
import random

class Carta:

    def __init__(self,tanto,palo):
        self.tanto = tanto
        self.palo = palo
    
    def __str__(self):
        return "[{}-{}]".format(self.tanto,self.palo)

class Baraja:
    def __init__(self):
        palo = [pica, corazon, diamante, trebol]
        tantos = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.mazo = []
        for j in tantos:
            for h in palo:
                cartas = Carta (j,h)
                self.mazo.append(cartas)


    def mostrar_baraja(self):
      print()
      for num,cartas in enumerate(self.mazo):
            if (num-3) % 4 != 0:
                print(cartas, end=" ")
            else:
                print(cartas)
      print()

def __init__(self):
    

Baraja = Baraja()
Baraja.mostrar_baraja()







    