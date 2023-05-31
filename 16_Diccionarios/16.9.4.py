# Párrafo de ejemplo escrito por Ralph Waldo Emerson
texto = "La confianza en sí mismo es el primer secreto del éxito."

# Crear una lista de palabras
palabras = texto.split()

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
