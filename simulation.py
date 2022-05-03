from experimento import experimento # Clase Tienda
exp1 = experimento(m=10, pasos=500)
exp1.correr()
rep1 = exp1.reporte_liquidez()
rep2 = exp1.reportes()
exp1.archivar_reportes('archivo.xls')
print(rep1)
exp1.graficar_precio()