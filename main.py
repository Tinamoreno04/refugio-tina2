from animal import Animal


luna = Animal("Luna", 3, "gato")
rocky = Animal("Rocky", 5, "perro")
kiwi = Animal("Kiwi", 2, "loro")

luna.presentarse()
rocky.presentarse()
kiwi.presentarse()

luna.jugar()
luna.comer(150)
luna.dormir()

rocky.jugar()
rocky.jugar()
rocky.jugar()
rocky.comer(300)

kiwi.comer(100)
kiwi.dormir()

print(f"Luna: energía {luna.energia}")
print(f"Rocky: energía {rocky.energia}")
print(f"Kiwi: energía {kiwi.energia}")