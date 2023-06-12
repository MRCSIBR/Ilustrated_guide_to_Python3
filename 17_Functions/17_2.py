#17.2 Funcion para determinar si un numero es primo

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True
number = 31

if is_prime(number):
    print(number, "es un número primo.")
else:
    print(number, "no es un número primo.")
