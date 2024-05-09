def seleccion_sort(lista):
    """Implementación del algoritmo de ordenación de selección."""
    n = len(lista)
    for i in range(n - 1):
        # Encontrar el índice del mínimo elemento en el resto de la lista
        indice_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

        # Intercambiar el elemento actual con el mínimo encontrado
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

# Lista desordenada
numeros = [64, 25, 12, 22, 11]

# Ordenar la lista utilizando el algoritmo de selección
seleccion_sort(numeros)

# Imprimir la lista ordenada
print("Lista ordenada:", numeros)