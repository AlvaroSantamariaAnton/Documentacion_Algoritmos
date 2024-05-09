# Solicitar la calificación del estudiante
calificacion = float(input("Ingrese la calificación del estudiante: "))

# Utilizar la estructura de elección para determinar si el estudiante ha aprobado
if calificacion >= 60:
    print("¡Felicidades! Has aprobado el curso.")
else:
    print("Lo siento, has reprobado el curso. ¡Mejor suerte la próxima vez!")