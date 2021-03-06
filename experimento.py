# Importación de las librerias
from random import randint, choice # Elección al azar de un número entero
from comprador import comprador # Clase Comprador
from tienda import tienda # Clase Tienda
import sys
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
from pandas import DataFrame

fileDirectory = os.path.abspath(__file__)
parentDirectory = os.path.dirname(fileDirectory)
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
        
        for i in range(0,self.pasos):
            
            if i % self.m == 0:  # Casos enteros de m.
                for ntienda in range(len(self.tiendas)):
                    empanadas = randint(2*self.m,5*self.m)
                    self.tiendas[ntienda].sumar_empanadas(empanadas) # Cargar empanada a tiendas

                for ncomprador in range(self.m):
                    self.compradores[ncomprador].cargar_dinero() # Cargar dinero a los compradores

                if i  > 0:
                    for ntienda in range(len(self.tiendas)):
                        self.tiendas[ntienda].regula_precio(self.m) # Cargar empanada a tiendas

                orden = [i for i in range(0,self.m)]
                num = choice(orden)
                self.compradores[num].comprar(self.tiendas) # Se compran en las tiendas
                orden.remove(num)

            else:
                num = choice(orden)
                self.compradores[num].comprar(self.tiendas) # Se compran en las tiendas
                orden.remove(num)

    # Este metodo grafica el inventario con los mismos datos del reporte de excel
    def graficar_inventario(self):
        fig = plt.figure(figsize=(280, 5))
        ax = fig.gca()
        
        if int(self.pasos/(self.m)) <= 120:
               
            xtick = [(int(self.pasos/(10*self.m)) + 15)*i for i in range(0, int(self.pasos/self.m))]

            if int(self.pasos/(self.m)) >= 50:
                ax.bar(xtick, self.tiendas[0].his_inventario,
                label="Inventario Tienda La central", align= 'edge', width=- (int(self.pasos/(10 * self.m))) )
                ax.bar(xtick, self.tiendas[1].his_inventario,
                label="Inventario Tienda Kokoriko", align= 'edge', width=  (int(self.pasos/(10 * self.m))) )
            else:
                ax.bar(xtick, self.tiendas[0].his_inventario,
                label="Inventario Tienda La central", align= 'edge', width= -(int(self.pasos/(10 * self.m)) + 5) )
                ax.bar(xtick, self.tiendas[1].his_inventario,
                label="Inventario Tienda Kokoriko", align= 'edge', width=  (int(self.pasos/(10 * self.m)) + 5) )
        
            xtick0 = [(int(self.pasos/(10 * self.m)) + 15)*i - 1/2 for i in range(0, int(self.pasos/self.m))]
            ax.plot(xtick0, self.tiendas[0].his_inventario, '--', alpha= .5)
            xtick1 = [(int(self.pasos/(10 * self.m)) + 15)*i + 1/2 for i in range(0, int(self.pasos/self.m))]
            ax.plot(xtick1, self.tiendas[1].his_inventario, '--', alpha= .5)

            if int(self.pasos/(self.m)) > 50:
                plt.xticks(xtick, np.arange(1, int(self.pasos/self.m) + 1, step=1))
                plt.xticks(rotation = -45, fontsize= 6)
            else:
                plt.xticks(xtick, np.arange(1, int(self.pasos/self.m) + 1, step=1))
                
        else:
            ax.plot(range(0, int(self.pasos/self.m)), self.tiendas[0].his_inventario, label="Inventario Tienda La central")
            ax.plot(range(0, int(self.pasos/self.m)), self.tiendas[1].his_inventario, label="Inventario Tienda Kokoriko")

        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['left'].set_visible(False)
        plt.xlabel('Días')               # label on the x axis
        plt.ylabel('Cantidad Empanadas')               # label on the y axis
        plt.title('Cantidad Empanadas vs Días')
        plt.legend()
        plt.gca().yaxis.grid(True)
        plt.show()

    def graficar_precio(self):
        fig = plt.figure(figsize=(48, 8))
        ax = fig.gca()
        ax.plot(range(0, int(self.pasos/self.m)), self.tiendas[0].his_precio, label="Precio Tienda La central")
        ax.plot(range(0, int(self.pasos/self.m)), self.tiendas[1].his_precio, label="Precio Tienda Kokoriko")
        plt.xlabel('Días')               # label on the x axis
        plt.ylabel('Precio')               # label on the y axis
        plt.title('Precio vs Días')
        plt.grid(True)
        plt.legend()
        plt.show()

    def graficar_ganancia(self):
        fig = plt.figure(figsize=(48, 8))
        ax = fig.gca()
        ax.plot(range(0, int(self.pasos/self.m)), self.tiendas[0].historial_ganancias, label="Ganancia Tienda La central")
        ax.plot(range(0, int(self.pasos/self.m)), self.tiendas[1].historial_ganancias, label="Ganancia Tienda Kokoriko")
        plt.xlabel('Días')               # label on the x axis
        plt.ylabel('Ganacias')               # label on the y axis
        plt.title('Ganancias vs Días')
        plt.grid(True)
        plt.legend()
        plt.show()
        
    def reportes(self):
        if not os.path.exists(parentDirectory):
            os.makedirs(parentDirectory)

        out_path = os.path.join(parentDirectory, "reporte.xlsx")
        df = DataFrame({'Inventario tienda La central': self.tiendas[0].his_inventario,
        'Inventario tienda Kokoriko': self.tiendas[1].his_inventario,
        'Precio tienda La central': self.tiendas[0].his_precio, 
        'Precio tienda Kokoriko': self.tiendas[1].his_precio,
        'Ganancia diaria tienda La central': self.tiendas[0].historial_ganancias,
        'Ganancia diaria tienda Kokoriko': self.tiendas[1].historial_ganancias })
        df.index = range(1, int(self.pasos/self.m) + 1)

        writer = pd.ExcelWriter(out_path)
        df.to_excel(writer, sheet_name='sheet1', index=True)
        writer.save()
