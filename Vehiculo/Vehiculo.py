def arrancar():
    return 'Motor encendido'


class Coche:
    motor = None
    puertas= 0
    ruedas= 0
    techo = False

    def __init__(self, motor, puertas, ruedas):
        self.motor = motor
        self.puertas = puertas
        self.ruedas = ruedas

    def __str__(self):
        return f'Este coche tiene {self.puertas} puertas, {self.ruedas} ruedas, motor {self.motor}'

    def abrirtecho(self):
        self.techo = True

auto1 = Coche(123, 3, 4)
