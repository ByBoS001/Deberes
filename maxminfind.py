def encontrar_maximo_y_minimo():
    # Solicitar al usuario que ingrese la cantidad de números
    cantidad_numeros = int(input("Ingrese la cantidad de números: "))
    
    # Verificar si la cantidad de números es válida
    if cantidad_numeros < 1:
        return None, None  # Si no es válida, devolver None para ambos valores
    
    # Inicializar el máximo y el mínimo con valores extremos
    minimo_numero = float('inf')
    maximo_numero = float('-inf')

    # Bucle para iterar sobre la cantidad de números ingresados
    for cont in range(cantidad_numeros):
        # Solicitar al usuario que ingrese un número específico
        num = int(input(f"Ingrese número {cont + 1}: "))
        
        # Actualizar el mínimo si es necesario
        if num < minimo_numero:
            minimo_numero = num
        # Actualizar el máximo si es necesario
        elif num > maximo_numero:
            maximo_numero = num

    # Devolver el mínimo y el máximo encontrados
    return minimo_numero, maximo_numero

# Ejemplo de uso de la función
minimo, maximo = encontrar_maximo_y_minimo()
# Imprimir los resultados
print("Número Mínimo =", minimo, ", Número Máximo =", maximo)
