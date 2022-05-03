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
            print(self.tiendas[0].cantidad_empanadas(), self.tiendas[0].obtener_ganacias(), self.tiendas[1].cantidad_empanadas(),self.tiendas[1].obtener_ganacias())
            if i % self.m == 0:  # Casos enteros de m.
                for ntienda in range(len(self.tiendas)):
                    empanadas = randint(2*self.m,5*self.m)
                    self.tiendas[ntienda].sumar_empanadas(empanadas) # Cargar empanada a tiendas
                for ncomprador in range(self.m):
                    self.compradores[ncomprador].cargar_dinero() # Cargar dinero a los compradores
                if i  > 0:
                    for ntienda in range(len(self.tiendas)):
                        self.tiendas[ntienda].regula_precio() # Cargar empanada a tiendas
                orden = [i for i in range(0,self.m)]
                num = choice(orden)
                self.compradores[num].comprar(self.tiendas) # Se compran en las tiendas
                orden.remove(num)
                print(self.tiendas[0].precio_empanada(),self.tiendas[1].precio_empanada())
                print(self.tiendas[0].historial_ganancias, self.tiendas[1].historial_ganancias)
            else:
                num = choice(orden)
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

exp1 = Experimento(m=10, pasos=500)
print(exp1.correr())