class Nodo:
    """
    Clase Nodo representa un nodo en el árbol binario.

    Atributos:
        elemento (int): Valor del nodo.
        hijo_izquierdo (Nodo): Referencia al hijo izquierdo.
        hijo_derecho (Nodo): Referencia al hijo derecho.
    """

    def __init__(self, elemento):
        """
        Inicializa el nodo con el valor dado.
        """
        self.elemento = elemento
        self.hijo_izquierdo = None
        self.hijo_derecho = None

    def es_hoja(self):
        """
        Verifica si el nodo actual es una hoja.

        Retorna:
            True si no tiene hijos, False en caso contrario.
        """
        return self.hijo_izquierdo is None and self.hijo_derecho is None

