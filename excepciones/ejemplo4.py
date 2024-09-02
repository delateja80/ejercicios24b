try:
    archivito = open("c:/Users/lenovo/Desktop/Ejemplos python/excepciones/archivo.txt", "r")
    data = archivito.read()
    print(data)
except IOError:
    print("Error al leer el archivo")
finally:
    archivito.close()
