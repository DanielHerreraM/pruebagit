from Nodo import Nodo

class ArbolBB:
    """
    Clase ArbolBB representa un Árbol Binario de Búsqueda.

    Atributos:
        raiz (Nodo): Nodo raíz del árbol.
    """

    def __init__(self):
        """
        Constructor. Inicializa el árbol vacío.
        """
        self.raiz = None

    def es_vacio(self):
        """
        Verifica si el árbol está vacío.

        Retorna:
            True si no hay nodos en el árbol, False en caso contrario.
        """
        return self.raiz is None

    def insertar_nodo(self, valor):
        """
        Inserta un nuevo valor en el árbol de forma recursiva.

        Parámetros:
            valor (int): Valor a insertar.
        """
        self.raiz = self._insertar_nodo_rec(self.raiz, valor)

    def _insertar_nodo_rec(self, nodo, valor):
        """
        Método auxiliar recursivo para insertar un nodo.
        """
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.elemento:
            nodo.hijo_izquierdo = self._insertar_nodo_rec(nodo.hijo_izquierdo, valor)
        elif valor > nodo.elemento:
            nodo.hijo_derecho = self._insertar_nodo_rec(nodo.hijo_derecho, valor)
        return nodo

    def buscar_x(self, valor):
        """
        Busca si un valor existe en el árbol de forma recursiva.

        Parámetros:
            valor (int): Valor a buscar.

        Retorna:
            True si existe, False si no.
        """
        return self._buscar_x_rec(self.raiz, valor)

    def _buscar_x_rec(self, nodo, valor):
        """
        Método auxiliar recursivo para buscar un valor.
        """
        if nodo is None:
            return False
        if nodo.elemento == valor:
            return True
        if valor < nodo.elemento:
            return self._buscar_x_rec(nodo.hijo_izquierdo, valor)
        else:
            return self._buscar_x_rec(nodo.hijo_derecho, valor)

    def in_orden(self):
        """
        Realiza un recorrido inorden del árbol (izquierda, raíz, derecha).
        """
        self._in_orden_rec(self.raiz)
        print() # Salto de línea al final

    def _in_orden_rec(self, nodo):
        if nodo is not None:
            self._in_orden_rec(nodo.hijo_izquierdo)
            print(nodo.elemento, end=" ")
            self._in_orden_rec(nodo.hijo_derecho)

    def pre_orden(self):
        """
        Realiza un recorrido preorden del árbol (raíz, izquierda, derecha).
        """
        self._pre_orden_rec(self.raiz)
        print()

    def _pre_orden_rec(self, nodo):
        if nodo is not None:
            print(nodo.elemento, end=" ")
            self._pre_orden_rec(nodo.hijo_izquierdo)
            self._pre_orden_rec(nodo.hijo_derecho)

    def post_orden(self):
        """
        Realiza un recorrido postorden del árbol (izquierda, derecha, raíz).
        """
        self._post_orden_rec(self.raiz)
        print()

    def _post_orden_rec(self, nodo):
        if nodo is not None:
            self._post_orden_rec(nodo.hijo_izquierdo)
            self._post_orden_rec(nodo.hijo_derecho)
            print(nodo.elemento, end=" ")


if __name__ == "__main__":
    arbol = ArbolBB()

    # Insertamos algunos valores
    arbol.insertar_nodo(50)
    arbol.insertar_nodo(30)
    arbol.insertar_nodo(70)

    print("Recorrido InOrden del árbol:")
    arbol.in_orden()
