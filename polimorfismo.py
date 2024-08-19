# Clase base (superclase)
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        return "Sonido genérico"

# Subclase que hereda de Animal
class Gallina(Animal):
    def hacer_sonido(self):
        return "Cluck cluck"

# Otra subclase que hereda de Animal
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau guau"

# Subclase adicional
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Función que demuestra polimorfismo
def imprimir_sonido(animal):
    print(animal.hacer_sonido())

# Ejemplo de uso
gallina = Gallina("Lola", 2)
perro = Perro("Rex", 5)
gato = Gato("Mishi", 3)

imprimir_sonido(gallina)  # Imprime: Cluck cluck
imprimir_sonido(perro)  # Imprime: Guau guau
imprimir_sonido(gato)  # Imprime: Miau