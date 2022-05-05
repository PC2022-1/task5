# Tarea 5
## Simulación de Oferta y Demanda
* Hay dos tiendas que venden empanadas.
* Hay M compradores de empanadas.
* En cada paso del experimento se escoge un comprador aleatoriamente y este decide cuantas empanadas compra y a cual tienda.
### Restriciones de la tienda
* Cada tienda produce un número de empenadas cada M pasos.
* En cada paso la empresa puede fijar el precio de las empanadas.
* Para esta decisión la tienda conoce el historial de sus propias ventas y cuantas empanadas le quedan. Queda a discreción del programador automatizar esta desición.
### Restriciones de los compradores
* Cada {M} pasos, cada comprador recibe una cantidad de dinero para comprar empanadas.
* En un paso dado el comprador solo le puede comprar a una tienda.
* Para esta decisión el comprador conoce el precio y disponibilidad de empanadas de cada tienda. Queda a discreción del programador automatizar esta desición.
### Inicialización del experimento
* La cantidad de dinero que recibe cada comprador es un número aleatorio entre $2000$ y $5000$.
* El número de empanadas producidas por cada empresa cada M pasos es un número aleatorio definido en el rango 2$m$ y 5$m$.
### Ejecución del experimento
* Ejecutar el experimento por un número de pasos.
* Almacenar el historial de compras, inventarios, y liquidez.
* Al terminar el experimento reportar gráficas de precio, inventario y liquidez del mercado.
### Implementación
* Implementar una clase `Comprador`, una clase `Tienda`, y una clase `Experimento`.

###Comentarios
No es cad
