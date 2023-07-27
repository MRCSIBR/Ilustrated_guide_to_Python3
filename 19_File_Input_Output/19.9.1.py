import csv

def write_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Address', 'Age'])
        for item in data:
            writer.writerow(item)
        file.close()

data = [('John', '123 Main St', 25), ('Jane', '456 Elm St', 30), ('Bob', '789 Oak St', 40)]

# Llamamos la funcion
write_csv('output.csv', data)
