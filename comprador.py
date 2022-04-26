from random import randint, random, randrange

from tienda import tienda


class comprador:
    def __init__(self):
        self.dinero = randrange(2000,5000,50)
    def cargar_dinero(self):
        self.dinero += randrange(2000,5000,50)
    def comprar(self, tiendas):
        if tiendas[0].cantidad_empanadas() > 0 and tiendas[1].cantidad_empanadas() > 0:
            if tiendas[0].precio_empanada() < tiendas[1].precio_empanada():
                posibilidad = self.dinero//tiendas[0].precio_empanada()
                cant_compra = randint(0,posibilidad)
                tiendas[0].vender(cant_compra)
            else:
                posibilidad = self.dinero//tiendas[1].precio_empanada()
                cant_compra = randint(0,posibilidad)
                tiendas[1].vender(cant_compra)
        elif tiendas[0].cantidad_empanadas() > 0:
            posibilidad = self.dinero//tiendas[0].precio_empanada()
            cant_compra = randint(0,posibilidad)
            tiendas[0].vender(cant_compra)
        elif tiendas[1].cantidad_empanadas() > 0:
            posibilidad = self.dinero//tiendas[1].precio_empanada()
            cant_compra = randint(0,posibilidad)
            tiendas[1].vender(cant_compra)
