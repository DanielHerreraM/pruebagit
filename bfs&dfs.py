from collections import deque


def bfs(self):
        """Recorrido por niveles (BFS)."""
        if not self.raiz:
            return

        cola = deque()
        cola.append(self.raiz)

        print("Recorrido BFS:")
        while cola:
            nodo = cola.popleft()
            print(nodo.valor, end=' ')

            if nodo.izquierda:
                cola.append(nodo.izquierda)
            if nodo.derecha:
                cola.append(nodo.derecha)