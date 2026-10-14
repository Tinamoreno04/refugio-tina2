''''''
class animal:
    def __init__(self,p_nombre, p_edad, p_especie):
      self.nombre = p_nombre
      self.edad = p_edad
      self.especie = p_especie
      self.energia = 50

    def presentarse(self):
        print(f"Hola, soy un animal{self.especie} y me llamo {self.nombre}. Tengo {self.edad} años y mi nivel de energía es {self.energia}")
    def jugar(self):
        self.energia -= 20
        if self.energia < 0:
            self.energia = 0
        print("Estoy jugando")

    def comer(self, gramos: int):
        self.energia += (gramos // 10)
        if self.energia > 100:
            self.energia = 100
        print(f"Estoy comiendo. Mi nivel de energía es {self.energia}")
    def dormir(self):
        self.energia += 30
        if self.energia > 100:
            self.energia = 100
        print(f"Estoy durmiendo. Mi nivel de energía es {self.energia}")