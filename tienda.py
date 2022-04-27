from random import randint, randrange
class tienda:
    def __init__(self):
        self.empanadas = 1
        self.precio = randrange(100, 2000, 50)
        self.ganancias_diarias = 0
        self.ganancias = 0
        self.venta = 0
    def sumar_empanadas(self, empanadas):
        self.ganancias += self.ganancias_diarias
        self.empanadas += empanadas
        self.ganancias_anterior = self.ganancias_diarias
        self.ganancias_diarias = 0
    def cantidad_empanadas(self):
        return self.empanadas
    def precio_empanada(self):
        return self.precio
    def vender(self, cantidad):
        self.empanadas -= cantidad
        self.ganancias_diarias += cantidad*self.precio
        self.venta += 1
    def regula_precio(self):
        self.precio=(self.ganancias_anterior / self.empanadas) * (1 +(randint(0,10)/100)) #Se busca ganar más que el dia anterior aleaotriamente entre el 0 y el 10%
    def obtener_ganacias(self):
        return self.ganancias_diarias