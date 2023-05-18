# La principal diferencia entre listas y tuplas es que las lista son mutables
# mientras que las tuplas son inmutables.

list_obj = [1, 2, 3, 4, 5]
tuple_obj = (3, 4, 5, 6, 7)

list_set = set(list_obj)                     # Con set se puede convertir a lista para aplecar la funcion difference
tuple_set = set(tuple_obj)

diff_set = list_set.difference(tuple_set)
print(diff_set)

