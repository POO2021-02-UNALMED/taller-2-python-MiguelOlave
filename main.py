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
        cantidadCreados = 0
        def __init__(self, modelo, precio, asientos, marca, motor, registro):
            self.modelo = modelo
            self.precio = precio
            self.asientos = asientos
            self.marca = marca
            self.motor = motor
            self.registro = registro

        def cantidadAsientos(self):
            totAsientos = 0
            for asiento in self.asientos:
                if isinstance(asiento, Asiento):
                    totAsientos += totAsientos
            return totAsientos

        def verificarIntegridad(self):
            if (self.registro != self.motor.registro):
                return "Las piezas no son originales"
            for asientos in self.asientos:
                if (asientos.registro != self.registro):
                    return "Las piezas no son originales"
            return "Auto original"


