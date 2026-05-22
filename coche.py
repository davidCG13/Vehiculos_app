class Coche:
    def __init__(self, marca, modelo, año, puertas):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.puertas = puertas

    def descripcion(self):
    return f"{self.marca} {self.modelo} ({self.año}) - {self.puertas} puertas"
