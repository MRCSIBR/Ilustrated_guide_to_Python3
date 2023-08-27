import unicodedata

# Definir el codepoint del caracter 
code_point = 9731

# Codepoint del caracter
character = chr(code_point)

# Obteber el nombre del caracter
name = unicodedata.name(character)

# Luego imprimimos el caracter y su nombre
print(f"Character: {character}")
print(f"Name: {name}")