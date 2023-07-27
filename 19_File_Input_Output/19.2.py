import csv

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            data.append(row)
        file.close()
        return data

data = read_csv('output.csv')
print(data)