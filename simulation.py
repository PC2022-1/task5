import sys
try: 
    m = int(sys.argv[1])   
except IndexError:
    print("Falta ingresar el número de compradores")
    exit()

try: 
    pasos = int(sys.argv[2])  
except IndexError:
    print("Falta ingresar el número de pasos")
    exit()

from experimento import Experimento # Clase Experimento
exp1 = Experimento(m=m, pasos=pasos)
exp1.correr()
exp1.graficar_inventario() #Gráfica Inventario vs. Número de pasos
exp1.graficar_precio() #Gráfica Precio vs. Número de pasos
exp1.graficar_ganancia() #Gráfica Ganancias vs. Número de pasos
exp1.reportes() #Reporte en un archivo en Excel con el inventario, precios y ganancias según el número de pasos
