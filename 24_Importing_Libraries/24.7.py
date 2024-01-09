import json  # Import the json module

# Create a sample dictionary
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Serialize the dictionary to a JSON string
json_string = json.dumps(data)

# Print the serialized JSON string
print(json_string)
