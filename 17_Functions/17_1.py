#17.1

def is_even(number):
    '''
       Funcion para determinar si un nro es par o impar.
       Si el parametro es 0 return = None
    '''

    if number <= 0:
        print("El número debe ser mayor que 0.")
        return None

    if number % 2 == 0:
        return True
    else:
        return False


number = 12

result = is_even(number)
if result is not None:
    if result:
        print(number, "es un número par.")
    else:
        print(number, "es un número impar.")
