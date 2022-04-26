from random import randint
class tienda:
    def __init__(self):
        self.empanadas = 0
        self.precio = randint(2000, 5000)
    def sumar_empanadas(self, empanadas):
        self.empanadas += empanadas
    def precioEmpanada(self, precio):
        self.precio = precio
    def regulaPrecio(self):
        return None
    