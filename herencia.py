# Clase base (superclase)
class Animal:
    def __init__(self, nombre, edad,tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo=tipo

    def hacer_sonido(self):
        return "Sonido genérico"

    def info(self):
        return f"Soy {self.nombre} y tengo {self.edad} años."

# Subclase que hereda de Animal
class Gallina(Animal):
    def __init__(self, nombre, edad, numero_huevos):
        super().__init__(nombre, edad)  # Llamada al constructor de la superclase
        self.numero_huevos = numero_huevos

    def hacer_sonido(self):
        return "Cluck cluck"

    def poner_huevo(self):
        self.numero_huevos += 1
        return f"La gallina ha puesto un huevo. Ahora tiene {self.numero_huevos} huevos."

# Otra subclase que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "Guau guau"

    def info(self):
        return f"Soy {self.nombre}, un {self.raza} y tengo {self.edad} años."

# Ejemplo de uso
gallina = Gallina("Lola", 2, 10)
perro = Perro("Rex", 5, "Labrador")

print(gallina.info())  # Imprime: Soy Lola y tengo 2 años.
print(gallina.hacer_sonido())  # Imprime: Cluck cluck
print(gallina.poner_huevo())  # Imprime: La gallina ha puesto un huevo. Ahora tiene 11 huevos.

print(perro.info())  # Imprime: Soy Rex, un Labrador y tengo 5 años.
print(perro.hacer_sonido())  # Imprime: Guau guau