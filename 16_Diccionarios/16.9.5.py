# Párrafo de ejemplo
texto = "La mente, una vez estirada por una nueva idea, nunca vuelve a sus dimensiones originales.."

# Crear una lista de palabras
palabras = texto.split()

# Crear un diccionario vacío para guardar los anagramas encontrados
anagramas = dict()

# Iterar sobre la lista de palabras y ordenar las letras de cada palabra alfabéticamente
for palabra in palabras:
    palabra_ordenada = ''.join(sorted(palabra))
    if palabra_ordenada in anagramas:
        anagramas[palabra_ordenada].append(palabra)
    else:
        anagramas[palabra_ordenada] = [palabra]

# Iterar sobre el diccionario anagramas e imprimir las listas de palabras que tienen más de un elemento
for lista_palabras in anagramas.values():
    if len(lista_palabras) > 1:
        print(lista_palabras)
