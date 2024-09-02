try:
    x = int(input("Introduce un número: "))
except ValueError:
    print("Debes introducir un número válido.")
else:
    print(f"El número es {x}")