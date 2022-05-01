from random import randint, randrange # Se importan las librerias a usar
class tienda:
    # Iniciación del experimento
    def __init__(self):
        self.empanadas = 1
        self.precio = randrange(100, 2000, 50) # No se define un precio fijo de empanadas?
        # Acumuladores
        self.ganancias_diarias = 0
        self.ganancias = 0
        self.venta = 0

    # Se agregan / Refill de empanadas
    def sumar_empanadas(self, empanadas):
        self.ganancias += self.ganancias_diarias
        self.empanadas += empanadas
        self.ganancias_anterior = self.ganancias_diarias
        self.ganancias_diarias = 0
    
    # Conteo de la cantidad de empanadas
    def cantidad_empanadas(self):
        return self.empanadas
    
    # Precio de la empanada 
    def precio_empanada(self):
        return self.precio

    # Acción de venta
    def vender(self, cantidad):
        self.empanadas -= cantidad
        self.ganancias_diarias += cantidad*self.precio
        self.venta += 1

    # Regulación de precios
    def regula_precio(self):
        self.precio=(self.ganancias_anterior / self.empanadas) * (1 +(randint(0,10)/100)) #Se busca ganar más que el dia anterior aleaotriamente entre el 0 y el 10%
    
    # ¿Por que se diferencian?
    def obtener_ganacias(self):
        return self.ganancias_diarias