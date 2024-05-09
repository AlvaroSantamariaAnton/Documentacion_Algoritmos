# Ejercicio 10.1: Calcular el área de un triángulo dado un lado y la altura relativa a este lado

def area_triangulo_lado_altura(lado, altura):
    """
    Calcula el área de un triángulo dado un lado y la altura relativa a este lado.

    Args:
    - lado (float): Longitud del lado del triángulo.
    - altura (float): Altura relativa al lado del triángulo.

    Returns:
    float: Área del triángulo.
    """
    return (lado * altura) / 2

# Ejemplo de uso
lado = 5
altura = 8
area = area_triangulo_lado_altura(lado, altura)
print("Área del triángulo: ", area)


# Ejercicio 10.2: Calcular el área de un triángulo rectángulo dado los dos lados perpendiculares

def area_triangulo_rectangulo(cateto1, cateto2):
    """
    Calcula el área de un triángulo rectángulo dado los dos lados perpendiculares.

    Args:
    - cateto1 (float): Longitud del primer cateto.
    - cateto2 (float): Longitud del segundo cateto.

    Returns:
    float: Área del triángulo rectángulo.
    """
    return (cateto1 * cateto2) / 2

# Ejemplo de uso
cateto1 = 3
cateto2 = 4
area_rectangulo = area_triangulo_rectangulo(cateto1, cateto2)
print("Área del triángulo rectángulo: ", area_rectangulo)