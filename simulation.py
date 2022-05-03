import sys
try: 
    m = int(sys.argv[1])   
except IndexError:
    print("Falta ingresar el numero de compradores")
    exit()

try: 
    pasos = int(sys.argv[2])  
except IndexError:
    print("Falta ingresar el numero pasos")
    exit()

from experimento import Experimento # Clase Tienda
exp1 = Experimento(m=10, pasos=500)
exp1.correr()
exp1.graficar_inventario()
exp1.graficar_precio()
exp1.graficar_ganancia()
rep2 = exp1.reportes()
