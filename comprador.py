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
        if tiendas[0].cantidad_empanadas() > 0 or tiendas[1].cantidad_empanadas() > 0:
            lista = abs(int(tiendas[0].cantidad_empanadas() * (2000 - tiendas[0].precio_empanada())/100)) * [0] + abs(int(tiendas[1].cantidad_empanadas() * (3000 - tiendas[1].precio_empanada())/100)) * [1]
            if len(lista)>0:
                sel = choice(lista)
                pos_compra = int(self.dinero/tiendas[sel].precio_empanada())
                if pos_compra < tiendas[sel].cantidad_empanadas():
                    cantidad = randint(0,int(self.dinero/tiendas[sel].precio_empanada()))
                else:
                    cantidad = randint(0,tiendas[sel].cantidad_empanadas())
                tiendas[sel].vender(cantidad)
