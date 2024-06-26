class Nodo:
    def __init__(self, dato):
        self.dato = dato       # Inicializa el nodo con un dato específico
        self.siguiente = None  # Puntero al siguiente nodo, inicialmente None
        self.anterior = None   # Puntero al nodo anterior, inicialmente None


        
class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None    # Inicializa la cabeza de la lista como None
        self.cola = None      # Inicializa la cola de la lista como None
        self.cursor = None    # Inicializa el cursor en None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)  # Crea un nuevo nodo con el dato proporcionado
        if self.cabeza is None:
            # Si la lista está vacía, el nuevo nodo se convierte en la cabeza, la cola y el cursor
            self.cabeza = self.cola = nuevo_nodo
            self.cursor = nuevo_nodo
        else:
            if self.cursor.siguiente:
                # Si hay un nodo siguiente al cursor, ajusta los punteros para insertar el nuevo nodo
                nuevo_nodo.siguiente = self.cursor.siguiente
                self.cursor.siguiente.anterior = nuevo_nodo
            else:
                self.cola = nuevo_nodo  # El nuevo nodo se convierte en la nueva cola
            
            nuevo_nodo.anterior = self.cursor  # El nodo anterior al nuevo nodo es el cursor actual
            self.cursor.siguiente = nuevo_nodo  # El siguiente del cursor es el nuevo nodo
            self.cursor = nuevo_nodo  # El cursor ahora apunta al nuevo nodo

    def eliminar(self):
        if self.cursor is None:
            return  # Si el cursor es None, no se puede eliminar nada

        if self.cursor == self.cabeza:
            # Si el cursor está en la cabeza, ajusta la cabeza y sus punteros
            self.cabeza = self.cursor.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
        elif self.cursor == self.cola:
            # Si el cursor está en la cola, ajusta la cola y sus punteros
            self.cola = self.cursor.anterior
            self.cola.siguiente = None
        else:
            # Si el cursor está en otro lugar, ajusta los punteros de los nodos vecinos
            self.cursor.anterior.siguiente = self.cursor.siguiente
            self.cursor.siguiente.anterior = self.cursor.anterior
        
        self.cursor = self.cursor.anterior  # Mueve el cursor al nodo anterior

    def mover_cursor_izquierda(self):
        if self.cursor and self.cursor.anterior:
            self.cursor = self.cursor.anterior  # Mueve el cursor hacia la izquierda si es posible

    def mover_cursor_derecha(self):
        if self.cursor and self.cursor.siguiente:
            self.cursor = self.cursor.siguiente  # Mueve el cursor hacia la derecha si es posible

    def mostrar(self):
        actual = self.cabeza
        texto = []
        while actual:
            texto.append(actual.dato)  # Agrega el dato del nodo actual a la lista de texto
            actual = actual.siguiente  # Avanza al siguiente nodo
        
        return ''.join(texto)  # Devuelve el texto como una cadena concatenada
    
# Ejemplo de uso del editor de texto simple
editor = ListaDoblementeEnlazada()

# Insertar caracteres
editor.insertar('B')
editor.insertar('X')
editor.insertar('O')
editor.insertar('S')
print(editor.mostrar())  # Salida: "Jair"

# Mover el cursor a la izquierda y eliminar un carácter
editor.mover_cursor_izquierda()
editor.eliminar()
print(editor.mostrar())  # Salida: "Jar"

# Insertar más caracteres
editor.insertar('X')
print(editor.mostrar())  # Salida: "Jair"

# Mover el cursor a la izquierda y a la derecha
editor.mover_cursor_izquierda()
editor.mover_cursor_izquierda()
editor.insertar(' ')
print(editor.mostrar())  # Salida: "Ja ir"R