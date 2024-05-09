def bubble_sort():
    """
    Solicita al usuario que ingrese 5 números separados por comas y los ordena utilizando el algoritmo de bubble sort.
    """
    while True:
        entrada_usuario = input("Ingrese los 5 números separados por comas: ")
        numeros = entrada_usuario.split(',')
        
        if len(numeros)!= 5:
            print("Error!!! Por favor, ingrese exactamente 5 números separados por comas.")
            continue
        
        try:
            arreglo = [int(elemento) for elemento in numeros]
            break
        except ValueError:
            print("Error!!! Por favor, ingrese solo números separados por comas.")
            continue
    
    n = len(arreglo)
    intercambio = True
    
    while intercambio:
        intercambio = False
        
        for i in range(n - 1):
            if arreglo[i] > arreglo[i + 1]:
                arreglo[i], arreglo[i + 1] = arreglo[i + 1], arreglo[i]
                intercambio = True
        
        n -= 1
    
    print("Arreglo ordenado:", arreglo)

bubble_sort()
