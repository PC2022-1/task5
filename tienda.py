from random import randint, randrange
from statistics import mean # Se importan las librerias a usar
class tienda:
    # Iniciación de la tienda
    def __init__(self):
        self.empanadas = 0
        self.precio = randrange(200,400,100) # precio inicial
        # Acumuladores
        self.ganancias_diarias = 0
        self.ganancias = 0
        self.ventadiaria = 0
        self.historial_ganancias = []
        self.emp_vendidas = []
        self.his_precio = []
        self.his_inventario = []
        self.empandasfindia = 0

    # Se agregan / Refill de empanadas
    def sumar_empanadas(self, empanadas):
        self.empandasfindia = self.empanadas
        self.ganancias += self.ganancias_diarias
        self.empanadas += empanadas
        self.historial_ganancias += [self.ganancias_diarias]
        self.ganancias_diarias = 0
        self.emp_vendidas += [self.ventadiaria]
        self.ventadiaria = 0
        self.his_precio += [self.precio]
        self.his_inventario += [self.empanadas]
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
    def regula_precio(self,m):
        try:
            if self.empandasfindia == 0:
                self.precio = round((self.precio * 2)/100)*100

            elif self.empandasfindia <= 2*m*0.1:
                self.precio = (1+round(((1 + ((mean(self.emp_vendidas[1:]) - self.emp_vendidas[-1]) / mean(self.emp_vendidas[1:]))) *
                (mean(self.historial_ganancias) / self.empanadas) * (1 +(randrange(35,50,5)/100)))/100)) *100

            elif self.empandasfindia <= 2*m*0.2:
                self.precio = (1+round(((1 + ((mean(self.emp_vendidas[1:]) - self.emp_vendidas[-1]) / mean(self.emp_vendidas[1:]))) *
                (mean(self.historial_ganancias) / self.empanadas) * (1 +(randrange(20,35,5)/100)))/100)) *100 # Se busca ganar más que el dia anterior aleaotriamente entre el 0 y el 10%

            elif self.empandasfindia <= 2*m*0.5:
                self.precio = (1+round(((1 + ((mean(self.emp_vendidas[1:]) - self.emp_vendidas[-1]) / mean(self.emp_vendidas[1:]))) *
                (mean(self.historial_ganancias) / self.empanadas) * (1 +(randrange(0,20,5)/100)))/100)) *100

            else:
                self.precio = (1+round(((1 + ((mean(self.emp_vendidas[1:]) - self.emp_vendidas[-1]) / mean(self.emp_vendidas[1:]))) *
                (mean(self.historial_ganancias) / self.empanadas) )/100)) *100
        except:
            self.precio = self.precio
        
        if self.precio == 0:
            self.precio = 100
        

    def obtener_ganacias(self):
        return self.ganancias_diarias
    def get_inv(self):
        return self.his_inventario
