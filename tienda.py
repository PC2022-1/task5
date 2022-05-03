from random import randint, randrange # Se importan las librerias a usar
class tienda:
    # Iniciación de la tienda
    def __init__(self):
        self.empanadas = 0
        self.precio = randrange(100,2000,100) # No se define un precio fijo de empanadas?
        # Acumuladores
        self.ganancias_diarias = 0
        self.ganancias = 0
        self.ventadiaria = 0
        self.historial_ganancias = []
        self.emp_vendidas = []
        self.his_precio = []
        self.his_inventario = []

    # Se agregan / Refill de empanadas
    def sumar_empanadas(self, empanadas):
        self.ganancias += self.ganancias_diarias
        self.empanadas += empanadas
        self.historial_ganancias += [self.ganancias_diarias]
        self.ganancias_diarias = 0
        self.emp_vendidas += [self.ventadiaria]
        self.ventadiaria = 0
        self.his_precio += [self.precio]
        self.his_inventario = [self.empanadas]
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
        self.ventadiaria += 1

    # Regulación de historial_ganancias
    def regula_precio(self):
        if self.historial_ganancias[-1] != 0:
            self.precio = int(((self.historial_ganancias[-1] / self.empanadas) * (1 +(randint(0,10)/100))))#Se busca ganar más que el dia anterior aleaotriamente entre el 0 y el 10%
        else:
            self.precio = self.precio/2
    # ¿Por que se diferencian?
    def obtener_ganacias(self):
        return self.ganancias_diarias
