from abc import ABC, abstractmethod

# Definición de la interfaz del TDA para la lista enlazada
class ListaEnlazadaTDA(ABC):
    @abstractmethod
    def insertar(self, dato):
        pass
    
    @abstractmethod
    def eliminar(self, dato):
        pass
    
    @abstractmethod
    def obtener(self, indice):
        pass

# Definición de la clase Nodo que representa un nodo en la lista enlazada
class Nodo:
    def _init_(self, dato):
        self.dato = dato
        self.siguiente = None

# Implementación de la lista enlazada que cumple con la interfaz TDA
class ListaEnlazada(ListaEnlazadaTDA):
    def _init_(self):
        self.cabeza = None  # Inicialmente la cabeza de la lista es None
        self.tamaño = 0     # El tamaño de la lista se inicializa en 0

    # Método para insertar un dato al final de la lista
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:  # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo  # Se agrega el nuevo nodo al final de la lista
        self.tamaño += 1  # Se incrementa el tamaño de la lista

    # Método para eliminar un dato de la lista
    def eliminar(self, dato):
        if self.cabeza is None:  # Si la lista está vacía, no hay nada que eliminar
            return
        if self.cabeza.dato == dato:  # Si el dato a eliminar está en la cabeza, se actualiza la cabeza
            self.cabeza = self.cabeza.siguiente
            self.tamaño -= 1
            return
        actual = self.cabeza
        while actual.siguiente is not None and actual.siguiente.dato != dato:
            actual = actual.siguiente
        if actual.siguiente is not None:
            actual.siguiente = actual.siguiente.siguiente  # Se salta el nodo que contiene el dato a eliminar
            self.tamaño -= 1

    # Método para obtener un dato en un índice específico de la lista
    def obtener(self, indice):
        if indice < 0 or indice >= self.tamaño:
            raise IndexError("Índice fuera de rango")
        actual = self.cabeza
        for i in range(indice):
            actual = actual.siguiente
        return actual.dato

    # Método para obtener el tamaño actual de la lista
    def tamaño(self):
        return self.tamaño

# Método main para probar la lista enlazada implementada
def main():
    lista = ListaEnlazada()

    # Insertamos algunos datos en la lista
    lista.insertar(5)
    lista.insertar(10)
    lista.insertar(15)

    # Imprimimos un elemento en un índice específico y el tamaño de la lista
    print("Elemento en índice 1:", lista.obtener(1))
    print("Tamaño de la lista:", lista.tamaño)

    # Eliminamos un dato de la lista y mostramos el tamaño actualizado
    lista.eliminar(10)
    print("Tamaño después de eliminar:", lista.tamaño)

if __name__ == "__main__":
    main()