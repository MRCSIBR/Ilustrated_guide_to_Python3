class Chairlift:
    ''' Clase Chairlift: modela un funicular de 4 pasajeros
        
        Metodos: load_passenger
                unload_passenger    
    '''
    
    def __init__(self):
        self.max_occupancy = 4                           # Atributos constantes de la clase
        self.current_occupancy = 0
    
    def load_passenger(self):                            # Metodo
        if self.current_occupancy < self.max_occupancy:
            self.current_occupancy += 1
            print("Passenger loaded.")
        else:
            print("Chairlift is already full.")
    
    def unload_passenger(self):
        if self.current_occupancy > 0:
            self.current_occupancy -= 1
            print("Passenger unloaded.")
        else:
            print("Chairlift is already empty.")
            

silla1 = Chairlift()                                    # Crear una nueva instancia 'Chairlift'

# Cargar pasajeros
silla1.load_passenger() 
silla1.load_passenger()            

# Descargar pasajeros
silla1.unload_passenger()            
silla1.unload_passenger()
silla1.unload_passenger()            
