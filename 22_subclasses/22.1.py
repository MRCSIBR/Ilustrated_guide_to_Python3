# Example of a subclass
# define a superclass
class Animal:
    # attribute and method of the parent class
    name = ""
    def eat(self):
        print("Puedo comer grajeas.. woof")

# inherit from Animal class
class Dog(Animal):
    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("Mi nombre es: ", self.name)

# create an object of the subclass
labrador = Dog()

# access superclass attribute and method
labrador.name = "Rohu"
labrador.eat()

# call subclass method
labrador.display()
