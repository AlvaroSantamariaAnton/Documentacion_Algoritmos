# Ejercicio 9.1: Calcular la media aritmética de tres números dados

def media_aritmetica(a, b, c):
    """
    Calcula la media aritmética de tres números.

    Args:
    - a (float): Primer número.
    - b (float): Segundo número.
    - c (float): Tercer número.

    Returns:
    float: Media aritmética de los tres números.
    """
    return (a + b + c) / 3

# Ejemplo de uso
numero1 = 10
numero2 = 20
numero3 = 30
media = media_aritmetica(numero1, numero2, numero3)
print("Media aritmética de los números: ", media)


# Ejercicio 9.2: Calcular la media ponderada de números dados y sus coeficientes de ponderación

def media_ponderada(valores, ponderaciones):
    """
    Calcula la media ponderada de una lista de valores con sus respectivos coeficientes de ponderación.

    Args:
    - valores (list): Lista de valores.
    - ponderaciones (list): Lista de coeficientes de ponderación.

    Returns:
    float: Media ponderada de los valores.
    """
    if len(valores) != len(ponderaciones):
        raise ValueError("Las listas de valores y ponderaciones deben tener la misma longitud.")
    
    numerador = sum(valores[i] * ponderaciones[i] for i in range(len(valores)))
    denominador = sum(ponderaciones)
    
    return numerador / denominador

# Ejemplo de uso
valores = [10, 20, 30]
ponderaciones = [0.2, 0.3, 0.5]
media_pond = media_ponderada(valores, ponderaciones)
print("Media ponderada de los valores con sus ponderaciones: ", media_pond)
