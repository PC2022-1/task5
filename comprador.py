# Se importan las librerias a usar
from random import randint, randrange, choice
from tienda import tienda


class comprador:
    # Inicialización de Comprador
    def __init__(self):
        self.dinero = 0 # Monto inicial
        
    def cargar_dinero(self):
        self.dinero += randrange(2000,5000, 50) # Monto cargado

    def comprar(self, tiendas): # Métodología de compra, precios max empanada 3000
        Lista = int(tiendas[0].cantidad_empanadas() * (3000 - tiendas[0].precio_empanada())/50) * [0] + int(tiendas[1].cantidad_empanadas() * (3000 - tiendas[1].precio_empanada())/50) * [1]
        print(tiendas[0].cantidad_empanadas(), tiendas[1].cantidad_empanadas())
        sel = choice(Lista)
        cantidad = randint(0,int(self.dinero/tiendas[sel].precio_empanada()))
        tiendas[sel].vender(cantidad)
