def sequential_search(arr, key):
    """
    Esta función realiza una búsqueda secuencial en un array para encontrar una clave dada.
    :param arr: lista, el array que se va a buscar
    :param key: int, la clave que se va a buscar
    :return: int, el índice de la clave si se encuentra, de lo contrario -1
    """
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    """
    Esta función realiza una búsqueda binaria en un array ordenado para encontrar una clave dada.
    :param arr: lista, el array ordenado que se va a buscar
    :param key: int, la clave que se va a buscar
    :return: int, el índice de la clave si se encuentra, de lo contrario -1
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def bubble_sort(arr):
    """
    Esta función ordena un array usando el algoritmo de ordenamiento de burbuja.
    :param arr: lista, el array que se va a ordenar
    :return: None
    """
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":
    arr = []
    print("Ingrese 20 elementos del array:")
    for i in range(20):
        arr.append(int(input()))

    key = int(input("Ingrese la clave a buscar: "))

    bubble_sort(arr)
    print("Array ordenado:", arr)

    index_binary = binary_search(arr, key)
    if index_binary!= -1:
        print(f"Clave encontrada en el índice {index_binary} con búsqueda binaria")
    else:
        print("Clave no encontrada con búsqueda binaria")

    index_sequential = sequential_search(arr, key)
    if index_sequential!= -1:
        print(f"Clave encontrada en el índice {index_sequential} con búsqueda secuencial")
    else:
        print("Clave no encontrada con búsqueda secuencial")
