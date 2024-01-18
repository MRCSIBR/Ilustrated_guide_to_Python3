import json  # Importar el modulo json

# Crear un diccionario de ejemplo
data = {
    "nombre": "John",
    "edad": 30,
    "ciudad": "New York"
}

# Serialize the dictionary to a JSON string
json_string = json.dumps(data)

# Print the serialized JSON string
print(json_string)
