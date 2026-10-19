import cowsay


class Animal:
    def __init__(self, p_nombre, p_edad, p_especie):
        self.nombre = p_nombre
        self.edad = p_edad
        self.especie = p_especie
        self.energia = 50

    def presentarse(self):
        cowsay.cow(
            f"Hola, soy {self.nombre}. Especie: {self.especie}. "
            f"Edad: {self.edad} años."
        )

    def jugar(self):
        self.energia -= 20
        if self.energia < 0:
            self.energia = 0

    def comer(self, gramos: int):
        self.energia += gramos // 10
        if self.energia > 100:
            self.energia = 100
        if self.energia < 0:
            self.energia = 0

    def dormir(self):
        self.energia += 30
        if self.energia > 100:
            self.energia = 100