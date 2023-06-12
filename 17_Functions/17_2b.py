# Encontrar un numero primo usando la criba de Eratostenes

def sieve_of_eratosthenes(n):
    # Crear una lista de booleanos para marcar los números compuestos (no primos)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # Aplicar la Criba de Eratóstenes
    p = 2
    while p * p <= n:
        if is_prime[p]:
            # Marcar todos los múltiplos de p como compuestos
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # Recopilar los números primos en una lista
    primes = [i for i in range(n + 1) if is_prime[i]]

    return primes


n = 100
prime_numbers = sieve_of_eratosthenes(n)

print("Números primos hasta", n, ":")
print(prime_numbers)
