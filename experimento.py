from random import randint
from comprador import comprador
from tienda import tienda

class Experimento:
    def __init__(self,m,pasos):
        self.m = m
        self.pasos = pasos
    def correr(self):
        tiendas = [tienda(), tienda()]
        compradores = []
        for i in range(len(tiendas)):
            empanadas = randint(2*self.m,5*self.m)
            tiendas[i].sumar_empanadas(empanadas) 
        for i in range(self.m):
            compradores.append(comprador())
        for i in range(1,self.pasos+1):
            print(tiendas[0].obtener_ganacias(), tiendas[1].obtener_ganacias(), tiendas[0].venta)
            if i%self.m == 0:
                for i in range(self.m):
                    compradores[i].cargar_dinero()
                for i in range(len(tiendas)):
                    empanadas = randint(2*self.m,5*self.m)
                    tiendas[i].sumar_empanadas(empanadas)                    
                for i in range(self.m):
                    compradores[i].comprar(tiendas)
            else:
                for i in range(self.m):
                    compradores[i].comprar(tiendas)
        return tiendas[0].obtener_ganacias(), tiendas[1].obtener_ganacias()
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