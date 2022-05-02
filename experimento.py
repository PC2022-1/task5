# Importación de las librerias
from random import randint, choice # Elección al azar de un número entero
from comprador import comprador # Clase Comprador
from tienda import tienda # Clase Tienda
tienda1 = tienda()
class Experimento:
    # Iniciación del experimento
    def __init__(self,m,pasos):
        self.m = m
        self.pasos = pasos
        self.tiendas= [tienda(),tienda()]
        self.compradores =[]
        for i in range(self.m):
            self.compradores.append(comprador())

    # Método correr del experimento
    def correr(self):
        # Se generan las tiendas y los compradores
        for i in range(0,self.pasos):
            print(self.tiendas[0].obtener_ganacias(), self.tiendas[1].obtener_ganacias(), self.tiendas[0].venta)
            if i % self.m == 0:  # Casos enteros de m.
                for tienda in range(len(self.tiendas)):
                    empanadas = randint(2*self.m,5*self.m)
                    tienda.sumar_empanadas(empanadas) # Cargar empanada a tiendas
                for i in range(self.compradores):
                    self.compradores[i].cargar_dinero() # Cargar dinero a los compradores
                orden = [i for i in range(0,self.m)]
            for j in range(self.m):
                num= choice(orden)
                self.compradores[num].comprar(self.tiendas) # Se compran en las tiendas
                orden.remove(num)


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