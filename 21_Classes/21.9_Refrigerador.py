class Refrigerator:
    def __init__(self, brand, model, capacity):
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.temperature = 4
    
    def set_temperature(self, temperature):
        self.temperature = temperature
    
    def get_temperature(self):
        return self.temperature


my_refrigerator = Refrigerator("Samsung", "RF28R7351SR", 28)

# set the temperature of the refrigerator
my_refrigerator.set_temperature(2)

# get the current temperature of the refrigerator
current_temperature = my_refrigerator.get_temperature()

# print the current temperature of the refrigerator
print(f"The current temperature of the refrigerator is: {current_temperature}")
