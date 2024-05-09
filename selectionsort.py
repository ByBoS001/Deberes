def selection_sort():
    # Solicitar al usuario que ingrese los 5 números separados por comas
    entrada_usuario = input("Ingrese los 5 números separados por comas: ")

    # Convertir la entrada del usuario en una lista de números enteros
    numeros = entrada_usuario.split(',')
    arreglo = []
    
    # Verificar si se ingresaron exactamente 5 números
    if len(numeros) != 5:
        print("¡Error! Debe ingresar exactamente 5 números separados por comas.")
        return

    # Convertir los elementos a enteros y agregarlos al arreglo
    for elemento in numeros:
        try:
            numero_entero = int(elemento)
            arreglo.append(numero_entero)
        except ValueError:
            print("¡Error! Ingrese solo números separados por comas.")
            return

    n = len(arreglo)  # Obtener la longitud del arreglo

    # Algoritmo de Selection Sort
    for i in range(n - 1):
        # Encontrar el índice del mínimo elemento en el subarreglo no ordenado
        indice_minimo = i
        for j in range(i + 1, n):
            if arreglo[j] < arreglo[indice_minimo]:
                indice_minimo = j

        # Intercambiar el elemento actual con el mínimo encontrado
        arreglo[i], arreglo[indice_minimo] = arreglo[indice_minimo], arreglo[i]

    # Imprimir el arreglo ordenado
    print("Arreglo ordenado:", arreglo)

# Llamar a la función para ordenar los 5 números ingresados por el usuario
selection_sort()
