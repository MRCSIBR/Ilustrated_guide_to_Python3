# Lista de tuplas de origen y destino de enlaces
links = [('a', 'b'), ('a', 'c'), ('b', 'c')]

# Crear un conjunto de nodos
nodos = set()
for origen, destino in links:
    nodos.add(origen)
    nodos.add(destino)

# Crear un diccionario de enlaces salientes para cada nodo
enlaces_salientes = dict()
for origen, destino in links:
    if origen in enlaces_salientes:
        enlaces_salientes[origen].append(destino)
    else:
        enlaces_salientes[origen] = [destino]

# Inicializar el PageRank de cada nodo
pagerank = dict()
for nodo in nodos:
    pagerank[nodo] = 1 / len(nodos)

# Iterar 10 veces sobre los enlaces
for i in range(10):
    # Crear un diccionario de PageRank temporal
    pagerank_temporal = dict()
    for nodo in nodos:
        pagerank_temporal[nodo] = 0

    # Calcular el PageRank temporal para cada nodo
    for origen in nodos:
        for destino in enlaces_salientes.get(origen, []):
            pagerank_temporal[destino] += pagerank[origen] / len(enlaces_salientes.get(origen, []))

    # Actualizar el PageRank de cada nodo
    for nodo in nodos:
        pagerank[nodo] = pagerank_temporal[nodo]

# Imprimir el PageRank de cada nodo
for nodo in nodos:
    print(f'{nodo}: {pagerank[nodo]}')
