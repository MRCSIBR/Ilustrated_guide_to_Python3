# Párrafo de ejemplo
parrafo = "Este es un ejemplo de párrafo. En este párrafo se cuentan las palabras."

# Crear una lista de palabras
palabras = parrafo.split()

# Crear un diccionario vacío para guardar el conteo de cada palabra
conteo_palabras = dict()

# Iterar sobre la lista de palabras y contar cada una
for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

# Imprimir el diccionario con el conteo de cada palabra
print(conteo_palabras)
