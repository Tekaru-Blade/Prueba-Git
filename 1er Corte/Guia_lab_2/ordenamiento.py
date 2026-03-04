class AlgoritmosOrdenamiento:
    """Implementación de métodos de ordenamiento para listas de flotantes."""

    def burbuja(self, lista):
        """Método de burbuja: intercambia elementos adyacentes."""
        A = lista[:]
        n = len(A)
        for j in range(n - 1):
            for i in range(n - j - 1):
                if A[i] > A[i+1]:
                    A[i], A[i+1] = A[i+1], A[i]
        return A

    def insercion(self, lista):
        """Método de inserción: ordena como una baraja de cartas."""
        A = lista[:]
        for j in range(1, len(A)):
            key = A[j]
            i = j - 1
            while i >= 0 and A[i] > key:
                A[i + 1] = A[i]
                i -= 1
            A[i + 1] = key
        return A

    def seleccion(self, lista):
        """Método de selección: busca el mínimo en cada iteración."""
        A = lista[:]
        n = len(A)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if A[j] < A[min_idx]:
                    min_idx = j
            A[i], A[min_idx] = A[min_idx], A[i]
        return A

    def mergesort(self, A):
        """Método merge: estrategia divide y vencerás."""
        if len(A) <= 1:
            return A
        
        mitad = len(A) // 2
        izquierda = self.mergesort(A[:mitad])
        derecha = self.mergesort(A[mitad:])
        
        return self._merge(izquierda, derecha)

    def _merge(self, izq, der):
        resultado = []
        i = j = 0
        while i < len(izq) and j < len(der):
            if izq[i] <= der[j]:
                resultado.append(izq[i])
                i += 1
            else:
                resultado.append(der[j])
                j += 1
        resultado.extend(izq[i:])
        resultado.extend(der[j:])
        return resultado