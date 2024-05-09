# Ejercicio 11: Calcular el importe de las horas extra a pagar

def calcular_horas_extra(salario_bruto_mensual, horas_extra):
    """
    Calcula el importe de las horas extra a pagar.

    Args:
    - salario_bruto_mensual (float): Salario bruto mensual del empleado.
    - horas_extra (int): Cantidad de horas extra trabajadas en el mes.

    Returns:
    float: Importe de las horas extra a pagar.
    """
    # Calcular la tarifa por hora normal
    tarifa_por_hora_normal = salario_bruto_mensual / (35 * 4)  # 35 horas por semana, 4 semanas por mes
    
    # Calcular la cantidad de horas normales y horas extra
    horas_normales = 35 * 4
    horas_extra_1 = min(max(0, horas_extra - 35), 7)  # Horas entre la 36ª y la 43ª
    horas_extra_2 = max(0, horas_extra - 42)  # Horas a partir de la 44ª
    
    # Calcular el importe de las horas extra
    importe_horas_extra_1 = horas_extra_1 * tarifa_por_hora_normal * 1.25
    importe_horas_extra_2 = horas_extra_2 * tarifa_por_hora_normal * 1.5
    
    # Sumar los importes de las horas extra
    importe_total_horas_extra = importe_horas_extra_1 + importe_horas_extra_2
    
    return importe_total_horas_extra

# Ejemplo de uso
salario_bruto_mensual = 3000  # Ejemplo de salario bruto mensual
horas_extra_trabajadas = 50  # Ejemplo de horas extra trabajadas en el mes
importe_horas_extra = calcular_horas_extra(salario_bruto_mensual, horas_extra_trabajadas)
print("Importe de las horas extra a pagar: ", importe_horas_extra)
