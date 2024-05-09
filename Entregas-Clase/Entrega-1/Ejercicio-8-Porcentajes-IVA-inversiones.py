# Ejercicio 8.1: Calcular el precio con todos los impuestos incluidos (TII)

def calcular_precio_con_impuestos(precio_sin_impuestos, porcentaje_iva):
    """
    Calcula el precio con todos los impuestos incluidos (TII).

    Args:
    - precio_sin_impuestos (float): Precio sin impuestos.
    - porcentaje_iva (float): Porcentaje del IVA.

    Returns:
    float: Precio con todos los impuestos incluidos (TII).
    """
    iva = precio_sin_impuestos * (porcentaje_iva / 100)
    precio_con_impuestos = precio_sin_impuestos + iva
    return precio_con_impuestos

# Ejemplo de uso
precio_sin_impuestos = 100
porcentaje_iva = 16
precio_con_impuestos = calcular_precio_con_impuestos(precio_sin_impuestos, porcentaje_iva)
print("Precio con todos los impuestos incluidos: ", precio_con_impuestos)


# Ejercicio 8.2: Calcular el importe de los intereses generados por un capital invertido

def calcular_intereses(capital, tasa_interes, tiempo_meses):
    """
    Calcula el importe de los intereses generados por un capital invertido.

    Args:
    - capital (float): Capital invertido.
    - tasa_interes (float): Tasa de interés (porcentaje).
    - tiempo_meses (int): Tiempo en meses.

    Returns:
    float: Importe de los intereses generados.
    """
    tasa_decimal = tasa_interes / 100
    intereses = capital * tasa_decimal * (tiempo_meses / 12)
    return intereses

# Ejemplo de uso
capital = 1000
tasa_interes = 5
tiempo_meses = 6
intereses_generados = calcular_intereses(capital, tasa_interes, tiempo_meses)
print("Intereses generados: ", intereses_generados)
