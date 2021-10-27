class Asiento:
        def __init__(self, color, precio, registro):
            self.color = color
            self.precio = precio
            self.registro = registro

        def cambiarColor(self, color):
            if color in ["rojo", "verde", "amarillo", "negro", "blanco"]:
                self.color = color
class Motor:
        def __init__(self, numeroCilindros, tipo, registro):
            self.numeroCilindros = numeroCilindros
            self.tipo = tipo
            self.registro = registro

        def cambiarRegistro(self, registro):
            self.registro = registro

        def asignarTipo(self, tipo):
            if tipo in ["electrico", "gasolina"]:
                self.tipo = tipo

class Auto:
        def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
            self.modelo = modelo
            self.precio = precio
            self.asientos = asientos
            self.marca = marca
            self.motor = motor
            self.registro = registro
            self.cantidadCreados = cantidadCreados





