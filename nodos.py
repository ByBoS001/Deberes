class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def eliminar_nodo(self, valor):
        if not self.cabeza:
            return
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return
        nodo_anterior = self.cabeza
        nodo_actual = self.cabeza.siguiente
        while nodo_actual:
            if nodo_actual.valor == valor:
                nodo_anterior.siguiente = nodo_actual.siguiente
                return
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente

    def mostrar_lista(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

# Ejemplo de uso
playlist = ListaEnlazada()
playlist.agregar_nodo("Canción 1")
playlist.agregar_nodo("Canción 2")
playlist.agregar_nodo("Canción 3")
playlist.mostrar_lista()  # Muestra: Canción 1, Canción 2, Canción 3
print()
playlist.eliminar_nodo("Canción 2")
playlist.mostrar_lista()  # Muestra: Canción 1, Canción 3
print()
playlist.agregar_nodo("Canción 4")
playlist.mostrar_lista()  # Muestra: Canción 1, Canción 3, Canción 4