from random import randint, random


class comprador:
    def __init__(self):
        self.dinero = 0
    def cargarDinero(self, dinero):
        self.dinero = dinero    
    def escogerTienda(self, tiendas):
        numero = randint(0,len(tiendas)-1)
        self.tiendas = tiendas[numero]
        