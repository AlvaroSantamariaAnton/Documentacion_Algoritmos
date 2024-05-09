def factorial(n):
    """Función recursiva para calcular el factorial de un número."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número entero para calcular su factorial: "))

# Calcular el factorial utilizando la función recursiva
resultado = factorial(numero)

# Imprimir el resultado
print("El factorial de", numero, "es:", resultado)