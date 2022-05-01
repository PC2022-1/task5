# Importación de las librerias
from random import randint # Elección al azar de un número entero
from comprador import comprador # Clase Comprador
from tienda import tienda # Clase Tienda

class Experimento:
    # Iniciación del experimento
    def __init__(self,m,pasos):
        self.m = m
        self.pasos = pasos

    # Método correr del experimento
    def correr(self):
        # Se generan las tiendas y los compradores
        tiendas = 2 * [tienda()]
        compradores = self.m * [comprador()]

        for tienda in tiendas:
            empanadas = randint(2*self.m,5*self.m)
            tiendas.sumar_empanadas(empanadas) # Se inicializan las empanadas en la tienda

        for i in range(1,self.pasos+1):

            print(tiendas[0].obtener_ganacias(), tiendas[1].obtener_ganacias(), tiendas[0].venta)
            if i % self.m == 0:  # Casos enteros de m.
                for comprador in compradores:
                    comprador.cargar_dinero() # Cargar dinero a los compradores

                for tienda in tiendas:
                    empanadas = randint(2*self.m,5*self.m)
                    tienda.sumar_empanadas(empanadas) # Cargar empanada a tiendas

                    
            for comprador in compradores:
                comprador.comprar(tiendas) # Se compran en las tiendas


    def reportes(self):
        return None

    def reporte_liquidez(self):
        return None

    def graficar_precio(self):
        return None

    def archivar_reportes(self):
        return None

exp1 = Experimento(m=10, pasos=30)
print(exp1.correr())